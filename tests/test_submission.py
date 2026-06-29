import csv
from pathlib import Path


SUBMISSION_FILE = (
    Path("submissions")
    / "submission.csv"
)


def main():
    assert SUBMISSION_FILE.exists()

    with open(
        SUBMISSION_FILE,
        "r",
        encoding="utf-8",
    ) as f:
        rows = list(
            csv.DictReader(f)
        )

    assert len(rows) == 100000

    expected_columns = {
        "rank",
        "candidate_id",
        "score",
    }

    assert (
        set(rows[0].keys())
        == expected_columns
    )

    assert (
        rows[0]["rank"]
        == "1"
    )

    assert (
        rows[-1]["rank"]
        == "100000"
    )

    print(
        "Submission test passed."
    )


if __name__ == "__main__":
    main()