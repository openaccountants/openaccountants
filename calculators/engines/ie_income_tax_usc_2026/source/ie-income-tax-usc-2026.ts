// Ireland PAYE employee: income tax and USC for a full year, 2026. Skill: ie-payroll.
import { FactReader, taxYearFact, missingRule, money, ok, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "ie-payroll";
export const RATES = rule("INCOME_TAX_RATES", [0.2, 0.4], S, "Rates, bands and thresholds", "Income Tax standard rate / higher rate | 20% / 40% | 2026");
export const CUTOFF = rule("CUTOFF_SINGLE", 44_000, S, "Rates, bands and thresholds", "Standard rate cut-off point: single, widowed or surviving civil partner, no qualifying children | EUR 44,000");
export const SPC = rule("SINGLE_PERSON_CREDIT", 2_000, S, "Rates, bands and thresholds", "Single Person Tax Credit / Married or Civil Partner Tax Credit | EUR 2,000 / EUR 4,000");
export const EMP = rule("EMPLOYEE_PAYE_CREDIT", 2_000, S, "Rates, bands and thresholds", "Employee (PAYE) Tax Credit | EUR 2,000");
export const USC = rule<[number | null, number][]>(
  "USC_BANDS",
  [[12_012, 0.005], [16_688, 0.02], [41_344, 0.03], [null, 0.08]],
  S,
  "Rates, bands and thresholds",
  "USC bands (standard) | 0.5% on first EUR 12,012; 2% on next EUR 16,688; 3% on next EUR 41,344; 8% on the balance",
);
export const USC_EX = rule("USC_EXEMPT_LIMIT", 13_000, S, "Rates, bands and thresholds", "USC exemption: total income at or below | EUR 13,000 (above it, USC on all income)");
const CONSTS = [RATES, CUTOFF, SPC, EMP, USC, USC_EX];

export const spec: EngineSpec = {
  name: "ie_income_tax_usc_2026",
  version: "1.2.0",
  jurisdiction: "IE",
  tax_years: ["2026"],
  summary: "Ireland 2026: income tax (after personal + PAYE credits) and USC for a single PAYE employee for the full year, cumulative basis.",
  topics: /income tax|\busc\b|universal social charge|take.?home|net pay|salary|\bpaye\b/,
  facts: {
    gross_pay: { type: "number", required: true, description: "EUR" },
    employee_pension_contribution: { type: "number", required: false, default: 0, description: "EUR (relieved for income tax, not USC)" },
    status: { type: "string", required: true, description: "single, married, etc. (only single without children is computed; others are refused)" },
    age_70_or_full_medical_card: { type: "boolean", required: false, default: false, description: "aged 70+ or holds a full medical card" },
    tax_year: taxYearFact(["2026"]),
  },
  outputs: { taxable_pay: "EUR", gross_income_tax: "EUR", tax_credits: "EUR", income_tax: "EUR", usc: "EUR", income_tax_plus_usc: "EUR" },
};

export const anchors = ["ie-payroll Example 1: EUR 5,000/month, EUR 4,750 taxable -> income tax EUR 833.33, USC EUR 111.07 a month"];

export function incomeTax(taxable: number, cutoff = CUTOFF.value, credits = SPC.value + EMP.value): number {
  const g = Math.min(taxable, cutoff) * RATES.value[0] + Math.max(taxable - cutoff, 0) * RATES.value[1];
  return Math.max(g - credits, 0);
}

export function usc(gross: number): number {
  if (gross <= USC_EX.value) return 0.0;
  let rem = gross;
  let tot = 0.0;
  for (const [width, rate] of USC.value) {
    const part = width === null ? rem : Math.min(rem, width);
    tot += part * rate;
    rem -= part;
    if (rem <= 0) break;
  }
  return tot;
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const gross = f.number("gross_pay");
  const pen = f.number("employee_pension_contribution", 0);
  const status = f.string("status");
  const old = f.bool("age_70_or_full_medical_card", false);
  const used = { gross_pay: gross, employee_pension_contribution: pen, status, age_70_or_full_medical_card: old };
  if (status !== "single") {
    return missingRule(spec.name, `cut-off and credits for status '${status}'`, "Only single without children is implemented.", CONSTS, { inputsUsed: used });
  }
  if (old) return missingRule(spec.name, "USC reduced rates engine", "Reduced USC rates are in the skill but not implemented in this engine.", CONSTS, { inputsUsed: used });
  const taxable = gross - pen;
  const it = incomeTax(taxable);
  const u = usc(gross);
  const grossIt = Math.min(taxable, CUTOFF.value) * 0.2 + Math.max(taxable - CUTOFF.value, 0) * 0.4;
  const credits = SPC.value + EMP.value;
  const steps = [
    `Taxable pay = EUR ${money(gross)} less pension contribution EUR ${money(pen)} = EUR ${money(taxable)}`,
    `Income tax before credits = 20% up to the EUR ${money(CUTOFF.value)} cut-off, 40% above = EUR ${money(grossIt)}`,
    `Less personal and PAYE credits EUR ${money(credits)} = income tax EUR ${money(it)}`,
    gross <= USC_EX.value
      ? `USC: total income at or below EUR ${money(USC_EX.value)}, so exempt`
      : `USC on EUR ${money(gross)} through the standard bands = EUR ${money(u)}`,
    `Income tax + USC = EUR ${money(it + u)}`,
  ];
  return ok(
    spec.name,
    { label: "Income tax + USC for 2026", value: r2(it + u), currency: "EUR" },
    { taxable_pay: r2(taxable), gross_income_tax: r2(grossIt), tax_credits: credits, income_tax: r2(it), usc: r2(u), income_tax_plus_usc: r2(it + u) },
    steps,
    CONSTS,
    used,
    { assumptions: ["Full-year cumulative basis", "Under 70, no full medical card (standard USC)", "PRSI not included (not asked)"], anchors },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
