from src.features.feature_builder import (
    CandidateFeatureVector,
)


class CandidateRanker:

    def score(
        self,
        features: CandidateFeatureVector,
    ) -> float:

        final_score = (
             0.30 * features.title_match
            + 0.20 * features.career_score
            + 0.20 * features.experience_match
            + 0.10 * features.behavioral_score
            + 0.10 * features.availability_score
            + 0.05 * features.profile_quality_score
            + 0.05 * features.engagement_score
        )


        return final_score