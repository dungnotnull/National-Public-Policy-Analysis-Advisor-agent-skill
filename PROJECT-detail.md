# PROJECT-detail.md — National Public Policy Analysis Advisor

## 1. Problem Statement

A skill supporting researchers, students, and civil servants in structurally analyzing a country's public policy on a given issue, using established policy-analysis methodology (problem definition, stakeholder mapping, alternatives analysis, evaluation criteria) and presenting balanced perspectives on contested policy questions.

## 2. Target Users

Describe the primary user personas for this skill (fill in based on real usage once built): e.g., students, professionals, hobbyists, or practitioners in the relevant domain.

## 3. Functional Specification

### 3.1 Core Capabilities

- Apply structured policy-problem definition and framing analysis
- Map stakeholders and their interests (stakeholder analysis)
- Generate and evaluate policy alternatives against defined criteria (multi-criteria policy analysis)
- Apply policy-cycle stage analysis (agenda-setting, formulation, implementation, evaluation)
- Summarize empirical evidence on policy effectiveness from multiple sources
- Present balanced perspectives for genuinely contested policy debates

### 3.2 Key Methodologies & Frameworks Applied

- **Policy Cycle model (Lasswell; Jann & Wegrich)**
- **Stakeholder analysis framework**
- **Multi-criteria policy-alternatives evaluation (Bardach's Eightfold Path)**
- **Evidence-based policy analysis discipline**

Each framework above should be operationalized as a concrete step, checklist, or template inside the skill's SKILL.md and reference files once this scaffold is turned into a runnable skill (see `DEVELOPMENT-TASK-BY-PHASES.md`).

### 3.3 Expected Input

Typical user requests this skill should handle (fill in with real example prompts during development and testing).

### 3.4 Expected Output Format

Define the structured output format(s) this skill should produce (e.g., structured report, checklist, scored recommendation, memo). Align with the methodologies above so outputs are consistent and auditable.

## 4. Out of Scope / Guardrails

- Always include the standing disclaimer for this domain (see CLAUDE.md).
- Never present output as a certified/professional determination (e.g., not a diagnosis, not a legal opinion, not a guaranteed forecast).
- Where the skill involves a named third party (e.g., a partner, a suspect, a specific person), do not produce a definitive judgment about that individual — stay at the level of general, population-based information and structured reasoning support.
- Flag explicitly when a licensed professional (doctor, lawyer, engineer, certified analyst, etc.) should be consulted.

## 5. Knowledge Base Dependency

This skill's reasoning quality depends on the research foundations catalogued in `SECOND-BRAIN-KNOWLEDGE-PAPER.md`. When building the actual skill (SKILL.md + references/), extract the operational principles from each paper into concrete reference files rather than leaving them as a flat reading list.

## 6. Success Criteria

- Output correctly applies the named methodologies rather than generic reasoning.
- Output is well-structured and consistent across repeated runs on similar inputs.
- Domain-appropriate guardrails/disclaimers are respected in every response.
- Test prompts (see `DEVELOPMENT-TASK-BY-PHASES.md`, Phase 5) produce outputs a subject-matter-competent reviewer would rate as sound.
