# Scenario Walkthrough: Small Software/Tech Shop

> **Note: This is a synthetic, illustrative scenario.** It is a composite built to demonstrate the assessment methodology in `docs/methodology.md`. It does not describe any specific client, engagement, or real organization. Names, figures, and details below are fictional.

## Background

A 25-person software consultancy runs a mix of internal tooling and client-delivered systems:
- An internal project-tracking tool, self-hosted on an aging on-prem server, built in-house years ago
- A CI/CD pipeline currently running on a single on-prem build server with no redundancy
- Client-facing demo environments, spun up manually per project on local VMs

The firm is growing and has started losing time to build-server outages and the manual overhead of spinning up demo environments. Unlike a non-technical small business, this organization has in-house engineering capacity to execute a migration — but still has constrained budget, since infrastructure modernization competes directly with billable client work for the same engineers' time.

## Step 1: Environment Inventory (abridged)

- **Internal tooling:** Project-tracking tool, in-house built, moderate coupling to local database and file storage
- **CI/CD:** Single build server, Jenkins-based, no failover
- **Demo environments:** Manually provisioned VMs, inconsistent configuration, "it works on my machine" reliability problems
- **Constraints:** Engineering time is the real constraint, not raw budget; any migration work directly displaces billable hours

## Step 2: Scoring Each Workload

### Workload A: CI/CD Pipeline

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 2 | Moderate budget available, no hard external deadline, but outages are a growing pain point |
| Technical Debt | 2 | Standard Jenkins setup, well-understood, moderate refactor surface |
| Downtime | 3 | Build failures block the whole engineering team — high operational impact even if not customer-facing |
| Compliance | 1 | No regulated data in the build pipeline itself |

**Composite:** (2×0.35) + (2×0.25) + (3×0.20) + (1×0.20) = **1.9 → Re-platform.** Given available engineering time and no urgent deadline, moving to a managed CI/CD service (e.g., Azure DevOps Pipelines or GitHub Actions runners) rather than just lifting the Jenkins box to a cloud VM addresses both the redundancy gap and reduces ongoing maintenance burden.

### Workload B: Client demo environments

| Dimension | Score | Rationale |
|---|---|---|
| Cost & Timeline | 3 | Constrained — engineering time is scarce, firm wants a fix without a large time investment |
| Technical Debt | 4 | No standardization at all; every demo environment is bespoke |
| Downtime | 1 | Demo environments are ephemeral by nature; downtime tolerance is high |
| Compliance | 2 | Some client data present in demos, but typically anonymized or synthetic |

**Composite:** (3×0.35) + (4×0.25) + (1×0.20) + (2×0.20) = **2.65 → Lift-and-shift, with re-platform roadmap.** The immediate fix is templated, repeatable cloud VM provisioning (e.g., via Infrastructure-as-Code templates) to kill the "bespoke every time" problem cheaply. A longer-term move to fully ephemeral, container-based demo environments is flagged as a future phase once time allows — it's the technically better answer, but the Technical Debt score alone doesn't justify a full refactor when the Cost & Timeline pressure is this high.

## Step 3: Why This Differs From the Accounting Firm Scenario

Compare this to `small-firm-walkthrough.md`: here, the Cost & Timeline dimension is driven by *engineering time scarcity*, not literal budget — the framework's scoring logic doesn't care which kind of constraint it is, only how tight it is. This is a deliberate feature of the methodology: "cost and timeline" should be read as "real-world capacity to execute," whether that capacity is measured in dollars, available staff hours, or both.

---

*This scenario deliberately avoids specifying exact dollar figures, vendor names, or identifying details, consistent with the illustrative nature of this walkthrough.*
