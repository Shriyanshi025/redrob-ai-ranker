from src.pipeline.pipeline import CandidateRankingPipeline
from src.retrieval.candidate_retriever import CandidateRetriever

pipeline = CandidateRankingPipeline()
retriever = CandidateRetriever()

results = pipeline.run(top_k=10)
candidate_map = {c["candidate_id"]: c for c in retriever.stream_candidates()}

for score, candidate_id in results:
    candidate = candidate_map[candidate_id]

    print("=" * 80)
    print(candidate_id)
    print("Score:", round(score, 4))
    print("Title:", candidate["profile"]["current_title"])
    print(
        "Experience:",
        candidate["profile"]["years_of_experience"],
    )
    print(
        "Company:",
        candidate["profile"]["current_company"],
    )
