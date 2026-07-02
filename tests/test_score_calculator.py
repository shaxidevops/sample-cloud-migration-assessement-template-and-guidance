"""
Unit tests for score_calculator.py

Run with: python -m pytest tests/test_score_calculator.py -v
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from score_calculator import score_workload, _strategy_from_composite


class TestScoreWorkload:
    def test_low_composite_recommends_refactor(self):
        result = score_workload(cost=1, techdebt=1, downtime=1, compliance=1)
        assert result.composite_score == 1.0
        assert result.default_strategy == "Refactor"
        assert result.overrides_triggered == []

    def test_high_composite_recommends_lift_and_shift(self):
        result = score_workload(cost=4, techdebt=3, downtime=3, compliance=3)
        assert result.default_strategy in (
            "Lift-and-shift (with re-platform roadmap)",
            "Lift-and-shift only (revisit in 6-12 months)",
        )

    def test_compliance_override_triggers(self):
        result = score_workload(cost=4, techdebt=4, downtime=1, compliance=4)
        assert any("Compliance score = 4" in o for o in result.overrides_triggered)

    def test_downtime_override_triggers(self):
        result = score_workload(cost=4, techdebt=1, downtime=4, compliance=1)
        assert any("Downtime score = 4" in o for o in result.overrides_triggered)

    def test_no_overrides_when_scores_below_threshold(self):
        result = score_workload(cost=3, techdebt=3, downtime=3, compliance=3)
        assert result.overrides_triggered == []

    def test_invalid_score_raises(self):
        with pytest.raises(ValueError):
            score_workload(cost=5, techdebt=2, downtime=2, compliance=2)

    def test_invalid_score_zero_raises(self):
        with pytest.raises(ValueError):
            score_workload(cost=0, techdebt=2, downtime=2, compliance=2)

    def test_non_integer_score_raises(self):
        with pytest.raises(ValueError):
            score_workload(cost=2.5, techdebt=2, downtime=2, compliance=2)

    def test_custom_weights_must_sum_to_one(self):
        bad_weights = {"cost": 0.5, "techdebt": 0.5, "downtime": 0.5, "compliance": 0.5}
        with pytest.raises(ValueError):
            score_workload(cost=2, techdebt=2, downtime=2, compliance=2, weights=bad_weights)

    def test_custom_weights_applied_correctly(self):
        custom_weights = {"cost": 0.20, "techdebt": 0.20, "downtime": 0.30, "compliance": 0.30}
        result = score_workload(cost=2, techdebt=2, downtime=2, compliance=2, weights=custom_weights)
        assert result.composite_score == 2.0


class TestStrategyBoundaries:
    @pytest.mark.parametrize("composite,expected", [
        (1.0, "Refactor"),
        (1.8, "Refactor"),
        (1.81, "Re-platform"),
        (2.6, "Re-platform"),
        (2.61, "Lift-and-shift (with re-platform roadmap)"),
        (3.4, "Lift-and-shift (with re-platform roadmap)"),
        (3.41, "Lift-and-shift only (revisit in 6-12 months)"),
        (4.0, "Lift-and-shift only (revisit in 6-12 months)"),
    ])
    def test_boundary_values(self, composite, expected):
        assert _strategy_from_composite(composite) == expected
