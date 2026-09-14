from career_agent.analysis import compare_cv_to_job


def test_skill_comparison_is_case_insensitive():
    result = compare_cv_to_job("Built apps with Python and AWS", "Requires PYTHON, AWS, and Docker")
    assert result["score"] == 67
    assert result["matched"] == ["python", "aws"]
    assert result["missing"] == ["docker"]


def test_empty_skill_vocabulary_does_not_claim_match():
    result = compare_cv_to_job("Writer", "Create excellent editorial copy")
    assert result["score"] == 0
    assert result["required"] == []

