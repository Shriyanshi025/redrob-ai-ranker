"""
Behavioral and platform signal scoring.
"""


def calculate_availability_score(candidate: dict) -> float:
    signals = candidate["redrob_signals"]

    score = 0.0

    if signals.get("open_to_work_flag"):
        score += 0.5

    notice = signals.get(
        "notice_period_days",
        90,
    )

    if notice <= 30:
        score += 0.3
    elif notice <= 60:
        score += 0.2
    else:
        score += 0.1

    if signals.get("willing_to_relocate"):
        score += 0.2

    return min(score, 1.0)


def calculate_profile_quality_score(
    candidate: dict,
) -> float:
    signals = candidate["redrob_signals"]

    return (
        signals.get(
            "profile_completeness_score",
            0,
        )
        / 100.0
    )


def calculate_engagement_score(
    candidate: dict,
) -> float:
    signals = candidate["redrob_signals"]

    response = signals.get(
        "recruiter_response_rate",
        0,
    )

    interview = signals.get(
        "interview_completion_rate",
        0,
    )

    acceptance = signals.get(
        "offer_acceptance_rate",
        0,
    )

    return 0.4 * response + 0.3 * interview + 0.3 * acceptance
