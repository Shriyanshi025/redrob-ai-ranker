"""
Dataset Overview Analysis

Phase:
    0.5.1 Dataset Intelligence

Purpose:
    Perform structural validation and high-level analysis of the
    candidates dataset.

Outputs:
    - analysis/statistics/dataset_stats.json
    - analysis/reports/dataset_overview_report.md
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from analysis.common import (
    DATA_DIR,
    REPORT_DIR,
    STATISTICS_DIR,
    Timer,
    human_readable_size,
    save_json,
    save_markdown,
    setup_logging,
)

logger = setup_logging()

DATASET_PATH = DATA_DIR / "candidates.jsonl"

REPORT_PATH = REPORT_DIR / "dataset_overview_report.md"

STATISTICS_PATH = STATISTICS_DIR / "dataset_stats.json"

REQUIRED_FIELDS = (
    "candidate_id",
    "profile",
    "career_history",
    "education",
    "skills",
    "redrob_signals",
)


@dataclass
class DatasetStatistics:
    total_records: int = 0
    valid_records: int = 0
    invalid_records: int = 0
    empty_lines: int = 0

    smallest_record_size: float = field(default_factory=lambda: float("inf"))
    largest_record_size: int = 0
    total_record_size: int = 0

    processing_time_seconds: float = 0.0

    required_field_presence: dict[str, int] = field(
        default_factory=lambda: {
            field_name: 0
            for field_name in REQUIRED_FIELDS
        }
    )

    @property
    def average_record_size(self) -> float:
        if self.valid_records == 0:
            return 0.0

        return self.total_record_size / self.valid_records


def validate_json_line(line: str) -> dict | None:
    try:
        return json.loads(line)
    except Exception:
        return None


def get_record_size(line: str) -> int:
    return len(line.encode("utf-8"))


def check_required_fields(record: dict) -> dict[str, bool]:
    return {
        field: field in record
        for field in REQUIRED_FIELDS
    }


def analyze_dataset(file_path: Path) -> DatasetStatistics:
    stats = DatasetStatistics()
    timer = Timer()

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                stats.empty_lines += 1
                continue

            stats.total_records += 1

            size = get_record_size(line)
            stats.total_record_size += size

            stats.smallest_record_size = min(stats.smallest_record_size, size)
            stats.largest_record_size = max(stats.largest_record_size, size)

            record = validate_json_line(line)

            if not record:
                stats.invalid_records += 1
                continue

            stats.valid_records += 1

            field_check = check_required_fields(record)

            for k, v in field_check.items():
                if v:
                    stats.required_field_presence[k] += 1

    stats.processing_time_seconds = timer.elapsed()
    return stats


def generate_markdown_report(stats: DatasetStatistics) -> str:
    smallest_size = (
        0 if stats.smallest_record_size == float("inf")
        else stats.smallest_record_size
    )

    return f"""# Dataset Overview Report

## Summary

- Total Records: {stats.total_records}
- Valid Records: {stats.valid_records}
- Invalid Records: {stats.invalid_records}
- Empty Lines: {stats.empty_lines}

## Record Size

- Smallest: {human_readable_size(int(smallest_size))}
- Largest: {human_readable_size(stats.largest_record_size)}
- Average: {human_readable_size(int(stats.average_record_size))}

## Required Field Presence

{chr(10).join(f"- {k}: {v}" for k, v in stats.required_field_presence.items())}

## Processing

- Time: {stats.processing_time_seconds:.2f} seconds
"""


def main() -> None:
    logger.info("Starting dataset overview...")

    stats = analyze_dataset(DATASET_PATH)

    save_json(asdict(stats), STATISTICS_PATH)

    report = generate_markdown_report(stats)
    save_markdown(report, REPORT_PATH)

    logger.info("Analysis completed successfully.")
    logger.info(f"Valid Records: {stats.valid_records}")
    logger.info(f"Invalid Records: {stats.invalid_records}")


if __name__ == "__main__":
    main()