# PROJECT MASTER PLAN

**Version:** 1.0
**Project Name:** Redrob AI Ranker – Intelligent Candidate Discovery & Ranking System
**Challenge:** India Runs Data & AI Challenge – Intelligent Candidate Discovery
**Repository:** redrob-ai-ranker
**Project Type:** AI/ML Ranking System

---

# 1. Project Overview

## Objective

Build a robust, explainable, and efficient AI-powered candidate ranking system capable of understanding complex job descriptions, evaluating candidate profiles beyond keyword matching, integrating behavioral and technical signals, and producing a highly accurate Top-100 ranked shortlist with evidence-based reasoning.

The system must strictly follow the official challenge specifications while remaining reproducible, interview-defendable, and optimized for the provided runtime constraints.

---

## Primary Goal

Design a production-quality Proof of Concept that behaves like an intelligent recruiter instead of a traditional resume filtering system.

The solution should prioritize semantic understanding, contextual reasoning, behavioral intelligence, profile consistency validation, and explainable decision making.

---

## Project Philosophy

Every implementation decision must be traceable to an official challenge requirement.

No feature will be implemented without a clear purpose.

Architecture will be finalized before implementation.

Each development phase must be validated before moving to the next phase.

The project will prioritize correctness, explainability, maintainability, reproducibility, and efficient execution over unnecessary complexity.

---

## Submission Target

Deliver a submission that is:

* Technically accurate
* Semantically intelligent
* Runtime efficient
* Explainable
* Reproducible
* Fully aligned with the official challenge evaluation process

The objective is not only to produce a strong ranking but also to build a system that can withstand manual review and technical interviews.


# 2. Challenge Summary

## Challenge Statement

The objective of this challenge is to build an intelligent AI-powered candidate discovery and ranking system capable of identifying the most suitable candidates for a given job description.

Unlike traditional resume filtering systems, the solution must understand the intent of the job description, evaluate semantic relevance instead of relying on keyword matching, integrate technical and behavioral signals, and produce a highly accurate and explainable Top-100 ranked shortlist.

---

## Core Problem

Traditional Applicant Tracking Systems primarily depend on keyword matching.

This challenge requires designing an intelligent ranking engine that understands:

* candidate capability
* career progression
* production experience
* contextual relevance
* behavioral indicators
* recruiter engagement
* profile consistency

The ranking should reflect the overall hiring suitability of a candidate rather than simple textual similarity.

---

## Expected System Capabilities

The final system should be capable of:

* Understanding complex job descriptions.
* Identifying implicit hiring requirements.
* Evaluating candidates semantically.
* Distinguishing between research and production experience.
* Understanding career progression.
* Combining technical and behavioral evidence.
* Detecting inconsistent or suspicious candidate profiles.
* Producing explainable ranking decisions.
* Ranking candidates within the official runtime constraints.

---

## Available Candidate Information

The ranking system has access to multiple categories of information including:

* Candidate profile
* Career history
* Education
* Skills
* Certifications
* Languages
* Behavioral signals from the Redrob platform

These information sources must be evaluated collectively instead of independently.

---

## Evaluation Philosophy

The objective is not to maximize keyword overlap.

The objective is to estimate overall candidate suitability using multiple evidence sources while remaining explainable, reproducible, and aligned with the official challenge specifications.

---

## Engineering Interpretation

From an engineering perspective, this project is not a search engine.

It is a multi-factor intelligent ranking system.

Every candidate should be evaluated using several complementary dimensions instead of a single similarity score.

The final ranking should represent a balanced assessment of technical capability, contextual relevance, behavioral quality, profile credibility, and hiring readiness.

---

## Project Success Definition

The project will be considered successful only if the final solution:

* Produces highly relevant rankings.
* Generates explainable ranking decisions.
* Detects inconsistent candidate profiles.
* Avoids keyword-only ranking.
* Integrates behavioral intelligence.
* Remains computationally efficient.
* Can be defended during technical review.
* Fully complies with the official challenge requirements.



# 3. Official Constraints

This section contains the official constraints and requirements that govern the design and implementation of the ranking system. Every architectural and implementation decision must comply with these constraints.

---

## Functional Constraints

The system must:

* Accept a job description as input.
* Process the complete candidate dataset.
* Intelligently rank candidates instead of performing simple filtering.
* Produce the required ranked output in the official submission format.
* Generate explainable ranking decisions that are supported by candidate data.
* Integrate multiple sources of candidate information rather than relying on a single feature.

---

## Ranking Constraints

The ranking process must:

* Go beyond keyword matching.
* Evaluate contextual and semantic relevance.
* Consider both technical and behavioral evidence.
* Assess overall hiring suitability rather than textual similarity alone.
* Produce consistent and reproducible rankings for the same inputs.

---

## Data Constraints

The system must correctly utilize the available structured information, including:

* Candidate profile
* Career history
* Education
* Skills
* Certifications (when available)
* Languages (when available)
* Redrob platform behavioral signals

Missing or optional fields should be handled gracefully without causing failures or invalid rankings.

---

## Explainability Constraints

Every ranking decision should be explainable.

Explanations must:

* Be grounded in available candidate information.
* Reflect actual evidence used during ranking.
* Avoid unsupported assumptions or fabricated reasoning.
* Remain consistent with the calculated ranking.

---

## Quality Constraints

The implementation should prioritize:

* Correctness
* Robustness
* Maintainability
* Reproducibility
* Efficient resource utilization
* Deterministic behavior whenever applicable

---

## Compliance Rules

The project must remain aligned with the official challenge requirements throughout development.

Any implementation that conflicts with the published specifications must be rejected or redesigned before integration.

Whenever uncertainty exists, the official challenge documentation takes precedence over implementation convenience.

---

## Engineering Principle

Official challenge requirements are the highest authority for this project.

Architecture, algorithms, optimizations, and implementation details must always support the challenge objectives rather than replacing or redefining them.

---

## Phase 0 Checkpoint

Before moving to the next section, verify:

* [ ] All identified constraints originate from the official challenge requirements.
* [ ] No implementation decisions have been mixed with official constraints.
* [ ] Every future module can be validated against this section.
* [ ] Any ambiguity will be resolved by referring back to the official documentation before implementation.



# 4. Success Criteria

This section defines the measurable objectives that the project must satisfy before it is considered ready for final submission.

These criteria serve as the internal quality benchmark for every implementation phase.

---

## Functional Success

The system should successfully:

* Parse and understand a given job description.
* Process the complete candidate dataset without failures.
* Evaluate every candidate using multiple evidence sources.
* Produce a ranked shortlist in the required submission format.
* Generate evidence-based explanations for ranking decisions.

---

## Intelligence Success

The ranking system should demonstrate:

* Semantic understanding beyond keyword matching.
* Context-aware candidate evaluation.
* Multi-factor decision making.
* Appropriate use of behavioral signals.
* Recognition of career progression and relevant experience.
* Consistent treatment of similar candidate profiles.

---

## Engineering Success

The implementation should be:

* Modular.
* Maintainable.
* Reproducible.
* Efficient.
* Well documented.
* Easy to validate and debug.

Every module should have a clearly defined responsibility and interface.

---

## Reliability Success

The system should:

* Handle incomplete or optional candidate information gracefully.
* Avoid unexpected failures on valid input.
* Produce deterministic results for identical inputs whenever applicable.
* Generate rankings that remain consistent with the supporting evidence.

---

## Explainability Success

Every ranking decision should be supported by factual evidence derived from candidate data.

Generated explanations should:

* Reflect actual scoring factors.
* Avoid unsupported assumptions.
* Be internally consistent.
* Be understandable by recruiters and reviewers.

---

## Challenge Alignment Success

The final solution should remain aligned with the official challenge objectives by:

* Understanding job descriptions deeply.
* Ranking candidates intelligently rather than filtering.
* Combining technical and behavioral evidence.
* Producing accurate and explainable results.
* Following the official submission requirements.

---

## Final Submission Readiness

Before submission, the project should satisfy all of the following:

* Functional implementation completed.
* Architecture remains aligned with the master plan.
* All planned validation checks completed.
* Documentation updated.
* Final output verified.
* No known critical issues remain unresolved.

---

## Phase Validation Principle

A project phase will be considered complete only when:

* Its objective has been achieved.
* Required validation has passed.
* Outputs match the expected deliverables.
* No unresolved critical risks remain.

Only after satisfying these conditions should the project proceed to the next phase.

---

## Phase 0 Checkpoint

Before moving forward, verify:

* [ ] Success criteria are measurable.
* [ ] Every future phase can be evaluated against these criteria.
* [ ] The criteria align with the official challenge objectives.
* [ ] No success criterion contradicts the published specifications.



# 5. Non-Negotiable Rules

This section defines the engineering principles that must be followed throughout the project lifecycle.

These rules are mandatory unless a change is explicitly justified, documented, and validated against the official challenge requirements.

---

## Challenge Alignment

* Every implementation must directly support an official challenge requirement.
* No feature will be added without a clearly defined purpose.
* Official challenge documentation always takes precedence over assumptions or personal preferences.

---

## Architecture

* Architecture must be finalized before major implementation begins.
* Major architectural changes should be avoided after the Architecture Freeze unless absolutely necessary.
* Every module must have a single, clearly defined responsibility.

---

## Development Workflow

* Every phase must begin with a clearly defined objective.
* Every phase must specify its inputs, outputs, risks, validation criteria, and completion criteria.
* A phase is considered complete only after successful validation.
* The next phase must not begin until the current phase has been validated.

---

## Code Quality

* Prioritize correctness over speed of implementation.
* Prefer readable and maintainable code over unnecessary complexity.
* Avoid premature optimization.
* Keep modules modular, reusable, and testable.

---

## AI & Decision Making

* AI assistance should accelerate development, not replace engineering judgment.
* Every AI-generated solution must be reviewed before integration.
* No implementation should be accepted solely because an AI suggested it.
* Technical decisions must always be supported by reasoning.

---

## Ranking Philosophy

* Never rely solely on keyword matching.
* Never evaluate candidates using a single factor.
* Always combine multiple evidence sources when producing rankings.
* Behavioral signals should complement technical evaluation rather than replace it.
* Ranking decisions should remain explainable and evidence-based.

---

## Explainability

* Never generate unsupported explanations.
* Never fabricate candidate information.
* Every explanation must be traceable to available candidate data.
* Explanations must remain consistent with the underlying ranking logic.

---

## Risk Management

* Avoid unnecessary refactoring.
* Avoid experimental features unless they clearly improve alignment with the challenge objectives.
* Protect working implementations using meaningful Git commits.
* If a proposed change introduces significant risk close to the submission deadline, prefer stability over unnecessary innovation.

---

## Documentation

* Important engineering decisions must be recorded in the Decision Log.
* Project documentation should be updated whenever major architectural or implementation changes occur.
* The PROJECT_MASTER_PLAN.md file is the primary source of truth for project planning.

---

## Validation

Before any implementation is considered complete, verify:

* Functional correctness.
* Challenge alignment.
* Explainability.
* Reproducibility.
* Robustness.
* Documentation updates.

---

## Project Discipline

* Do not deviate from the agreed roadmap without documenting the reason.
* Do not skip validation to save time.
* Do not sacrifice correctness for rapid implementation.
* When uncertainty exists, pause implementation, verify the requirements, and then proceed.

---

## Engineering Principle

A stable, explainable, and challenge-aligned solution is more valuable than a complex solution that introduces unnecessary risk.

The objective is to maximize the quality of the final submission while minimizing avoidable mistakes.

---

## Phase 0 Checkpoint

Before proceeding, verify:

* [ ] Every engineering rule supports the challenge objectives.
* [ ] No rule contradicts the official documentation.
* [ ] The development workflow remains structured and traceable.
* [ ] The project roadmap remains the primary guide for implementation.



# 6. Risk Register

This section identifies the major risks that could affect the successful completion of the project.

Each identified risk includes its potential impact, likelihood, mitigation strategy, and current status. The register should be reviewed regularly throughout development.

---

| Risk ID | Risk Description                                                      | Impact | Probability | Mitigation Strategy                                                                                       | Status    |
| ------- | --------------------------------------------------------------------- | ------ | ----------- | --------------------------------------------------------------------------------------------------------- | --------- |
| R-01    | Misinterpreting official challenge requirements                       | High   | Medium      | Validate every major implementation against the official documentation before development.                | Open      |
| R-02    | Building features that are not aligned with the evaluation objectives | High   | Medium      | Every feature must map to at least one official requirement.                                              | Open      |
| R-03    | Excessive architectural changes after implementation begins           | High   | Medium      | Freeze the architecture after Phase 0 and document any approved changes.                                  | Open      |
| R-04    | Loss of project direction due to long conversations or context limits | Medium | High        | Maintain PROJECT_MASTER_PLAN.md and Decision Log as the permanent project reference.                      | Mitigated |
| R-05    | Insufficient testing before the final submission                      | High   | Medium      | Reserve dedicated time for validation, regression testing, and final review before submission.            | Open      |
| R-06    | Runtime or memory issues when processing the complete dataset         | High   | Unknown     | Design for scalability from the beginning and validate performance on the full dataset before submission. | Open      |
| R-07    | Explainability not matching the actual ranking logic                  | High   | Low         | Generate explanations directly from validated scoring evidence rather than assumptions.                   | Open      |
| R-08    | Inconsistent ranking behaviour after future modifications             | High   | Medium      | Use meaningful Git commits and perform regression validation after major changes.                         | Open      |
| R-09    | Hidden evaluation scenarios exposing weaknesses in the ranking logic  | High   | Unknown     | Build a robust, generalizable solution rather than optimizing for sample data only.                       | Open      |
| R-10    | Running out of time before the submission deadline                    | High   | Medium      | Follow the phased roadmap, prioritize core functionality first, and avoid unnecessary work.               | Open      |

---

## Risk Management Principles

* Risks should be identified before implementation whenever possible.
* High-impact risks receive priority over low-impact risks.
* Every completed phase should include a risk review.
* New risks discovered during development should be added to this register with an appropriate mitigation plan.

---

## Risk Review Schedule

Risk assessment should be performed:

* Before starting a new phase.
* After completing a major implementation milestone.
* Before the final submission.
* Whenever significant architectural changes are proposed.

---

## Phase 0 Checkpoint

Before moving to the next section, verify:

* [ ] Major project risks have been identified.
* [ ] Every high-impact risk has a mitigation strategy.
* [ ] Risk management is integrated into the development workflow.
* [ ] The project plan includes sufficient time for validation and final review.




# 7. High-Level Roadmap

This roadmap defines the complete execution strategy for the project. Each phase has a clear objective, expected deliverables, validation requirements, and exit criteria.

Progression to the next phase is permitted only after the current phase satisfies its validation and completion criteria.

---

## Phase 0 — Requirements Analysis & Planning

### Objective

Translate the official challenge documents into engineering requirements and establish the complete project roadmap.

### Deliverables

* Project Master Plan
* Requirement analysis
* Challenge constraints
* Risk register
* High-level roadmap

### Validation

* Requirements reviewed against official documentation.
* Planning sections completed.
* No unresolved ambiguities remain.

### Exit Criteria

Project planning approved and architecture design can begin.

---

## Phase 1 — System Architecture & Foundation

### Objective

Design the complete system architecture and establish the development foundation.

### Deliverables

* Architecture document
* Module definitions
* Folder structure
* Development environment
* Dependency management
* Configuration strategy

### Validation

* Every module has a clearly defined responsibility.
* Data flow is fully documented.
* Architecture supports all identified requirements.

### Exit Criteria

Architecture is frozen and implementation order is finalized.

---

## Phase 2 — Data Pipeline

### Objective

Develop the data ingestion, validation, preprocessing, and loading pipeline.

### Deliverables

* Dataset loader
* Schema validation
* Data preprocessing pipeline
* Data quality checks

### Validation

* Complete dataset loads successfully.
* Invalid records handled safely.
* Processing remains efficient.

### Exit Criteria

Reliable data pipeline available for downstream modules.

---

## Phase 3 — Job Description Intelligence

### Objective

Build the system responsible for understanding job descriptions and extracting structured hiring intent.

### Deliverables

* Job description parser
* Requirement extraction
* Hiring signal identification

### Validation

* Important hiring requirements correctly extracted.
* Output suitable for candidate matching.

### Exit Criteria

Structured representation of job requirements available.

---

## Phase 4 — Candidate Intelligence

### Objective

Extract meaningful technical, career, educational, and behavioral features from candidate profiles.

### Deliverables

* Feature extraction pipeline
* Candidate representation
* Behavioral feature integration

### Validation

* Candidate information represented consistently.
* Missing values handled correctly.

### Exit Criteria

Candidate intelligence layer completed.

---

## Phase 5 — Matching & Ranking Engine

### Objective

Develop the core intelligence responsible for evaluating candidate suitability.

### Deliverables

* Semantic matching
* Technical scoring
* Behavioral scoring
* Score fusion
* Ranking algorithm

### Validation

* Rankings align with challenge objectives.
* Multi-factor evaluation confirmed.
* Ranking remains explainable.

### Exit Criteria

Core ranking engine completed.

---

## Phase 6 — Explainability Engine

### Objective

Generate factual, evidence-based explanations for ranking decisions.

### Deliverables

* Explanation generator
* Evidence tracing
* Recruiter-friendly summaries

### Validation

* Every explanation supported by candidate data.
* No unsupported reasoning produced.

### Exit Criteria

Explainability integrated with ranking.

---

## Phase 7 — Validation & Optimization

### Objective

Evaluate the complete system for correctness, robustness, efficiency, and challenge alignment.

### Deliverables

* Testing
* Performance optimization
* Error handling improvements
* Final quality assurance

### Validation

* Functional tests pass.
* Performance acceptable.
* Documentation updated.

### Exit Criteria

System ready for submission preparation.

---

## Phase 8 — Submission Preparation

### Objective

Prepare the final deliverables according to the official submission requirements.

### Deliverables

* Final ranked output
* Required metadata
* Documentation review
* Submission package

### Validation

* Submission format verified.
* Final checklist completed.
* No critical issues remain.

### Exit Criteria

Project approved for final submission.

---

## Roadmap Principles

* Complete one phase at a time.
* Validate before progressing.
* Record important decisions.
* Avoid unnecessary architectural changes after implementation begins.
* Maintain continuous alignment with the official challenge requirements.

---

## Current Status

**Current Phase:** Phase 0 – Requirements Analysis & Planning

**Project Status:** 🟡 In Progress

**Overall Progress:** Initial Planning Stage

---

## Phase 0 Checkpoint

Before beginning implementation:

* [ ] Planning document completed.
* [ ] Requirements understood.
* [ ] Architecture approved.
* [ ] Risks identified.
* [ ] Development roadmap finalized.
* [ ] Project ready for architecture design.
