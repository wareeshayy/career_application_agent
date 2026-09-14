"""Safe, in-memory CV text extraction."""

from io import BytesIO


def extract_text(data: bytes, filename: str) -> str:
    """Extract text from PDF, DOCX, or TXT data without persisting the CV."""
    suffix = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""
    if suffix == "txt":
        return data.decode("utf-8", errors="replace")
    if suffix == "pdf":
        from pypdf import PdfReader

        return "\n".join(page.extract_text() or "" for page in PdfReader(BytesIO(data)))
    if suffix == "docx":
        from docx import Document

        return "\n".join(p.text for p in Document(BytesIO(data)).paragraphs)
    raise ValueError("Please upload a PDF, DOCX, or TXT file.")

