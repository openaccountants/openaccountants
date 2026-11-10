// Ireland, self-employed individual (sole trader): income tax, USC and PRSI Class S for tax years
// 2025 and 2026, and the minimum preliminary tax for the following year. Skills: ie-income-tax-form11,
// ie-usc, ie-prsi-class-s, ie-preliminary-tax.
//
// Money is exact: inputs are read to the cent and every charge is computed in exact decimals, then
// rounded to the cent half up. Floating point would decide ties such as 36,500 x 4.125% = 1,505.625
// by the binary value of the product instead of the cent rule.
//
// The PAYE engine (ie_income_tax_usc_2026, skill ie-payroll) is not imported: its band functions
// work in floating point and hold 2026 figures only. The tests check that both give the same 2026
// income tax and USC on the cases they share.
import { FactReader, NeedsInput, missingRule, money, ok, pct, rule, taxYearFact, type Engine, type EngineSpec, type Rule } from "./types";

const F11 = "ie-income-tax-form11";
const USCS = "ie-usc";
const PRSI = "ie-prsi-class-s";
const PRE = "ie-preliminary-tax";
const RATES = "Rates, bands and thresholds";
const BASE = "The taxable base";
const DEADLINES = "Deadlines and filing";

// Income tax (Form 11 skill: bands and credits are the same for 2025 and 2026).
export const BAND_SINGLE = rule("BAND_SINGLE", 44_000, F11, RATES,
  "Standard rate band, single or widowed, no qualifying children (s.15, Table Part 1) | first EUR 44,000 at 20%, balance at 40% | 2025 and 2026");
export const BAND_SPCCC = rule("BAND_SINGLE_PARENT", 48_000, F11, RATES,
  "Band, single person qualifying for the Single Person Child Carer Credit (s.15, Part 2) | first EUR 48,000 at 20%, balance at 40% | 2025 and 2026");
export const BAND_MARRIED = rule("BAND_MARRIED", 53_000, F11, RATES,
  "Band, married or civil partners (s.15, Part 3) | first EUR 53,000 at 20%, balance at 40% | 2025 and 2026");
export const BAND_INCREASE = rule("BAND_SECOND_INCOME_INCREASE", 35_000, F11, RATES,
  "Increase for a second income (s.15(3)(i)) | lower of EUR 35,000 or the lower earner's income; not transferable | 2025 and 2026");
export const IT_RATES = rule("INCOME_TAX_RATES", [0.2, 0.4], F11, RATES,
  "Standard rate band, single or widowed, no qualifying children (s.15, Table Part 1) | first EUR 44,000 at 20%, balance at 40%");
export const PERSONAL = rule("PERSONAL_CREDITS", { single: 2_000, married: 4_000 }, F11, RATES,
  "Single Person Tax Credit / Married or Civil Partner Tax Credit (s.461) | EUR 2,000 / EUR 4,000 | 2025 and 2026");
export const SPCCC = rule("SINGLE_PERSON_CHILD_CARER_CREDIT", 1_900, F11, RATES,
  "Single Person Child Carer Credit (s.462B) | EUR 1,900 | 2025 and 2026");
export const EMPLOYEE = rule("EMPLOYEE_CREDIT", 2_000, F11, RATES,
  "Employee (PAYE) Tax Credit (s.472) | EUR 2,000 | 2025 and 2026");
export const EIC = rule("EARNED_INCOME_CREDIT", { max: 2_000, rate: 0.2 }, F11, RATES,
  "Earned Income Tax Credit (s.472AB) | lower of EUR 2,000 or 20% of qualifying earned income; with the Employee credit, the two together cannot exceed EUR 2,000 | 2025 and 2026");
export const EIC_SCOPE = rule("EARNED_INCOME_CREDIT_SCOPE", true, F11, BASE,
  "Then subtract credits; credits reduce tax, not income ... The Earned Income Credit is for self-employed earned income and a proprietary director's pay, not rent or interest.");
export const HOME_CARER = rule("HOME_CARER_CREDIT_MAX", 1_950, F11, RATES, "Home Carer Tax Credit, maximum (s.466A) | EUR 1,950 | 2025 and 2026");
export const AGE_CREDIT = rule("AGE_CREDIT", { single: 245, married: 490 }, F11, RATES, "Age Tax Credit, single / married | EUR 245 / EUR 490 | 2025 and 2026");
export const PENSION_PCT = rule<[number, number][]>("PENSION_RELIEF_PERCENT_BY_AGE",
  [[30, 0.15], [40, 0.2], [50, 0.25], [55, 0.3], [60, 0.35], [Infinity, 0.4]], F11, RATES,
  "Pension relief (RAC, PRSA), % of net relevant earnings by age | under 30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% | 2026");
export const PENSION_CAP = rule("PENSION_EARNINGS_LIMIT", 115_000, F11, RATES, "Pension relief earnings limit | EUR 115,000 a year | 2026");
export const RENT_NOT_NRE = rule("RENT_NOT_RELEVANT_EARNINGS", true, F11, BASE,
  "Deduct pension contributions (Panel I) within the age percentage of net relevant earnings and the EUR 115,000 earnings limit. Rental income is not relevant earnings.");
export const BEFORE_PENSION = rule("USC_PRSI_BEFORE_PENSION", true, F11, BASE,
  "USC: on total income after capital allowances (active traders) but before pension contributions; the surcharge tests non-PAYE income only.\nPRSI Class S: on gross income after capital allowances, before pension contributions; minimum EUR 650");

// USC.
export const USC_2026 = rule<[number | null, number][]>("USC_BANDS_2026", [[12_012, 0.005], [16_688, 0.02], [41_344, 0.03], [null, 0.08]], USCS, RATES,
  "Standard band 1 (s.531AN, Table Part 1) | 0.5% on the first EUR 12,012 | 2026\nStandard band 2 | 2% on the next EUR 16,688 | 2026\nStandard band 3 | 3% on the next EUR 41,344 | 2026\nBalance | 8% on the remainder (above EUR 70,044) | 2026");
/** 2025 bands as the skill states them: upper limits, not widths. */
export const USC_2025 = rule<[number | null, number][]>("USC_BANDS_2025", [[12_012, 0.005], [27_382, 0.02], [70_044, 0.03], [null, 0.08]], F11, RATES,
  "USC for the 2025 return due now | 0.5% on first EUR 12,012; 2% from EUR 12,012 to EUR 27,382; 3% to EUR 70,044; 8% on the balance | 2025");
export const USC_EXEMPT = rule("USC_EXEMPTION_LIMIT_2026", 13_000, USCS, RATES,
  "Exemption: no USC if aggregate income does not exceed (s.531AM(2)); above it, USC on the full income | EUR 13,000 | 2026");
export const USC_MEDICAL = rule("USC_MEDICAL_CARD_2026", { limit: 60_000, standard_up_to: 28_700, rate: 0.02 }, USCS, RATES,
  "Reduced rate, full medical card holder under 70, aggregate income EUR 60,000 or less (s.531AN(3)) | Standard bands up to EUR 28,700, then 2% at most on the excess (same result as the reduced rates) | 2026\nAbove EUR 60,000 the standard rates apply to all income, not just the excess");
export const USC_SURCHARGE = rule("USC_NON_PAYE_SURCHARGE_2026", { over: 100_000, rate: 0.03 }, USCS, RATES,
  "Surcharge on relevant (non-PAYE) income over EUR 100,000 (s.531AN(2)) | 3% on the excess, so 11% in total on it | 2026");

// PRSI Class S.
export const PRSI_2026 = rule("CLASS_S_RATE_2026", 0.042375, PRSI, RATES,
  "Blended rate for 2026 self-assessed income: ((4.2 x 9) + (4.35 x 3)) / 12 | 4.2375% | 2026");
export const PRSI_MIN = rule("CLASS_S_MINIMUM_2026", 650, PRSI, RATES,
  "Minimum annual contribution (reckonable income, emoluments, or both together) | EUR 650 | 2026");
export const PRSI_FLOOR = rule("CLASS_S_FLOOR_2026", 5_000, PRSI, RATES,
  "Income floor: below this, no Class S (total before capital allowances) | under EUR 5,000 | 2026");
export const PRSI_2025 = rule("CLASS_S_2025", { rate: 0.04125, minimum: 650 }, F11, RATES, "PRSI Class S on 2025 income | 4.125% blended, minimum EUR 650 | 2025");
export const PRSI_FLOOR_TEST = rule("CLASS_S_FLOOR_TEST", true, PRSI, "Who this applies to",
  "a person whose total reckonable income, emoluments and earnings, before capital allowances, is below EUR 5,000");
export const PRSI_BASE = rule("CLASS_S_RECKONABLE_INCOME", true, PRSI, BASE,
  "Reckonable income is the aggregate income from all sources for the contribution year, as estimated under the Income Tax Acts, after capital allowances. It leaves out reckonable earnings and reckonable emoluments\nso each spouse or civil partner's Class S is worked out on their own income");
export const PRSI_AGE = rule("CLASS_S_AGE", 66, PRSI, "Who this applies to",
  "Every person aged over 16 and under pensionable age (66) who has reckonable income or reckonable emoluments is a self-employed contributor");

// Preliminary tax for the following year.
export const PRELIM_2026 = rule("PRELIMINARY_TAX_TESTS_2026", { current: 0.9, preceding: 1, pre_preceding: 1.05 }, PRE, RATES,
  "Safe harbour 1: current year | 90% of the income tax payable for 2026 | 2026\nSafe harbour 2: preceding year | 100% of the income tax payable for 2025 | 2026\nSafe harbour 3: pre-preceding year, direct debit payers only | 105% of the income tax payable for 2024; not available if that was nil");
export const PRELIM_WORKING = rule("PRELIMINARY_TAX_WORKING_RULE", true, PRE, BASE,
  "Working rule. For each option: income tax + USC + PRSI for that year, after credits and after tax deducted at source.");
export const PRELIM_DUE_2026 = rule("PRELIMINARY_TAX_DUE_2026", "2026-10-31", PRE, RATES,
  "Preliminary tax due date (not direct debit) | 31 October of the tax year: 31 October 2026 for 2026 | 2026\nROS extension, 2025 Form 11 balance and 2026 preliminary tax | Wednesday 18 November 2026, only if the person both pays and files through ROS | 2026");
export const PRELIM_LATE_2026 = rule("PRELIMINARY_TAX_SHORTFALL_2026", true, PRE, "Penalties and interest",
  "The whole 2026 income tax (with USC and PRSI) is treated as due on 31 October 2026 if (a) preliminary tax was not paid, (b) it was less than the lowest test that applies, or (c) it was paid after 31 October 2026 (s.959AO(3)).");
export const PRELIM_TESTS_GENERAL = rule("PRELIMINARY_TAX_TESTS", { current: 0.9, preceding: 1, pre_preceding: 1.05 }, F11, RATES,
  "Preliminary tax safe harbours (s.959AO) | lowest of 90% of current year, 100% of previous year, 105% of pre-preceding year (direct debit only, not if that year was nil) | 2026");
export const RETURN_2026 = rule("RETURN_2026_AND_PRELIMINARY_2027", "2027-10-31", F11, DEADLINES,
  "The 2026 return is due by 31 October 2027, with 2027 preliminary tax. Revenue has not yet announced the 2027 ROS date.");
export const BALANCE_2026 = rule("BALANCE_2026_DUE", "2027-10-31", PRE, RATES,
  "Balance of 2026 tax (if preliminary tax was sufficient and on time) | Specified return date: 31 October 2027 | 2026");

const CONSTS: Rule[] = [
  BAND_SINGLE, BAND_SPCCC, BAND_MARRIED, BAND_INCREASE, IT_RATES, PERSONAL, SPCCC, EMPLOYEE, EIC, EIC_SCOPE, HOME_CARER, AGE_CREDIT,
  PENSION_PCT, PENSION_CAP, RENT_NOT_NRE, BEFORE_PENSION, USC_2026, USC_2025, USC_EXEMPT, USC_MEDICAL, USC_SURCHARGE,
  PRSI_2026, PRSI_MIN, PRSI_FLOOR, PRSI_2025, PRSI_FLOOR_TEST, PRSI_BASE, PRSI_AGE,
  PRELIM_2026, PRELIM_WORKING, PRELIM_DUE_2026, PRELIM_LATE_2026, PRELIM_TESTS_GENERAL, RETURN_2026, BALANCE_2026,
];

const STATUSES = ["single", "married_one_income", "married_two_incomes", "single_parent"];

export const spec: EngineSpec = {
  name: "ie_self_employed_2025_2026",
  version: "1.0.0",
  jurisdiction: "IE",
  tax_years: ["2025", "2026"],
  summary:
    "Ireland, self-employed sole trader, tax year 2025 or 2026: income tax (bands, personal, earned income and employee credits, pension relief), USC, PRSI Class S, the Form 11 balance, and the minimum preliminary tax for the next year (lowest of 90% of next year, 100% of this year, 105% of the year before for direct debit).",
  topics: /self.?employ|sole.?trader|freelanc|\bform ?11\b|preliminary tax|\bclass s\b|trading profit|\bcase (?:i|ii)\b|earned income (?:tax )?credit|my (?:own )?business|contractor/,
  facts: {
    tax_year: taxYearFact(["2025", "2026"]),
    status: {
      type: "string",
      required: true,
      choices: STATUSES,
      description:
        "single (not widowed); single_parent (single and qualifies for the Single Person Child Carer Credit); married_one_income (married or civil partners, jointly assessed, the spouse has no income); married_two_incomes (jointly assessed, the spouse has a PAYE salary)",
    },
    trading_profit: {
      type: "number",
      required: true,
      description: "EUR, this person's adjusted Case I or II trading profit for the year after capital allowances, before pension contributions (an active sole trader)",
    },
    capital_allowances: {
      type: "number",
      required: false,
      default: 0,
      description: "EUR capital allowances already deducted in trading_profit (used only for the PRSI EUR 5,000 floor, which is tested before capital allowances)",
    },
    other_income: {
      type: "number",
      required: false,
      default: 0,
      description:
        "EUR this person's other taxable income: a PAYE salary (set other_income_is_paye true) or non-PAYE income such as Irish rental profit. Leave out social welfare payments, DIRT-paid deposit interest and other income exempt from USC or PRSI",
    },
    other_income_is_paye: { type: "boolean", required: false, description: "needed when other_income is more than 0: true if it is a PAYE salary from an employment" },
    spouse_income: { type: "number", required: false, description: "needed for married_two_incomes: EUR the spouse's PAYE salary for the year" },
    spouse_income_is_paye: { type: "boolean", required: false, description: "needed for married_two_incomes: true if the spouse's income is all PAYE salary (any other spouse income is refused)" },
    paye_income_tax_deducted: {
      type: "number",
      required: false,
      description: "needed when a PAYE salary is included: EUR income tax deducted under PAYE in the year from the salaries in this assessment (this person's and, for married_two_incomes, the spouse's)",
    },
    paye_usc_deducted: { type: "number", required: false, description: "needed when this person has a PAYE salary: EUR USC deducted from it in the year" },
    pension_contributions: { type: "number", required: false, default: 0, description: "EUR this person paid into a personal pension (RAC or PRSA) for the year; relieved for income tax only, within the age limit (2026 only)" },
    age: { type: "number", required: false, description: "needed when pension_contributions is more than 0: this person's age, for the pension relief percentage" },
    age_65_plus: { type: "boolean", required: false, default: false, description: "this person or the spouse is aged 65 or over in the year (refused: the skills do not settle these cases)" },
    medical_card: { type: "boolean", required: false, default: false, description: "this person held a full medical card (not a GP visit card) at any time in the year and told Revenue" },
    home_carer_credit: { type: "boolean", required: false, default: false, description: "the couple claims the Home Carer Tax Credit (refused: the skill states only its maximum)" },
    preliminary_tax_paid: { type: "number", required: false, default: 0, description: "EUR preliminary tax already paid for tax_year" },
    next_year_liability_estimate: {
      type: "number",
      required: false,
      description:
        "EUR expected income tax + USC + PRSI for the year after tax_year, after credits and tax deducted at source (for the 90% test). For 2026, run this engine for tax_year 2026 with the expected 2026 figures. Left out, the 90% test is not used",
    },
    pays_by_direct_debit: { type: "boolean", required: false, default: false, description: "pays next year's preliminary tax by monthly direct debit (the 105% test applies only then)" },
    liability_year_before: {
      type: "number",
      required: false,
      description: "EUR final income tax + USC + PRSI for the year before tax_year (2024 for tax_year 2025), after credits and tax deducted at source; needed for the 105% direct debit test",
    },
  },
  outputs: {
    taxable_income: "EUR",
    rate_band: "EUR at 20%",
    gross_income_tax: "EUR",
    tax_credits: "EUR",
    income_tax: "EUR",
    usc: "EUR",
    prsi_class_s: "EUR",
    total_liability: "EUR",
    tax_deducted_at_source: "EUR",
    net_liability: "EUR",
    balance_due: "EUR (negative = overpaid)",
    preliminary_tax: "options, minimum and due date for the next year",
    pay_by_return_date: "EUR balance due plus minimum preliminary tax",
  },
};

export const anchors = [
  "ie-income-tax-form11 Example 1: single, profit EUR 60,000 (2026) -> income tax EUR 11,200, USC EUR 1,332.82, PRSI EUR 2,542.50, total EUR 15,075.32",
  "ie-income-tax-form11 Example 2: profit EUR 93,500 after capital allowances, rent EUR 12,000, PRSA EUR 8,000 (2026) -> income tax EUR 26,200, USC EUR 4,635.62, PRSI EUR 4,470.56, total EUR 35,306.18",
  "ie-usc Example 1: income for USC EUR 56,000 -> USC EUR 1,212.82",
  "ie-prsi-class-s Example 1: reckonable income EUR 80,000 (2026) -> Class S EUR 3,390.00",
  "ie-prsi-class-s Example 2: 2025 reckonable income EUR 14,000 -> Class S EUR 650 (minimum)",
  "ie-preliminary-tax Example 1: 2025 liability EUR 18,400, 2026 estimate EUR 21,000 -> minimum EUR 18,400, pay EUR 20,800",
  "ie-preliminary-tax Example 2: direct debit, 2024 EUR 12,000, 2025 EUR 30,000, 2026 EUR 15,000 -> minimum EUR 12,600",
];

// ---- exact money ----------------------------------------------------------------------------
// An amount is a bigint count of 1e-14 euro. Inputs arrive to the cent (12 more digits of room),
// and every rate has at most 6 decimals, so two rate multiplications in a row stay exact.
const PER_CENT = BigInt("1000000000000");
const MILLION = BigInt(1_000_000);
const ZERO = BigInt(0);

/** Euro (read to the cent) as an exact amount. */
export function eur(x: number): bigint {
  return BigInt(Math.round(x * 100)) * PER_CENT;
}
function times(a: bigint, rate: number): bigint {
  const m = Math.round(rate * 1e6);
  if (Math.abs(m - rate * 1e6) > 1e-6) throw new Error(`rate ${rate} has more than 6 decimals`);
  const p = a * BigInt(m);
  if (p % MILLION !== ZERO) throw new Error("inexact money product");
  return p / MILLION;
}
const bmin = (a: bigint, b: bigint) => (a < b ? a : b);
const bmax = (a: bigint, b: bigint) => (a > b ? a : b);
/** Exact amount rounded to the cent, half up, as a number of euro. */
export function toEur(a: bigint): number {
  if (a < ZERO) return -toEur(-a);
  const cents = (a + PER_CENT / BigInt(2)) / PER_CENT;
  return Number(cents) / 100;
}
const roundCent = (a: bigint) => eur(toEur(a));

/** Tax on an amount through bands given as widths (null = the rest). */
function byWidths(x: bigint, bands: [number | null, number][]): bigint {
  let rem = x;
  let tot = ZERO;
  for (const [w, r] of bands) {
    if (rem <= ZERO) break;
    const part = w === null ? rem : bmin(rem, eur(w));
    tot += times(part, r);
    rem -= part;
  }
  return tot;
}
function widthsFromUppers(uppers: [number | null, number][]): [number | null, number][] {
  let prev = 0;
  return uppers.map(([u, r]) => {
    const w: [number | null, number] = [u === null ? null : u - prev, r];
    if (u !== null) prev = u;
    return w;
  });
}

/**
 * USC on aggregate income for one person (exact), or a reason it is not served.
 * 2025: the skill states the bands only, so the engine computes 2025 only above EUR 13,000 of
 * income, up to EUR 100,000 of non-PAYE income and without a medical card (the 2026 limits),
 * and refuses the rest.
 */
export function uscFor(year: string, aggregate: number, nonPaye: number, medicalCard: boolean): { usc: bigint; surcharge: bigint } | { refuse: string } {
  const agg = eur(aggregate);
  const np = eur(nonPaye);
  if (year === "2025") {
    if (agg <= eur(USC_EXEMPT.value)) return { refuse: "USC exemption limit for 2025" };
    if (np > eur(USC_SURCHARGE.value.over)) return { refuse: "USC surcharge on non-PAYE income for 2025" };
    if (medicalCard) return { refuse: "USC reduced rate for a medical card holder in 2025" };
    return { usc: byWidths(agg, widthsFromUppers(USC_2025.value)), surcharge: ZERO };
  }
  if (agg <= eur(USC_EXEMPT.value)) return { usc: ZERO, surcharge: ZERO };
  if (medicalCard && agg <= eur(USC_MEDICAL.value.limit)) {
    const upTo = eur(USC_MEDICAL.value.standard_up_to);
    return { usc: byWidths(bmin(agg, upTo), USC_2026.value) + times(bmax(agg - upTo, ZERO), USC_MEDICAL.value.rate), surcharge: ZERO };
  }
  const over = eur(USC_SURCHARGE.value.over);
  const surcharge = np > over ? times(np - over, USC_SURCHARGE.value.rate) : ZERO;
  return { usc: byWidths(agg, USC_2026.value) + surcharge, surcharge };
}

export interface PrelimOptions {
  current_year_90?: number;
  previous_year_100: number;
  pre_preceding_year_105?: number;
  minimum: number;
}

/** The preliminary tax tests (ie-preliminary-tax): the lowest of the options that apply. */
export function preliminaryOptions(thisYear: number, nextYearEstimate: number | null, yearBefore: number | null, directDebit: boolean): PrelimOptions {
  const t = PRELIM_2026.value;
  const out: PrelimOptions = { previous_year_100: toEur(times(bmax(eur(thisYear), ZERO), t.preceding)), minimum: 0 };
  if (nextYearEstimate !== null) out.current_year_90 = toEur(times(eur(nextYearEstimate), t.current));
  if (directDebit && yearBefore !== null && yearBefore > 0) out.pre_preceding_year_105 = toEur(times(eur(yearBefore), t.pre_preceding));
  out.minimum = Math.min(...[out.current_year_90, out.previous_year_100, out.pre_preceding_year_105].filter((v): v is number => v !== undefined));
  return out;
}

function pensionPct(age: number): number {
  return PENSION_PCT.value.find(([under]) => age < under)![1];
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const year = f.string("tax_year");
  const status = f.string("status", undefined, STATUSES);
  const trading = f.number("trading_profit");
  const ca = f.number("capital_allowances", 0);
  const other = f.number("other_income", 0);
  const pension = f.number("pension_contributions", 0);
  const old = f.bool("age_65_plus", false);
  const medical = f.bool("medical_card", false);
  const homeCarer = f.bool("home_carer_credit", false);
  const prelimPaid = f.number("preliminary_tax_paid", 0);
  const directDebit = f.bool("pays_by_direct_debit", false);
  const used: Record<string, unknown> = {
    tax_year: year, status, trading_profit: trading, capital_allowances: ca, other_income: other, pension_contributions: pension,
    age_65_plus: old, medical_card: medical, home_carer_credit: homeCarer, preliminary_tax_paid: prelimPaid, pays_by_direct_debit: directDebit,
  };
  const refuse = (what: string, why: string, consts: Rule[], partial: Record<string, unknown> = {}) =>
    missingRule(spec.name, what, why, consts, { inputsUsed: used, partial });

  if (old) {
    return refuse("income tax, USC and PRSI for a person aged 65 or over",
      "The Form 11 skill gives the Age Tax Credit (EUR 245 / EUR 490) but not the age it starts at, nor any age exemption limit for income tax; ie-prsi-class-s ends Class S at 66 unless no State Pension (Contributory) is awarded, and USC reduced rates start at 70. The engine does not compute these cases.",
      [AGE_CREDIT, PRSI_AGE]);
  }
  if (homeCarer) {
    return refuse("Home Carer Tax Credit", "The Form 11 skill states only its maximum (EUR 1,950), not who qualifies or how it is reduced by the carer's income.", [HOME_CARER]);
  }

  const ownPaye = other > 0 ? f.bool("other_income_is_paye") : false;
  if (other > 0) used.other_income_is_paye = ownPaye;
  const salary = ownPaye ? other : 0;
  const nonPayeOther = ownPaye ? 0 : other;
  let spouse = 0;
  if (status === "married_two_incomes") {
    spouse = f.number("spouse_income");
    const spousePaye = f.bool("spouse_income_is_paye");
    used.spouse_income = spouse;
    used.spouse_income_is_paye = spousePaye;
    if (!spousePaye) {
      return refuse("a spouse with non-PAYE income",
        "The engine computes a jointly assessed spouse only when the spouse's income is a PAYE salary; the spouse's own earned income credit, USC and Class S on non-PAYE income are not implemented.", [EIC, PRSI_BASE]);
    }
    if (spouse <= 0) throw new NeedsInput("status 'married_two_incomes' needs the spouse's salary in 'spouse_income'; with no spouse income use 'married_one_income'");
  }
  const smallSalary = (salary > 0 && salary < 10_000) || (status === "married_two_incomes" && spouse < 10_000);
  if (smallSalary) {
    return refuse("Employee (PAYE) Tax Credit on a salary under EUR 10,000",
      "The Form 11 skill gives the Employee credit as EUR 2,000 and limits only the Earned Income Credit to 20% of the income; it does not say whether the Employee credit is limited on a small salary. Below EUR 10,000 of salary that would change the answer, so the engine refuses.",
      [EMPLOYEE, EIC]);
  }

  // Pension relief (income tax only).
  let relief = ZERO;
  let age: number | null = null;
  const consts: Rule[] = [];
  if (pension > 0) {
    if (year === "2025") {
      return refuse("pension relief limits for 2025", "The Form 11 skill states the age percentages and the EUR 115,000 earnings limit for 2026 only.", [PENSION_PCT, PENSION_CAP]);
    }
    if (salary > 0) {
      return refuse("pension relief with a PAYE salary",
        "The skill measures the limit on net relevant earnings and does not say whether this salary counts (it would not if it is pensionable employment), so the engine does not compute it.", [PENSION_PCT, PENSION_CAP]);
    }
    age = f.number("age");
    if (!Number.isInteger(age)) throw new NeedsInput("input 'age' must be a whole number");
    if (age >= 65) throw new NeedsInput("input 'age' is 65 or over but 'age_65_plus' is false: check the age");
    used.age = age;
    const limit = times(bmin(eur(trading), eur(PENSION_CAP.value)), pensionPct(age));
    relief = bmin(eur(pension), limit);
    consts.push(PENSION_PCT, PENSION_CAP, RENT_NOT_NRE);
  }

  // Income tax.
  const ownIncome = eur(trading) + eur(other);
  let band = eur(status === "single" ? BAND_SINGLE.value : status === "single_parent" ? BAND_SPCCC.value : BAND_MARRIED.value);
  consts.unshift(status === "single" ? BAND_SINGLE : status === "single_parent" ? BAND_SPCCC : BAND_MARRIED);
  let increase = ZERO;
  if (status === "married_two_incomes") {
    const sp = eur(spouse);
    if (pension > 0 && ownIncome <= sp && ownIncome < eur(BAND_INCREASE.value)) {
      return refuse("the second-income band increase where the lower earner pays into a pension",
        "The skill sets the increase at the lower earner's income but does not say whether that income is before or after pension contributions.", [BAND_INCREASE]);
    }
    increase = bmin(eur(BAND_INCREASE.value), bmin(ownIncome, sp));
    band += increase;
    consts.push(BAND_INCREASE);
  }
  consts.push(IT_RATES);
  const taxable = ownIncome + eur(spouse) - relief;
  const [lo, hi] = IT_RATES.value;
  const grossIt = times(bmin(taxable, band), lo) + times(bmax(taxable - band, ZERO), hi);
  const personal = eur(status === "married_one_income" || status === "married_two_incomes" ? PERSONAL.value.married : PERSONAL.value.single);
  const spccc = status === "single_parent" ? eur(SPCCC.value) : ZERO;
  const employee = salary > 0 ? eur(EMPLOYEE.value) : ZERO;
  const eic = bmin(eur(EIC.value.max) - employee, times(eur(trading), EIC.value.rate));
  const spouseEmployee = status === "married_two_incomes" ? eur(EMPLOYEE.value) : ZERO;
  const credits = personal + spccc + employee + eic + spouseEmployee;
  const incomeTax = roundCent(bmax(grossIt - credits, ZERO));
  consts.push(PERSONAL);
  if (spccc > ZERO) consts.push(SPCCC);
  if (employee > ZERO || spouseEmployee > ZERO) consts.push(EMPLOYEE);
  consts.push(EIC, EIC_SCOPE);
  const itLines = {
    taxable_income: toEur(taxable), rate_band: toEur(band), gross_income_tax: toEur(grossIt),
    tax_credits: toEur(credits), income_tax: toEur(incomeTax),
  };

  // USC (this person only; a spouse's USC is charged separately).
  const aggregate = trading + other;
  const nonPaye = trading + nonPayeOther;
  const u = uscFor(year, aggregate, nonPaye, medical);
  consts.push(BEFORE_PENSION, year === "2025" ? USC_2025 : USC_2026, USC_EXEMPT);
  if (medical || year === "2025") consts.push(USC_MEDICAL);
  if (nonPaye > USC_SURCHARGE.value.over || year === "2025") consts.push(USC_SURCHARGE);
  if ("refuse" in u) {
    return refuse(u.refuse,
      "The Form 11 skill states the 2025 USC bands but no 2025 exemption limit, non-PAYE surcharge or reduced rate (ie-usc covers 2026 only). The engine computes 2025 USC only above EUR 13,000 of income, up to EUR 100,000 of non-PAYE income and without a medical card, where none of these can change the answer.",
      consts, itLines);
  }
  const usc = roundCent(u.usc);

  // PRSI Class S (this person's own reckonable income; a PAYE salary is outside it).
  const floorBase = eur(trading) + eur(ca) + eur(other);
  const reckonable = eur(nonPaye);
  const rate = year === "2025" ? PRSI_2025.value.rate : PRSI_2026.value;
  const minimum = year === "2025" ? PRSI_2025.value.minimum : PRSI_MIN.value;
  consts.push(year === "2025" ? PRSI_2025 : PRSI_2026, PRSI_FLOOR, PRSI_FLOOR_TEST, PRSI_BASE);
  if (year === "2026") consts.push(PRSI_MIN);
  const belowFloor = floorBase < eur(PRSI_FLOOR.value);
  if (belowFloor && year === "2025") {
    return refuse("PRSI Class S income floor for 2025",
      "The skills state the EUR 5,000 floor for 2026 only; for 2025 they give the rate and the EUR 650 minimum. Income here is below EUR 5,000, where the floor decides the answer.",
      consts, { ...itLines, usc: toEur(usc) });
  }
  const byRate = times(reckonable, rate);
  const prsi = belowFloor ? ZERO : roundCent(bmax(byRate, eur(minimum)));

  // Liability, balance and next year's preliminary tax.
  const total = incomeTax + usc + prsi;
  let deducted = ZERO;
  if (salary > 0 || spouse > 0) {
    const itDed = f.number("paye_income_tax_deducted");
    used.paye_income_tax_deducted = itDed;
    deducted += eur(itDed);
  }
  if (salary > 0) {
    const uscDed = f.number("paye_usc_deducted");
    used.paye_usc_deducted = uscDed;
    deducted += eur(uscDed);
  }
  const net = total - deducted;
  const balance = net - eur(prelimPaid);
  const nextEst = f.number("next_year_liability_estimate", null);
  const before = directDebit ? f.number("liability_year_before", null) : null;
  if (nextEst !== null) used.next_year_liability_estimate = nextEst;
  if (before !== null) used.liability_year_before = before;
  const options = preliminaryOptions(toEur(net), nextEst, before, directDebit);
  consts.push(year === "2025" ? PRELIM_2026 : PRELIM_TESTS_GENERAL, PRELIM_WORKING, year === "2025" ? PRELIM_DUE_2026 : RETURN_2026);
  if (year === "2025") consts.push(PRELIM_LATE_2026);
  else consts.push(BALANCE_2026);
  const nextYear = String(Number(year) + 1);
  const due = year === "2025"
    ? "31 October 2026, or 18 November 2026 if the 2025 return is filed and the 2025 balance and 2026 preliminary tax are paid through ROS"
    : "31 October 2027, with the 2026 return (Revenue has not yet announced a ROS date for 2027)";
  const payNow = toEur(bmax(balance, ZERO)) + options.minimum;

  const steps: string[] = [];
  if (pension > 0) {
    steps.push(`Pension relief: ${pct(pensionPct(age!))} (age ${age}) of net relevant earnings EUR ${money(Math.min(trading, PENSION_CAP.value))} allows up to EUR ${money(toEur(times(bmin(eur(trading), eur(PENSION_CAP.value)), pensionPct(age!))))}; relieved EUR ${money(toEur(relief))} of EUR ${money(pension)} paid (income tax only)`);
  }
  steps.push(
    `Taxable income = trading profit EUR ${money(trading)}${other > 0 ? ` + other income EUR ${money(other)}` : ""}${spouse > 0 ? ` + spouse's salary EUR ${money(spouse)}` : ""}${relief > ZERO ? ` - pension relief EUR ${money(toEur(relief))}` : ""} = EUR ${money(toEur(taxable))}`,
    `Rate band EUR ${money(toEur(band))}${increase > ZERO ? ` (EUR ${money(BAND_MARRIED.value)} + second-income increase EUR ${money(toEur(increase))})` : ""}: 20% up to it, 40% above = EUR ${money(toEur(grossIt))}`,
    `Credits: personal EUR ${money(toEur(personal))}${spccc > ZERO ? ` + single person child carer EUR ${money(toEur(spccc))}` : ""}${employee > ZERO ? ` + employee EUR ${money(toEur(employee))}` : ""} + earned income EUR ${money(toEur(eic))}${spouseEmployee > ZERO ? ` + spouse's employee EUR ${money(toEur(spouseEmployee))}` : ""} = EUR ${money(toEur(credits))}; income tax EUR ${money(toEur(incomeTax))}`,
    toEur(usc) === 0 && aggregate <= USC_EXEMPT.value
      ? `USC: income EUR ${money(aggregate)} does not exceed EUR ${money(USC_EXEMPT.value)}, so no USC`
      : `USC on EUR ${money(aggregate)} (after capital allowances, before pension)${medical && year === "2026" && aggregate <= USC_MEDICAL.value.limit ? " at the medical card rate" : ""}${u.surcharge > ZERO ? `, including the 3% surcharge EUR ${money(toEur(u.surcharge))} on non-PAYE income above EUR ${money(USC_SURCHARGE.value.over)}` : ""} = EUR ${money(toEur(usc))}`,
    belowFloor
      ? `PRSI Class S: total income before capital allowances EUR ${money(toEur(floorBase))} is under EUR ${money(PRSI_FLOOR.value)}, so none`
      : `PRSI Class S: EUR ${money(toEur(reckonable))} x ${pct(rate)} = EUR ${money(toEur(byRate))}, at least EUR ${money(minimum)} = EUR ${money(toEur(prsi))}`,
    `Total ${year} liability = EUR ${money(toEur(total))}${deducted > ZERO ? `, less PAYE deducted EUR ${money(toEur(deducted))} = EUR ${money(toEur(net))}` : ""}`,
    `Balance for ${year} after preliminary tax paid EUR ${money(prelimPaid)} = EUR ${money(toEur(balance))}`,
    `Preliminary tax for ${nextYear}: 100% of ${year} = EUR ${money(options.previous_year_100)}${options.current_year_90 !== undefined ? `; 90% of the ${nextYear} estimate = EUR ${money(options.current_year_90)}` : ""}${options.pre_preceding_year_105 !== undefined ? `; 105% of ${Number(year) - 1} (direct debit) = EUR ${money(options.pre_preceding_year_105)}` : ""}; minimum EUR ${money(options.minimum)}, due ${due}`,
  );

  const notes: string[] = [];
  if (options.current_year_90 === undefined) {
    notes.push(`The 90% test was not used: give next_year_liability_estimate (run this engine for ${nextYear}${year === "2026" ? ", once the skills hold 2027 figures" : ""}). If the estimate turns out low, that test fails.`);
  }
  if (directDebit && options.pre_preceding_year_105 === undefined) {
    notes.push(`The 105% test was not used: give liability_year_before (the final ${Number(year) - 1} liability); it does not apply if that liability was nil.`);
  }
  if (year === "2025") {
    notes.push("If 2026 preliminary tax is not paid by the due date, or is less than the lowest test, the whole 2026 liability is treated as due on 31 October 2026 and interest runs from then.");
    notes.push("The skill states the 2025 USC bands but no 2025 exemption limit or non-PAYE surcharge, and the PRSI floor for 2026 only. This 2025 figure is given only because income is above EUR 13,000, non-PAYE income is not above EUR 100,000 and income is at least EUR 5,000, where those rules cannot change it.");
  } else {
    notes.push("Preliminary tax for 2027 uses the same tests (the Form 11 skill: the 2026 liability sets 2027 preliminary tax under the 100% test). Budget 2027 changes are not law yet and are not in the skills.");
  }
  if (pension > 0 && relief < eur(pension)) notes.push(`EUR ${money(pension - toEur(relief))} of the pension contribution is above the limit and gets no relief in this computation.`);

  return ok(
    spec.name,
    { label: `Income tax + USC + PRSI for ${year}`, value: toEur(total), currency: "EUR" },
    {
      ...itLines,
      usc: toEur(usc),
      prsi_class_s: toEur(prsi),
      total_liability: toEur(total),
      tax_deducted_at_source: toEur(deducted),
      net_liability: toEur(net),
      preliminary_tax_paid: toEur(eur(prelimPaid)),
      balance_due: toEur(balance),
      preliminary_tax: { year: nextYear, ...options, due },
      pay_by_return_date: payNow,
    },
    steps,
    consts,
    used,
    {
      assumptions: [
        "Irish resident, an active sole trader, aged under 65, insured in Ireland (no A1 certificate for another country)",
        "Only the personal, single person child carer, employee and earned income credits; no other credits or reliefs (rent, medical expenses, Home Carer, HIER)",
        "Jointly assessed if married or in a civil partnership; the spouse's own USC and PRSI on their salary are deducted by their employer and not included",
        "Amounts read to the cent; each charge rounded to the cent, half up",
      ],
      anchors,
      notes,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
