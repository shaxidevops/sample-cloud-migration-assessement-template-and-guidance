# Assessment Methodology

## 1. Purpose

This methodology answers one question for a legacy environment under consideration for cloud migration:

> Given this organization's real-world cost and timeline constraints, which migration strategy — lift-and-shift, re-platform, or refactor — is appropriate for each workload, and in what order should they move?

It is built for environments where migration budget and timeline are fixed constraints set by the business, not variables the technical team controls. That is the normal situation for small and mid-sized organizations, and a different starting point than most cloud-vendor frameworks assume.

## 2. The Four Assessment Dimensions

Each workload being considered for migration is scored against four dimensions. Cost & Timeline is weighted most heavily by default, reflecting the real-world driver in most engagements — but the weighting is configurable (see Section 4) because compliance-heavy or uptime-critical workloads sometimes need it inverted.

### 2.1 Cost & Timeline Constraint (default weight: 35%)

The most common forcing function. Questions to answer:
- Is there a hard deadline (e.g., a lease expiring, an EOL/EOS date on existing hardware, a contract renewal)?
- What is the available migration budget relative to the workload's complexity?
- Is the organization able to run legacy and cloud environments in parallel during transition, or does cost pressure require a fast cutover?

| Score | Condition |
|---|---|
| 1 | Ample budget, no hard deadline, parallel-run is affordable |
| 2 | Moderate budget, soft deadline (next 6–12 months) |
| 3 | Constrained budget, firm deadline (next 1–6 months) |
| 4 | Minimal budget, urgent/forced deadline (e.g., hardware failure risk, EOL system) |

**Higher score → favors lift-and-shift** (fastest, lowest upfront engineering cost). **Lower score → opens the door to re-platform/refactor**, since there's runway to do it properly.

### 2.2 Technical Debt & Architecture Age (default weight: 25%)

- Is the application monolithic, tightly coupled to on-prem infrastructure (e.g., hardcoded IPs, local file system dependencies), or built on an end-of-support stack?
- Is there available documentation, or is institutional knowledge the only source of truth?

| Score | Condition |
|---|---|
| 1 | Modern, modular, already container-friendly |
| 2 | Some coupling, but manageable refactor surface |
| 3 | Significant coupling to legacy infrastructure |
| 4 | Monolithic, undocumented, built on end-of-support platforms |

**Higher score → re-platform or refactor becomes necessary**, not optional — lift-and-shift just moves the problem to the cloud without fixing it.

### 2.3 Downtime Tolerance / Business Continuity (default weight: 20%)

- Can this workload tolerate a scheduled maintenance window, or does it need near-zero downtime?
- Is there a regulatory or contractual SLA attached to availability?

| Score | Condition |
|---|---|
| 1 | Tolerant of multi-hour or overnight windows |
| 2 | Needs short (under 1 hour) windows, schedulable |
| 3 | Needs near-zero downtime, but has redundancy options |
| 4 | Mission-critical, contractual uptime SLA, no acceptable downtime |

**Higher score → favors a phased/parallel-run approach** regardless of cost pressure, since outage risk becomes the dominant constraint.

### 2.4 Data Sensitivity & Compliance Exposure (default weight: 20%)

- Does the workload handle regulated data (financial records, PII, health data, client confidentiality obligations)?
- Are there specific compliance frameworks in scope (e.g., SOC 2, GLBA for financial services, HIPAA, state-level data protection laws)?

| Score | Condition |
|---|---|
| 1 | No sensitive data |
| 2 | Some sensitive data, standard cloud provider controls sufficient |
| 3 | Regulated data, requires specific architecture controls (encryption at rest/in transit, access logging, data residency) |
| 4 | Highly regulated, requires formal compliance attestation or audit trail |

**Higher score → adds mandatory architecture requirements** to whichever strategy is chosen — it doesn't change lift-and-shift vs. refactor by itself, but it gates what "done" looks like.

## 3. Composite Scoring & Strategy Selection

Calculate a weighted composite score:

```
Composite = (CostTimeline × 0.35) + (TechDebt × 0.25) + (Downtime × 0.20) + (Compliance × 0.20)
```

| Composite Score Range | Recommended Default Strategy |
|---|---|
| 1.0 – 1.8 | Refactor (time/budget allows doing it right; low urgency) |
| 1.9 – 2.6 | Re-platform (balance of speed and improvement) |
| 2.7 – 3.4 | Lift-and-shift, with a re-platform roadmap for later phases |
| 3.5 – 4.0 | Lift-and-shift only; revisit in 6–12 months once pressure eases |

This is a starting recommendation, not a rule. Two cases where the composite score should be overridden:

- **Compliance score of 4 regardless of composite** → the architecture must include the required controls from day one, even under a lift-and-shift approach. Cost pressure does not waive compliance requirements; it changes *how* they're implemented (e.g., using built-in Azure compliance offerings rather than custom-built controls).
- **Downtime score of 4 regardless of composite** → even under extreme cost/timeline pressure, a mission-critical workload needs a parallel-run cutover, not a hard switchover, to avoid catastrophic business risk. The cost pressure changes the *length* of the parallel-run window, not whether one happens.

## 4. Adjusting the Weights

Default weights assume a typical small-to-mid-size business migration where cost/timeline is the primary driver. Two common situations call for re-weighting:

- **Regulated industries (financial services, healthcare, government-adjacent contractors):** increase Compliance weight to 30–35%, reduce Cost & Timeline to 20–25%.
- **Mission-critical operational systems (e.g., systems with contractual uptime penalties):** increase Downtime weight to 30%+, reduce Technical Debt weight correspondingly.

See `templates/scoring-worksheet.md` for an editable version of this rubric.

## 5. Migration Sequencing

Once each workload has a recommended strategy, sequence the overall migration using this priority order:

1. **Lowest-risk, highest-learning workloads first** — pick a non-critical workload with a straightforward lift-and-shift profile as the pilot. This validates tooling, networking, and team familiarity before tackling harder workloads.
2. **Compliance-gated workloads next, deliberately** — these need the most architecture planning; starting them early gives room to get it right without time pressure compounding.
3. **High-downtime-sensitivity workloads last**, once the team has cutover experience from earlier, lower-stakes migrations.

This sequencing exists because the single biggest real-world failure mode in small-organization migrations isn't choosing the wrong strategy — it's attempting the hardest workload first, before the team has any cloud-operations experience to draw on.
