from src.features.feature_builder import CandidateFeatureVector


class CandidateRanker:

    def score(
        self,
        features: CandidateFeatureVector,
    ) -> float:

        return 0.0