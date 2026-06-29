from pathlib import Path


FILES = [
    "outputs/top_candidates_with_insights.json",
    "outputs/recruiter_report.json",
    "outputs/system_metrics.json",
]


def main():
    for file in FILES:
        path = Path(file)

        assert path.exists()

        assert (
            path.stat().st_size > 0
        )

        print(
            f"Found: {file}"
        )

    print(
        "Reports test passed."
    )


if __name__ == "__main__":
    main()