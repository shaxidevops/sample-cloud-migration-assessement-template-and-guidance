# Scenario Walkthrough: Small Retail/Services Business

> **Note: This is a synthetic, illustrative scenario.** It is a composite built to demonstrate the assessment methodology in `docs/methodology.md`. It does not describe any specific client, engagement, or real organization. Names, figures, and details below are fictional.

## Background

A small multi-location retail business (e.g., a regional chain of specialty shops, 6 locations) currently runs:
- A point-of-sale (POS) system per location, each storing transaction data locally, with no centralized reporting
- Inventory tracked in spreadsheets, manually reconciled across locations weekly
- Customer loyalty/contact data kept in a mix of POS exports and a separate marketing spreadsheet

Leadership wants centralized, real-time visibility into sales and inventory across locations — the current weekly manual reconciliation means decisions are made on data that's often a week stale. There's appetite to invest, but as with most retail operating margins, the payback period matters more than for, say, a regulated financial firm — the business needs to see a clear return, not just a technical improvement.

## Step 1: Environment Inventory (abridged)

- **POS systems:** 6 separate local installations, vendor-supported but not networked across locations
- **Inventory:** Spreadsheet-based, manually reconciled, prone to human error and staleness
- **Customer data:** Loyalty program contact details, purchase history exports — moderate sensitivity, no health/financial regulatory scope but standard consumer privacy considerations apply
- **Constraints:** Moderate budget tied to demonstrable ROI; no dedicated IT staff, relies on the POS vendor's support plus outside contractors

## Step 2: Scoring Each Workload

### Workload A: Inventory & sales reporting consolidation

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 2 | Budget available, justified by clear ROI case; no externally imposed deadline |
| Technical Debt | 3 | Spreadsheet-based process has no real "architecture" to lift — this is closer to greenfield than migration |
| Downtime | 1 | Reporting can tolerate scheduled updates; not a live transactional system |
| Compliance | 2 | Aggregated sales/inventory data, low individual sensitivity |

**Composite:** (2×0.35) + (3×0.25) + (1×0.20) + (2×0.20) = **2.05 → Re-platform.** Rather than "lifting" a spreadsheet process (there's nothing meaningful to lift), the practical move is adopting a cloud-based retail reporting/inventory platform that ingests data from each location's POS and consolidates it centrally — closer to adopting a managed service than migrating existing infrastructure.

### Workload B: Customer loyalty data centralization

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 2 | Same budget posture as Workload A, often bundled into the same initiative |
| Technical Debt | 2 | Data exists in usable export formats already; consolidation is more integration than re-engineering |
| Downtime | 1 | Not a live operational dependency |
| Compliance | 3 | Customer PII at moderate scale across multiple locations raises standard data-handling obligations even without industry-specific regulation |

**Composite:** (2×0.35) + (2×0.25) + (1×0.20) + (3×0.20) = **2.0 → Re-platform.** Consolidating into a properly access-controlled cloud customer data platform, rather than continuing with spreadsheet exports, is justified primarily by the Compliance score here — even though urgency is moderate, handling consolidated customer PII without basic access controls is a risk worth closing proactively.

## Step 3: Why This Scenario Is Different Again

Unlike the accounting firm (urgency-driven) or the tech shop (engineering-time-constrained), this scenario's main driver is **ROI justification under a moderate, not urgent, budget posture** — and a Technical Debt dimension that's almost moot, since "migrating from a spreadsheet" doesn't fit the usual lift-and-shift/re-platform/refactor framing cleanly. The methodology still produces a useful answer here, but it's worth noting explicitly: when the "legacy environment" is informal (spreadsheets, manual processes) rather than a formal system, most workloads will score toward re-platform almost by default, since there's no existing architecture worth preserving via lift-and-shift.

---

*This scenario deliberately avoids specifying exact dollar figures, vendor names, or identifying details, consistent with the illustrative nature of this walkthrough.*
