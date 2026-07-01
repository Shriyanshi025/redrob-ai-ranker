"""
Project-wide constants for the Candidate Ranking Engine.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

DOCS_DIR = PROJECT_ROOT / "docs"
JOB_DESCRIPTION_PATH = DOCS_DIR / "job_description.docx"

CANDIDATE_DATASET = DATA_DIR / "candidates.jsonl"

TOP_K_DEFAULT = 100

MAX_EXPERIENCE_YEARS = 30

MIN_PROFILE_COMPLETENESS = 60

EXPERIENCE_NORMALIZATION = 30.0

SKILL_PROFICIENCY = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4,
}

WORK_MODE_PRIORITY = {
    "remote": 1,
    "hybrid": 2,
    "onsite": 3,
    "flexible": 4,
}
