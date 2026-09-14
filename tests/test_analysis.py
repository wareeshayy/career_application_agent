from career_agent.analysis import inspect_document


def test_extracts_dates_requirements_and_risks():
    text = "You must submit a passport by September 20, 2026. Late applications will be rejected."
    result = inspect_document(text, "I have my passport")
    assert result["dates"] == ["September 20, 2026"]
    assert "must submit" in result["requirements"][0].lower()
    assert "rejected" in result["risks"][0].lower()
    assert result["context_provided"] is True


def test_no_invented_dates_or_requirements():
    result = inspect_document("Welcome to the program.")
    assert result["dates"] == []
    assert result["requirements"] == []
    assert result["risks"] == []

