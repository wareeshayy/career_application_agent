"""Build an auditable evidence graph from document text."""

from hashlib import sha256

from .analysis import inspect_document


def build_evidence_graph(document_text: str, user_context: str = "") -> dict:
    """Map extracted claims to source excerpts and explicit dependencies."""
    findings = inspect_document(document_text, user_context)
    nodes = []
    for index, statement in enumerate(findings["requirements"], start=1):
        nodes.append({
            "id": f"REQ-{index:02d}",
            "type": "requirement",
            "claim": statement,
            "evidence": statement,
            "source_hash": sha256(statement.encode("utf-8")).hexdigest()[:12],
            "confidence": "explicit",
            "status": "unverified",
        })

    edges = []
    for index, node in enumerate(nodes[:-1]):
        if any(marker in node["claim"].lower() for marker in ("before", "first", "prior to")):
            edges.append({"from": node["id"], "to": nodes[index + 1]["id"], "relation": "precedes"})

    unknowns = []
    if not findings["dates"]:
        unknowns.append("No explicit deadline was detected.")
    if not nodes:
        unknowns.append("No explicit requirement statement was detected.")
    if "how" not in document_text.lower() and "portal" not in document_text.lower():
        unknowns.append("Submission channel is not clearly identified.")

    return {
        "document_fingerprint": sha256(document_text.encode("utf-8")).hexdigest()[:16],
        "nodes": nodes,
        "edges": edges,
        "dates": findings["dates"],
        "risks": findings["risks"],
        "unknowns": unknowns,
        "human_verification_required": True,
    }

