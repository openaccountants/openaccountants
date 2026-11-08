// Australian resident individual: income tax (after LITO) plus Medicare levy, and take-home,
// 2026-27. Skills: au-rates-2026-27 (rates, LITO, Medicare, MLS, standard WRE deduction),
// au-deductions-offsets (worked example).
import { FactReader, taxYearFact, missingRule, money, ok, pct, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "au-rates-2026-27";
export const BRACKETS = rule<[number, number | null, number][]>(
  "RESIDENT_BRACKETS_2026_27",
  [[0, 18_200, 0.0], [18_200, 45_000, 0.15], [45_000, 135_000, 0.3], [135_000, 190_000, 0.37], [190_000, null, 0.45]],
  S,
  "Individual income tax / Resident brackets",
  "Taxable income | 2025-26 rate | 2026-27 rate\n$0 -- $18,200 | 0% | 0%\n$18,201 -- $45,000 | 16% | **15%**\n$45,001 -- $135,000 | 30% | 30%\n$135,001 -- $190,000 | 37% | 37%\n$190,001+ | 45% | 45%",
);
export const LITO = rule(
  "LITO",
  { max: 700, t1: 37_500, taper1: 0.05, t2: 45_000, taper2: 0.015, nil_at: 66_667 },
  S,
  "Individual income tax / Offsets and deductions",
  "LITO | $700 to $37,500; taper 5c/$1 to $45,000; then 1.5c/$1 to nil at $66,667",
);
export const ML = rule("MEDICARE_LEVY_RATE", 0.02, S, "Medicare", "Levy | 2% of taxable income");
export const ML_LOW = rule("MEDICARE_LOW_INCOME_SINGLE_2025_26", [28_011, 35_013], S, "Medicare", "Item | 2025-26 | Source\nLow-income threshold (single) | $28,011 / shade-in to $35,013 | ATO QC 27031\n2026-27 Medicare low-income thresholds index with CPI; confirm at ATO QC 27031");
export const MLS = rule("MLS_BASE_TIER_SINGLE", 101_000, S, "Medicare", "MLS base tier | Single $101,000 / family $202,000 (then 1% / 1.25% / 1.5%)");
export const WRE = rule("STANDARD_WRE_DEDUCTION", 1_000, S, "Individual income tax / Offsets and deductions", "$1,000 standard WRE deduction | From 1 July 2026 (2026-27 returns). Excludes PSI and business-only earners");
const CONSTS = [BRACKETS, LITO, ML, ML_LOW, MLS, WRE];

export const spec: EngineSpec = {
  name: "au_resident_tax_2026_27",
  version: "1.2.0",
  jurisdiction: "AU",
  tax_years: ["2026-27"],
  summary:
    "Australia, resident for the full 2026-27 year: income tax on taxable income less LITO, plus 2% Medicare levy, plus MLS check; take-home = gross income less those.",
  topics: /income tax|take.?home|medicare|net pay|salary|tax (do|will|would) i (pay|owe)/,
  facts: {
    gross_income: { type: "number", required: true, description: "AUD (salary etc.)" },
    other_deductions: { type: "number", required: false, default: 0, description: "AUD" },
    has_salary_or_wage_income: {
      type: "boolean",
      required: true,
      description: "does the person earn salary or wages (labour income)? The engine then applies the $1,000 standard work deduction itself",
    },
    actual_work_expenses_claimed: { type: "number", required: false, default: 0, description: "work-related expenses the person chooses to claim with records" },
    has_private_hospital_cover: { type: "boolean", required: true, description: "private patient hospital cover for the full year" },
    has_help_debt: { type: "boolean", required: false, default: false, description: "HELP (study loan) debt" },
    tax_year: taxYearFact(["2026-27"]),
  },
  outputs: {
    taxable_income: "AUD", gross_tax: "AUD", lito: "AUD", income_tax_after_offsets: "AUD",
    medicare_levy: "AUD", medicare_levy_surcharge: "AUD", income_tax_plus_medicare: "AUD", take_home_pay: "AUD",
  },
};

export const anchors = [
  "Tax on full bands 2026-27: $4,020 / $31,020 / $51,370",
  "au-deductions-offsets example: TI $88,340 -> gross tax $17,022, Medicare $1,766.80",
  "LITO nil at $66,667",
];

export function taxOn(ti: number): number {
  let t = 0.0;
  for (const [lo, hi, rate] of BRACKETS.value) {
    if (ti > lo) t += ((hi === null ? ti : Math.min(ti, hi)) - lo) * rate;
  }
  return t;
}

export function lito(ti: number): number {
  const L = LITO.value;
  if (ti <= L.t1) return L.max;
  if (ti <= L.t2) return L.max - (ti - L.t1) * L.taper1;
  return Math.max(0.0, L.max - (L.t2 - L.t1) * L.taper1 - (ti - L.t2) * L.taper2);
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const gross = f.number("gross_income");
  const ded = f.number("other_deductions", 0);
  const labour = f.bool("has_salary_or_wage_income");
  const workExp = f.number("actual_work_expenses_claimed", 0);
  const phi = f.bool("has_private_hospital_cover");
  const help = f.bool("has_help_debt", false);
  const used = {
    gross_income: gross, other_deductions: ded, has_salary_or_wage_income: labour,
    actual_work_expenses_claimed: workExp, has_private_hospital_cover: phi, has_help_debt: help,
  };
  // Decided by the engine, not the AI: from 2026-27 the $1,000 standard deduction is
  // automatic for residents with salary or wage income; actual work expenses claimed
  // replace it only when larger (ATO example: $550 claimed -> $450 standard), so total
  // work deductions = max(actual, $1,000). Skill gap: au-rates says "confirm whether
  // automatic" (issue #1278).
  const workDed = labour ? Math.max(workExp, WRE.value) : workExp;
  const ti = Math.max(gross - ded - workDed, 0);
  if (help) {
    return missingRule(spec.name, "HELP repayment 2026-27 thresholds", "au-rates-2026-27 gives 2025-26 repayment thresholds only.", CONSTS, { inputsUsed: used });
  }
  if (ti <= ML_LOW.value[1]) {
    return missingRule(spec.name, "Medicare levy low-income thresholds 2026-27", "Only 2025-26 thresholds are served; 2026-27 index with CPI (skill says confirm at ATO QC 27031).", CONSTS, { inputsUsed: used });
  }
  if (!phi && ti > MLS.value) {
    return missingRule(spec.name, "MLS 2026-27 tiers", "Skill gives the base tier and rates but not the 2026-27 tier bands; MLS would apply here.", CONSTS, { inputsUsed: used });
  }
  const grossTax = taxOn(ti);
  const off = Math.min(lito(ti), grossTax);
  const netTax = grossTax - off;
  const levy = ti * ML.value;
  const total = netTax + levy;
  const takeHome = gross - total;
  const steps = [
    labour
      ? `Work deductions = the larger of actual work expenses AUD ${money(workExp)} and the standard AUD ${money(WRE.value)} = AUD ${money(workDed)} (applied automatically for salary or wage income)`
      : `Work deductions = actual work expenses AUD ${money(workExp)} (no salary or wage income, so no standard deduction)`,
    `Taxable income = AUD ${money(gross)} less other deductions AUD ${money(ded)} less work deductions AUD ${money(workDed)} = AUD ${money(ti)}`,
    `Tax on taxable income at the 2026-27 resident rates = AUD ${money(grossTax)}`,
    `Low income tax offset = AUD ${money(off)}; income tax after offsets = AUD ${money(netTax)}`,
    `Medicare levy ${pct(ML.value)} of taxable income = AUD ${money(levy)}; no surcharge (${phi ? "private hospital cover" : "income under the base tier"})`,
    `Income tax + Medicare = AUD ${money(total)}; take-home = AUD ${money(takeHome)}`,
  ];
  return ok(
    spec.name,
    { label: "Income tax + Medicare levy 2026-27 (take-home in lines)", value: r2(total), currency: "AUD" },
    {
      taxable_income: r2(ti), gross_tax: r2(grossTax), lito: r2(off), income_tax_after_offsets: r2(netTax),
      medicare_levy: r2(levy), medicare_levy_surcharge: 0.0, income_tax_plus_medicare: r2(total), take_home_pay: r2(takeHome),
    },
    steps,
    CONSTS,
    used,
    {
      assumptions: [
        "Resident for the full year",
        "No Medicare levy reduction (income above the low-income range)",
        "Take-home = gross income less income tax and Medicare levy (super is on top of salary)",
        "Standard $1,000 work deduction applied automatically for salary/wage earners (ATO 2026-27); actual work expenses replace it only if larger",
      ],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
