"""
Skill matching for the Redrob challenge.
"""

TARGET_SKILLS = {
    "information retrieval",
    "recommendation systems",
    "semantic search",
    "sentence transformers",
    "embeddings",
    "vector search",
    "pinecone",
    "faiss",
    "rag",
    "fine-tuning llms",
    "qlora",
    "llms",
    "hugging face transformers",
    "mlops",
    "langchain",
}


def calculate_skill_score(candidate: dict) -> float:
    def normalize_skill(skill: str) -> str:
        return (
            skill.lower()
            .replace("-", " ")
            .replace("_", " ")
            .replace(".", " ")
            .replace("/", " ")
            .replace("recommendationsystems", "recommendation systems")
            .replace("vectorsearch", "vector search")
            .strip()
        )


    skills = {
        normalize_skill(skill["name"])
        for skill in candidate.get("skills", [])
    }

    matches = len(
        skills.intersection(TARGET_SKILLS)
    )

    return min(matches / 6.0, 1.0)