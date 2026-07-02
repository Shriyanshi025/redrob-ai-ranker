"""
Candidate Retrieval Engine
"""

import json

from src.config.constants import CANDIDATE_DATASET


class CandidateRetriever:
    def stream_candidates(self):
        if not CANDIDATE_DATASET.exists():
            raise FileNotFoundError(f"""
Dataset not found.

Please download candidates.jsonl from the GitHub Releases page:

https://github.com/Shriyanshi025/redrob-ai-ranker/releases

Then place it here:

{CANDIDATE_DATASET}

Expected structure:

project_root/
└── data/
    └── candidates.jsonl
""")

        with CANDIDATE_DATASET.open(
            "r",
            encoding="utf-8",
        ) as file:
            for line in file:
                if line.strip():
                    yield json.loads(line)

    def get_all_candidates(self):
        return list(self.stream_candidates())
