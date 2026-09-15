from career_agent.analysis import inspect_document
from career_agent.evidence_graph import build_evidence_graph


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


def test_evidence_graph_preserves_source_and_requires_human_check():
    text = "You must submit a passport before registration."
    graph = build_evidence_graph(text)
    assert graph["nodes"][0]["id"] == "REQ-01"
    assert graph["nodes"][0]["evidence"] == text
    assert graph["nodes"][0]["confidence"] == "explicit"
    assert graph["human_verification_required"] is True
