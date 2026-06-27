from src.features.feature_builder import (
    CandidateFeatureVector,
)


class CandidateRanker:

    def score(
        self,
        features: CandidateFeatureVector,
    ) -> float:

        final_score = (
            0.20 * features.title_match
            + 0.20 * features.skill_score
            + 0.20 * features.retrieval_score
            + 0.15 * features.career_score
            + 0.10 * features.experience_match
            + 0.10 * features.company_score
            + 0.03 * features.behavioral_score
            + 0.01 * features.availability_score
            + 0.005 * features.profile_quality_score
            + 0.005 * features.engagement_score
        )


        return final_score