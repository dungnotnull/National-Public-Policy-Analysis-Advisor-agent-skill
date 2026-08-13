# Cognitive Mapping and Visualization System

## Research Foundation

This system implements cognitive mapping for policy analysis, drawing from:

- **Eden (1988)** - Cognitive Mapping
- **Ackermann & Eden (2011)** - Making Strategy: Mapping Strategic Success
- **Axelrod (1976)** - Structure of Decision
- **Kosko (1986)** - Fuzzy Cognitive Maps
- **Novak (2010)** - Learning, Creating, and Using Knowledge
- **Morgan & Morrison (1999)** - Critical Visual Literacy

## Core Concepts

### 1. Cognitive Maps

**Definition:** Graphical representations of mental models showing causal relationships between concepts.

**Components:**
- **Nodes:** Concepts, variables, factors
- **Edges:** Causal relationships
- **Signs:** Positive (+) or negative (-) relationships
- **Weights:** Strength of relationships

### 2. Mental Models in Policy

**Why Mental Models Matter:**
- Stakeholders have different mental models
- Mental models drive positions and behaviors
- Conflict often stems from model differences
- Policy success requires model alignment

**Types of Policy Mental Models:**
- Causal models (how policy affects outcomes)
- Value models (what outcomes matter)
- Institutional models (how system works)
- Stakeholder models (who matters and why)

### 3. Cognitive Mapping for Policy Analysis

**Applications:**
- Elicit stakeholder mental models
- Compare models across stakeholders
- Identify consensus and conflict
- Facilitate shared understanding
- Design better policies

## Cognitive Mapping Process

### Step 1: Concept Elicitation

**Goal:** Identify key concepts in stakeholder mental models

**Techniques:**
- Cognitive interviewing
- Concept listing
- Free elicitation
- Prompted elicitation

**Example Questions:**
- "What factors influence [policy issue]?"
- "What causes [problem]?"
- "What would happen if [policy] was implemented?"
- "What are the most important considerations?"

**Concept Categories:**
- Policy instruments
- Outcomes/effects
- Stakeholders
- Contextual factors
- Values/goals
- Barriers/enablers

### Step 2: Causal Relationship Identification

**Goal:** Identify causal connections between concepts

**Techniques:**
- "What causes what?" questions
- "What leads to what?" questions
- Relationship elicitation
- Scenario-based elicitation

**Relationship Types:**
- Direct causality
- Indirect causality
- Bidirectional causality
- Feedback loops

**Coding:**
- Positive (+): Increase in A leads to increase in B
- Negative (-): Increase in A leads to decrease in B
- Weighted: Strength (weak, moderate, strong)
- Probabilistic: Certainty level

### Step 3: Map Construction

**Goal:** Create visual representation of cognitive map

**Software Tools:**
- Mental Modeler (web-based)
- Decision Explorer (specialized)
- FCMapper (fuzzy cognitive maps)
- Network analysis tools (Gephi, Cytoscape)

**Construction Process:**
1. Arrange concepts spatially
2. Draw causal arrows
3. Add signs (+/-)
4. Add weights if desired
5. Organize hierarchically
6. Add visual styling

### Step 4: Map Analysis

**Structural Analysis:**
- Centrality measures (which concepts central)
- Cluster analysis (concept groupings)
- Path analysis (causal pathways)
- Feedback loop identification

**Comparative Analysis:**
- Overlap analysis (shared concepts)
- Conflict analysis (different causal beliefs)
- Stakeholder grouping by model similarity
- Bridge concepts (potential consensus points)

**Dynamic Analysis:**
- Simulation of interventions
- Sensitivity analysis
- Scenario testing
- Leverage point identification

## Cognitive Mapping Templates

### Stakeholder Cognitive Map Template

```json
{
  "cognitive_map": {
    "stakeholder": "Stakeholder name",
    "date_created": "Date",
    "interviewer": "Analyst name",
    "concepts": [
      {
        "id": "concept_id",
        "label": "Concept name",
        "type": "instrument/outcome/stakeholder/context/value",
        "description": "Concept definition"
      }
    ],
    "relationships": [
      {
        "from": "concept_id_1",
        "to": "concept_id_2",
        "causal_type": "positive/negative",
        "strength": "weak/moderate/strong",
        "certainty": "low/medium/high",
        "description": "Explanation of causal relationship"
      }
    ],
    "clusters": [
      {
        "name": "Cluster theme",
        "concepts": ["concept_id_1", "concept_id_2"]
      }
    ],
    "leverage_points": ["High-impact intervention points"],
    "assumptions": ["Key underlying assumptions"]
  }
}
```

### Comparative Cognitive Map Template

```json
{
  "comparative_analysis": {
    "stakeholders_compared": ["Stakeholder 1", "Stakeholder 2"],
    "shared_concepts": ["Concepts in both maps"],
    "unique_concepts": {
      "stakeholder_1": ["Concepts only in map 1"],
      "stakeholder_2": ["Concepts only in map 2"]
    },
    "consensus_relationships": [
      {
        "relationship": "Causal link agreed upon",
        "convergence_type": "identical/similar/different"
      }
    ],
    "conflict_relationships": [
      {
        "relationship": "Causal link disagreed upon",
        "stakeholder_1_view": "How stakeholder 1 sees it",
        "stakeholder_2_view": "How stakeholder 2 sees it"
      }
    ],
    "consensus_clusters": ["Areas of agreement"],
    "conflict_clusters": ["Areas of disagreement"],
    "bridge_concepts": ["Potential areas for agreement"],
    "negotiation_points": ["Areas for potential compromise"]
  }
}
```

## Policy Causal Modeling

### Systems Thinking in Policy

**Why Systems Thinking:**
- Policies operate in complex systems
- Interventions have indirect effects
- Feedback loops create dynamics
- Policies can create resistance

**Systems Concepts:**
- Feedback loops (reinforcing, balancing)
- Delays (policy effect timing)
- Non-linearities (threshold effects)
- Emergence (system-level patterns)

### Causal Loop Diagrams

**Components:**
- Variables (system states)
- Causal links (arrows)
- Polarities (+/-)
- Delays (||- marks)

**Common Archetypes:**
- Limits to growth
- Shifting the burden
- Fixes that fail
- Tragedy of the commons
- Growth and underinvestment

### Stock and Flow Modeling

**Components:**
- Stocks (accumulations)
- Flows (rates of change)
- Converters (auxiliary variables)
- Connections (information links)

**Applications:**
- Policy simulation
- Dynamic hypothesis testing
- Scenario analysis
- Leverage point identification

## Visualization Techniques

### Network Visualization

**Layout Algorithms:**
- Force-directed (natural clustering)
- Hierarchical (level-based)
- Circular (cyclical relationships)
- Radial (central concept focus)

**Visual Encodings:**
- Node size: Concept importance
- Node color: Concept type
- Edge thickness: Relationship strength
- Edge color: Relationship type
- Edge style: Relationship certainty

### Interactive Visualizations

**Features:**
- Zoom and pan
- Click for details
- Filter by concept type
- Highlight paths
- Toggle relationships
- Compare stakeholder maps

### Dashboard Integration

**Components:**
- Map overview
- Concept search
- Relationship explorer
- Stakeholder comparison
- Scenario simulation
- Consensus/conflict display

## Advanced Analysis Features

### Influence Path Analysis

**Purpose:** Identify how changes propagate through cognitive maps

**Method:**
1. Select intervention point
2. Trace forward paths
3. Identify affected concepts
4. Assess impact magnitude
5. Identify feedback loops

### Cognitive Map Metrics

**Centrality Metrics:**
- Degree centrality (direct connections)
- Betweenness centrality (bridge concepts)
- Closeness centrality (influence reach)
- Eigenvector centrality (influence importance)

**Structural Metrics:**
- Map density (connection richness)
- Clustering coefficient (group formation)
- Path length (causal distance)
- Feedback loop count (cyclical causality)

### Consensus Analysis

**Overlap Measures:**
- Jaccard similarity (concept overlap)
- Relationship similarity
- Path similarity
- Structural similarity

**Conflict Identification:**
- Opposing causal beliefs
- Differing causal structures
- Different leverage points
- Value conflicts

### Scenario Simulation

**What-If Analysis:**
- Test policy interventions
- Simulate causal effects
- Identify second-order effects
- Assess unintended consequences

**Fuzzy Cognitive Maps:**
- Probabilistic causal relationships
- Iterative simulation
- Convergence testing
- Sensitivity analysis

## Cognitive Mapping for Policy Stages

### Problem Definition Stage

**Applications:**
- Map stakeholder problem definitions
- Identify causal beliefs about problems
- Reveal problem framing differences
- Find consensus problem definitions

### Formulation Stage

**Applications:**
- Elicit stakeholder solution theories
- Map how stakeholders think solutions work
- Identify solution assumptions
- Find design consensus points

### Decision Stage

**Applications:**
- Map stakeholder decision criteria
- Visualize value conflicts
- Identify decision factors
- Find compromise opportunities

### Implementation Stage

**Applications:**
- Map implementer mental models
- Identify implementation assumptions
- Reveal potential implementation barriers
- Find implementation design improvements

### Evaluation Stage

**Applications:**
- Map theory of change
- Identify evaluation-relevant concepts
- Reveal expected causal pathways
- Improve evaluation design

## Practical Implementation

### Elicitation Protocols

**Individual Elicitation:**
1. Explain purpose and process
2. Start with broad question
3. Probe for details
4. Encourage elaboration
5. Check for completeness
6. Verify understanding

**Group Elicitation:**
1. Elicit individual maps first
2. Present aggregate map
3. Discuss differences
4. Reveal conflicts
5. Explore consensus
6. Create shared map

### Map Quality Assessment

**Quality Criteria:**
- Completeness (key concepts included)
- Accuracy (reflects stakeholder views)
- Clarity (concepts clearly defined)
- Consistency (logical coherence)
- Depth (sufficient detail)

**Validation:**
- Member checking (stakeholder verification)
- Triangulation (multiple sources)
- Peer review (expert review)
- Predictive validity (map predicts positions)

## Integration with Existing Frameworks

### Stakeholder Analysis + Cognitive Mapping

**Enhanced Stakeholder Analysis:**
- Cognitive maps of stakeholder views
- Mental model comparison
- Belief system identification
- Conflict and consensus mapping

**Template Integration:**
```json
{
  "stakeholder_analysis_enhanced": {
    "basic_analysis": "Standard stakeholder data",
    "cognitive_map": "Stakeholder mental model",
    "causal_beliefs": "How stakeholder thinks system works",
    "value_beliefs": "What outcomes stakeholder values",
    "assumptions": "Key underlying assumptions"
  }
}
```

### Problem Definition + Cognitive Mapping

**Enhanced Problem Definition:**
- Map causal beliefs about problems
- Reveal problem framing differences
- Identify root cause beliefs
- Find consensus problem definitions

### Alternatives Evaluation + Cognitive Mapping

**Enhanced Alternatives Evaluation:**
- Map theory of change for each alternative
- Compare stakeholder causal models
- Identify unintended consequence beliefs
- Find implementation assumption conflicts

## Cognitive Mapping Templates

### Policy Causal Model Template

```json
{
  "policy_causal_model": {
    "policy_name": "Policy being analyzed",
    "theory_of_change": "How policy is supposed to work",
    "intervention_points": ["Where policy acts"],
    "causal_pathways": [
      {
        "pathway_id": "path_1",
        "steps": [
          {
            "from": "Policy instrument",
            "to": "Immediate effect",
            "mechanism": "How effect occurs",
            "timing": "When effect occurs",
            "certainty": "How certain"
          }
        ],
        "final_outcome": "Ultimate policy goal"
      }
    ],
    "feedback_loops": [
      {
        "loop_type": "reinforcing/balancing",
        "pathway": ["Loop elements"],
        "delay": "Timing of feedback",
        "implications": "What loop means for policy"
      }
    ],
    "assumptions": ["Key causal assumptions"],
    "leverage_points": ["High-impact intervention points"]
  }
}
```

### Stakeholder Belief System Template

```json
{
  "stakeholder_belief_system": {
    "stakeholder": "Stakeholder name",
    "causal_beliefs": {
      "problem_causes": ["What stakeholder believes causes problem"],
      "solution_mechanisms": ["How stakeholder believes solutions work"],
      "outcome_expectations": ["What stakeholder expects from solutions"]
    },
    "value_beliefs": {
      "primary_values": ["Core values"],
      "outcome_priorities": ["Which outcomes matter most"],
      "tradeoff_preferences": ["How stakeholder trades off values"]
    },
    "institutional_beliefs": {
      "how_system_works": "Stakeholder's institutional understanding",
      "who_matters": "Stakeholder's view of power structure",
      "what_works": "Stakeholder's beliefs about effective strategies"
    },
    "epistemic_beliefs": {
      "what_counts_as_evidence": "Stakeholder's epistemic criteria",
      "who_counts_as_expert": "Stakeholder's authority structure",
      "what_uncertainties": "Stakeholder's uncertainty areas"
    }
  }
}
```

## Visualization Output Formats

### Static Outputs

**PNG/JPEG Images:**
- High-resolution maps
- Publication-ready graphics
- Presentation slides

**PDF Documents:**
- Map documentation
- Analysis reports
- Stakeholder profiles

**SVG Graphics:**
- Scalable vector graphics
- Editable in design tools
- Web-embeddable

### Interactive Outputs

**Web Applications:**
- D3.js visualizations
- Interactive network graphs
- Filterable interfaces

**Dashboard Components:**
- Real-time map updates
- Scenario simulations
- Comparative analysis tools

**Mobile Apps:**
- Field data collection
- Stakeholder interviews
- Quick reference tools

## Specialized Applications

### Conflict Analysis

**Cognitive Mapping for Conflict:**
- Identify conflicting causal beliefs
- Map value conflicts
- Reveal communication breakdowns
- Find resolution pathways

### Negotiation Support

**Cognitive Mapping for Negotiation:**
- Elicit underlying interests
- Find common ground
- Identify tradeoff opportunities
- Support joint fact-finding

### Consensus Building

**Cognitive Mapping for Consensus:**
- Create shared mental models
- Identify areas of agreement
- Bridge divergent views
- Develop collective understanding

### Learning and Evaluation

**Cognitive Mapping for Learning:**
- Map stakeholder learning
- Track mental model changes
- Document knowledge acquisition
- Improve future interventions

This cognitive mapping and visualization system provides powerful tools for eliciting, analyzing, and visualizing stakeholder mental models, enabling deeper understanding of the beliefs, assumptions, and causal reasoning that drive policy positions and behaviors. It transforms abstract mental models into concrete, analyzable structures that support better policy design and implementation.
