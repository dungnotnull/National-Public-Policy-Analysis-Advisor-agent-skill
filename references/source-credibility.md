# Source Credibility Assessment Framework

## Framework Overview

This framework provides systematic guidance for assessing the credibility of sources used in policy analysis. Not all sources are equally reliable—explicit assessment of source quality improves analysis rigor and defensibility.

## Core Principles

### 1. Source Credibility Is Multi-Dimensional

Credibility involves multiple factors: methodology expertise, transparency, independence, peer review, and track record. No single factor determines credibility.

### 2. Credibility Is Context-Dependent

A source highly credible for one purpose may be less credible for another. Academic papers may be authoritative on methodology but weak on political feasibility.

### 3. Assess Sources Systematically

Use consistent criteria to assess sources rather than relying on intuition or reputation alone. Systematic assessment reduces bias and improves transparency.

### 4. Acknowledge Credibility Limitations

Even the best sources have limitations. Explicitly acknowledge what sources can and cannot credibly claim.

## Credibility Dimensions

### 1. Methodological Rigor

**Assessment criteria:**
```
Research design: Experimental > quasi-experimental > observational > descriptive
Sample size: Larger samples more credible
Measurement quality: Valid, reliable measures preferred
Analysis appropriateness: Methods match research questions
Statistical significance: Results reported with confidence intervals
Replicability: Methods and data transparent enough for replication
```

**Indicators of high rigor:**
- Pre-registered study designs
- Peer review by qualified experts
- Transparency about methods and limitations
- Appropriate statistical controls
- Robustness checks and sensitivity analysis

**Red flags:**
- Cherry-picked data or time periods
- Inappropriate statistical methods
- Overstated findings from weak designs
- Non-reproducible analysis
- Methodology not described or unclear

### 2. Source Expertise

**Assessment criteria:**
```
Subject matter expertise: Authors' qualifications in relevant field
Technical expertise: Authors' capability with methods used
Experience: Authors' track record with similar research
Reputation: Standing among peer experts
```

**Indicators of expertise:**
- Academic appointments in relevant field
- Publications in peer-reviewed venues
- Citations by other experts
- Invited expert testimony or consultation
- Leadership in professional associations

**Red flags:**
- Authors outside area of expertise
- No prior work in relevant field
- Lack of peer-reviewed publications
- Ideological or financial bias apparent

### 3. Institutional Quality

**Assessment criteria:**
```
Organization reputation: Institution's standing in field
Editorial standards: Quality controls for publications
Funding transparency: Sources of funding disclosed
Mission independence: Independence from political/commercial pressure
```

**High-quality institutions:**
- Peer-reviewed academic journals
- Government statistical agencies with technical independence
- Reputable think tanks with transparent methodology
- International organizations with technical capacity (OECD, World Bank)
- University research centers with academic freedom

**Variable quality:**
- Advocacy organizations (may have good methods but ideological lens)
- Commercial research firms (competent but may tailor to client needs)
- Media outlets (quality varies enormously, fact-checking varies)
- Blogs and social media (generally low credibility without verification)

**Red flags:**
- Anonymous sources
- Organizations with transparent ideological missions
- Funding from stakeholders with vested interests
- No methodological transparency
- Published solely in non-peer-reviewed outlets

### 4. Transparency and Replicability

**Assessment criteria:**
```
Methods described: Sufficient detail to understand approach
Data accessibility: Data available for verification
Code sharing: Analysis code available
Limitations acknowledged: Authors note weaknesses
Conflicts disclosed: Financial and other interests reported
```

**Transparency indicators:**
- Detailed methods sections
- Data and code shared in repositories
- Pre-registration of study designs
- Explicit discussion of limitations
- Clear conflict of interest statements

**Red flags:**
- Methods not described adequately
- Data not available despite claims
- No discussion of limitations
- Conflicts of interest not disclosed
- Proprietary methods ("black box")

### 5. Recency and Relevance

**Assessment criteria:**
```
Publication date: More recent generally better for fast-changing fields
Context relevance: Research in similar contexts more applicable
Methodological age: Methods have evolved over time
```

**Recency considerations:**
- Fast-changing fields: Technology, climate science, economics—prioritize recent
- Slow-changing findings: Basic principles, historical analysis—older sources okay
- Methodological evolution: Recent methods often more sophisticated

**Relevance considerations:**
- Geographic relevance: Same or similar countries more applicable
- Temporal relevance: Similar time periods more comparable
- Institutional relevance: Similar institutional arrangements more transferable

### 6. Independence and Bias

**Assessment criteria:**
```
Funding sources: Who paid for the research?
Author affiliations: What institutions employ authors?
Ideological lens: Does source have transparent perspective?
Selection bias: What evidence was included/excluded?
Publication bias: Are null findings reported?
```

**Independence indicators:**
- Diverse funding sources
- Disclosure of conflicts
- Transparent about ideological perspective
- Reports null as well as positive findings
- Seeks to disconfirm own claims

**Red flags:**
- Single stakeholder funding
- Non-transparent funding
- Clear ideological mission not acknowledged
- Only reports positive findings
- Ignores contrary evidence

## Source Quality Classification

### Academic Sources

**High quality:**
- Peer-reviewed journal articles (especially top journals)
- University working papers (with methodological rigor)
- Books from academic presses (peer-reviewed)
- PhD dissertations (committee-reviewed)

**Medium quality:**
- Conference papers (peer-reviewed but less rigorous)
- Master's theses (reviewed but less rigorous)
- Pre-prints (not yet peer-reviewed but transparent)
- Government research reports (varying quality)

**Lower quality:**
- Unpublished manuscripts (without review)
- Student papers (undergraduate or informal)
- Course materials or lecture notes (not peer-reviewed)

### Government Sources

**High quality:**
- Official statistical agencies (with technical independence)
- Central bank research (often technically rigorous)
- Parliamentary budget offices (non-partisan analysis)
- Audit institutions (with independence mandates)

**Medium quality:**
- Departmental research reports (may have political pressures)
- Policy evaluation studies (varying rigor)
- Consultation documents (often less analytical)

**Variable quality:**
- Political documents ( speeches, press releases—analytical content limited)
- Agency websites (quality varies by agency)
- Regulatory impact analyses (varying rigor by jurisdiction)

### Think Tank and NGO Sources

**High quality:**
- Think tanks with transparent methodologies and peer review
- International organizations with technical capacity (OECD, World Bank)
- NGOs with research capacity and transparent methods

**Medium quality:**
- Think tanks with consistent ideological lens (high quality but biased)
- Professional associations (industry expertise but may have bias)
- Advocacy organizations (passionate but may cherry-pick)

**Lower quality:**
- Purely advocacy organizations (no research capacity)
- Political party research arms (clearly partisan)
- Industry front groups (biased toward industry interests)

### Media Sources

**High quality:**
- Newspapers of record with fact-checking (NYT, Guardian, etc.)
- Newsmagazines with research capacity (Economist, etc.)
- Public broadcasting with editorial standards (BBC, NPR, etc.)

**Medium quality:**
- Specialized business press (sector-specific expertise)
- Quality local newspapers (local expertise, fewer resources)
- Newsmagazines (less depth than papers of record)

**Lower quality:**
- Partisan outlets (clear ideological framing)
- Tabloid press (sensationalism over accuracy)
- Digital-only outlets without editorial standards
- Social media posts (no verification process)

### Online Sources

**High quality:**
- University or research institute websites
- Government agency websites with data and analysis
- International organization websites (UN, OECD, World Bank)
- Reputable academic blogs (by credentialed experts)

**Medium quality:**
- Professional association websites
- Established think tank websites
- Some business and consulting firm publications

**Lower quality:**
- Personal blogs (unless author credentials clear)
- Wikipedia articles (useful for overview, not primary source)
- Social media posts (no verification)
- Anonymous websites

## Credibility Assessment Template

For each source used, assess:

```json
{
  "source": {
    "type": "academic/government/think_tank/media/online/other",
    "authors": ["Author names and affiliations"],
    "publication": "Journal, organization, or outlet",
    "year": "Publication year",
    "title": "Document title",
    "url_or_access": "How accessed"
  },
  "credibility_assessment": {
    "methodological_rigor": "High/Medium/Low",
    "rigor_evidence": ["Specific indicators of rigor"],
    "expertise": "High/Medium/Low",
    "expertise_evidence": ["Evidence of expertise"],
    "institutional_quality": "High/Medium/Low",
    "institution_evidence": ["Indicators of quality"],
    "transparency": "High/Medium/Low",
    "transparency_evidence": ["Transparency indicators"],
    "independence": "High/Medium/Low",
    "independence_evidence": ["Independence indicators"],
    "recency": "Recent/Medium/Older",
    "relevance": "High/Medium/Low",
    "relevance_evidence": ["Relevance considerations"]
  },
  "overall_quality": "High/Medium/Low",
  "appropriate_uses": ["What this source can credibly support"],
  "limitations": ["What this source cannot credibly claim"],
  "biases": ["Potential biases to be aware of"],
  "verification_needed": ["What should be verified from other sources"]
}
```

## Quality Assurance Practices

### Triangulation

Cross-verify findings across multiple sources:
- Find same result from different methodologies
- Confirm from different types of sources (academic + government + think tank)
- Check from different ideological perspectives

### Source Diversity

Ensure source representativeness:
- Different institutional types (not just think tanks)
- Different methodological approaches
- Different time periods for comparison
- Different contexts where relevant

### Attribution

Always attribute findings to sources:
- Cite specific sources for specific claims
- Distinguish between source claims and your synthesis
- Make clear what evidence supports what conclusions

### Humility About Evidence

Acknowledge evidence limitations:
- State what evidence can and cannot support
- Note where evidence is mixed or contested
- Identify gaps in the evidence base
- Distinguish between strong and weak evidence

## Common Pitfalls

### 1. Assuming All Academic Sources Are Credible

Academic quality varies enormously across journals, authors, and fields. Assess each source individually rather than assuming peer review guarantees credibility.

### 2. Treating Government Sources as Neutral

Government sources often have political pressures, selection biases, or methodological limitations. Even statistical agencies face constraints that affect their work.

### 3. Ignoring Think Tank Bias

Think tanks produce valuable research but often have explicit ideological perspectives. Use their research but acknowledge their lens and seek contrary perspectives.

### 4. Overweighting Recent Sources

Recency matters more in fast-moving fields. For foundational concepts or historical analysis, older sources may be equally or more credible.

### 5. Confiding in Single Sources

Even high-quality sources can be wrong. Important claims should be supported by multiple sources and triangulated across methodologies.

## Quick Reference Guide

### When to Use Different Source Types

| Source Type | Best For | Be Careful About |
|-------------|-----------|-------------------|
| Academic journals | Methodology, theory, causal claims | Relevance to policy context |
| Government data | Official statistics, administrative data | Political interference in reporting |
| Think tanks | Policy analysis, real-world cases | Ideological bias, cherry-picking |
| International orgs | Cross-country comparisons, best practices | One-size-fits-all recommendations |
| Media | Current events, political context | Sensationalism, lack of depth |
| Stakeholder research | Practitioner perspectives, implementation | Self-serving bias |

### Credibility Red Flags

⚠️ Source won't share methodology or data
⚠️ Source has clear ideological mission not acknowledged
⚠️ Only reports positive findings, never null results
⚠️ Funding from stakeholders with clear vested interest
⚠️ No prior work or credentials in relevant field
⚠️ Published only in non-peer-reviewed outlets
⚠️ Results too good to be true
⚠️ Methods not described or inappropriate
⚠️ No discussion of limitations
⚠️ Clear conflicts of interest not disclosed

### Credibility Green Flags

✅ Transparent about methods and limitations
✅ Discloses funding and conflicts of interest
✅ Reports null as well as positive findings
✅ Subject-matter expertise demonstrated
✅ Published in peer-reviewed venues
✅ Replicable analysis with shared data/code
✅ Appropriate methodology for question
✅ Acknowledges alternative interpretations
✅ Cited by other credible sources
✅ Institutional reputation for quality

## References

- Easton, J. (2013). The Role of Research in Policy Networks: The Case of Education Research. British Educational Research Journal.
- Nutley, S. M., Walter, I., & Davies, H. T. O. (2007). Using Evidence: How Research Can Inform Public Services. Policy Press.
- Majone, G. (1989). Evidence, Argument, and Persuasion in the Policy Process. In Congress and the Policy Process.
- Head, B. W. (2008). Three Lenses of Evidence-Based Policy. Australian Journal of Public Administration.
- Weiss, C. H. (1979). The Many Meanings of Research Utilization. Public Administration Review.
