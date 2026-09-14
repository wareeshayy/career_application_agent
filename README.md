# Career Compass

Career Compass is an end-to-end AI career application assistant built for the **Agents for Humans Hackathon** (Professional Agents track). It compares a candidate's real CV evidence with a target job, identifies honest skill gaps, drafts a tailored cover letter, creates interview questions, and produces a 7-day action plan.

![Architecture](docs/architecture.svg)

## Why it matters

Job seekers often spend hours decoding job descriptions and rewriting applications. Generic AI writing tools can also invent experience. Career Compass grounds its output in the supplied CV, uses a deterministic skill-gap tool, and explicitly forbids fabricated claims.

## Features

- PDF, DOCX, and TXT CV input
- Custom Strands `skill_gap_analyzer` tool
- Amazon Bedrock-powered personalized report
- Honest match heuristic—not a hiring probability
- Cover-letter draft and interview plan
- Local fallback mode for reliable demos without AWS credentials
- Downloadable Markdown report

## Run locally

Requires Python 3.10+ and AWS credentials with Amazon Bedrock model access for AI mode.

```powershell
cd career-application-agent
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:AWS_REGION="us-west-2"
$env:BEDROCK_MODEL_ID="global.anthropic.claude-sonnet-4-6"
streamlit run app.py
```

Use the sidebar toggle to run deterministic local demo mode. For Bedrock, configure credentials using the standard AWS CLI or `AWS_*` environment variables and enable the selected model in Amazon Bedrock.

## Agent workflow

1. The user supplies a CV and job description.
2. The parser extracts text in memory.
3. The Strands agent calls `skill_gap_analyzer` for grounded comparison.
4. Amazon Bedrock produces a structured, evidence-bound report.
5. The interface presents and exports the result.
6. If cloud access is unavailable, a deterministic local report keeps the workflow functional.

## Safety and privacy

- No demographic information is requested.
- The score is a transparent keyword heuristic, never a hiring prediction.
- The prompt forbids invented credentials, experience, or metrics.
- Uploaded files are processed in memory and are not intentionally persisted.
- Users should review every generated application before submission.

## Test

```powershell
python -m pytest -q
```

## Suggested Devpost assets

- Architecture diagram: `docs/architecture.svg`
- Demo script: `docs/DEMO_SCRIPT.md`
- Project description: `docs/DEVPOST_SUBMISSION.md`

## License

MIT

