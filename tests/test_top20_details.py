from src.pipeline.pipeline import CandidateRankingPipeline
from src.retrieval.candidate_retriever import CandidateRetriever

results = CandidateRankingPipeline().run(top_k=20)

candidate_map = {
    c["candidate_id"]: c
    for c in CandidateRetriever().stream_candidates()
}

for rank, (score, candidate_id) in enumerate(results, start=1):
    c = candidate_map[candidate_id]

    print("=" * 100)
    print(f"Rank: {rank}")
    print(f"ID: {candidate_id}")
    print(f"Score: {score:.4f}")
    print(f"Title: {c['profile']['current_title']}")
    print(f"Company: {c['profile']['current_company']}")
    print(f"Experience: {c['profile']['years_of_experience']}")

    print(
        "Skills:",
        [s["name"] for s in c["skills"][:10]]
    )