# Cloud Migration Assessment & Decision Framework

A practitioner-built methodology for assessing legacy IT environments and selecting the right cloud migration strategy — with a primary lens on **cost and timeline constraints**, the factor that most often determines outcomes for small and mid-sized organizations migrating to Microsoft Azure.

## Why this exists

Most published migration guidance (including vendor playbooks like AWS's 6 R's or Azure's Cloud Adoption Framework) assumes the organization has dedicated migration budget, a multi-quarter timeline, and a team that can absorb the change. In practice — especially for small businesses, regional firms, and organizations migrating for the first time — the real constraint is usually **how much can we spend, and how fast do we need this done**, with everything else (architecture purity, long-term scalability) negotiated around that.

This repository documents a decision framework built around that reality: a structured way to assess a legacy environment, weigh cost/timeline against other factors (downtime tolerance, compliance, technical debt), and arrive at a defensible migration strategy — lift-and-shift, re-platform, or refactor — without defaulting to the most expensive option by habit.

The framework is deliberately industry-agnostic. The same four dimensions apply whether the organization is a small accounting or financial services practice (client records, regulatory exposure), a small tech/software shop (legacy internal tooling, CI/CD modernization), or a retail/services business (point-of-sale systems, inventory, customer data) — what changes between sectors is mainly the weighting of the Compliance dimension, not the underlying logic. See `scenarios/` for sector-specific illustrative walkthroughs.

This is a generalized, illustrative framework. It does not contain or reference any specific client's infrastructure, data, or engagement details. All scenarios in `/scenarios` are synthetic composites built to demonstrate the methodology, not case studies of real engagements.

## What's in this repo

| Folder | Contents |
|---|---|
| `/docs` | The assessment methodology, scoring rubric, and decision logic |
| `/templates` | Reusable assessment templates (environment inventory, scoring worksheet, migration runbook) |
| `/scenarios` | Synthetic example walkthroughs across three small-business sectors (professional services/accounting, tech/software, retail/services) |
| `/diagrams` | Decision trees and process flow diagrams |
| `/scripts` | Lightweight scoring calculator for the assessment rubric |

## Scope

This framework is written with an Azure-first lens (Azure Migrate, Azure App Service, Azure SQL, Azure Storage are the primary reference services), since that's where most of the underlying experience comes from. The underlying decision logic is platform-agnostic and can be adapted to AWS or GCP equivalents with minimal changes — see `docs/platform-notes.md`.

## Relationship to other frameworks

This complements broader infrastructure-modernization work (Terraform/Ansible/compliance-mapping focused) published separately. Where that work addresses *how to build* the target cloud environment, this repository addresses an earlier question: *which migration strategy is right, given real-world constraints, before any infrastructure work begins.*

## License

MIT — see LICENSE.
