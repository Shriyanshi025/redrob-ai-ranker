"""
Common utilities for dataset analysis.

This module provides shared functionality used by all analysis scripts,
including path management, logging, file saving, timing, and formatting.

Phase:
    Dataset Intelligence
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
REPORT_DIR = PROJECT_ROOT / "analysis" / "reports"
STATISTICS_DIR = PROJECT_ROOT / "analysis" / "statistics"
PLOTS_DIR = PROJECT_ROOT / "analysis" / "plots"


# =============================================================================
# Logging
# =============================================================================


def setup_logging() -> logging.Logger:
    """
    Configure and return the project logger.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )

    return logging.getLogger(__name__)


# =============================================================================
# File Saving Utilities
# =============================================================================


def save_json(data: Any, output_path: Path) -> None:
    """
    Save data as formatted JSON.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def save_markdown(content: str, output_path: Path) -> None:
    """
    Save markdown report.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        content,
        encoding="utf-8",
    )


# =============================================================================
# Formatting Utilities
# =============================================================================


def human_readable_size(size_bytes: int) -> str:
    """
    Convert bytes into a human-readable string.
    """

    units = ["Bytes", "KB", "MB", "GB", "TB"]

    size = float(size_bytes)

    for unit in units:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


# =============================================================================
# Timer
# =============================================================================


class Timer:
    """
    Simple execution timer.
    """

    def __init__(self) -> None:
        self.start_time = time.perf_counter()

    def elapsed(self) -> float:
        """
        Return elapsed time in seconds.
        """
        return time.perf_counter() - self.start_time
