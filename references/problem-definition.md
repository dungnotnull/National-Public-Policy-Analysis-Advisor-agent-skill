# Problem Definition and Framing Analysis

## Framework Overview

Problem definition is the foundational step in policy analysis. How a problem is framed determines which solutions are considered and which stakeholders are engaged. This framework operationalizes Stone's "Policy Paradox" and Bardach's problem definition approach.

## Core Principles

### 1. Problems Are Socially Constructed

Policy problems are not objective facts waiting to be discovered—they are constructed through narrative, interpretation, and political contestation. Different stakeholders will frame the same situation differently.

**Example:** "Housing affordability" can be framed as:
- A market failure requiring supply-side solutions
- A rights issue requiring affordability guarantees
- A planning challenge requiring zoning reform
- An inequality issue requiring redistribution

### 2. Separate Problems from Solutions

A common pitfall is defining problems in solution-specific ways ("We need more public housing" is a solution, not a problem definition). The problem should be stated in ways that allow multiple solution approaches.

### 3. Surface Competing Framings

Good policy analysis makes competing framings explicit rather than implicitly accepting one framing as "obvious."

## Step-by-Step Methodology

### Step 1: Describe the Situation

Start with a neutral, descriptive statement of the situation that people agree is problematic:

```
What is happening?
Where is it happening?
When is it happening?
Who is affected?
What are the observable consequences?
```

**Template:**
```
In [country/region], [description of situation with observable metrics].
This affects [stakeholders groups], resulting in [consequences].
```

### Step 2: Identify the Core Problem

Move from description to problem statement by asking:

```
Why is this situation problematic?
What values are being violated or threatened?
What expectations are not being met?
What's the gap between current state and desired state?
```

**Template:**
```
The core problem is [clear statement], which violates [values/expectations]
and creates [harms/consequences].
```

### Step 3: Map Competing Framings

Identify at least 3-5 different ways the problem could be framed:

```
Economic framing: [Problem as market failure/inefficiency]
Rights framing: [Problem as rights violation/entitlement]
Technical framing: [Problem as system failure/design flaw]
Political framing: [Problem as power imbalance/injustice]
Cultural framing: [Problem as value conflict/norms change]
```

For each framing:
- What narrative does this framing tell?
- Which solutions does this framing make logical?
- Who benefits from this framing?
- Who is disadvantaged by this framing?

### Step 4: Analyze Framing Consequences

For each competing framing, analyze:

```
Solution space: What solutions become visible/invisible?
Stakeholder inclusion: Who gets a voice? Who is excluded?
Responsibility: Who is responsible for fixing it?
Success metrics: What counts as success?
Tradeoffs: What values are prioritized? What is sacrificed?
```

### Step 5: Select Working Framing(s)

Rather than choosing one "correct" framing, policy analysis should:

```
Acknowledge multiple valid framings exist
State which framing(s) will be used for the analysis
Explain why these framing(s) were selected
Note what alternative framings would emphasize
```

**Template:**
```
This analysis primarily uses [selected framing(s)], which focuses on
[what this framing highlights]. Alternative framings would emphasize
[what other framings would highlight].
```

## Common Framing Patterns

### Economic Framing

Frames problems as:
- Market failures (externalities, information asymmetry, public goods)
- Efficiency problems (allocation, production, distribution)
- Cost-benefit optimization

Leads to solutions like:
- Price signals, incentives, market mechanisms
- Cost-benefit analysis, efficiency metrics
- Privatization, deregulation, competition

### Rights Framing

Frames problems as:
- Rights violations or entitlement gaps
- Equality/inequity issues
- Justice and fairness concerns

Leads to solutions like:
- Legal rights, protections, guarantees
- Anti-discrimination policies
- Universal access, equal treatment

### Technical Framing

Frames problems as:
- System failures or design flaws
- Implementation gaps
- Process inefficiencies

Leads to solutions like:
- Technical improvements, system redesign
- Better implementation, capacity building
- Process optimization, standardization

### Political Framing

Frames problems as:
- Power imbalances or exclusion
- Injustice or oppression
- Democratic deficits

Leads to solutions like:
- Power redistribution, inclusion
- Accountability mechanisms
- Participatory processes

## Quality Checks

A good problem definition should:

```
✓ Be solution-neutral (multiple solutions are possible)
✓ Make competing framings explicit
✓ Identify who is affected and how
✓ Surface values at stake
✓ Clarify what counts as success
✓ Acknowledge what the definition excludes
```

**Red flags:**
```
✗ Problem defined in solution-specific language
✗ Single framing presented as "obvious"
✗ Stakeholders not identified
✗ Values not clarified
✗ Success metrics not defined
✗ Definition implicitly excludes legitimate perspectives
```

## Application Examples

### Example 1: Housing Affordability

**Situation:**
In Canada, median home prices are 8x median household income. Renters spend 35% of income on housing on average. Homeownership rates for under-35s declined from 45% to 35% since 2000.

**Core Problem:**
Housing is not meeting basic needs for shelter at reasonable cost for a significant portion of the population, threatening economic stability and social cohesion.

**Competing Framings:**

1. **Economic:** Housing supply fails to meet demand at affordable prices due to regulatory constraints
   - Solutions: Deregulation, zoning reform, supply incentives

2. **Rights:** Housing is a human right not adequately protected in current system
   - Solutions: Right-to-housing legislation, guaranteed minimum housing standards

3. **Inequality:** Housing wealth concentration exacerbates intergenerational inequality
   - Solutions: Wealth taxes, housing-specific redistribution, tenant protections

4. **Financial:** Housing is treated as speculative asset rather than utility
   - Solutions: Speculation taxes, financial regulation, alternative investment channels

5. **Planning:** Urban planning has failed to anticipate growth and demographic change
   - Solutions: Better planning, transit-oriented development, regional coordination

**Working Framing:**
This analysis uses the economic framing (supply-demand imbalance) supplemented by inequality framing (distributional consequences). The rights framing is noted as relevant for long-term normative considerations.

### Example 2: Climate Policy

**Situation:**
Global temperatures are rising 1.1°C above pre-industrial levels. Extreme weather events are increasing in frequency and intensity. Emissions continue to rise despite commitments.

**Core Problem:**
Greenhouse gas emissions are altering the climate system, creating systemic risks to human and natural systems at global scale.

**Competing Framings:**

1. **Market Failure:** Climate change as the greatest market failure in history (externalities not priced)
2. **Existential Threat:** Climate change as existential threat to human civilization
3. **Intergenerational Injustice:** Current generations imposing costs on future generations
4. **Global Injustice:** Historical emitters imposing costs on those who didn't cause the problem
5. **Planetary Boundaries:** Humanity exceeding safe operating space in Earth system
6. **Technological Opportunity:** Climate as driver for technological transformation

**Working Framing:**
This analysis uses market failure framing (central to economic solutions) supplemented by global justice framing (international equity considerations). The existential framing is noted for setting urgency but not determining specific policy choices.

## Template Integration

Use the `problem-definition-template.json` for structured output:

```json
{
  "situation_description": "Neutral description of observable facts",
  "core_problem": "Clear statement of what makes situation problematic",
  "affected_stakeholders": ["List of affected groups"],
  "consequences": ["Observable and potential consequences"],
  "competing_framings": [
    {
      "type": "economic/rights/technical/political/cultural",
      "narrative": "How this framing tells the story",
      "solutions_implied": ["What solutions this framing makes logical"],
      "beneficiaries": ["Who benefits from this framing"],
      "disadvantaged": ["Who is disadvantaged"]
    }
  ],
  "working_framings": ["Selected framing(s) for analysis"],
  "framing_rationale": "Why these framings were selected",
  "alternative_notes": "What other framings would emphasize",
  "values_at_stake": ["Values implicated in this problem"],
  "success_metrics": ["What would count as progress/success"]
}
```

## References

- Stone, D. (2012). Policy Paradox: The Art of Political Decision Making (3rd ed.). Norton.
- Bardach, E. (2000). A Practical Guide for Policy Analysis: The Eightfold Path to More Effective Problem Solving. Chatham House.
- Rochefort, D. A., & Cobb, R. W. (1994). The Politics of Problem Definition. University Press of Kansas.
