# System Architecture

```text
Candidate JSON
       ↓
Candidate Retriever
       ↓
Feature Extraction
       ↓
Skill Scoring
       ↓
Experience Scoring
       ↓
Role Alignment
       ↓
Career Signals
       ↓
Final Weighted Score
       ↓
Candidate Ranking
       ↓
submission.csv
```

## Components

### Candidate Retriever
Streams candidate profiles efficiently.

### Feature Extractor
Converts raw profiles into ranking features.

### Ranking Engine
Computes final candidate score.

### Submission Generator
Creates final ranked output.