"""MCP interface so other assistants can call ProofPath."""

from mcp.server.mcpserver import MCPServer

from career_agent.evidence_graph import build_evidence_graph

mcp = MCPServer("ProofPath Evidence Server")


@mcp.tool()
def map_document_requirements(document_text: str, user_context: str = "") -> dict:
    """Return an evidence-linked graph; never make an eligibility decision."""
    return build_evidence_graph(document_text, user_context)


if __name__ == "__main__":
    mcp.run()
