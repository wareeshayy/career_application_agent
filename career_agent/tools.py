"""Custom Strands tools for grounded CV/job comparison."""

from strands import tool

from .analysis import compare_cv_to_job


@tool
def skill_gap_analyzer(cv_text: str, job_description: str) -> dict:
    """Compare explicit skills in a CV with a job description.

    Args:
        cv_text: Plain text extracted from the candidate's CV.
        job_description: The complete target job description.
    """
    return compare_cv_to_job(cv_text, job_description)

