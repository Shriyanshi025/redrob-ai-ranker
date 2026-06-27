from src.pipeline.pipeline import CandidateRankingPipeline
from src.retrieval.candidate_retriever import CandidateRetriever

results = CandidateRankingPipeline().run(top_k=5)

candidate_map = {
    c["candidate_id"]: c
    for c in CandidateRetriever().stream_candidates()
}

for score, candidate_id in results:
    c = candidate_map[candidate_id]

    print("=" * 100)
    print(candidate_id)
    print(c["profile"]["current_title"])
    print(score)

    print(
        [s["name"] for s in c["skills"]]
    )