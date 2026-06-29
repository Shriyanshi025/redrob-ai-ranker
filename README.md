# AI Talent Intelligence Platform

An AI-powered candidate ranking and talent intelligence system that identifies the most relevant candidates for modern AI/ML roles.

## Problem Statement

Recruiters spend significant time manually screening thousands of resumes and profiles. Traditional keyword-based filtering often misses strong candidates and ranks irrelevant profiles highly.

This project builds an intelligent ranking engine that evaluates candidates using:

- Skills relevance
- Experience alignment
- Role similarity
- Production AI expertise
- Retrieval and LLM capabilities
- Career signals

## Features

- Rank 100,000+ candidates
- Hybrid scoring pipeline
- Semantic skill matching
- Experience normalization
- AI/ML domain understanding
- Explainable ranking
- Role Recommendation
- Skill Gap Analysis
- Recruiter Reports
- System Metrics
- Production-ready pipeline

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- JSON
- CSV

## Project Structure

```text
src/
tests/
docs/
submissions/
```

## Running

```bash
python -m src.run_pipeline
python -m src.generate_submission
python -m src.generate_candidate_insights
python -m src.generate_recruiter_report
python -m src.generate_system_metrics
```

## Output

```text
submission.csv
rank,candidate_id,score
```

## Future Scope

- Recruiter copilot
- Skill-gap analysis
- Interview recommendations
- Personalized hiring insights
- Explainable AI recommendations