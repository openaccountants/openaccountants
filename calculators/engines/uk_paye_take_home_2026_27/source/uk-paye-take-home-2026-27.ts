// UK employee: income tax (code 1257L, rUK bands) and employee Class 1 NIC on an annual
// salary, 2026-27. Skills: uk-payroll (rates), uk-income-tax-sa100 (allowance taper rounding).
import { FactReader, taxYearFact, missingRule, money, ok, pct, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "uk-payroll";
export const PA = rule("PERSONAL_ALLOWANCE", 12_570, S, "Rates, bands and thresholds", "Personal allowance (code 1257L) | £12,570 a year, £1,048 a month");
export const BASIC_BAND = rule("BASIC_RATE_BAND", 37_700, S, "Rates, bands and thresholds", "PAYE, England, NI and Wales | 20% to £37,700; 40% £37,701 to £125,140; 45% above");
export const ADD_START = rule("ADDITIONAL_RATE_START", 125_140, S, "Rates, bands and thresholds", "40% £37,701 to £125,140; 45% above");
export const RATES = rule("RATES", [0.2, 0.4, 0.45], S, "Rates, bands and thresholds", "PAYE, England, NI and Wales | 20% ... 40% ... 45%");
export const TAPER = rule("TAPER_START", 100_000, S, "Rates, bands and thresholds", "Allowance taper | £1 lost per £2 of adjusted net income above £100,000; nil at £125,140");
export const TAPER_ROUND = rule("TAPER_ROUNDING", "round reduction up to whole pound", "uk-income-tax-sa100", "The taxable base / Step 4: the Personal Allowance", "A result that is not a whole pound rounds up (ITA 2007 s.35(2)-(3))");
export const PT = rule("NIC_PRIMARY_THRESHOLD", 12_570, S, "Rates, bands and thresholds", "NIC primary threshold / UEL | ... £12,570 / £50,270 a year");
export const UEL = rule("NIC_UPPER_EARNINGS_LIMIT", 50_270, S, "Rates, bands and thresholds", "NIC primary threshold / UEL | ... £12,570 / £50,270 a year");
export const EE_MAIN = rule("EE_NIC_MAIN_RATE", 0.08, S, "Rates, bands and thresholds", "Employee Class 1 (category A) | 8% PT to UEL, 2% above");
export const EE_UPPER = rule("EE_NIC_UPPER_RATE", 0.02, S, "Rates, bands and thresholds", "Employee Class 1 (category A) | 8% PT to UEL, 2% above");
const CONSTS = [PA, BASIC_BAND, ADD_START, RATES, TAPER, TAPER_ROUND, PT, UEL, EE_MAIN, EE_UPPER];

const REGIONS = ["england", "wales", "northern_ireland", "scotland"];

export const spec: EngineSpec = {
  name: "uk_paye_take_home_2026_27",
  version: "1.2.0",
  jurisdiction: "GB",
  tax_years: ["2026-27"],
  summary:
    "UK employee annual income tax (rUK rates: England, Wales, Northern Ireland) and employee Class 1 NIC (category A) on salary for 2026-27, and take-home pay. Annual basis.",
  topics: /take.?home|net pay|\bpaye\b|national insurance|\bnics?\b|income tax|salary/,
  facts: {
    annual_salary: { type: "number", required: true, description: "GBP" },
    region: { type: "string", required: true, choices: REGIONS, description: "where the employee lives for tax: england|wales|northern_ireland|scotland (Scottish taxpayers are refused: no Scottish engine yet)" },
    nic_category: { type: "string", required: false, default: "A", description: "A (only A supported)" },
    other_income: { type: "number", required: false, default: 0, description: "GBP, non-savings, no NIC" },
    gross_pension_contributions_ras: { type: "number", required: false, default: 0, description: "GBP gross relief-at-source contributions" },
    tax_year: taxYearFact(["2026-27"]),
  },
  outputs: {
    adjusted_net_income: "GBP", personal_allowance: "GBP", taxable_income: "GBP",
    income_tax: "GBP", employee_nic: "GBP", take_home_pay: "GBP",
  },
};

export const anchors = [
  "uk-payroll Example 1: £42,000 -> PAYE £490.50/month; ee NIC £196.16/month",
  "uk-income-tax-sa100 Example 2: salary £112,000, RAS gross £5,000 -> PA £9,070, taxable £102,930, tax £32,632",
];

export function allowance(ani: number): number {
  if (ani <= TAPER.value) return PA.value;
  return Math.max(PA.value - Math.ceil((ani - TAPER.value) / 2), 0);
}

export function incomeTax(nonSavings: number, ani: number, rasGross = 0): [number, number, number] {
  const pa = allowance(ani);
  const taxable = Math.max(nonSavings - pa, 0);
  const brb = BASIC_BAND.value + rasGross;
  const basic = Math.min(taxable, brb);
  // The 40% band runs to £125,140 of taxable income, extended by RAS gross.
  const higherTop = ADD_START.value + rasGross;
  const higher = Math.max(Math.min(taxable, higherTop) - brb, 0);
  const additional = Math.max(taxable - higherTop, 0);
  const r = RATES.value;
  return [pa, taxable, basic * r[0] + higher * r[1] + additional * r[2]];
}

export function eeNic(pay: number): number {
  return Math.max(Math.min(pay, UEL.value) - PT.value, 0) * EE_MAIN.value + Math.max(pay - UEL.value, 0) * EE_UPPER.value;
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const salary = f.number("annual_salary");
  const region = f.string("region", undefined, REGIONS);
  const cat = f.string("nic_category", "A");
  const other = f.number("other_income", 0);
  const ras = f.number("gross_pension_contributions_ras", 0);
  const used = { annual_salary: salary, region, nic_category: cat, other_income: other, gross_pension_contributions_ras: ras };
  if (region === "scotland") {
    return missingRule(spec.name, "Scottish income tax engine", "This engine implements rUK bands only; the Scottish bands are in uk-payroll but no Scottish engine was built for this test.", CONSTS, { inputsUsed: used });
  }
  if (cat !== "A") return missingRule(spec.name, `NIC category ${cat}`, "Only category A is implemented.", CONSTS, { inputsUsed: used });
  const totalNs = salary + other;
  const ani = totalNs - ras;
  const [pa, taxable, it] = incomeTax(totalNs, ani, ras);
  const nic = eeNic(salary);
  const takeHome = salary + other - it - nic;
  const steps = [
    `Adjusted net income = GBP ${money(totalNs)} less gross relief-at-source contributions GBP ${money(ras)} = GBP ${money(ani)}`,
    ani > TAPER.value
      ? `Personal allowance tapered: GBP ${money(PA.value)} less half the excess over GBP ${money(TAPER.value)} (rounded up) = GBP ${money(pa)}`
      : `Personal allowance = GBP ${money(pa)}`,
    `Taxable income = GBP ${money(taxable)}; basic rate band GBP ${money(BASIC_BAND.value + ras)} at ${pct(RATES.value[0])}, then ${pct(RATES.value[1])} to GBP ${money(ADD_START.value + ras)}, then ${pct(RATES.value[2])}`,
    `Income tax = GBP ${money(it)}`,
    `Employee NIC = ${pct(EE_MAIN.value)} of pay between GBP ${money(PT.value)} and GBP ${money(UEL.value)} plus ${pct(EE_UPPER.value)} above = GBP ${money(nic)}`,
    `Take-home = GBP ${money(salary + other)} less income tax and NIC = GBP ${money(takeHome)}`,
  ];
  return ok(
    spec.name,
    { label: "Take-home pay after income tax and employee NIC, 2026-27", value: r2(takeHome), currency: "GBP" },
    { adjusted_net_income: r2(ani), personal_allowance: pa, taxable_income: r2(taxable), income_tax: r2(it), employee_nic: r2(nic), take_home_pay: r2(takeHome) },
    steps,
    CONSTS,
    used,
    {
      assumptions: [
        "Annual basis (cumulative PAYE over a full year gives the same total; per-period rounding can differ by pennies)",
        "Category A, under State Pension age",
        "Take-home ignores pension, student loan and salary sacrifice unless entered",
      ],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
