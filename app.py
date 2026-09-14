"""Streamlit interface for Career Compass."""

import streamlit as st

from career_agent.parser import extract_text
from career_agent.workflow import analyze_application

st.set_page_config(page_title="Career Compass", page_icon="✦", layout="wide")

st.markdown("""
<style>
    .stApp {background: #f7f5ef; color: #17221d;}
    .hero {padding: 2.4rem; border-radius: 24px; background: linear-gradient(120deg,#153f32,#25664e); color:white; margin-bottom:1.5rem;}
    .hero h1 {font-size:3rem; margin:0 0 .4rem 0; letter-spacing:-.04em;}
    .hero p {font-size:1.05rem; opacity:.88; max-width:700px;}
    .step {font-size:.75rem; text-transform:uppercase; letter-spacing:.12em; color:#39705b; font-weight:700;}
    [data-testid="stButton"] button {background:#e76f51; color:white; border:0; border-radius:999px; font-weight:700;}
</style>
<div class="hero">
  <div style="opacity:.75;font-weight:700;letter-spacing:.12em">AI CAREER COPILOT</div>
  <h1>Career Compass</h1>
  <p>Turn one CV and one job description into an honest gap analysis, tailored application draft, and practical interview plan.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("How it works")
    st.write("1. Upload your CV\n\n2. Paste the target role\n\n3. Run the end-to-end agent")
    use_ai = st.toggle("Use Strands + Bedrock", value=True, help="Falls back to local demo mode if AWS is not configured.")
    st.caption("Privacy: uploads are processed in memory. This prototype does not intentionally store your CV.")

left, right = st.columns(2, gap="large")
with left:
    st.markdown('<div class="step">Step 01</div>', unsafe_allow_html=True)
    st.subheader("Your CV")
    upload = st.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"])
    sample_cv = st.text_area("Or paste CV text", height=260, placeholder="Experience, education, skills, achievements…")
with right:
    st.markdown('<div class="step">Step 02</div>', unsafe_allow_html=True)
    st.subheader("Target role")
    job_text = st.text_area("Paste the full job description", height=330, placeholder="Responsibilities, requirements, preferred skills…")

if st.button("Analyze my application →", type="primary", use_container_width=True):
    try:
        cv_text = extract_text(upload.getvalue(), upload.name) if upload else sample_cv
        if len(cv_text.strip()) < 40 or len(job_text.strip()) < 40:
            st.warning("Please provide a fuller CV and job description (at least 40 characters each).")
        else:
            with st.spinner("The agent is comparing evidence and building your plan…"):
                report, mode = analyze_application(cv_text, job_text, use_ai=use_ai)
            st.success(f"Analysis complete · {mode}")
            st.markdown(report)
            st.download_button("Download report", report, "career-compass-report.md", "text/markdown")
    except Exception as exc:
        st.error(f"Could not analyze this application: {exc}")

st.divider()
st.caption("Career Compass supports—not replaces—your judgment. It never needs demographic data and does not predict hiring decisions.")

