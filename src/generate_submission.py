from pathlib import Path
import csv

from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)

OUTPUT_FILE = Path("submissions") / "submission.csv"


def main():
    pipeline = CandidateRankingPipeline()

    print("Running ranking pipeline...")
    results = pipeline.run(top_k=100000)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(f"Writing {len(results)} candidates...")

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.writer(f)

        writer.writerow(
            [
                "rank",
                "candidate_id",
                "score",
            ]
        )

        for rank, (
            score,
            candidate_id,
        ) in enumerate(
            results,
            start=1,
        ):
            writer.writerow(
                [
                    rank,
                    candidate_id,
                    round(score, 6),
                ]
            )

    print(f"Saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
