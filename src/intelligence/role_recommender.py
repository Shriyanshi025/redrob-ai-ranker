from typing import Dict, List


class RoleRecommender:
    ROLE_SKILLS = {
        "LLM Engineer": {
            "llms",
            "rag",
            "langchain",
            "prompt engineering",
            "fine-tuning llms",
            "hugging face transformers",
            "embeddings",
        },
        "Retrieval Engineer": {
            "information retrieval",
            "vector search",
            "semantic search",
            "faiss",
            "pinecone",
            "qdrant",
            "milvus",
            "bm25",
            "elasticsearch",
            "opensearch",
        },
        "Machine Learning Engineer": {
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "mlops",
            "feature engineering",
            "scikit-learn",
        },
        "Computer Vision Engineer": {
            "computer vision",
            "opencv",
            "yolo",
            "image classification",
            "object detection",
            "gans",
            "diffusion models",
        },
        "Speech AI Engineer": {
            "asr",
            "speech recognition",
            "tts",
        },
    }

    def recommend(self, candidate: Dict) -> List[str]:
        skills = {s.get("name", "").lower() for s in candidate.get("skills", [])}

        scores = []

        for role, role_skills in self.ROLE_SKILLS.items():
            matched = len(skills.intersection(role_skills))
            scores.append((role, matched))

        scores.sort(key=lambda x: x[1], reverse=True)

        recommendations = [role for role, score in scores if score >= 2]

        return recommendations[:3]
