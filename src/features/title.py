AI_TITLES = {
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "applied scientist",
    "nlp engineer",
    "data scientist",
    "search engineer",
    "recommendation engineer",
    "research engineer",
}


def calculate_title_match(candidate: dict) -> float:
    title = candidate["profile"].get("current_title", "").lower()

    for target in AI_TITLES:
        if target in title:
            return 1.0

    return 0.0
