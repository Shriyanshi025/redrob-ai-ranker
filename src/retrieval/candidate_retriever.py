"""
Candidate Retrieval Engine
"""

import json

from src.config.constants import CANDIDATE_DATASET


class CandidateRetriever:

    def stream_candidates(self):
        with CANDIDATE_DATASET.open(
            "r",
            encoding="utf-8",
        ) as file:
            for line in file:
                if line.strip():
                    yield json.loads(line)

    def get_all_candidates(self):
        return list(self.stream_candidates())
