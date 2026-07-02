# Scenario Walkthrough: Small Professional Services Firm

> **Note: This is a synthetic, illustrative scenario.** It is a composite built to demonstrate the assessment methodology in `docs/methodology.md`. It does not describe any specific client, engagement, or real organization. Names, figures, and details below are fictional.

## Background

A 15-person professional services firm (e.g., an accounting or legal practice) currently runs:
- Client records and billing data on a local NAS device, backed up irregularly
- A practice management application installed on three office workstations
- Email and document handling split between a legacy on-prem mail server and ad hoc cloud storage

The firm has been told their current backup solution is unreliable, and a recent near-miss data loss incident has prompted leadership to evaluate cloud migration. Budget is limited — this is a discretionary spend for a small firm, not a board-mandated initiative — and there's pressure to show results within the current quarter rather than embark on a multi-year transformation.

## Step 1: Environment Inventory

Using `templates/environment-inventory.md`:

- **Infrastructure:** 1 NAS device (4TB, ~70% full), 3 workstations, no formal server
- **Applications:** Practice management software (Windows-based, vendor still supports it), Outlook/local mail server
- **Data:** Client financial records (regulated — subject to client confidentiality and, depending on jurisdiction, financial data handling obligations), billing records, internal documents
- **Constraints:** Budget is limited (low five figures), no hard deadline but strong preference for a fast win, one part-time IT contractor, no dedicated in-house technical staff

## Step 2: Scoring Each Workload

### Workload A: File storage & backup (NAS → cloud storage)

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 4 | Urgent — recent near-miss, firm wants resolution fast, limited budget |
| Technical Debt | 1 | Simple file storage, no application coupling |
| Downtime | 1 | Can be migrated with a scheduled cutover, low risk |
| Compliance | 3 | Client financial records present; needs access controls and audit logging |

**Composite:** (4×0.35) + (1×0.25) + (1×0.20) + (3×0.20) = **2.25 → Re-platform** (in this case: move from raw file storage to a managed cloud storage service, e.g., Azure Storage with proper access controls — not a like-for-like "just copy the files" lift-and-shift, because the compliance score requires structured controls cloud storage can provide cheaply)

### Workload B: Practice management application

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 3 | Constrained budget, soft deadline |
| Technical Debt | 3 | Windows-based, locally installed, some coupling to local network resources |
| Downtime | 2 | Needs short, schedulable windows — firm can plan around business hours |
| Compliance | 3 | Same client data sensitivity as Workload A |

**Composite:** (3×0.35) + (3×0.25) + (2×0.20) + (3×0.20) = **2.8 → Lift-and-shift, with re-platform roadmap.** Given the budget and timeline pressure, move the application to a cloud VM first (e.g., via Azure Migrate) to get off unreliable local infrastructure quickly, with a planned follow-up phase to evaluate a SaaS or managed-service alternative once budget allows.

## Step 3: Sequencing

Per the methodology's sequencing logic:
1. **File storage migrates first** — lower risk, immediate reliability improvement, builds team familiarity with the cloud environment.
2. **Practice management application migrates second** — once the team has operational experience from Workload A, the higher-technical-debt workload is tackled with more confidence.

## Step 4: Outcome Pattern

This scenario illustrates a common pattern for small-organization migrations: **no single "right" cloud strategy exists for an entire organization.** Even within one 15-person firm, one workload scored toward re-platform and another toward lift-and-shift, because the four dimensions genuinely differed between them. A framework that recommends one strategy for an entire organization, rather than scoring per-workload, would have missed this.

---

*This scenario deliberately avoids specifying exact dollar figures, vendor names, or identifying details, consistent with the illustrative nature of this walkthrough.*
