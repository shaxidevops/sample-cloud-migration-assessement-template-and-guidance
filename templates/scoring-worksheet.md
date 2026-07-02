# Scoring Worksheet Template

Copy this table per workload being assessed. Fill in scores 1–4 per the rubric in `docs/methodology.md`, Section 2.

## Workload: [Name/Identifier]

**Description:** [One-line description of the workload — e.g., "Customer billing application, currently on-prem SQL Server + IIS"]

| Dimension | Weight (default) | Score (1-4) | Notes |
|---|---|---|---|
| Cost & Timeline Constraint | 0.35 | | |
| Technical Debt & Architecture Age | 0.25 | | |
| Downtime Tolerance | 0.20 | | |
| Data Sensitivity & Compliance | 0.20 | | |

**Composite Score:** `(Cost × 0.35) + (TechDebt × 0.25) + (Downtime × 0.20) + (Compliance × 0.20) = ___`

**Recommended Strategy (before overrides):** [Lift-and-shift / Re-platform / Refactor]

**Override checks:**
- [ ] Compliance score = 4? → Mandatory controls apply regardless of composite (see Section 3)
- [ ] Downtime score = 4? → Parallel-run cutover required regardless of composite (see Section 3)

**Final Recommended Strategy:** [ ]

**Rationale (2-3 sentences):**

---

## Notes on use

- Score each workload independently. A single organization migrating ten systems will typically end up with a mix of strategies — that's expected, not a sign the framework failed.
- Re-score if material facts change (e.g., a "soft deadline" becomes a hard one after a vendor contract notice, or new compliance scope is discovered mid-assessment).
- Keep notes specific and factual ("SQL Server 2012, vendor support ended 2022" rather than "old system") — vague notes make the score impossible to defend or revisit later.
