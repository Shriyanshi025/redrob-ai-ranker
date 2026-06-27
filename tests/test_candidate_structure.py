from src.retrieval.candidate_retriever import CandidateRetriever
import json

retriever = CandidateRetriever()

candidate = next(retriever.stream_candidates())

print(json.dumps(candidate, indent=2)[:8000])