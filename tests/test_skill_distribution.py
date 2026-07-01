from collections import Counter

from src.retrieval.candidate_retriever import CandidateRetriever

counter = Counter()

for candidate in CandidateRetriever().stream_candidates():
    for skill in candidate.get("skills", []):
        counter[skill["name"]] += 1

for skill, count in counter.most_common(100):
    print(f"{skill}: {count}")
