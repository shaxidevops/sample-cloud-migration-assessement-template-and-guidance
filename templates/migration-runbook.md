# Migration Runbook Template

A lightweight runbook to track execution once a strategy has been selected for a workload. Designed to be filled in per-workload, not as one giant document for the whole migration — small organizations rarely have the staff to manage a single monolithic project plan, and per-workload runbooks are easier to hand off or pick up if priorities shift.

## Workload: [Name]

**Selected Strategy:** [Lift-and-shift / Re-platform / Refactor]
**Composite Score:** [from scoring-worksheet.md]
**Target Go-Live Window:** [Date range]

### Pre-Migration Checklist

- [ ] Environment inventory completed and reviewed with workload owner/SME
- [ ] Backup of current state confirmed and tested (not just "a backup exists" — confirm it restores)
- [ ] Target cloud environment provisioned (resource groups, networking, identity)
- [ ] Compliance controls identified and provisioned if Compliance score ≥ 3 (see methodology.md)
- [ ] Rollback plan documented and understood by everyone involved, not just the migration lead

### Migration Steps

| Step | Owner | Status | Notes |
|---|---|---|---|
| 1. | | | |
| 2. | | | |
| 3. | | | |

### Cutover Plan

- **Cutover window:** [Date/time, accounting for Downtime Tolerance score from scoring-worksheet.md]
- **Parallel-run required?** [Yes/No — mandatory Yes if Downtime score = 4]
- **Rollback trigger conditions:** [What specific failure conditions trigger a rollback decision, decided in advance, not improvised during the cutover]

### Post-Migration Validation

- [ ] Functional validation completed (the workload does what it did before)
- [ ] Performance validation completed (the workload performs acceptably — not just "it works," but "it works well enough")
- [ ] Compliance controls validated against the requirements identified pre-migration
- [ ] Legacy environment decommission scheduled (don't decommission immediately — keep a fallback window)

### Lessons Learned

[Filled in after the migration — what would you do differently next time. This section is often skipped under time pressure and is usually the most valuable part of the document for the next workload.]
