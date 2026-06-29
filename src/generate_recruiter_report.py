import json
from pathlib import Path

from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)
from src.retrieval.candidate_retriever import (
    CandidateRetriever,
)
from src.explainability.explainer import (
    CandidateExplainer,
)
from src.intelligence.role_recommender import (
    RoleRecommender,
)
from src.intelligence.skill_gap_analyzer import (
    SkillGapAnalyzer,
)

TOP_N = 10


def main():
    pipeline = CandidateRankingPipeline()
    retriever = CandidateRetriever()
    explainer = CandidateExplainer()
    recommender = RoleRecommender()
    gap_analyzer = SkillGapAnalyzer()

    results = pipeline.run(
        top_k=TOP_N
    )

    candidate_map = {
        c["candidate_id"]: c
        for c in retriever.stream_candidates()
    }

    report = []

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

        profile = candidate.get(
            "profile",
            {}
        )

        report.append(
            {
                "rank": rank,
                "candidate_id": candidate_id,
                "score": round(score, 6),
                "name": profile.get(
                    "name",
                    "Unknown"
                ),
                "current_title": profile.get(
                    "current_title",
                    ""
                ),
                "years_of_experience": profile.get(
                    "years_of_experience",
                    0,
                ),
                "top_reasons": explanation[
                    "top_reasons"
                ],
                "recommended_roles": roles,
                "skill_gaps": gaps,
            }
        )

    output_dir = Path("outputs")
    output_dir.mkdir(
        exist_ok=True
    )

    output_file = (
        output_dir
        / "recruiter_report.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            report,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(
        f"Saved: {output_file}"
    )


if __name__ == "__main__":
    main()