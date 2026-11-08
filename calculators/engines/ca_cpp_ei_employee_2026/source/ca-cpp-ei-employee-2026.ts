// Canada employee CPP, CPP2 and EI for a full year, 2026. Skill: canada-payroll (2026 rows).
// ca-fed-cpp-ei serves 2025 figures only (YMPE $71,300), so the 2026 rows come from canada-payroll.
import { FactReader, taxYearFact, missingRule, money, ok, pct, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "canada-payroll";
export const CPP_RATE = rule("CPP_EMPLOYEE_RATE", 0.0595, S, "Rates and thresholds / Payroll", "CPP employee rate — 5.95%");
export const EXEMPT = rule("BASIC_EXEMPTION", 3_500, S, "Rates and thresholds / Payroll", "Basic exemption — $3,500");
export const YMPE = rule("YMPE_2026", 74_600, S, "Rates and thresholds / Payroll", "YMPE (2026) — $74,600");
export const YAMPE = rule("YAMPE_2026", 85_000, S, "Rates and thresholds / Payroll", "YAMPE (2026) — $85,000");
export const CPP2_RATE = rule("CPP2_EMPLOYEE_RATE", 0.04, S, "Section 3 -- Social Security: Employee Deductions / Canada Pension Plan (CPP) -- 2026", "CPP2 (second additional) | 4.00% | Earnings between YMPE $74,600 and YAMPE $85,000 | $416.00");
export const EI_RATE = rule("EI_EMPLOYEE_RATE_NON_QC", 0.0163, S, "Rates and thresholds / Payroll", "EI employee rate (non-QC) — 1.63%");
export const MIE = rule("EI_MAX_INSURABLE_EARNINGS", 68_900, S, "Rates and thresholds / Payroll", "Max insurable earnings — $68,900");
const CONSTS = [CPP_RATE, EXEMPT, YMPE, YAMPE, CPP2_RATE, EI_RATE, MIE];

export const spec: EngineSpec = {
  name: "ca_cpp_ei_employee_2026",
  version: "1.2.0",
  jurisdiction: "CA",
  tax_years: ["2026"],
  summary:
    "Canada (outside Quebec) employee CPP (base + first additional), CPP2 and EI premiums for a full calendar year 2026 with one employer.",
  topics: /\bcpp2?\b|\bei\b|employment insurance|canada pension|payroll deductions?/,
  facts: {
    annual_pensionable_earnings: { type: "number", required: true, description: "CAD (salary)" },
    province: { type: "string", required: true, description: "province of employment, two-letter code, e.g. ON (QC is refused: Quebec uses QPP)" },
    months_employed: { type: "number", required: false, default: 12, description: "integer 1-12" },
    tax_year: taxYearFact(["2026"]),
  },
  outputs: { cpp_base_and_first_additional: "CAD", cpp2: "CAD", ei_premium: "CAD", total: "CAD" },
};

export const anchors = [
  "Max CPP 2026 $4,230.45 and max CPP2 $416.00 reproduced",
  "Max EI premium $1,123.07 reproduced",
  "Pattern 1 (biweekly $2,884.62): EI $47.02 exact; CPP $163.60 stated vs $163.625 from the skill's own inputs (skill arithmetic off ~3 cents)",
];

export function cpp(e: number): [number, number] {
  return [
    Math.max(Math.min(e, YMPE.value) - EXEMPT.value, 0) * CPP_RATE.value,
    Math.max(Math.min(e, YAMPE.value) - YMPE.value, 0) * CPP2_RATE.value,
  ];
}

export function ei(e: number): number {
  return Math.min(e, MIE.value) * EI_RATE.value;
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const e = f.number("annual_pensionable_earnings");
  const prov = f.string("province").toUpperCase();
  const months = Math.trunc(f.number("months_employed", 12));
  const used = { annual_pensionable_earnings: e, province: prov, months_employed: months };
  if (prov === "QC" || prov === "QUEBEC") {
    return missingRule(spec.name, "Quebec QPP rates", "Quebec uses QPP and a reduced EI rate; this engine covers CPP provinces only.", CONSTS, { inputsUsed: used });
  }
  if (months !== 12) {
    return missingRule(spec.name, "part-year basic exemption proration", "The skill says the exemption is pro-rated per pay period but this engine only implements a full year.", CONSTS, { inputsUsed: used });
  }
  const [b, c2] = cpp(e);
  const base = r2(b);
  const cpp2 = r2(c2);
  const premium = r2(ei(e));
  const total = r2(base + cpp2 + premium);
  const steps = [
    `CPP = ${pct(CPP_RATE.value)} x (min(earnings, YMPE CAD ${money(YMPE.value)}) less basic exemption CAD ${money(EXEMPT.value)}) = CAD ${money(base)}`,
    `CPP2 = ${pct(CPP2_RATE.value)} x earnings between YMPE CAD ${money(YMPE.value)} and YAMPE CAD ${money(YAMPE.value)} = CAD ${money(cpp2)}`,
    `EI = ${pct(EI_RATE.value)} x min(earnings, CAD ${money(MIE.value)}) = CAD ${money(premium)}`,
    `Total = CAD ${money(total)}`,
  ];
  return ok(
    spec.name,
    { label: "Employee CPP + CPP2 + EI for 2026", value: total, currency: "CAD" },
    { cpp_base_and_first_additional: base, cpp2, ei_premium: premium, total },
    steps,
    CONSTS,
    used,
    {
      assumptions: [
        "Age 18 to 70, not receiving CPP disability, no CPT30 election",
        "One employer for the whole year (no overcontribution across employers)",
        "Annual totals; per-pay-period rounding can differ by cents",
      ],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
