"""
Experience feature scoring.
"""

from src.core.job_parser import JobRequirements


def calculate_experience_match(
    candidate: dict,
    job: JobRequirements,
) -> float:
    """
    Returns a score between 0.0 and 1.0 based on how well the
    candidate's experience matches the job requirement.
    """

    years = candidate["profile"]["years_of_experience"]
    required = job.minimum_experience

    if required <= 0:
        return 1.0

    ratio = years / required

    return min(ratio, 1.0)
