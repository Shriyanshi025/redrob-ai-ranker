from src.core.job_analyzer import JobAnalyzer
from src.core.job_loader import load_job_description
from src.features.feature_builder import (
    FeatureBuilder,
)
from src.ranker.ranker import CandidateRanker
from src.retrieval.candidate_retriever import (
    CandidateRetriever,
)
from src.config.constants import JOB_DESCRIPTION_PATH


class CandidateRankingPipeline:

    def run(self, top_k: int = 10):

        job_text = load_job_description(
            JOB_DESCRIPTION_PATH
        )

        job = JobAnalyzer().parse(job_text)

        retriever = CandidateRetriever()
        builder = FeatureBuilder()
        ranker = CandidateRanker()

        results = []

        for candidate in retriever.stream_candidates():

            features = builder.build(
                candidate,
                job,
            )

            score = ranker.score(features)

            results.append(
                (
                    score,
                    candidate["candidate_id"],
                )
            )

        results.sort(
            reverse=True,
            key=lambda x: x[0],
        )

        return results[:top_k]