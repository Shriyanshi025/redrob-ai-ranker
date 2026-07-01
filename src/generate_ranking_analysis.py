import json
from pathlib import Path
from statistics import mean, median

from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)


def main():
    pipeline = CandidateRankingPipeline()

    results = pipeline.run(top_k=100000)

    scores = [score for score, _ in results]

    analysis = {
        "total_candidates": len(scores),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "average_score": round(mean(scores), 6),
        "median_score": round(median(scores), 6),
        "top_100_cutoff": round(scores[99], 6),
        "top_1000_cutoff": round(scores[999], 6),
        "top_10000_cutoff": round(scores[9999], 6),
    }

    output = Path("outputs") / "ranking_analysis.json"

    with open(
        output,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(analysis, f, indent=2)

    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
