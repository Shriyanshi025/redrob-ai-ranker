# 🧠 Redrob AI Candidate Ranking System

> AI-powered candidate ranking system that ranks candidates the way an experienced recruiter would — beyond simple keyword matching.

---

## 🚀 Overview

Recruiters often rely on keyword-based filtering systems that fail to capture true candidate suitability.

This project introduces an **AI-powered candidate ranking system** capable of understanding:

- Job descriptions semantically (not just keywords)
- Candidate career trajectories and progression
- Skill relevance and experience depth
- Behavioral and profile quality signals
- Contextual alignment between candidates and roles

The system generates a trustworthy ranked shortlist of candidates by combining semantic job understanding, candidate signals, and explainable multi-factor scoring.

---

## 🎯 Problem Statement

Traditional hiring systems:

- Depend heavily on keyword matching
- Ignore career progression and context
- Fail to interpret behavioral signals
- Produce incomplete or biased shortlists

This solution addresses these limitations using an **AI-driven multi-signal candidate ranking framework**.

---

## 🧠 Solution Approach

### 1️⃣ Job Understanding

- Parses job descriptions into structured requirements
- Extracts:
  - Skills
  - Experience requirements
  - Role expectations
  - Hiring signals

### 2️⃣ Candidate Feature Engineering

Each candidate is analyzed across multiple dimensions:

- Skill Match
- Experience Relevance
- Career Progression
- Company Signals
- Profile Quality Indicators
- Retrieval Similarity Features

### 3️⃣ Retrieval & Ranking

The system performs:

- Efficient candidate retrieval
- Multi-signal feature scoring
- Weighted ranking
- Final candidate ordering

### 4️⃣ Explainability Layer

Generates human-readable explanations describing:

- Why a candidate ranked highly
- Which signals contributed most
- Areas of strength and potential gaps

---

## 🏗️ System Architecture

```text
Job Description
        ↓
Job Parser + Analyzer
        ↓
Feature Extraction Layer
        ↓
Candidate Retrieval Engine
        ↓
Multi-Signal Ranking Model
        ↓
Explainability Engine
        ↓
Final Ranked Output
```

---

## ⚙️ Key Modules

| Module | Purpose |
|---------|----------|
| `src/core` | Job parsing and understanding |
| `src/features` | Feature engineering pipeline |
| `src/retrieval` | Candidate retrieval system |
| `src/ranker` | Candidate scoring and ranking |
| `src/explainability` | Ranking explanation generation |
| `src/intelligence` | Skill gap analysis and role recommendation |
| `src/pipeline` | End-to-end orchestration |

---

## 📂 Repository Structure

```text
src/
├── config/
├── core/
├── explainability/
├── features/
├── intelligence/
├── pipeline/
├── ranker/
├── retrieval/
├── utils/
├── generate_candidate_insights.py
├── generate_dataset_stats.py
├── generate_project_summary.py
├── generate_ranking_analysis.py
├── generate_recruiter_report.py
├── generate_submission.py
├── generate_system_metrics.py
├── main.py
├── run_pipeline.py
└── validate_submission.py

analysis/
docs/
tests/
outputs/
submissions/
data/
```

---

## 📊 Generated Outputs

The system automatically generates:

- `submissions/submission.csv`
- `outputs/recruiter_report.json`
- `outputs/top_candidates_with_insights.json`
- `outputs/ranking_analysis.json`
- `outputs/system_metrics.json`
- `outputs/project_summary.json`

---

## 📁 Dataset

The dataset is large and therefore provided separately through **GitHub Releases**.

### Download Dataset

➡️ **Releases Page**

https://github.com/Shriyanshi025/redrob-ai-ranker/releases

After downloading, place the file here:

```text
project_root/
└── data/
    └── candidates.jsonl
```

---

## 💻 Requirements

- Python 3.10+
- 4GB+ RAM recommended
- Windows, Linux, or macOS

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/Shriyanshi025/redrob-ai-ranker
cd redrob-ai-ranker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Pipeline

### Run Complete Ranking Pipeline

```bash
python -m src.run_pipeline
```

### Generate Submission File

```bash
python -m src.generate_submission
```

### Validate Submission

```bash
python -m src.validate_submission
```

---

## 🧪 Running Tests

```bash
python -m tests.test_pipeline
python -m tests.test_submission
python -m tests.test_reports
python -m tests.test_ranking_analysis
python -m tests.test_project_summary
```

---

## 🔍 Code Quality Checks

```bash
python -m ruff check .
python -m black --check .
python -m radon cc src -a
python -m radon mi src
```

---

## ✅ Quality Metrics

- Ruff Linting: Passed ✅
- Black Formatting: Passed ✅
- Automated Tests: Passed ✅
- Average Cyclomatic Complexity: **A (2.97)** ✅
- Maintainability Index: **A** ✅
- Successfully processes 100,000 candidate profiles within challenge constraints ✅

---

## 📦 Included Deliverables

- ✅ Complete Source Code
- ✅ Presentation Deck (PDF)
- ✅ Ranked Candidate Submission File
- ✅ Recruiter Reports
- ✅ Candidate Insights
- ✅ Ranking Analytics
- ✅ System Metrics

---

## 🎯 Challenge Alignment

This solution satisfies all challenge requirements by:

- ✅ Understanding job descriptions semantically
- ✅ Evaluating candidates beyond keyword matching
- ✅ Combining multiple candidate signals
- ✅ Producing explainable rankings
- ✅ Delivering recruiter-ready candidate shortlists

---

## 📈 Evaluation Summary

The project successfully demonstrates:

- Semantic understanding of job requirements
- Multi-factor candidate ranking
- Explainable recommendations
- Scalable processing of 100,000 candidate profiles
- Fully reproducible pipeline and outputs
- Clean, tested, and maintainable codebase

---

## 👩‍💻 Developer

**Shriyanshi Sinha**  
**Team Name:** Kernel.One  
**Participation:** Individual Participant

Built for the **Redrob AI Candidate Ranking Challenge**.

---

## 📄 License

This project has been developed solely for educational and competition purposes.