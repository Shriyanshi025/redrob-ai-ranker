from typing import Dict, List


class CandidateExplainer:
    def explain(
        self,
        candidate: Dict,
        score: float,
        feature_scores: Dict | None = None,
    ) -> Dict:

        reasons: List[str] = []

        profile = candidate.get("profile", {})
        skills = candidate.get("skills", [])

        years = profile.get("years_of_experience", 0)
        title = profile.get("current_title", "")

        skill_names = {
            s.get("name", "").lower()
            for s in skills
        }

        ai_skills = {
            "llms",
            "rag",
            "langchain",
            "embeddings",
            "vector search",
            "nlp",
            "fine-tuning llms",
            "hugging face transformers",
            "semantic search",
            "information retrieval",
        }

        matched = ai_skills.intersection(skill_names)
        
        data_skills = {
            "spark",
            "sql",
            "airflow",
            "data pipelines",
            "apache beam",
            "kafka",
        }

        data_matched = data_skills.intersection(skill_names)

        if len(data_matched) >= 2:
            reasons.append(
                f"Strong data engineering background ({len(data_matched)} skills)"
            )

        if len(matched) >= 2:
            reasons.append(
                f"Strong AI skill set ({len(matched)} relevant skills)"
            )

        if years >= 5:
            reasons.append(
                f"{years:.1f} years of industry experience"
            )

        title_lower = title.lower()

        important_titles = [
            "machine learning",
            "ai engineer",
            "nlp engineer",
            "applied scientist",
            "data scientist",
            "backend engineer",
            "software engineer",
            "search engineer",
        ]

        if any(t in title_lower for t in important_titles):
            reasons.append(
                f"Relevant role: {title}"
            )

        if feature_scores:
            top = sorted(
                feature_scores.items(),
                key=lambda x: x[1],
                reverse=True,
            )[:2]

            for name, value in top:
                reasons.append(
                    f"Strong {name.replace('_', ' ')} ({value:.2f})"
                )

        if not reasons:
            reasons.append(
                "Good overall profile alignment"
            )

        return {
            "candidate_id": candidate["candidate_id"],
            "score": round(score, 4),
            "top_reasons": reasons[:5],
        }