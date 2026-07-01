from src.retrieval.candidate_retriever import CandidateRetriever

retriever = CandidateRetriever()

count = 0

for _ in retriever.stream_candidates():
    count += 1

print(count)
