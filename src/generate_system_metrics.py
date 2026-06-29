import json
import time
from pathlib import Path

from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)


def main():
    start = time.time()

    pipeline = CandidateRankingPipeline()

    results = pipeline.run(
        top_k=100
    )

    runtime = round(
        time.time() - start,
        2,
    )

    scores = [
        score
        for score, _
        in results
    ]

    metrics = {
        "pipeline_status": "success",
        "total_top_candidates": len(
            results
        ),
        "highest_score": round(
            max(scores),
            6,
        ),
        "lowest_score": round(
            min(scores),
            6,
        ),
        "average_score": round(
            sum(scores) / len(scores),
            6,
        ),
        "runtime_seconds": runtime,
    }

    output_dir = Path("outputs")
    output_dir.mkdir(
        exist_ok=True
    )

    output_file = (
        output_dir /
        "system_metrics.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            metrics,
            f,
            indent=2,
        )

    print(
        f"Saved: {output_file}"
    )


if __name__ == "__main__":
    main()