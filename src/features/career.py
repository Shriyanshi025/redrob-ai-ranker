"""
Career-history intelligence.
"""

KEYWORDS = {
    "retrieval",
    "ranking",
    "recommendation",
    "recommender",
    "search",
    "embeddings",
    "vector database",
    "semantic search",
    "information retrieval",
    "machine learning",
    "deep learning",
    "llm",
    "nlp",
    "transformer",
}


def calculate_career_score(candidate: dict) -> float:
    history = candidate.get("career_history", [])

    matches = 0

    for job in history:

        text = " ".join(str(v) for v in job.values()).lower()

        for keyword in KEYWORDS:
            if keyword in text:
                matches += 1

    return min(matches / 5.0, 1.0)
