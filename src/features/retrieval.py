KEYWORDS = {
    "information retrieval",
    "retrieval",
    "search",
    "ranking",
    "learning to rank",
    "recommendation systems",
    "recommendation",
    "recommender",
    "embeddings",
    "vector search",
    "semantic search",
    "bm25",
    "elasticsearch",
    "opensearch",
    "faiss",
    "pinecone",
    "qdrant",
    "weaviate",
    "milvus",
    "sentence transformers",
}


def calculate_retrieval_score(
    candidate: dict,
) -> float:

    skills = {s["name"].lower() for s in candidate.get("skills", [])}

    matches = len(skills.intersection(KEYWORDS))

    return min(
        matches / 5.0,
        1.0,
    )
