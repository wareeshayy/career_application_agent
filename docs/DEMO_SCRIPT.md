# Five-minute demo script

**0:00–0:35 — Problem**  
“Job seekers repeatedly decode long job descriptions and often receive generic advice. Career Compass turns a real CV and role into an honest, actionable plan.”

**0:35–1:05 — Audience and value**  
“It is designed for students, career switchers, and busy applicants. It saves time without fabricating qualifications.”

**1:05–2:45 — Live workflow**  
Upload a sample CV, paste a job description, keep Strands + Bedrock enabled, and click Analyze. Show the match overview, evidence, gaps, cover letter, interview questions, and 7-day plan. Download the report.

**2:45–3:35 — Technical architecture**  
Show `docs/architecture.svg`. Explain that Streamlit handles input, Strands orchestrates the workflow, the custom tool performs deterministic comparison, and Bedrock creates the evidence-bound report. Briefly show `career_agent/tools.py` and `career_agent/workflow.py`.

**3:35–4:15 — Reliability and responsibility**  
Disable AI mode and rerun to demonstrate the local fallback. Mention in-memory parsing, no demographic inputs, transparent heuristic scoring, and the anti-fabrication prompt.

**4:15–4:45 — Impact**  
Explain saved preparation time and better-targeted applications. Do not claim measured impact unless you have conducted a study.

**4:45–5:00 — Close**  
“Career Compass helps real people move from uncertainty to an honest next step—one application at a time.”

