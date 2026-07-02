# Legacy Environment Inventory Template

Complete this before scoring individual workloads. A clear inventory is the difference between a defensible migration plan and a guess.

## 1. Infrastructure Inventory

| Item | Detail |
|---|---|
| Physical/virtual servers (count, OS, age) | |
| Network architecture (VLANs, firewall rules, VPN dependencies) | |
| Storage (local disks, NAS/SAN, capacity, growth rate) | |
| Backup solution currently in use | |
| Identity/directory services (e.g., on-prem AD) | |

## 2. Application Inventory

For each application/workload:

| App Name | Purpose | Hosting (on-prem/VM/physical) | Dependencies | Data Sensitivity | Owner/SME |
|---|---|---|---|---|---|
| | | | | | |

## 3. Data Inventory

| Data Type | Volume (approx.) | Sensitivity | Current Storage | Retention Requirement |
|---|---|---|---|---|
| | | | | |

## 4. Constraints Inventory

- **Budget:** [Available migration budget, if known]
- **Timeline drivers:** [Lease expirations, EOL hardware/software dates, contract renewals]
- **Staffing:** [In-house IT capacity available to support migration; outsourcing needs]
- **Regulatory scope:** [Any compliance frameworks applicable — list explicitly, don't assume "none"]

## 5. Risk Notes

Document anything that doesn't fit cleanly into the categories above — undocumented dependencies, single points of failure, "nobody knows why this works but don't touch it" systems. These are usually where migrations actually go wrong.

---

*This template intentionally has no client-specific content pre-filled. It is meant to be copied and completed fresh for each assessment.*
