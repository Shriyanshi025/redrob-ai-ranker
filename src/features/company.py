PRODUCT_COMPANIES = {
    "google",
    "meta",
    "flipkart",
    "cred",
    "netflix",
    "zomato",
    "linkedin",
    "freshworks",
    "yellow.ai",
    "sarvam ai",
    "salesforce",
    "paytm",
    "unacademy",
    "haptik",
}


def calculate_company_score(
    candidate: dict,
) -> float:
    history = candidate.get(
        "career_history",
        []
    )

    for job in history:
        company = (
            job.get("company", "")
            .lower()
            .strip()
        )

        if company in PRODUCT_COMPANIES:
            return 1.0

    return 0.0