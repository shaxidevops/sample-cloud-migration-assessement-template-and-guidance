#!/usr/bin/env python3
"""
Cloud Migration Strategy Scoring Calculator

Implements the weighted composite scoring model from docs/methodology.md.
Given scores (1-4) for each of the four assessment dimensions, returns the
recommended migration strategy and flags any mandatory overrides.

Usage:
    python score_calculator.py --cost 3 --techdebt 2 --downtime 1 --compliance 2

    Or import as a module:
        from score_calculator import score_workload
        result = score_workload(cost=3, techdebt=2, downtime=1, compliance=2)
"""

import argparse
from dataclasses import dataclass


DEFAULT_WEIGHTS = {
    "cost": 0.35,
    "techdebt": 0.25,
    "downtime": 0.20,
    "compliance": 0.20,
}


@dataclass
class ScoringResult:
    composite_score: float
    default_strategy: str
    final_strategy: str
    overrides_triggered: list


def _validate_score(name: str, value: int) -> None:
    if not isinstance(value, int) or not (1 <= value <= 4):
        raise ValueError(f"{name} score must be an integer between 1 and 4, got {value}")


def _strategy_from_composite(composite: float) -> str:
    if composite <= 1.8:
        return "Refactor"
    elif composite <= 2.6:
        return "Re-platform"
    elif composite <= 3.4:
        return "Lift-and-shift (with re-platform roadmap)"
    else:
        return "Lift-and-shift only (revisit in 6-12 months)"


def score_workload(cost: int, techdebt: int, downtime: int, compliance: int,
                    weights: dict = None) -> ScoringResult:
    """
    Calculate the weighted composite score and recommended strategy for a
    single workload, applying mandatory overrides where applicable.
    """
    for name, value in [("cost", cost), ("techdebt", techdebt),
                         ("downtime", downtime), ("compliance", compliance)]:
        _validate_score(name, value)

    w = weights or DEFAULT_WEIGHTS
    if abs(sum(w.values()) - 1.0) > 0.001:
        raise ValueError(f"Weights must sum to 1.0, got {sum(w.values())}")

    composite = (
        cost * w["cost"]
        + techdebt * w["techdebt"]
        + downtime * w["downtime"]
        + compliance * w["compliance"]
    )
    composite = round(composite, 2)

    default_strategy = _strategy_from_composite(composite)
    final_strategy = default_strategy
    overrides = []

    if compliance == 4:
        overrides.append(
            "Compliance score = 4: mandatory architecture controls required "
            "from day one regardless of chosen strategy (see methodology.md Section 3)."
        )
    if downtime == 4:
        overrides.append(
            "Downtime score = 4: parallel-run cutover required regardless of "
            "cost/timeline pressure (see methodology.md Section 3)."
        )

    return ScoringResult(
        composite_score=composite,
        default_strategy=default_strategy,
        final_strategy=final_strategy,
        overrides_triggered=overrides,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Calculate cloud migration strategy recommendation from assessment scores."
    )
    parser.add_argument("--cost", type=int, required=True, help="Cost & Timeline score (1-4)")
    parser.add_argument("--techdebt", type=int, required=True, help="Technical Debt score (1-4)")
    parser.add_argument("--downtime", type=int, required=True, help="Downtime Tolerance score (1-4)")
    parser.add_argument("--compliance", type=int, required=True, help="Compliance/Sensitivity score (1-4)")
    args = parser.parse_args()

    result = score_workload(
        cost=args.cost,
        techdebt=args.techdebt,
        downtime=args.downtime,
        compliance=args.compliance,
    )

    print(f"Composite Score: {result.composite_score}")
    print(f"Recommended Strategy: {result.default_strategy}")
    if result.overrides_triggered:
        print("\nMandatory overrides triggered:")
        for o in result.overrides_triggered:
            print(f"  - {o}")


if __name__ == "__main__":
    main()
