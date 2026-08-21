#!/usr/bin/env python3
"""
Tax Accuracy & Grounding Evaluator for AI Agents.

Quantitatively scores AI agent responses against OpenAccountants benchmark scenarios,
evaluating statutory citation recall, numerical precision, and fact grounding.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class ScenarioResult:
    scenario_id: str
    jurisdiction: str
    citation_score: float
    numeric_score: float
    overall_score: float
    passed_citations: list[str]
    missing_citations: list[str]
    numeric_matches: list[dict[str, Any]]
    numeric_mismatches: list[dict[str, Any]]


class TaxAccuracyEvaluator:
    def __init__(self, scenarios_path: str | Path | None = None) -> None:
        if scenarios_path is None:
            scenarios_path = Path(__file__).resolve().parent / "scenarios.json"
        with open(scenarios_path, encoding="utf-8") as fh:
            self.scenarios = json.load(fh)

    def evaluate_response(self, scenario_id: str, response_text: str) -> ScenarioResult:
        scenario = next((s for s in self.scenarios if s["id"] == scenario_id), None)
        if scenario is None:
            raise KeyError(f"Unknown scenario ID: {scenario_id}")

        expected = scenario["expected"]
        required_citations = expected.get("required_citations", [])
        numeric_facts = expected.get("numeric_facts", [])

        # 1. Evaluate Citations
        passed_citations = []
        missing_citations = []
        for cite in required_citations:
            pattern = re.escape(cite)
            if re.search(pattern, response_text, re.IGNORECASE):
                passed_citations.append(cite)
            else:
                missing_citations.append(cite)

        citation_score = len(passed_citations) / len(required_citations) if required_citations else 1.0

        # 2. Evaluate Numeric Facts
        numeric_matches = []
        numeric_mismatches = []
        for fact in numeric_facts:
            target_val = float(fact["value"])
            tolerance = float(fact.get("tolerance", 0.0))
            found = False

            # Pattern for percent or number
            if fact.get("unit") == "percent":
                # Matches e.g. 12%, 12.0%, 12 percent
                for m in re.finditer(r"(\d+(?:\.\d+)?)\s*(?:%|percent)", response_text, re.IGNORECASE):
                    val = float(m.group(1))
                    if abs(val - target_val) <= tolerance:
                        found = True
                        break
            else:
                # Matches currency or raw numbers e.g. $16,129 or 16129 or 1,000,000
                for m in re.finditer(r"(?:\$|€|£|S\$)?\s?(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)", response_text):
                    cleaned = m.group(1).replace(",", "")
                    try:
                        val = float(cleaned)
                        if abs(val - target_val) <= tolerance:
                            found = True
                            break
                    except ValueError:
                        continue

            fact_info = {"concept": fact["concept"], "expected": target_val, "tolerance": tolerance}
            if found:
                numeric_matches.append(fact_info)
            else:
                numeric_mismatches.append(fact_info)

        numeric_score = len(numeric_matches) / len(numeric_facts) if numeric_facts else 1.0

        # Composite overall score: 50% citations, 50% numeric precision
        overall_score = round(0.5 * citation_score + 0.5 * numeric_score, 4)

        return ScenarioResult(
            scenario_id=scenario_id,
            jurisdiction=scenario["jurisdiction"],
            citation_score=round(citation_score, 4),
            numeric_score=round(numeric_score, 4),
            overall_score=overall_score,
            passed_citations=passed_citations,
            missing_citations=missing_citations,
            numeric_matches=numeric_matches,
            numeric_mismatches=numeric_mismatches,
        )

    def evaluate_all(self, responses_by_id: dict[str, str]) -> dict[str, Any]:
        results = []
        for s in self.scenarios:
            sid = s["id"]
            resp = responses_by_id.get(sid, "")
            res = self.evaluate_response(sid, resp)
            results.append(asdict(res))

        avg_overall = sum(r["overall_score"] for r in results) / len(results) if results else 0.0
        avg_citation = sum(r["citation_score"] for r in results) / len(results) if results else 0.0
        avg_numeric = sum(r["numeric_score"] for r in results) / len(results) if results else 0.0

        return {
            "total_scenarios": len(results),
            "average_overall_score": round(avg_overall, 4),
            "average_citation_score": round(avg_citation, 4),
            "average_numeric_score": round(avg_numeric, 4),
            "results": results,
        }
