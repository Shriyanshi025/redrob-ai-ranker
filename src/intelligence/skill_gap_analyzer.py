from typing import Dict, List


class SkillGapAnalyzer:
    ROLE_REQUIREMENTS = {
        "LLM Engineer": {
            "llms",
            "rag",
            "langchain",
            "prompt engineering",
            "fine-tuning llms",
            "embeddings",
            "mlops",
            "docker",
        },
        "Retrieval Engineer": {
            "information retrieval",
            "vector search",
            "faiss",
            "pinecone",
            "qdrant",
            "milvus",
            "elasticsearch",
            "bm25",
        },
        "Machine Learning Engineer": {
            "machine learning",
            "deep learning",
            "pytorch",
            "tensorflow",
            "mlops",
            "docker",
            "kubernetes",
        },
        "Computer Vision Engineer": {
            "computer vision",
            "opencv",
            "yolo",
            "image classification",
            "object detection",
            "pytorch",
        },
        "Speech AI Engineer": {
            "asr",
            "speech recognition",
            "tts",
            "deep learning",
        },
    }

    def analyze(
        self,
        candidate: Dict,
        recommended_roles: List[str],
    ) -> Dict[str, List[str]]:

        skills = {s.get("name", "").lower() for s in candidate.get("skills", [])}

        gaps = {}

        for role in recommended_roles:
            required = self.ROLE_REQUIREMENTS.get(role, set())

            missing = sorted(required - skills)

            gaps[role] = missing[:5]

        return gaps
