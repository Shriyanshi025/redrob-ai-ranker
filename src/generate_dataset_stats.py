import json
from collections import Counter
from pathlib import Path

from src.retrieval.candidate_retriever import (
    CandidateRetriever,
)


def main():
    retriever = CandidateRetriever()

    total = 0
    experience = []

    skills = Counter()
    titles = Counter()

    for c in retriever.stream_candidates():
        total += 1

        profile = c.get(
            "profile",
            {}
        )

        years = profile.get(
            "years_of_experience",
            0,
        )

        experience.append(
            years
        )

        title = profile.get(
            "current_title",
            "Unknown",
        )

        titles[title] += 1

        for skill in c.get(
            "skills",
            []
        ):
            skills[
                skill.get(
                    "name",
                    "Unknown"
                )
            ] += 1

    stats = {
        "total_candidates": total,
        "average_experience":
            round(
                sum(experience)
                / max(total, 1),
                2,
            ),
        "top_skills":
            skills.most_common(10),
        "top_titles":
            titles.most_common(10),
    }

    output_dir = Path(
        "outputs"
    )

    output_dir.mkdir(
        exist_ok=True
    )

    output_file = (
        output_dir
        / "dataset_stats.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            stats,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(
        f"Saved: {output_file}"
    )


if __name__ == "__main__":
    main()