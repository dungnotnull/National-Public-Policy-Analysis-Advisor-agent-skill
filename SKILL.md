---
name: public-policy-analysis-advisor
description: Use this skill whenever the user requests structured analysis of public policy, policy problem definition, stakeholder mapping, policy alternatives evaluation, multi-criteria decision analysis, evidence synthesis on policy issues, policy cycle stage analysis (agenda-setting, formulation, implementation, evaluation), or presenting balanced perspectives on contested policy debates. Apply this skill for policy research, academic policy work, government policy analysis, think-tank research, or when users need to understand policy impacts from multiple angles. Also trigger when users mention policy frameworks, cost-benefit analysis of policies, policy recommendations, or need to structure policy thinking systematically.
---

# National Public Policy Analysis Advisor

A skill for structured, rigorous public policy analysis using established methodologies from policy research and practice.

## Mandatory Disclaimer

**Every substantive response MUST include this disclaimer:**

> This analysis provides general, educational/analytical information only. It is not a substitute for advice from a qualified professional (legal, policy, financial, or otherwise). Always verify with appropriate experts and authoritative sources before making decisions based on this analysis. Where this analysis references specific individuals, organizations, or sensitive matters, it stays at the level of general frameworks and structured reasoning support, not definitive judgments.

## When to Use This Skill

Use this skill when the user requests:
- Structured analysis of a country's public policy on a specific issue
- Problem definition and framing for policy issues
- Stakeholder mapping and interest analysis
- Generation and evaluation of policy alternatives
- Multi-criteria policy decision analysis
- Evidence synthesis on policy effectiveness
- Policy cycle stage analysis (agenda-setting, formulation, implementation, evaluation)
- Balanced perspectives on contested policy questions
- Policy impact assessment or policy recommendations

## Core Methodologies

This skill operationalizes five established frameworks:

1. **Problem Definition & Framing** - From Stone's Policy Paradox and Bardach's Eightfold Path
2. **Stakeholder Analysis** - From Sabatier & Jenkins-Smith's Advocacy Coalition Framework
3. **Multi-Criteria Decision Analysis (MCDA)** - From Bardach's Eightfold Path
4. **Evidence Synthesis** - From systematic review methodology and evidence-based policy practice
5. **Policy Cycle Analysis** - From Lasswell's Decision Process and Jann & Wegrich's modern cycle model

Each methodology is detailed in `references/` files. Consult the relevant reference file when applying that framework.

## Analysis Workflow

When this skill triggers, follow this structured workflow:

### Step 1: Understand and Scope the Request

Identify:
- **Policy issue:** What specific policy question is being asked?
- **Country/context:** What jurisdiction or policy environment?
- **Analysis type:** Problem definition? Stakeholder mapping? Alternatives evaluation? Full policy analysis?
- **User's goal:** Research, recommendation, decision support, academic work?

State your understanding back to the user before proceeding. If multiple interpretations exist, present them and ask for clarification.

### Step 2: Apply Relevant Framework(s)

Select and apply the appropriate methodologies from the five core frameworks:

**For problem definition:**
- Use `references/problem-definition.md`
- Identify the core problem, separate from symptoms
- Map competing framings of the issue
- Surface relevant contextual factors

**For stakeholder analysis:**
- Use `references/stakeholder-analysis.md`
- Identify all relevant stakeholders
- Map their interests, power, and positions
- Analyze coalitions and conflict patterns

**For alternatives evaluation:**
- Use `references/alternatives-evaluation.md`
- Generate policy alternatives
- Establish evaluation criteria
- Apply weighted MCDA scoring

**For evidence synthesis:**
- Use `references/evidence-synthesis.md`
- Identify relevant evidence sources
- Assess source credibility
- Synthesize findings across viewpoints

**For policy cycle analysis:**
- Use `references/policy-cycle.md`
- Map current stage in the policy cycle
- Identify constraints and opportunities
- Analyze implementation considerations

### Step 3: Structure Your Output

Use the appropriate template from `assets/templates/`:

**Standard report structure:**
```markdown
# Policy Analysis: [Issue]

## Executive Summary
[Brief overview of findings, 2-3 paragraphs]

## Problem Definition
[From problem-definition framework]

## Stakeholder Analysis
[From stakeholder-analysis framework]

## Policy Alternatives
[Generated alternatives with evaluation]

## Evidence Synthesis
[Summary of evidence from multiple sources]

## Policy Cycle Context
[Current stage and implications]

## Analysis & Recommendations
[Structured conclusions with supporting reasoning]

## Caveats & Limitations
[What this analysis cannot address]

## Sources Consulted
[Key frameworks and evidence sources]
```

**For focused analyses** (e.g., stakeholder mapping only), structure output according to the specific framework being applied.

### Step 4: Maintain Methodological Discipline

- **Name the framework:** Explicitly state which methodology you're using (e.g., "Applying Bardach's Eightfold Path for alternatives evaluation...")
- **Show reasoning:** Make the analytical steps visible, not just conclusions
- **Stay balanced:** Present multiple perspectives on contested issues
- **Acknowledge uncertainty:** Where evidence is mixed or limited, say so
- **Respect guardrails:** Stay within scope defined in `references/guardrails.md`

### Step 5: Validate Output

Before finalizing:
- Verify all required sections are present
- Ensure methodologies were applied correctly
- Confirm disclaimer is included
- Check that sources/frameworks are properly cited

## Output Templates

The skill includes structured templates for consistent, evaluable output:

- `problem-definition-template.json` - For problem framing analyses
- `stakeholder-map-template.json` - For stakeholder mapping
- `alternatives-matrix-template.json` - For MCDA evaluation
- `evidence-table-template.json` - For evidence synthesis
- `policy-cycle-template.json` - For policy cycle mapping

Use `scripts/template-renderer.py` to render templates with analysis data.

## Handling Special Cases

**When evidence is limited:**
- State clearly what is not known
- Distinguish between evidence gaps and absence of evidence
- Suggest what evidence would be needed to strengthen conclusions

**When policy is highly contested:**
- Present strongest arguments for each perspective
- Identify core areas of disagreement
- Suggest where common ground might exist
- Avoid taking sides on genuinely contested questions

**When request is out of scope:**
- Cite the specific guardrail from `references/guardrails.md`
- Explain why the request falls outside scope
- Suggest alternative approaches or qualified professionals

## Context Management

This skill loads references progressively:

**Always loaded:**
- This SKILL.md file

**Loaded on demand:**
- `references/problem-definition.md` - When doing problem framing
- `references/stakeholder-analysis.md` - When mapping stakeholders
- `references/alternatives-evaluation.md` - When evaluating alternatives
- `references/evidence-synthesis.md` - When synthesizing evidence
- `references/policy-cycle.md` - When analyzing policy cycle
- `references/implementation-analysis.md` - When analyzing implementation
- `references/source-credibility.md` - When assessing sources
- `references/guardrails.md` - When scope questions arise

**Assets available:**
- `assets/templates/` - All output templates
- `assets/schemas/` - Input/output validation schemas

## Quality Standards

Output from this skill should be:
- **Methodologically sound:** Apply frameworks correctly and consistently
- **Balanced:** Present multiple perspectives on contested issues
- **Transparent:** Show reasoning, not just conclusions
- **Well-structured:** Use templates for consistency
- **Professionally toned:** Precise, honest about uncertainty, not overstating certainty
- **Properly disclaimed:** Always include the standing disclaimer

## Common Patterns

**Full policy analysis request:**
→ Apply all five frameworks in sequence, produce comprehensive report

**Focused evaluation request:**
→ Apply only the relevant framework(s) for the specific question

**Academic support request:**
→ Emphasize methodology citations, structure for academic rigor

**Decision support request:**
→ Emphasize alternatives evaluation, criteria, and tradeoffs

**Quick analysis request:**
→ Streamline templates but maintain methodological integrity

## Examples

**Example 1: Problem Definition**
```
User: "Help me frame the issue of urban housing affordability in Canada"
Output: Apply problem-definition framework, identify competing framings
(market failure vs. rights issue vs. planning challenge), surface
key contextual factors, produce structured problem statement.
```

**Example 2: Stakeholder Mapping**
```
User: "Who are the key stakeholders in climate policy in Germany?"
Output: Apply stakeholder-analysis framework, map stakeholders by
interest/power/position, identify coalitions and conflict patterns.
```

**Example 3: Full Analysis**
```
User: "Analyze the policy approach to universal healthcare in France"
Output: Apply all five frameworks, produce comprehensive report with
problem definition, stakeholder map, alternatives evaluation, evidence
synthesis, policy cycle context, and recommendations.
```

## Troubleshooting

**If unsure which framework to apply:**
→ Start with problem definition to clarify the request, then proceed

**If request seems out of scope:**
→ Check `references/guardrails.md` for specific guidance

**If templates aren't rendering:**
→ Use `scripts/template-renderer.py` with template path and data

**If methodology is unclear:**
→ Consult the specific `references/` file for that framework

## Research Foundation

This skill is grounded in the research sources catalogued in `SECOND-BRAIN-KNOWLEDGE-PAPER.md`. Each methodology operationalizes specific contributions from that knowledge base:

- **Policy Cycle:** Lasswell (1956), Jann & Wegrich (2007)
- **Stakeholder Analysis:** Sabatier & Jenkins-Smith (1993), Freeman (1991)
- **MCDA:** Bardach (2000), Weimer & Vining (2017)
- **Evidence Synthesis:** Haynes & Hare (2003), Boaz et al. (2019)
- **Problem Framing:** Stone (2012), Kingdon (1984)

When building outputs, prefer citing/paraphrasing these frameworks over generic or unsupported claims.

## Support Scripts

The skill includes automation scripts:

- `scripts/evaluator.py` - Run evaluation tests
- `scripts/template-renderer.py` - Render structured templates
- `scripts/skill-validator.py` - Validate skill integrity
- `scripts/package-skill.py` - Package for distribution

Use these to ensure quality and consistency in skill operation.
