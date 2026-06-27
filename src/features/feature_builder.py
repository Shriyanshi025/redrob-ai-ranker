"""
Builds ranking features from a candidate profile.
"""

from dataclasses import dataclass
from src.features.experience import calculate_experience_match
from src.features.behavioral import calculate_behavioral_score
from src.features.title import calculate_title_match
from src.features.career import (
    calculate_career_score,
)
from src.features.signals import (
    calculate_availability_score,
    calculate_profile_quality_score,
    calculate_engagement_score,
)
from src.features.skills import (
    calculate_skill_score,
)
from src.features.company import (
    calculate_company_score,
)
from src.features.retrieval import (
    calculate_retrieval_score,
)


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
    
    skill_score: float = 0.0

    embedding_score: float = 0.0
    
    career_score: float = 0.0

    llm_score: float = 0.0

    behavioral_score: float = 0.0

    activity_score: float = 0.0
    
    availability_score: float = 0.0
    
    profile_quality_score: float = 0.0
    
    engagement_score: float = 0.0

    recruiter_response_score: float = 0.0
    
    company_score: float = 0.0

    github_score: float = 0.0
    
    retrieval_score: float = 0.0

    relocation_score: float = 0.0
    
    capability_score: float = 0.0
    
    fit_score: float = 0.0
    
    hireability_score: float = 0.0

    final_score: float = 0.0
    
class FeatureBuilder:

    def build(
        self,
        candidate: dict,
        job,
    ) -> CandidateFeatureVector:

        return CandidateFeatureVector(
            candidate_id=candidate["candidate_id"],
            title_match=calculate_title_match(candidate),
            experience_match=calculate_experience_match(
                candidate,
                job,
            ),
            behavioral_score=calculate_behavioral_score(
                candidate,
            ),
            career_score=calculate_career_score(
                candidate,
            ),
            availability_score=
            calculate_availability_score(
                candidate
            ),

            profile_quality_score=
            calculate_profile_quality_score(
                candidate
            ),

            engagement_score=
            calculate_engagement_score(
                candidate
            ),
            skill_score=
            calculate_skill_score(
                candidate
            ),
            company_score=
            calculate_company_score(
                candidate
            ),
            retrieval_score=
            calculate_retrieval_score(
                candidate
            ),
        )