# Devpost story

## Inspiration

Important opportunities are often hidden behind confusing paperwork. ProofPath was inspired by people navigating unfamiliar systems—especially non-native speakers, first-generation students, immigrants, caregivers, and busy families.

## What it does

ProofPath turns an official document into a verified action path: plain-language explanation, deadlines, requirements checklist, risk flags, missing questions, ordered next steps, and a clarification message for the issuer. It can respond in Roman Urdu when requested.

## How we built it

Streamlit accepts PDF, DOCX, TXT, or pasted text. A Strands Agent orchestrates a deterministic `requirement_mapper` and Amazon Bedrock. The tool grounds the workflow in explicit evidence; Bedrock produces a context-aware plan. A local fallback keeps the core workflow available without cloud credentials.

## Challenges

The main challenge was being helpful without inventing high-stakes details. ProofPath separates facts from suggestions, labels uncertainty, treats uploaded text as untrusted data, and tells users to verify critical details.

## What we learned

People rarely need another summary—they need the next safe action. Deterministic extraction plus agent orchestration makes outputs practical and verifiable.

## What's next

OCR, deadline reminders, multilingual voice guidance, issuer-specific templates, dependency-aware timelines, AgentCore deployment, and encrypted history.

