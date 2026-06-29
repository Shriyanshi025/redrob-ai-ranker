import csv
from pathlib import Path

SUBMISSION_FILE = (
    Path("submissions")
    / "submission.csv"
)


def main():
    if not SUBMISSION_FILE.exists():
        print("Submission file not found.")
        return

    with open(
        SUBMISSION_FILE,
        "r",
        encoding="utf-8",
    ) as f:
        rows = list(csv.DictReader(f))

    print(f"Rows: {len(rows)}")

    ids = [
        row["candidate_id"]
        for row in rows
    ]

    unique_ids = len(set(ids))

    print(f"Unique IDs: {unique_ids}")

    if len(rows) != unique_ids:
        print("Duplicate candidate IDs found.")
    else:
        print("No duplicates found.")

    scores = [
        float(row["score"])
        for row in rows
    ]

    print(
        f"Highest score: {max(scores):.6f}"
    )
    print(
        f"Lowest score: {min(scores):.6f}"
    )

    print(
        "Submission validation completed."
    )


if __name__ == "__main__":
    main()