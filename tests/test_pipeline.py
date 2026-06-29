from src.pipeline.pipeline import (
    CandidateRankingPipeline,
)


def main():
    pipeline = CandidateRankingPipeline()

    results = pipeline.run(
        top_k=100000
    )

    print(
        f"Results: {len(results)}"
    )

    assert len(results) == 100000

    scores = [
        score
        for score, _
        in results
    ]

    assert scores == sorted(
        scores,
        reverse=True,
    )

    ids = [
        candidate_id
        for _, candidate_id
        in results
    ]

    assert len(ids) == len(
        set(ids)
    )

    print(
        "Pipeline test passed."
    )


if __name__ == "__main__":
    main()