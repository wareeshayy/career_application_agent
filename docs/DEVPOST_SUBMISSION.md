# Devpost submission copy

## Inspiration

Applying for work is repetitive and emotionally demanding. Candidates need more than another chatbot: they need a workflow that checks evidence, identifies gaps, and creates usable next steps without inventing qualifications.

## What it does

Career Compass accepts a CV and job description, compares explicit skills, and creates a structured application report: match overview, strong evidence, honest gaps, CV improvements, tailored cover-letter draft, interview questions, and a 7-day plan. Reports can be downloaded for editing.

## How we built it

The interface uses Streamlit. A Strands Agent orchestrates a custom deterministic skill-gap tool and Amazon Bedrock. Grounding rules require the agent to rely only on supplied CV evidence. PDF and DOCX files are parsed in memory. A local fallback keeps the core workflow demonstrable if cloud credentials are unavailable.

## Challenges

The key challenge was balancing useful personalization with honesty. We separated deterministic comparison from generative writing, labeled the match score as a heuristic, and prohibited fabricated experience or metrics.

## Accomplishments

We built a complete input-to-export workflow, a custom Strands tool, graceful cloud fallback, transparent scoring, and privacy-conscious file handling.

## What we learned

Agent quality improves when orchestration, deterministic tools, and explicit safety boundaries work together. A dependable fallback also makes demos and real products more resilient.

## What's next

Next steps include multilingual support, user-controlled skill taxonomies, ATS format checks, optional AgentCore deployment, and opt-in outcome evaluation with job seekers.

