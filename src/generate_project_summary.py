import json
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    metrics = load_json(
        "outputs/system_metrics.json"
    )

    ranking = load_json(
        "outputs/ranking_analysis.json"
    )

    dataset = load_json(
        "outputs/dataset_stats.json"
    )

    report = {
        "project_name":
            "Redrob AI Ranker",

        "pipeline_status":
            metrics["pipeline_status"],

        "dataset_size":
            dataset["total_candidates"],

        "average_experience":
            dataset["average_experience"],

        "highest_score":
            ranking["highest_score"],

        "top_100_cutoff":
            ranking["top_100_cutoff"],

        "runtime_seconds":
            metrics["runtime_seconds"],

        "generated_reports": [
            "submission.csv",
            "top_candidates_with_insights.json",
            "recruiter_report.json",
            "system_metrics.json",
            "dataset_stats.json",
            "ranking_analysis.json",
        ],
    }

    output = (
        Path("outputs")
        / "project_summary.json"
    )

    with open(
        output,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            report,
            f,
            indent=2,
        )

    print(f"Saved: {output}")


if __name__ == "__main__":
    main()