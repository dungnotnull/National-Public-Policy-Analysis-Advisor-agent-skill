# Policy Alternatives Evaluation and Multi-Criteria Decision Analysis

## Framework Overview

This framework covers the generation and systematic evaluation of policy alternatives using Multi-Criteria Decision Analysis (MCDA) grounded in Bardach's Eightfold Path methodology. It provides a structured approach to comparing policy options across multiple dimensions.

## Core Principles

### 1. Generate Before You Evaluate

Don't evaluate alternatives while you're generating them. Separate the creative process of generating options from the analytical process of evaluating them. Mixing these processes prematurely narrows the solution space.

### 2. Compare Alternatives, Not Alternatives to Status Quo

The most meaningful comparison is between viable alternatives, not between each alternative and doing nothing. The status quo should be included as one of the alternatives to be evaluated.

### 3. Evaluation Requires Criteria

You cannot evaluate alternatives without explicit criteria. "Better" is meaningless without specifying "better for whom, according to what values, measured how."

### 4. All Policies Have Tradeoffs

No policy alternative dominates across all criteria. Every choice involves tradeoffs between competing values. Make these tradeoffs explicit.

## Step-by-Step Methodology

### Step 1: Generate Policy Alternatives

Use creative techniques to generate a diverse set of alternatives:

**Brainstorming approaches:**
```
Market-based solutions: Price signals, incentives, market creation
Regulatory solutions: Rules, standards, prohibitions
Public provision: Government delivery, public services
Information-based: Transparency, labeling, education
Hybrid approaches: Combinations of the above
```

**Idea generation techniques:**
- **Benchmarking:** What do other jurisdictions do?
- **Reverse engineering:** What would perfect and terrible policies look like?
- **Stakeholder proposals:** What do different stakeholders propose?
- **Laddering:** What higher-order solutions might address root causes?

**Minimum viable set:**
- Generate at least 3-5 distinct alternatives
- Ensure alternatives are genuinely different (not minor variations)
- Include status quo as an alternative
- Include both "realistic" and "aspirational" options

### Step 2: Define Evaluation Criteria

Select 5-9 criteria spanning different value dimensions:

**Common criterion categories:**
```
Effectiveness: Does it solve the problem?
Efficiency: Cost per unit of outcome
Equity: Distribution of impacts
Feasibility: Political, administrative, technical
Sustainability: Long-term viability
Side effects: Unintended consequences
Administrative ease: Implementation complexity
```

**Criteria quality checks:**
```
✓ Criteria are value-relevant (not just procedural)
✓ Criteria are measurable (even if qualitatively)
✓ Criteria are independent (not overlapping)
✓ Criteria are comprehensive (cover major value dimensions)
✓ Criteria are few enough to be manageable (5-9 optimal)
```

### Step 3: Establish Criterion Weights

Not all criteria are equally important. Weight criteria to reflect relative priority:

**Weighting approaches:**
```
Equal weighting: Simple baseline (can be adjusted)
User-specified weights: Stakeholder preferences
Analytical weights: Derived from stated priorities
Deliberative weights: Through structured discussion
```

**Weight validation:**
- Sum of weights should equal 1.0 (or 100%)
- No single criterion should dominate (>50%)
- Explain why weights are set as they are
- Test sensitivity: Do conclusions change with different weights?

### Step 4: Score Alternatives on Criteria

For each alternative-criterion pair, assign a score:

**Scoring approaches:**
```
Quantitative: Metric-based scoring (e.g., cost per ton of CO2 reduced)
Qualitative: Judgment-based scoring (e.g., 1-5 scale)
Mixed: Quantitative where available, qualitative where not
```

**Scoring guidelines:**
```
5: Excellent performance on this criterion
4: Good performance with minor limitations
3: Adequate performance with notable limitations
2: Poor performance with significant problems
1: Fails to address this criterion
0: Negative impact on this criterion
```

**Evidence standards:**
- Base scores on empirical evidence where available
- Use expert judgment where evidence is lacking
- Document evidence sources and uncertainty
- Distinguish between factual and normative judgments

### Step 5: Apply Weighted Scoring

Calculate weighted scores for each alternative:

```
For each alternative:
  For each criterion:
    Weighted Score = Raw Score × Criterion Weight
  Total Score = Sum of Weighted Scores
```

**Alternative scoring methods:**
```
Additive: Simple weighted sum (most common)
Multiplicative: Penalizes poor performance on any dimension
Geometric: Balances across dimensions
Minimax: Focus on worst performance
```

### Step 6: Analyze Results and Sensitivity

Examine the scoring results:

```
Rank alternatives by total score
Identify top-performing alternatives
Examine which criteria drive rankings
Test sensitivity to weight changes
Check for robustness to uncertainty
```

**Sensitivity analysis:**
- What if environmental weights are higher?
- What if cost considerations dominate?
- What if political feasibility is critical?
- Do rankings change under reasonable weight variations?

### Step 7: Make Tradeoffs Explicit

Identify where tradeoffs exist:

```
Which alternatives excel on effectiveness but struggle on equity?
Which alternatives are cost-effective but politically infeasible?
Which alternatives satisfy current needs but compromise sustainability?
Where are the painful tradeoffs that cannot be avoided?
```

**Tradeoff communication:**
- Don't hide tradeoffs behind composite scores
- Show performance on each criterion individually
- Make clear who gains and who loses
- Identify opportunities for compensation or mitigation

## Quality Assurance

### Bias Checks

Watch for these common biases:

```
Status quo bias: Overweighting familiarity and stability
Optimism bias: Overestimating benefits of preferred alternatives
Confirmation bias: Selectively using evidence favoring preferred option
Anchoring: Being influenced by initially presented information
Availability bias: Overweighting salient or recent examples
```

### Validation Techniques

```
Cross-validation: Do different methods yield similar conclusions?
Stakeholder review: Do relevant stakeholders find analysis credible?
Case comparison: How do results compare to similar cases?
Expert review: Do domain experts find assumptions reasonable?
```

### Robustness Testing

```
Weight variations: Test different reasonable weight combinations
Score variations: Test different plausible scores
Criterion variations: Test adding/removing criteria
Alternative variations: Test adding/removing alternatives
```

## Application Example: Carbon Pricing Policy

### Alternatives Generated

1. **Carbon Tax:** Economy-wide price on carbon emissions
2. **Cap-and-Trade:** Quantity-based emissions trading system
3. **Hybrid:** Carbon tax with price ceiling/floor
4. **Regulatory Standards:** Technology-based emissions standards
5. **Status Quo:** No new carbon pricing

### Evaluation Criteria

1. **Environmental Effectiveness** (Weight: 0.25)
2. **Economic Efficiency** (Weight: 0.20)
3. **Political Feasibility** (Weight: 0.15)
4. **Administrative Ease** (Weight: 0.10)
5. **Distributional Equity** (Weight: 0.15)
6. **Business Competitiveness** (Weight: 0.10)
7. **International Coordination** (Weight: 0.05)

### Scoring Matrix

| Alternative | Effectiveness (0.25) | Efficiency (0.20) | Feasibility (0.15) | Admin (0.10) | Equity (0.15) | Competitiveness (0.10) | Coordination (0.05) | Total |
|-------------|---------------------|-------------------|--------------------|--------------|--------------|-------------------------|--------------------|--------|
| Carbon Tax | 5 | 5 | 3 | 5 | 2 | 3 | 4 | 4.10 |
| Cap-and-Trade | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 3.75 |
| Hybrid | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3.95 |
| Regulatory | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2.75 |
| Status Quo | 1 | 1 | 5 | 5 | 1 | 5 | 1 | 2.40 |

### Analysis Results

**Rankings:**
1. Carbon Tax (4.10)
2. Hybrid (3.95)
3. Cap-and-Trade (3.75)
4. Regulatory (2.75)
5. Status Quo (2.40)

**Key Insights:**
- Carbon tax leads on effectiveness and efficiency but struggles on equity
- Hybrid approach maintains most benefits with better balance
- Political feasibility is the constraint on theoretically superior options
- Distributional equity is the major tradeoff with market-based approaches

**Sensitivity Analysis:**
If political feasibility weight increases to 0.30:
- Status Quo becomes competitive (3.05)
- Carbon Tax drops to 3.70
- Hybrid becomes clear leader (3.85)

If equity weight increases to 0.30:
- Cap-and-Trade becomes more competitive (3.85)
- Carbon Tax drops to 3.65
- All market mechanisms face equity challenges

## Template Integration

Use the `alternatives-matrix-template.json` for structured output:

```json
{
  "policy_issue": "Brief description of issue",
  "alternatives": [
    {
      "name": "Alternative name",
      "description": "Clear description of alternative",
      "mechanism": "How it works",
      "key_features": ["Important characteristics"]
    }
  ],
  "criteria": [
    {
      "name": "Criterion name",
      "description": "What this criterion captures",
      "weight": 0.15,
      "measurement": "How measured or assessed",
      "weight_justification": "Why this weight"
    }
  ],
  "scoring_matrix": [
    {
      "alternative": "Alternative name",
      "scores": {
        "criterion_1": {"score": 4, "evidence": "Evidence source", "uncertainty": "Low/Medium/High"},
        "criterion_2": {"score": 3, "evidence": "Evidence source", "uncertainty": "Low/Medium/High"}
      },
      "weighted_score": 3.75
    }
  ],
  "results": {
    "rankings": ["Ranked alternatives"],
    "top_performer": "Best alternative",
    "tradeoffs": ["Key tradeoffs identified"],
    "sensitivity": ["How results change with different weights"]
  },
  "recommendations": {
    "recommended": "Recommended alternative(s)",
    "rationale": "Why this alternative",
    "conditions": ["Conditions for recommendation to hold"],
    "modifications": ["Suggested improvements or hybrid approaches"]
  },
  "uncertainties": {
    "data_limitations": ["Key data gaps"],
    "assumptions": ["Critical assumptions"],
    "expertise_uncertainty": ["Areas of limited consensus"]
  }
}
```

## Common Pitfalls

### 1. Too Many Criteria

More criteria (10+) creates complexity without adding insight. Stick to 5-9 criteria that capture the most important value dimensions.

### 2. Ignoring Implementation

Evaluation often focuses on design and neglects implementation. Include "administrative feasibility" or "implementation complexity" as criteria.

### 3. Over-Precision

Presenting scores to two decimal places creates false precision. Round to one decimal place and emphasize uncertainty ranges.

### 4. Forgetting Distribution

Aggregate scores hide distributional consequences. Always examine who gains and who loses, even if not formalized as a criterion.

### 5. Static Analysis

Policies operate in dynamic environments. Consider how alternatives might perform under different future scenarios.

## Advanced Techniques

### Cost-Benefit Integration

MCDA can incorporate CBA results:

```
Use CBA net present value as one criterion
Weight appropriately relative to other criteria
Allows CBA to inform but not dominate analysis
```

### Scenario Analysis

Evaluate alternatives under different futures:

```
Scenario 1: High economic growth
Scenario 2: Economic recession
Scenario 3: Technological breakthrough
Scenario 4: Political climate change
```

### Real Options Analysis

For policies with embedded flexibility:

```
Value of waiting: Delaying commitment
Value of flexibility: Adjusting as you learn
Value of growth: Expanding successful pilots
Value of abandonment: Exiting unsuccessful policies
```

## References

- Bardach, E. (2000). A Practical Guide for Policy Analysis: The Eightfold Path to More Effective Problem Solving. Chatham House.
- Weimer, D. L., & Vining, A. R. (2017). Policy Analysis: Concepts and Practice (6th ed.). Routledge.
- Belton, V., & Stewart, T. (2002). Multiple Criteria Decision Analysis: An Integrated Approach to Multi-Criteria Decision Analysis. Kluwer Academic.
- Gregory, R., et al. (2012). Structured Decision Making: A Practical Guide to Environmental Management Choices. Wiley.
- Keeney, R. L., & Raiffa, H. (1993). Decisions with Multiple Objectives: Preferences and Value Tradeoffs. Cambridge University Press.
