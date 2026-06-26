"""
Feature Extraction Engine

Converts candidate profiles into structured numerical features
for the ranking engine.
"""

from dataclasses import dataclass


@dataclass
class CandidateFeatures:
    candidate_id: str

    experience_score: float

    skill_score: float

    education_score: float

    activity_score: float

    profile_score: float

    career_score: float

    final_score: float = 0.0