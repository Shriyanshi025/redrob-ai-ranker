from src.features.feature_builder import (
    CandidateFeatureVector,
)


class CandidateRanker:

    def score(
        self,
        features: CandidateFeatureVector,
    ) -> float:

        final_score = (
            0.22 * features.title_match
            + 0.25 * features.skill_score
            + 0.18 * features.career_score
            + 0.15 * features.experience_match
            + 0.10 * features.company_score
            + 0.05 * features.behavioral_score
            + 0.03 * features.availability_score
            + 0.01 * features.profile_quality_score
            + 0.01 * features.engagement_score
        )


        return final_score