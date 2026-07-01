from dataclasses import dataclass, field


@dataclass
class JobRequirements:
    title: str = ""

    required_skills: list[str] = field(default_factory=list)

    preferred_skills: list[str] = field(default_factory=list)

    minimum_experience: float = 0.0

    preferred_education: list[str] = field(default_factory=list)

    industries: list[str] = field(default_factory=list)

    work_mode: str = ""

    keywords: list[str] = field(default_factory=list)

    summary: str = ""

    responsibilities: list[str] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    location: str = ""

    employment_type: str = ""
