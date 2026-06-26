"""
Builds ranking features from a candidate profile.
"""

from dataclasses import dataclass
from src.features.experience import calculate_experience_match


@dataclass
class CandidateFeatureVector:
    candidate_id: str

    semantic_skill_match: float = 0.0

    title_match: float = 0.0

    experience_match: float = 0.0

    industry_match: float = 0.0

    education_match: float = 0.0

    product_company_score: float = 0.0

    retrieval_system_score: float = 0.0

    ranking_system_score: float = 0.0

    embedding_score: float = 0.0

    llm_score: float = 0.0

    behavioral_score: float = 0.0

    activity_score: float = 0.0

    recruiter_response_score: float = 0.0

    github_score: float = 0.0

    relocation_score: float = 0.0

    final_score: float = 0.0
    
class FeatureBuilder:

    def build(
        self,
        candidate: dict,
        job,
    ) -> CandidateFeatureVector:

        return CandidateFeatureVector(
            candidate_id=candidate["candidate_id"],
            experience_match=calculate_experience_match(
                candidate,
                job,
            ),
        )