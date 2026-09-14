"""Custom Strands tools for evidence-grounded document navigation."""
from strands import tool
from .analysis import inspect_document


@tool
def requirement_mapper(document_text: str, user_context: str) -> dict:
    """Extract explicit deadlines, requirements, and risks from a document.

    Args:
        document_text: Text extracted from the user's document.
        user_context: The user's stated goal and already-available items.
    """
    return inspect_document(document_text, user_context)

