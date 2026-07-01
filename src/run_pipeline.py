from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)

pipeline = CandidateRankingPipeline()

results = pipeline.run(top_k=10)

for score, candidate_id in results:
    print(f"{candidate_id} -> {score:.4f}")
