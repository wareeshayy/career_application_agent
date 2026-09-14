"""Deterministic document triage for ProofPath."""
import re
from datetime import date

DATE_PATTERNS = (
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}(?:st|nd|rd|th)?(?:,\s*\d{4})?\b",
    r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", r"\b\d{4}-\d{2}-\d{2}\b",
)
REQUIREMENT_WORDS = ("must", "required", "provide", "submit", "attach", "include", "bring", "need to")
RISK_WORDS = ("penalty", "denied", "rejected", "cancelled", "canceled", "late fee", "legal action", "terminate", "suspended")


def _sentences(text: str) -> list[str]:
    cleaned = re.sub(r"[\t ]+", " ", text.replace("\r", "\n"))
    return [p.strip(" •-\n") for p in re.split(r"(?<=[.!?])\s+|\n+", cleaned) if len(p.strip()) > 3]


def inspect_document(document_text: str, user_context: str = "") -> dict:
    dates = []
    for pattern in DATE_PATTERNS:
        dates.extend(re.findall(pattern, document_text, flags=re.IGNORECASE))
    sentences = _sentences(document_text)
    return {
        "dates": list(dict.fromkeys(dates))[:10],
        "requirements": [s for s in sentences if any(w in s.lower() for w in REQUIREMENT_WORDS)][:12],
        "risks": [s for s in sentences if any(w in s.lower() for w in RISK_WORDS)][:8],
        "context_provided": bool(user_context.strip()), "generated_on": date.today().isoformat(),
    }


def baseline_report(document_text: str, user_context: str) -> str:
    result = inspect_document(document_text, user_context)
    dates = "\n".join(f"- {x}" for x in result["dates"]) or "- No explicit date detected—verify manually."
    reqs = "\n".join(f"- [ ] {x}" for x in result["requirements"]) or "- [ ] No explicit requirement detected—ask the issuer."
    risks = "\n".join(f"- {x}" for x in result["risks"]) or "- No explicit penalty or rejection language detected."
    context = user_context.strip() or "No personal situation was provided."
    return f"""## Plain-language overview

This document appears to communicate an administrative request or decision. Verify every extracted detail against the original document before acting.

**Your stated situation:** {context}

## Important dates
{dates}

## Requirements checklist
{reqs}

## Risk flags
{risks}

## Missing information to confirm
- [ ] Who exactly should receive the response?
- [ ] Is submission by portal, email, post, or in person?
- [ ] Will you receive proof of submission?
- [ ] Are copies accepted, or are originals/certified copies required?

## Step-by-step action plan
1. Compare every extracted item with the original document.
2. Ask the issuer about unclear deadlines or requirements.
3. Collect required items and keep copies.
4. Submit before the earliest confirmed deadline.
5. Save the receipt, confirmation, tracking number, or screenshot.
6. Follow up if confirmation does not arrive.

## Follow-up message draft
**Subject: Clarification regarding document requirements**

Hello,

I received your document and am preparing the requested information. Please confirm the complete list of required items, final deadline, accepted submission method, whether copies are acceptable, and whether I will receive proof of submission.

Thank you,

[Your name]

[Reference or case number]

> ProofPath provides organizational assistance, not legal, medical, immigration, or financial advice. Verify critical details with the issuer or a qualified professional.
"""
