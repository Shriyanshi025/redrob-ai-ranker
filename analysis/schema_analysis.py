"""
Schema Analysis

Purpose:
    Analyze the real schema of the candidate dataset.

Outputs:
    - analysis/statistics/schema_stats.json
    - analysis/reports/schema_report.md
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field

from analysis.common import (
    DATA_DIR,
    REPORT_DIR,
    STATISTICS_DIR,
    Timer,
    save_json,
    save_markdown,
    setup_logging,
)

logger = setup_logging()

DATASET_PATH = DATA_DIR / "candidates.jsonl"
REPORT_PATH = REPORT_DIR / "schema_report.md"
STATISTICS_PATH = STATISTICS_DIR / "schema_stats.json"


@dataclass
class SchemaStatistics:
    total_records: int = 0

    top_level_keys: dict[str, int] = field(default_factory=dict)

    profile_keys: dict[str, int] = field(default_factory=dict)

    redrob_signal_keys: dict[str, int] = field(default_factory=dict)

    max_career_entries: int = 0
    min_career_entries: int = 10**9

    max_education_entries: int = 0
    min_education_entries: int = 10**9

    max_skill_entries: int = 0
    min_skill_entries: int = 10**9

    processing_time_seconds: float = 0.0


def analyze_schema() -> SchemaStatistics:
    stats = SchemaStatistics()
    timer = Timer()

    with DATASET_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            record = json.loads(line)
            stats.total_records += 1

            # Top-level keys
            for key in record:
                stats.top_level_keys[key] = stats.top_level_keys.get(key, 0) + 1

            # Profile keys
            profile = record.get("profile", {})
            for key in profile:
                stats.profile_keys[key] = stats.profile_keys.get(key, 0) + 1

            # Redrob signal keys
            signals = record.get("redrob_signals", {})
            for key in signals:
                stats.redrob_signal_keys[key] = stats.redrob_signal_keys.get(key, 0) + 1

            # Career history
            career_count = len(record.get("career_history", []))
            stats.max_career_entries = max(
                stats.max_career_entries,
                career_count,
            )
            stats.min_career_entries = min(
                stats.min_career_entries,
                career_count,
            )

            # Education
            education_count = len(record.get("education", []))
            stats.max_education_entries = max(
                stats.max_education_entries,
                education_count,
            )
            stats.min_education_entries = min(
                stats.min_education_entries,
                education_count,
            )

            # Skills
            skills_count = len(record.get("skills", []))
            stats.max_skill_entries = max(
                stats.max_skill_entries,
                skills_count,
            )
            stats.min_skill_entries = min(
                stats.min_skill_entries,
                skills_count,
            )

    stats.processing_time_seconds = timer.elapsed()
    return stats


def generate_report(stats: SchemaStatistics) -> str:
    return f"""# Schema Analysis Report

Total Records: {stats.total_records}

## Top Level Keys

{chr(10).join(f"- {k}: {v}" for k, v in stats.top_level_keys.items())}

## Profile Keys

{chr(10).join(f"- {k}: {v}" for k, v in stats.profile_keys.items())}

## Redrob Signal Keys

{chr(10).join(f"- {k}: {v}" for k, v in stats.redrob_signal_keys.items())}

Career History
- Min Entries: {stats.min_career_entries}
- Max Entries: {stats.max_career_entries}

Education
- Min Entries: {stats.min_education_entries}
- Max Entries: {stats.max_education_entries}

Skills
- Min Entries: {stats.min_skill_entries}
- Max Entries: {stats.max_skill_entries}

Processing Time: {stats.processing_time_seconds:.2f} seconds
"""


def main() -> None:
    logger.info("Starting schema analysis...")

    stats = analyze_schema()

    save_json(asdict(stats), STATISTICS_PATH)
    save_markdown(generate_report(stats), REPORT_PATH)

    logger.info("Schema analysis completed.")


if __name__ == "__main__":
    main()
