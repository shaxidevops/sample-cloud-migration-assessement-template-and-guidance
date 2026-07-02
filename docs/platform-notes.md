# Platform Notes: Adapting Beyond Azure

The assessment methodology in `methodology.md` is platform-agnostic by design — the four scoring dimensions and decision logic don't change based on target cloud provider. What changes is which specific services map to each recommended strategy. This framework is written Azure-first because that reflects the majority of the underlying engagement experience, but the equivalents below make it usable regardless of target platform.

## Service Equivalents by Strategy

| Strategy | Azure | AWS | GCP |
|---|---|---|---|
| Lift-and-shift (VM-based) | Azure Migrate, Azure VMs | AWS Application Migration Service (MGN), EC2 | Migrate to Virtual Machines, Compute Engine |
| Re-platform (managed services) | Azure App Service, Azure SQL Managed Instance | Elastic Beanstalk, RDS | App Engine, Cloud SQL |
| Refactor (cloud-native) | Azure Kubernetes Service, Azure Functions | EKS, Lambda | GKE, Cloud Functions |
| Storage migration | Azure Storage, Azure File Sync | S3, AWS DataSync | Cloud Storage, Transfer Appliance |
| Compliance/governance | Microsoft Purview, Azure Policy | AWS Config, AWS Audit Manager | Cloud Asset Inventory, Policy Intelligence |

## Why Azure as the primary reference

Most of the hands-on engagements informing this framework — particularly with small and mid-sized organizations evaluating their first cloud migration — used Azure as the target platform, largely due to existing Microsoft 365 / on-prem Active Directory investments that make Azure AD (Entra ID) integration a natural on-ramp. That said, the underlying decision logic (cost/timeline weighting, technical debt scoring, downtime tolerance, compliance gating) applies identically regardless of target platform.

## Multi-cloud / vendor-neutral note

For organizations evaluating multiple cloud providers simultaneously, or operating in regulated sectors that require vendor diversification, this framework's scoring step should be run independently per candidate platform, since the Technical Debt and Compliance scores can shift depending on how well a given provider's tooling matches the existing environment (e.g., a Linux/open-source-heavy environment may score lower technical debt against a Kubernetes-native target than against a Windows-Server-centric one).
