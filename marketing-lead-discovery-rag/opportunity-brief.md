# Opportunity Brief: Marketing Lead Discovery RAG

## Decision

**Explore and build an offline prototype.** This opportunity is selected because it provides the closest portfolio evidence for Marketing AI while remaining safe to test with synthetic lead data and approved public-style sources.

## Persona and Job To Be Done

**Primary persona:** Marketing or business-development researcher supporting cross-border seller acquisition.

**Job to be done:** When I research potential seller leads, I want a source-supported company profile and ICP fit assessment so that I can prioritize outreach without manually consolidating fragmented public information.

## Problem and Baseline Assumption

The current conceptual workflow requires researchers to review multiple company sources, normalize the evidence, assess fit, and prepare an outreach brief. The prototype must not claim a measured baseline until authorized researchers record actual time, source coverage, and acceptance data.

## Alternatives Considered

| Alternative | Strength | Limitation | Decision |
|---|---|---|---|
| Manual web research | High reviewer control | Slow and inconsistent | Baseline comparator |
| Spreadsheet lead scoring | Transparent structured ranking | Cannot synthesize unstructured source evidence | Keep as scoring layer |
| Generic chatbot | Flexible wording | Weak evidence and poor repeatability | Do not use alone |
| Source-grounded RAG workflow | Combines evidence, synthesis, and review | Requires source governance and evaluation | Prototype choice |

## Why AI

AI is appropriate for summarizing mixed unstructured source excerpts and drafting a researcher-facing lead profile. Deterministic logic remains responsible for ICP scoring, source eligibility, duplicate handling, and any decision to contact a lead.

## Data and Source Policy

The prototype uses synthetic company profiles and synthetic approved-source excerpts. A real pilot must use only authorized sources, define freshness ownership, respect source terms, and avoid personal-data enrichment without a reviewed legal basis.

## Key Risks and Controls

| Risk | Control |
|---|---|
| Unsupported profile claim | Cite source excerpts and show evidence gaps |
| Stale source | Store source date and freshness owner |
| Low-quality lead | Keep deterministic ICP criteria and reviewer approval |
| Prompt injection in external sources | Treat sources as untrusted content; isolate from instructions; validate output |
| Privacy issue | Limit prototype to synthetic or authorized business data |

## Success Criteria for Prototype

- Generate a source-grounded profile with citations for each material claim.
- Show deterministic ICP score alongside the LLM narrative.
- Create a golden query set for retrieval and citation evaluation.
- Do not send outreach or create external records.

## Revisit Trigger

Proceed to an authorized reviewer pilot only if offline evaluation shows acceptable citation correctness, reviewer profile acceptance, source freshness, and estimated cost per accepted profile.
