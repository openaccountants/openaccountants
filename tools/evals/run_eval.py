#!/usr/bin/env python3
"""
Interactive Benchmark Runner CLI for OpenAccountants Tax Accuracy Evaluation.

Usage:
  python tools/evals/run_eval.py --demo
  python tools/evals/run_eval.py --input responses.json --out eval_report.md
  python tools/evals/run_eval.py --jurisdiction AU
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from evaluator import TaxAccuracyEvaluator


DEMO_BASELINE_RESPONSES = {
    "us-bonus-depreciation-2025": "Bonus depreciation is phasing down by 20% each year and is 40% for 2025.",
    "au-super-guarantee-2025-26": "The Australian super guarantee is 11.5% and will increase to 12% in future years.",
    "uk-badr-lifetime-limit": "Entrepreneurs relief has a £10 million lifetime allowance taxed at 10%.",
    "sg-gst-standard-rate": "Singapore GST increased to 8% in 2023 and 9% recently.",
    "ca-federal-bpa-2025": "The Canadian basic personal amount is approximately $15,000 for federal taxes.",
    "de-solz-freigrenze": "Germany abolished the solidarity surcharge for most taxpayers with an exemption around €18,000.",
}

DEMO_GROUNDED_RESPONSES = {
    "us-bonus-depreciation-2025": (
        "Under the OBBBA amendments to IRC §168(k), federal bonus depreciation is restored to 100% "
        "for qualified property acquired and placed in service in tax year 2025."
    ),
    "au-super-guarantee-2025-26": (
        "Under the Superannuation Guarantee (Administration) Act 1992 and official ATO guidance, "
        "the mandatory superannuation guarantee rate is 12% (12.0%) starting 1 July 2025 for the 2025-26 financial year."
    ),
    "uk-badr-lifetime-limit": (
        "Per TCGA 1992 provisions administered by HMRC, Business Asset Disposal Relief (BADR) has a lifetime "
        "limit of £1,000,000 (£1M) taxed at a 10% CGT rate."
    ),
    "sg-gst-standard-rate": (
        "Under the Goods and Services Tax Act administered by IRAS, the standard GST rate in Singapore is 9%."
    ),
    "ca-federal-bpa-2025": (
        "Under the federal Income Tax Act and CRA schedules, the maximum Basic Personal Amount (BPA) for individuals "
        "with net income up to $177,882 is $16,129 in 2025."
    ),
    "de-solz-freigrenze": (
        "Under SolzG and the EStG, the single taxpayer exemption threshold (Freigrenze) for the solidarity surcharge "
        "is €18,130, above which the standard 5.5% SolZ rate applies subject to the phase-in mitigation zone."
    ),
}


def render_terminal_table(title: str, report: dict[str, Any]) -> None:
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")
    print(f"{'Scenario ID':<30} | {'Jur':<4} | {'Citation':<9} | {'Numeric':<8} | {'Overall':<8}")
    print(f"{'-'*30}-+-{'-'*4}-+-{'-'*9}-+-{'-'*8}-+-{'-'*8}")
    for r in report["results"]:
        sid = r["scenario_id"]
        jur = r["jurisdiction"]
        cit = f"{r['citation_score']*100:.1f}%"
        num = f"{r['numeric_score']*100:.1f}%"
        ovr = f"{r['overall_score']*100:.1f}%"
        print(f"{sid:<30} | {jur:<4} | {cit:<9} | {num:<8} | {ovr:<8}")
    print(f"{'-'*70}")
    print(f"  Average Citation Recall: {report['average_citation_score']*100:.1f}%")
    print(f"  Average Numeric Exactness: {report['average_numeric_score']*100:.1f}%")
    print(f"  Composite Accuracy Score: {report['average_overall_score']*100:.1f}%")
    print(f"{'='*70}\n")


def generate_markdown_report(baseline: dict[str, Any] | None, grounded: dict[str, Any], output_path: Path) -> None:
    lines = [
        "# OpenAccountants AI Tax Grounding & Accuracy Benchmark Report\n",
        f"Generated automatically by `tools/evals/run_eval.py`.\n",
        "## Summary Scorecard\n",
        "| Metric | Baseline LLM | Grounded with OpenAccountants | Delta |",
        "|---|---|---|---|",
    ]
    if baseline:
        b_cit = baseline["average_citation_score"] * 100
        g_cit = grounded["average_citation_score"] * 100
        d_cit = g_cit - b_cit

        b_num = baseline["average_numeric_score"] * 100
        g_num = grounded["average_numeric_score"] * 100
        d_num = g_num - b_num

        b_ovr = baseline["average_overall_score"] * 100
        g_ovr = grounded["average_overall_score"] * 100
        d_ovr = g_ovr - b_ovr

        lines.append(f"| **Citation Recall** | {b_cit:.1f}% | **{g_cit:.1f}%** | +{d_cit:.1f}% |")
        lines.append(f"| **Numeric Exactness** | {b_num:.1f}% | **{g_num:.1f}%** | +{d_num:.1f}% |")
        lines.append(f"| **Overall Accuracy** | {b_ovr:.1f}% | **{g_ovr:.1f}%** | +{d_ovr:.1f}% |")
    else:
        g_cit = grounded["average_citation_score"] * 100
        g_num = grounded["average_numeric_score"] * 100
        g_ovr = grounded["average_overall_score"] * 100
        lines.append(f"| **Citation Recall** | N/A | **{g_cit:.1f}%** | - |")
        lines.append(f"| **Numeric Exactness** | N/A | **{g_num:.1f}%** | - |")
        lines.append(f"| **Overall Accuracy** | N/A | **{g_ovr:.1f}%** | - |")

    lines.append("\n## Detailed Scenario Results\n")
    lines.append("| Scenario ID | Jurisdiction | Citations Passed | Missing Citations | Score |")
    lines.append("|---|---|---|---|---|")
    for r in grounded["results"]:
        sid = r["scenario_id"]
        jur = r["jurisdiction"]
        passed = ", ".join(r["passed_citations"]) or "None"
        missing = ", ".join(r["missing_citations"]) or "None"
        score = f"{r['overall_score']*100:.1f}%"
        lines.append(f"| `{sid}` | {jur} | {passed} | {missing} | **{score}** |")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report exported successfully to: {output_path.resolve()}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run accuracy evaluations against OpenAccountants benchmark suite.")
    parser.add_argument("--demo", action="store_true", help="Run comparative demonstration (Baseline vs Grounded).")
    parser.add_argument("--input", type=str, help="Path to JSON file containing {scenario_id: response_text}.")
    parser.add_argument("--jurisdiction", type=str, help="Filter scenarios by jurisdiction code (US, UK, AU, etc.).")
    parser.add_argument("--out", type=str, default="eval_report.md", help="Output markdown scorecard file path.")

    args = parser.parse_args()
    evaluator = TaxAccuracyEvaluator()

    if args.jurisdiction:
        evaluator.scenarios = [s for s in evaluator.scenarios if s["jurisdiction"].upper() == args.jurisdiction.upper()]
        if not evaluator.scenarios:
            print(f"No benchmark scenarios found for jurisdiction: {args.jurisdiction}")
            return 1

    if args.demo:
        print("\n[Running Benchmark Evaluation: Baseline LLM vs Grounded Agent]\n")
        baseline_report = evaluator.evaluate_all(DEMO_BASELINE_RESPONSES)
        render_terminal_table("Baseline LLM Performance (Without Skills)", baseline_report)

        grounded_report = evaluator.evaluate_all(DEMO_GROUNDED_RESPONSES)
        render_terminal_table("Grounded Agent Performance (With OpenAccountants)", grounded_report)

        out_path = Path(args.out)
        generate_markdown_report(baseline_report, grounded_report, out_path)
        return 0

    if args.input:
        with open(args.input, encoding="utf-8") as fh:
            responses = json.load(fh)
        report = evaluator.evaluate_all(responses)
        render_terminal_table("Evaluation Report", report)
        if args.out:
            generate_markdown_report(None, report, Path(args.out))
        return 0

    # Default if no arguments: run on demo dataset
    print("No input provided. Running evaluation on grounded responses. (Use --demo or --input <file>).")
    report = evaluator.evaluate_all(DEMO_GROUNDED_RESPONSES)
    render_terminal_table("Grounded Agent Evaluation", report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
