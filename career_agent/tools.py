"""Custom Strands tools for evidence-grounded document navigation."""
from strands import tool
from .evidence_graph import build_evidence_graph


@tool
def requirement_mapper(document_text: str, user_context: str) -> dict:
    """Build an auditable graph of requirements, evidence, dependencies, and risks.

    Args:
        document_text: Text extracted from the user's document.
        user_context: The user's stated goal and already-available items.
    """
    return build_evidence_graph(document_text, user_context)
