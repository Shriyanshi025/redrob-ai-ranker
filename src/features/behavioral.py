"""
Behavioral and availability scoring.
"""


def calculate_behavioral_score(candidate: dict) -> float:
    signals = candidate.get("redrob_signals", {})

    score = 0.0

    if signals.get("open_to_work_flag"):
        score += 0.35

    response_rate = signals.get(
        "recruiter_response_rate",
        0.0,
    )
    score += response_rate * 0.30

    interview_rate = signals.get(
        "interview_completion_rate",
        0.0,
    )
    score += interview_rate * 0.20

    if signals.get("verified_email"):
        score += 0.05

    if signals.get("verified_phone"):
        score += 0.05

    if signals.get("linkedin_connected"):
        score += 0.05

    return min(score, 1.0)
