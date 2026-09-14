"""Deterministic baseline analysis used by tools and demo mode."""

import re

SKILLS = (
    "python", "javascript", "typescript", "react", "node.js", "node", "java",
    "sql", "aws", "amazon bedrock", "docker", "kubernetes", "git", "figma",
    "excel", "power bi", "tableau", "communication", "leadership", "marketing",
    "seo", "project management", "data analysis", "machine learning", "strands",
    "fastapi", "streamlit", "html", "css", "mongodb", "postgresql",
)


def _has_skill(text: str, skill: str) -> bool:
    return bool(re.search(rf"(?<!\w){re.escape(skill)}(?!\w)", text.lower()))


def compare_cv_to_job(cv_text: str, job_text: str) -> dict:
    required = [skill for skill in SKILLS if _has_skill(job_text, skill)]
    matched = [skill for skill in required if _has_skill(cv_text, skill)]
    missing = [skill for skill in required if skill not in matched]
    score = round(100 * len(matched) / len(required)) if required else 0
    return {"score": score, "required": required, "matched": matched, "missing": missing}


def baseline_report(cv_text: str, job_text: str) -> str:
    result = compare_cv_to_job(cv_text, job_text)
    matched = ", ".join(result["matched"]) or "No exact keyword matches found"
    missing = ", ".join(result["missing"]) or "No obvious keyword gaps found"
    return f"""## Match overview

**Keyword match score: {result['score']}%**

Matched skills: {matched}

Potential gaps: {missing}

## CV improvements

1. Put the most relevant experience and matched skills near the top.
2. Add measurable outcomes (time saved, revenue, users, accuracy, or growth) to achievement bullets.
3. Address the potential gaps only when you genuinely have that experience—never invent a skill.
4. Mirror the employer's language naturally while keeping every claim accurate.

## Cover-letter draft

Dear Hiring Manager,

I am excited to apply for this opportunity. My background includes {matched.lower()}, which aligns with key parts of the role. I am especially interested in contributing practical, measurable work while continuing to grow in the areas the position requires. I would welcome the chance to discuss how my experience and approach can support your team.

Sincerely,  
[Your name]

## Interview preparation

- Prepare one STAR story showing how you used a matched skill to create a measurable result.
- Explain a relevant challenge, your specific contribution, and what you learned.
- Be ready to discuss how you would close one genuine skill gap in your first 30 days.
- Ask: “What would success look like in the first 90 days?”

> This is decision support, not a hiring decision. Review and personalize all generated text before using it.
"""

