class CandidateRanker:

    def score(
        self,
        features,
    ) -> float:

        capability_score = (
            0.35 * features.skill_score
            + 0.30 * features.retrieval_score
            + 0.20 * features.career_score
            + 0.15 * features.experience_match
        )

        fit_score = 0.65 * features.title_match + 0.35 * features.company_score

        hireability_score = (
            0.45 * features.behavioral_score
            + 0.35 * features.availability_score
            + 0.20 * features.engagement_score
        )

        final_score = (
            0.60 * capability_score + 0.33 * fit_score + 0.07 * hireability_score
        )

        return final_score
