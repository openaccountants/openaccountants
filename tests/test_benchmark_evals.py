"""Unit tests for the AI agent accuracy evaluation engine."""

from __future__ import annotations

import unittest
from pathlib import Path

from tools.evals.evaluator import TaxAccuracyEvaluator


class BenchmarkEvaluatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evaluator = TaxAccuracyEvaluator()

    def test_loads_benchmark_scenarios(self) -> None:
        self.assertGreater(len(self.evaluator.scenarios), 0)
        scenario_ids = [s["id"] for s in self.evaluator.scenarios]
        self.assertIn("us-bonus-depreciation-2025", scenario_ids)
        self.assertIn("au-super-guarantee-2025-26", scenario_ids)
        self.assertIn("sg-gst-standard-rate", scenario_ids)

    def test_evaluates_perfect_response(self) -> None:
        resp = (
            "Under the Superannuation Guarantee (Administration) Act 1992 and current ATO guidance, "
            "the mandatory Australian superannuation guarantee rate is 12.0% for the 2025-26 financial year."
        )
        result = self.evaluator.evaluate_response("au-super-guarantee-2025-26", resp)
        self.assertEqual(result.citation_score, 1.0)
        self.assertEqual(result.numeric_score, 1.0)
        self.assertEqual(result.overall_score, 1.0)
        self.assertEqual(len(result.missing_citations), 0)

    def test_evaluates_missing_citations_and_wrong_number(self) -> None:
        resp = "I think the Australian super rate is 11.5%."
        result = self.evaluator.evaluate_response("au-super-guarantee-2025-26", resp)
        self.assertEqual(result.citation_score, 0.0)
        self.assertEqual(result.numeric_score, 0.0)
        self.assertEqual(result.overall_score, 0.0)
        self.assertIn("ATO", result.missing_citations)

    def test_evaluates_batch_all(self) -> None:
        responses = {
            "sg-gst-standard-rate": "According to the Goods and Services Tax Act administered by IRAS, the standard GST rate is 9%.",
            "ca-federal-bpa-2025": "Under the Income Tax Act from the CRA, the 2025 federal BPA is $16,129.",
        }
        report = self.evaluator.evaluate_all(responses)
        self.assertEqual(report["total_scenarios"], len(self.evaluator.scenarios))
        self.assertGreater(report["average_overall_score"], 0.0)


if __name__ == "__main__":
    unittest.main()
