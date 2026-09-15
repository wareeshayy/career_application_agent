"""Streamlit interface for ProofPath."""
import streamlit as st
from career_agent.parser import extract_text
from career_agent.workflow import navigate_document

st.set_page_config(page_title="ProofPath", page_icon="🧭", layout="wide")
st.markdown("""
<style>
.stApp{background:#f5f1e8;color:#18231e}.hero{padding:2.6rem;border-radius:26px;background:linear-gradient(120deg,#142f29,#315c4e);color:white;margin-bottom:1.5rem}.hero h1{font-size:3.3rem;margin:.15rem 0 .45rem;letter-spacing:-.05em}.hero p{font-size:1.08rem;opacity:.88;max-width:760px}.eyebrow,.step{font-size:.75rem;text-transform:uppercase;letter-spacing:.14em;font-weight:750}.step{color:#8a5a32}[data-testid="stButton"] button{background:#d76847;color:white;border:0;border-radius:999px;font-weight:700}
</style><div class="hero"><div class="eyebrow">DOCUMENT → DECISIONS → DONE</div><h1>ProofPath</h1><p>Turn a confusing official document into clear requirements, verified deadlines, risk flags, and a step-by-step completion plan.</p></div>
""", unsafe_allow_html=True)
st.caption("Evidence Graph · Strands tool use · Human verification · MCP-ready")
with st.sidebar:
    st.header("Your path")
    st.write("1. Add a document\n\n2. Explain your situation\n\n3. Generate an action path")
    use_ai = st.toggle("Use Strands + Bedrock", value=True, help="Falls back safely if AWS is not configured.")
    st.caption("Privacy: documents are processed in memory and not intentionally stored.")
left, right = st.columns(2, gap="large")
with left:
    st.markdown('<div class="step">Step 01 · The document</div>', unsafe_allow_html=True)
    st.subheader("What did you receive?")
    upload = st.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"])
    pasted_text = st.text_area("Or paste the document text", height=270, placeholder="Paste the letter, notice, requirements, or email…")
with right:
    st.markdown('<div class="step">Step 02 · Your situation</div>', unsafe_allow_html=True)
    st.subheader("What are you trying to do?")
    user_context = st.text_area("Add your goal and what you already have", height=270, placeholder="Example: I need to complete this university application. I already have my passport and transcript. Explain in Roman Urdu.")
    st.info("ProofPath organizes information—it does not replace advice from the issuer or a qualified professional.")
if st.button("Build my ProofPath →", type="primary", use_container_width=True):
    try:
        document_text = extract_text(upload.getvalue(), upload.name) if upload else pasted_text
        if len(document_text.strip()) < 40:
            st.warning("Please upload or paste a fuller document (at least 40 characters).")
        else:
            with st.spinner("Mapping facts, deadlines, requirements, and next steps…"):
                report, mode = navigate_document(document_text, user_context, use_ai=use_ai)
            st.success(f"Your path is ready · {mode}")
            st.markdown(report)
            st.download_button("Download action path", report, "proofpath-report.md", "text/markdown")
    except Exception as exc:
        st.error(f"Could not process this document: {exc}")
st.divider()
st.caption("ProofPath highlights uncertainty and keeps you in control. Always verify critical details against the original document.")
