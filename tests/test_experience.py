from src.features.experience import calculate_experience_match
from src.core.job_parser import JobRequirements

candidate = {
    "profile": {
        "years_of_experience": 8,
    }
}

job = JobRequirements(minimum_experience=5)

print(calculate_experience_match(candidate, job))
