# Devpost story

## Inspiration

Important opportunities are often hidden behind confusing paperwork. ProofPath was inspired by people navigating unfamiliar systems—especially non-native speakers, first-generation students, immigrants, caregivers, and busy families.

## What it does

ProofPath turns an official document into a verified action path: plain-language explanation, deadlines, requirements checklist, risk flags, missing questions, ordered next steps, and a clarification message for the issuer. Its Evidence Graph links every requirement to the exact source excerpt, gives it a confidence and verification state, and models ordering dependencies. It can respond in Roman Urdu when requested.

## How we built it

Streamlit accepts PDF, DOCX, TXT, or pasted text. A Strands Agent orchestrates a deterministic `requirement_mapper` and Amazon Bedrock. The tool builds a provenance-preserving Evidence Graph; Bedrock turns it into a context-aware plan without upgrading inference into fact. A human-in-the-loop checkpoint prevents automatic acceptance of critical claims. A local fallback keeps the workflow available without cloud credentials. The same mapping capability is exposed through an MCP server so other compatible assistants can use ProofPath as a trusted tool.

## Challenges

The main challenge was being helpful without inventing high-stakes details. ProofPath separates facts from suggestions, labels uncertainty, treats uploaded text as untrusted data, and tells users to verify critical details.

## What we learned

People rarely need another summary—they need the next safe action. Deterministic extraction plus agent orchestration makes outputs practical and verifiable.

## What's next

OCR, deadline reminders, multilingual voice guidance, issuer-specific templates, dependency-aware timelines, AgentCore deployment, and encrypted history.
