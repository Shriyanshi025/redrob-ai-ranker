import json
from pathlib import Path

from src.retrieval.candidate_retriever import CandidateRetriever
from src.explainability.explainer import CandidateExplainer
from src.intelligence.role_recommender import RoleRecommender
from src.intelligence.skill_gap_analyzer import SkillGapAnalyzer
from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)


TOP_N = 100


def main():
    explainer = CandidateExplainer()
    recommender = RoleRecommender()
    gap_analyzer = SkillGapAnalyzer()
    retriever = CandidateRetriever()
    pipeline = CandidateRankingPipeline()

    results = pipeline.run(
        top_k=TOP_N
    )

    candidate_map = {
        c["candidate_id"]: c
        for c in retriever.stream_candidates()
    }

    insights = []

    for rank, (
        score,
        candidate_id,
    ) in enumerate(
        results,
        start=1,
    ):
        candidate = candidate_map.get(
            candidate_id
        )

        if not candidate:
            continue

        explanation = explainer.explain(
            candidate,
            score,
        )

        roles = recommender.recommend(
            candidate
        )

        gaps = gap_analyzer.analyze(
            candidate,
            roles,
        )

        insights.append(
            {
                "rank": rank,
                "candidate_id": candidate_id,
                "score": round(score, 6),
                "recommended_roles": roles,
                "top_reasons": explanation[
                    "top_reasons"
                ],
                "skill_gaps": gaps,
            }
        )

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_file = (
        output_dir /
        "top_candidates_with_insights.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            insights,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()