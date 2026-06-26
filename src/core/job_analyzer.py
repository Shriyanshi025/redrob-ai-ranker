"""
Job Description Analyzer

Converts raw JD text into structured requirements.
"""

import re

from src.core.job_parser import JobRequirements


class JobAnalyzer:

    def parse(self, text: str) -> JobRequirements:

        requirements = JobRequirements()

        requirements.summary = text

        experience = re.search(
            r"(\d+(?:\.\d+)?)\+?\s*(?:years|yrs)",
            text,
            flags=re.IGNORECASE,
        )

        if experience:
            requirements.minimum_experience = float(
                experience.group(1)
            )

        return requirements