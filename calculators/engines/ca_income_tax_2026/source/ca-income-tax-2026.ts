// Canada personal income tax for a single individual, tax years 2025 and 2026: federal tax plus
// Ontario, British Columbia or Alberta tax, the balance owing or refund, and what more RRSP saves.
//
// Federal 2026: canada-payroll (brackets, basic personal amount), ca-fed-cpp-ei (credit rate),
// canada-tax-optimization (self-employed CPP). Federal 2025: ca-fed-t1-return (brackets, basic
// personal amount and its phase-down, credit rate, EI rate), ca-fed-cpp-ei (CPP). Both years: the
// Canada employment amount from ca-fed-t1-return. Employee CPP/EI for 2026 are the
// ca_cpp_ei_employee_2026 engine's own rules, imported, so the two engines cannot drift apart.
// Provinces: on-, bc- and ab-individual-return as rewritten on 8 Nov 2026 (ON428, BC428, AB428).
//
// Refused (missing_rule): Quebec (separate TP-1; the skill says the 2026 line 248 factors are not
// published), dividends, a spouse or partner, dependants, age 65 or over, employment and
// self-employment together (Schedule 8 Part 5), and the Alberta 2026 supplemental tax credit if it
// would apply (its 2026 base is derived from the escalator, not yet printed).
import { CPP2_RATE, CPP_RATE, EI_RATE, EXEMPT, MIE, YAMPE, YMPE } from "./ca-cpp-ei-employee-2026";
import { FactReader, missingRule, money, NeedsInput, ok, pct, pyRound, r2, rule, taxYearFact, type Engine, type EngineSpec, type Rule } from "./types";

const PAY = "canada-payroll";
const OPT = "canada-tax-optimization";
const T1 = "ca-fed-t1-return";
const CPPEI = "ca-fed-cpp-ei";
const ON = "on-individual-return";
const BC = "bc-individual-return";
const AB = "ab-individual-return";
const RATES = "Rates, bands and thresholds";

/** [upper limit of the bracket (null = no limit), rate]. */
type Bands = [number | null, number][];

// ---- 2026 federal ----------------------------------------------------------------------------
export const BRACKETS_26 = rule<Bands>("FEDERAL_BRACKETS_2026", [[58_523, 0.14], [117_045, 0.205], [181_440, 0.26], [258_482, 0.29], [null, 0.33]], PAY,
  "Section 2 -- Income Tax Withholding (Source Deductions) / Federal Tax Brackets (2026)",
  "Federal Tax Brackets (2026)\nTaxable Income (CAD) | Rate\n0 -- 58,523 | 14%\n58,523 -- 117,045 | 20.5%\n117,045 -- 181,440 | 26%\n181,440 -- 258,482 | 29%\n258,482+ | 33%");
export const BPA_26 = rule("FEDERAL_BPA_2026", { max: 16_452, min: 14_829 }, PAY,
  "Federal Basic Personal Amount (BPA) -- 2026",
  "Federal Basic Personal Amount (BPA) -- 2026\nIncome Level | BPA (CAD)\nUp to $181,440 | $16,452\n$181,440 -- $258,482 | Claws back to $14,829\nAbove $258,482 | $14,829");
export const LOWEST_26 = rule("FEDERAL_LOWEST_RATE_2026", 0.14, PAY, "Federal Tax Brackets (2026)",
  "The lowest bracket rate was reduced from 15% to 14% effective for the 2026 tax year");
export const CREDIT_RATE_26 = rule("FEDERAL_CREDIT_RATE_2026", 0.14, CPPEI, "4.5 Tax treatment of self-employed CPP (Tier 1)",
  "federal credit at the lowest federal rate: 14.5% for 2025, 14% for 2026");
export const SE_CPP_26 = rule("SELF_EMPLOYED_CPP_BOTH_HALVES_2026", 2, OPT, "Section 8 -- CPP/EI & Social Security Optimization / CPP Contributions (2026)",
  "Self-employed CPP -- Self-employed pay both halves (11.9% CPP1 + 8% CPP2)");

// ---- 2025 federal ----------------------------------------------------------------------------
export const BRACKETS_25 = rule<Bands>("FEDERAL_BRACKETS_2025", [[57_375, 0.145], [114_750, 0.205], [177_882, 0.26], [253_414, 0.29], [null, 0.33]], T1,
  "Section 1 -- Quick Reference / Federal Tax Brackets (2025)",
  "Federal Tax Brackets (2025)\nTaxable Income (CAD) | Rate | Cumulative Tax\n0 -- 57,375 | 14.5%* | 8,319\n57,376 -- 114,750 | 20.5% | 20,081\n114,751 -- 177,882 | 26% | 36,495\n177,883 -- 253,414 | 29% | 58,399\n253,415+ | 33% | 58,399+\n*14.5% is a blended rate for 2025 (15% Jan-Jun, 14% Jul-Dec).");
export const BPA_25 = rule("FEDERAL_BPA_2025", { max: 16_129, min: 14_538 }, T1, "Basic Personal Amount (2025)",
  "Basic Personal Amount (2025)\nNet Income | BPA\n$177,882 or less | $16,129\n$177,882 -- $253,414 | Graduated reduction\n$253,414+ | $14,538");
export const BPA_PHASE = rule("FEDERAL_BPA_PHASE_DOWN_METHOD", "linear between the 29% and 33% bracket thresholds, on net income", T1,
  "Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required) / 6.2 BPA Reduction for High Earners",
  "BPA = $16,129 - $1,591 x (net income - $177,882) / $75,532. Flag if net income between $177,882 and $253,414.");
export const CREDIT_RATE_25 = rule("FEDERAL_CREDIT_RATE_2025", 0.145, T1, "Section 7 -- Excel Working Paper Template",
  "D2. Non-refundable credits (x 14.5%)");
export const EI_RATE_25 = rule("EI_RATE_2025", 0.0164, T1, "Rates and thresholds / T1 Return", "EI rate (2025) -- $1.64/$100");
export const YMPE_25 = rule("YMPE_2025", 71_300, CPPEI, "Section 1 -- Quick reference / CPP1 thresholds (2025)",
  "CPP1 thresholds (2025)\nYear's Maximum Pensionable Earnings (YMPE) | $71,300.00");
export const EXEMPT_25 = rule("BASIC_EXEMPTION_2025", 3_500, CPPEI, "Section 1 -- Quick reference / CPP1 thresholds (2025)",
  "CPP1 thresholds (2025)\nYear's Basic Exemption | $3,500.00");
export const CPP_RATE_25 = rule("CPP_EMPLOYEE_RATE_2025", 0.0595, CPPEI, "Section 1 -- Quick reference / CPP1 thresholds (2025)",
  "CPP1 thresholds (2025)\nEmployee rate | 5.95%\nSelf-employed rate (2x employee) | 11.90%");
export const YAMPE_25 = rule("YAMPE_2025", 81_200, CPPEI, "Rates and thresholds / CPP-CPP2-EI", "YAMPE -- $81,200.00");
export const CPP2_RATE_25 = rule("CPP2_EMPLOYEE_RATE_2025", 0.04, CPPEI, "Rates and thresholds / CPP-CPP2-EI",
  "Employee CPP2 rate -- 4.00%\nSelf-employed CPP2 rate (2x employee) -- 8.00%");
export const MIE_25 = rule("EI_MAX_INSURABLE_EARNINGS_2025", 65_700, CPPEI, "Rates and thresholds / CPP-CPP2-EI", "Max insurable earnings (MIE) -- $65,700.00");

// ---- both years, federal ---------------------------------------------------------------------
export const CEA = rule("CANADA_EMPLOYMENT_AMOUNT", { "2025": 1_471, "2026": 1_501 } as Record<string, number>, T1, "Rates and thresholds / T1 Return",
  "Canada employment amount (line 31260) -- $1,471 (2025); $1,501 (2026). Employment income only; not for the self-employed");
export const CPP_BASE_RATE = rule("CPP_BASE_RATE_EACH_SIDE", 0.0495, CPPEI, "Rates and thresholds / CPP-CPP2-EI",
  "line 22200 deduction = employer-equivalent half of the BASE contribution (4.95% of the 9.9%) plus ALL enhancement (first-additional and CPP2) contributions; only the employee-equivalent half of the base is the line 31000 credit");
export const CPP2_DEDUCTIBLE = rule("CPP2_IS_A_DEDUCTION", true, CPPEI, "4.5 Tax treatment of self-employed CPP (Tier 1)",
  "CPP2 split -- CPP2 contributions (8% between YMPE and YAMPE) are DEDUCTIBLE, not creditable");
export const SE_SPLIT = rule("SELF_EMPLOYED_CPP_SPLIT", true, T1, "CPP Self-Employed (2025)",
  "Half of base CPP plus all first and second additional (CPP2) contributions are deductible (line 22200); the other half of base CPP is a non-refundable credit (line 31000).");
export const EI_CREDIT = rule("EI_PREMIUM_CREDIT", true, CPPEI, "4.6 EI for self-employed (Tier 1)", "(line 31200 is EI through employment)");

// ---- Ontario (ON428) -------------------------------------------------------------------------
export const ON_BANDS_26 = rule<Bands>("ON_BRACKETS_2026", [[53_891, 0.0505], [107_785, 0.0915], [150_000, 0.1116], [220_000, 0.1216], [null, 0.1316]], ON, RATES,
  "Band 1: taxable income up to $53,891 | 5.05% | 2026\nBand 2: $53,891.01 to $107,785 | 9.15% | 2026\nBand 3: $107,785.01 to $150,000 | 11.16% | 2026\nBand 4: $150,000.01 to $220,000 | 12.16% | 2026\nBand 5: over $220,000 | 13.16% | 2026");
export const ON_BANDS_25 = rule<Bands>("ON_BRACKETS_2025", [[52_886, 0.0505], [105_775, 0.0915], [150_000, 0.1116], [220_000, 0.1216], [null, 0.1316]], ON, RATES,
  "Band 1: taxable income up to $52,886 | 5.05% | 2025\nBand 2: $52,886.01 to $105,775 ... | 9.15% | 2025\nBand 3: $105,775.01 to $150,000 ... | 11.16% | 2025\nBand 4: $150,000.01 to $220,000 ... | 12.16% | 2025\nBand 5: over $220,000 ... | 13.16% | 2025");
export const ON_CREDIT_RATE = rule("ON_CREDIT_RATE", 0.0505, ON, RATES,
  "Non-refundable credit rate (all Part B amounts, CPP and EI included) | 5.05% | 2026, 2025");
export const ON_BPA_26 = rule("ON_BPA_2026", 12_989, ON, RATES, "Basic personal amount | $12,989 | 2026");
export const ON_BPA_25 = rule("ON_BPA_2025", 12_747, ON, RATES, "Basic personal amount | $12,747 | 2025");
export const ON_SURTAX_26 = rule("ON_SURTAX_2026", [5_818, 7_446], ON, RATES,
  "Ontario surtax | 20% of basic Ontario tax over $5,818, plus 36% of basic Ontario tax over $7,446 | 2026");
export const ON_SURTAX_25 = rule("ON_SURTAX_2025", [5_710, 7_307], ON, RATES,
  "Ontario surtax | 20% of basic Ontario tax over $5,710, plus 36% of basic Ontario tax over $7,307 | 2025");
export const ON_REDUCTION_26 = rule("ON_TAX_REDUCTION_2026", 300, ON, RATES,
  "Ontario tax reduction | basic $300 ... reduction is twice that total minus Ontario tax | 2026");
export const ON_REDUCTION_25 = rule("ON_TAX_REDUCTION_2025", 294, ON, RATES, "Ontario tax reduction | basic $294 ... | 2025");
export const ON_LIFT = rule("ON_LIFT_CREDIT", { max: 875, rate: 0.0505, threshold: 32_500, clawback: 0.05 }, ON, RATES,
  "LIFT credit | lesser of $875 and 5.05% of employment income, less 5% of the greater of adjusted net income over $32,500 and adjusted family net income over $65,000 | 2026, 2025");
/** Ontario Health Premium chart: [top of the step (null = no limit), premium at the step's floor, rate on the amount over the floor]. */
export const ON_OHP = rule<[number | null, number, number][]>("ON_HEALTH_PREMIUM", [
  [20_000, 0, 0], [25_000, 0, 0.06], [36_000, 300, 0], [38_500, 300, 0.06], [48_000, 450, 0], [48_600, 450, 0.25],
  [72_000, 600, 0], [72_600, 600, 0.25], [200_000, 750, 0], [200_600, 750, 0.25], [null, 900, 0],
], ON, "Rates, bands and thresholds / Ontario Health Premium chart (ON428, line 89)",
  "Ontario Health Premium | chart below; not indexed, same for 2025 and 2026 | 2026, 2025\n" +
  "$20,000 or less | $0\nmore than $20,000, not more than $25,000 | 6% of the amount over $20,000\nmore than $25,000, not more than $36,000 | $300\n" +
  "more than $36,000, not more than $38,500 | $300 plus 6% of the amount over $36,000\nmore than $38,500, not more than $48,000 | $450\n" +
  "more than $48,000, not more than $48,600 | $450 plus 25% of the amount over $48,000\nmore than $48,600, not more than $72,000 | $600\n" +
  "more than $72,000, not more than $72,600 | $600 plus 25% of the amount over $72,000\nmore than $72,600, not more than $200,000 | $750\n" +
  "more than $200,000, not more than $200,600 | $750 plus 25% of the amount over $200,000\nmore than $200,600 | $900");

// ---- British Columbia (BC428) ----------------------------------------------------------------
export const BC_BANDS_26 = rule<Bands>("BC_BRACKETS_2026", [[50_363, 0.056], [100_728, 0.077], [115_648, 0.105], [140_430, 0.1229], [190_405, 0.147], [265_545, 0.168], [null, 0.205]], BC,
  "Rates, bands and thresholds / 2026 brackets and rates",
  "Taxable income $0 to $50,363 | 5.6% | 2026\n$50,363.01 to $100,728 ... | 7.7% | 2026\n$100,728.01 to $115,648 ... | 10.5% | 2026\n$115,648.01 to $140,430 ... | 12.29% | 2026\n$140,430.01 to $190,405 ... | 14.7% | 2026\n$190,405.01 to $265,545 ... | 16.8% | 2026\nOver $265,545 ... | 20.5% | 2026");
export const BC_BANDS_25 = rule<Bands>("BC_BRACKETS_2025", [[49_279, 0.0506], [98_560, 0.077], [113_158, 0.105], [137_407, 0.1229], [186_306, 0.147], [259_829, 0.168], [null, 0.205]], BC,
  "Rates, bands and thresholds / 2025 figures (for 2025 returns), as printed on Form BC428 2025",
  "Taxable income $0 to $49,279 | 5.06% | 2025\n$49,279.01 to $98,560 ... | 7.7% | 2025\n$98,560.01 to $113,158 ... | 10.5% | 2025\n$113,158.01 to $137,407 ... | 12.29% | 2025\n$137,407.01 to $186,306 ... | 14.7% | 2025\n$186,306.01 to $259,829 ... | 16.8% | 2025\nOver $259,829 ... | 20.5% | 2025");
export const BC_CREDIT_26 = rule("BC_CREDIT_RATE_2026", 0.056, BC, "Rates, bands and thresholds / 2026 brackets and rates",
  "Credit rate for non-refundable credits (lowest rate) | 5.6% | 2026");
export const BC_CREDIT_25 = rule("BC_CREDIT_RATE_2025", 0.0506, BC, "Rates, bands and thresholds / 2025 figures", "Credit rate (line 55) | 5.06% | 2025");
export const BC_BPA_26 = rule("BC_BPA_2026", 13_216, BC, "2026 basic non-refundable credits", "Basic personal amount (BC428 line 16) | $13,216 | 2026");
export const BC_BPA_25 = rule("BC_BPA_2025", 12_932, BC, "Rates, bands and thresholds / 2025 figures", "Basic personal amount (line 16) | $12,932 | 2025");
export const BC_CPP_EI = rule("BC_CPP_EI_CREDITS", true, BC, "2026 basic non-refundable credits",
  "CPP base contributions | up to $3,519.45 | 2026\nEI premiums | up to $1,123.07 | 2026");
export const BC_REDUCTION_26 = rule("BC_TAX_REDUCTION_2026", { basic: 690, threshold: 25_570, rate: 0.0356 }, BC, "2026 BC tax reduction and other credits",
  "BC tax reduction, basic amount | $690 | 2026 to 2030\nBC tax reduction, net income threshold where it starts to fall | $25,570 | 2026\nBC tax reduction, rate of reduction | 3.56% of net income above the threshold | 2026");
export const BC_REDUCTION_25 = rule("BC_TAX_REDUCTION_2025", { basic: 562, threshold: 25_020, rate: 0.0356 }, BC, "Rates, bands and thresholds / 2025 figures",
  "BC tax reduction: basic reduction (line 73) | $562 | 2025\nBC tax reduction: base amount (line 75), where it starts to fall | $25,020 | 2025\nBC tax reduction: rate (line 77) | 3.56% | 2025");

// ---- Alberta (AB428) -------------------------------------------------------------------------
export const AB_BANDS_26 = rule<Bands>("AB_BRACKETS_2026", [[61_200, 0.08], [154_259, 0.1], [185_111, 0.12], [246_813, 0.13], [370_220, 0.14], [null, 0.15]], AB, RATES,
  "Taxable income up to $61,200 | 8% | 2026\n$61,200.01 to $154,259 | 10% | 2026\n$154,259.01 to $185,111 | 12% | 2026\n$185,111.01 to $246,813 | 13% | 2026\n$246,813.01 to $370,220 | 14% | 2026\nOver $370,220 | 15% | 2026");
export const AB_BANDS_25 = rule<Bands>("AB_BRACKETS_2025", [[60_000, 0.08], [151_234, 0.1], [181_481, 0.12], [241_974, 0.13], [362_961, 0.14], [null, 0.15]], AB, RATES,
  "Taxable income up to $60,000 | 8% | 2025\n$60,000.01 to $151,234 | 10% ... | 2025\n$151,234.01 to $181,481 | 12% ... | 2025\n$181,481.01 to $241,974 | 13% ... | 2025\n$241,974.01 to $362,961 | 14% ... | 2025\nOver $362,961 | 15% ... | 2025");
export const AB_CREDIT_RATE = rule("AB_CREDIT_RATE", 0.08, AB, RATES, `Rate used for non-refundable credits ("specified percentage") | 8% | 2025 and later`);
export const AB_BPA_26 = rule("AB_BPA_2026", 22_769, AB, RATES, "Basic personal amount | $22,769 | 2026");
export const AB_BPA_25 = rule("AB_BPA_2025", 22_323, AB, RATES, "Basic personal amount | $22,323 | 2025");
export const AB_CPP_EI = rule("AB_CPP_EI_CREDITS", true, AB, "The taxable base", "CPP and EI (lines 30800, 31000, 31200 and 31217 of the return)");
export const AB_SUPP_25 = rule("AB_SUPPLEMENTAL_CREDIT_2025", { base: 4_800, rate: 0.25 }, AB, RATES,
  "Supplemental tax credit | 25% of (credits at 8%, leaving out unused tuition, minus $4,800) | 2025");
export const AB_ESCALATOR_26 = rule("AB_2026_AMOUNTS_RISE", 0.02, AB, RATES, `Alberta says: "In 2026, thresholds and credit amounts will rise by 2%."`);
export const AB_SUPP_26_UNCONFIRMED = rule("AB_SUPPLEMENTAL_BASE_2026_NOT_PRINTED", 4_896, AB, RATES,
  "Three 2026 amounts are not printed by the CRA or Alberta yet\nsupplemental tax credit base: $4,896 (2025: $4,800);");

interface Fed {
  bands: Rule<Bands>;
  bpa: Rule<{ max: number; min: number }>;
  credit: Rule<number>;
  ympe: Rule<number>;
  exempt: Rule<number>;
  eeRate: Rule<number>;
  yampe: Rule<number>;
  cpp2: Rule<number>;
  mie: Rule<number>;
  ei: Rule<number>;
  se: Rule;
  extra: Rule[];
}

const FED: Record<string, Fed> = {
  "2026": { bands: BRACKETS_26, bpa: BPA_26, credit: CREDIT_RATE_26, ympe: YMPE, exempt: EXEMPT, eeRate: CPP_RATE, yampe: YAMPE, cpp2: CPP2_RATE, mie: MIE, ei: EI_RATE, se: SE_CPP_26, extra: [LOWEST_26] },
  "2025": { bands: BRACKETS_25, bpa: BPA_25, credit: CREDIT_RATE_25, ympe: YMPE_25, exempt: EXEMPT_25, eeRate: CPP_RATE_25, yampe: YAMPE_25, cpp2: CPP2_RATE_25, mie: MIE_25, ei: EI_RATE_25, se: CPP_RATE_25, extra: [] },
};

interface Prov {
  bands: Rule<Bands>;
  credit: Rule<number>;
  bpa: Rule<number>;
  rules: Rule[];
}

const PROV: Record<string, Prov> = {
  "ON-2026": { bands: ON_BANDS_26, credit: ON_CREDIT_RATE, bpa: ON_BPA_26, rules: [ON_SURTAX_26, ON_REDUCTION_26, ON_LIFT, ON_OHP] },
  "ON-2025": { bands: ON_BANDS_25, credit: ON_CREDIT_RATE, bpa: ON_BPA_25, rules: [ON_SURTAX_25, ON_REDUCTION_25, ON_LIFT, ON_OHP] },
  "BC-2026": { bands: BC_BANDS_26, credit: BC_CREDIT_26, bpa: BC_BPA_26, rules: [BC_CPP_EI, BC_REDUCTION_26] },
  "BC-2025": { bands: BC_BANDS_25, credit: BC_CREDIT_25, bpa: BC_BPA_25, rules: [BC_CPP_EI, BC_REDUCTION_25] },
  "AB-2026": { bands: AB_BANDS_26, credit: AB_CREDIT_RATE, bpa: AB_BPA_26, rules: [AB_CPP_EI, AB_SUPP_25, AB_ESCALATOR_26] },
  "AB-2025": { bands: AB_BANDS_25, credit: AB_CREDIT_RATE, bpa: AB_BPA_25, rules: [AB_CPP_EI, AB_SUPP_25] },
};

const CONSTS: Rule[] = [
  BRACKETS_26, BPA_26, LOWEST_26, CREDIT_RATE_26, SE_CPP_26,
  BRACKETS_25, BPA_25, BPA_PHASE, CREDIT_RATE_25, EI_RATE_25, YMPE_25, EXEMPT_25, CPP_RATE_25, YAMPE_25, CPP2_RATE_25, MIE_25,
  CEA, CPP_BASE_RATE, CPP2_DEDUCTIBLE, SE_SPLIT, EI_CREDIT,
  CPP_RATE, EXEMPT, YMPE, YAMPE, CPP2_RATE, EI_RATE, MIE,
  ON_BANDS_26, ON_BANDS_25, ON_CREDIT_RATE, ON_BPA_26, ON_BPA_25, ON_SURTAX_26, ON_SURTAX_25, ON_REDUCTION_26, ON_REDUCTION_25, ON_LIFT, ON_OHP,
  BC_BANDS_26, BC_BANDS_25, BC_CREDIT_26, BC_CREDIT_25, BC_BPA_26, BC_BPA_25, BC_CPP_EI, BC_REDUCTION_26, BC_REDUCTION_25,
  AB_BANDS_26, AB_BANDS_25, AB_CREDIT_RATE, AB_BPA_26, AB_BPA_25, AB_CPP_EI, AB_SUPP_25, AB_ESCALATOR_26, AB_SUPP_26_UNCONFIRMED,
];

const PROVINCES = ["ON", "BC", "AB", "QC"];
const NAMES: Record<string, string> = { ON: "Ontario", BC: "British Columbia", AB: "Alberta", QC: "Quebec" };

export const spec: EngineSpec = {
  name: "ca_income_tax_2026",
  version: "2.0.0",
  jurisdiction: "CA",
  tax_years: ["2025", "2026"],
  summary:
    "Canada personal income tax for 2026 or 2025 for a single person resident in Ontario, British Columbia or Alberta on 31 December: CPP and EI, net and taxable income, federal tax (basic personal amount with its phase-down, Canada employment amount), provincial tax (Ontario surtax, tax reduction, LIFT and Health Premium; BC tax reduction; Alberta 8% band and supplemental credit), the balance owing or refund against tax already paid, and what more RRSP saves. " +
    "Quebec, dividends, a spouse or dependants, age 65 or over, and employment plus self-employment together are refused.",
  // Income tax, refunds, balances owing and RRSP questions. CPP/EI-only, payroll, sales tax and
  // company questions are left to other engines (or none).
  topics:
    /^(?![\s\S]*\b(?:compan(?:y|y's|ies)|corporat\w*|gst|hst|pst|qst|sales tax|payroll)\b)[\s\S]*(?:income tax|tax refund|\brefund\b|balance owing|tax owing|\bowing\b|\brrsp\b|taxable income|federal tax|provincial tax|basic personal amount|marginal (?:tax )?rate|tax brackets?|how much tax|tax (?:bill|liability|payable|due|owed?))/,
  facts: {
    province: {
      type: "string",
      required: true,
      choices: PROVINCES,
      description: "province of residence on 31 December, two-letter code (QC is refused: Quebec tax is on a separate TP-1 return)",
    },
    employment_income: { type: "number", required: false, default: 0, description: "CAD, T4 employment income from one employer for the whole year (CPP and EI are computed from it)" },
    self_employment_net_income: { type: "number", required: false, default: 0, description: "CAD, net self-employment profit (T2125); a loss is not supported" },
    other_income: { type: "number", required: false, default: 0, description: "CAD, other fully taxable income with no credit of its own (interest, net rent)" },
    eligible_dividends: { type: "number", required: false, default: 0, description: "CAD, actual eligible dividends received (refused if more than 0)" },
    other_dividends: { type: "number", required: false, default: 0, description: "CAD, actual other-than-eligible dividends received (refused if more than 0)" },
    rrsp_deduction: { type: "number", required: false, default: 0, description: "CAD, RRSP deduction claimed for the year (within the limit on the notice of assessment)" },
    tax_withheld: { type: "number", required: false, default: 0, description: "CAD, income tax already deducted at source (T4 box 22) plus instalments paid for the year" },
    has_spouse_or_partner: { type: "boolean", required: false, default: false, description: "had a spouse or common-law partner on 31 December (refused if true: spouse credits and family tests are not computed)" },
    dependants: { type: "number", required: false, default: 0, description: "dependants supported (refused if more than 0)" },
    age_65_or_over: { type: "boolean", required: false, default: false, description: "65 or older on 31 December (refused if true: age and pension credits are not computed)" },
    tax_year: taxYearFact(["2025", "2026"]),
  },
  outputs: {
    taxable_income: "CAD",
    basic_federal_tax: "CAD",
    provincial_tax: "CAD",
    total_income_tax: "CAD",
    cpp_payable_with_return: "CAD (self-employed only)",
    balance_owing: "CAD (negative = refund)",
    rrsp_saving_next_1000: "CAD of income tax saved by CAD 1,000 more RRSP deduction",
    federal_saving_per_extra_rrsp_dollar: "CAD per CAD",
  },
};

export const anchors = [
  "ca-fed-cpp-ei Tests 1 to 4 (2025): self-employed CPP, line 22200 deduction and line 31000 credit base",
  "ca-fed-t1-return Examples 1 to 3 (2025): basic federal tax $7,978.82, $0 and $58,640.54",
  "on-individual-return Example 1 (2026, employee $34,000): Ontario tax $426.18; Example 2 (2025, $180,000, spouse, donations): $19,722.34",
  "bc-individual-return Example 1 (2026, $42,000): BC tax $1,506.81; Example 2 (2025, $120,000, spouse, donations): $7,275.24",
  "ab-individual-return Example 1 (2026, $75,000): Alberta tax $4,102.48; Example 2 (2025, $120,000, supplemental credit $59.30): $5,703.50",
  "canada-payroll (2026): employee maximums CPP $4,230.45, CPP2 $416.00, EI $1,123.07",
];

// ---- exact decimal arithmetic ------------------------------------------------------------------
// CRA's forms work in decimal and round each line half up to the cent: 16,129 x 14.5% = 2,338.705
// is 2,338.71 on the T1. A binary double holds 2,338.70499..., so r2 would give 2,338.70.
// Products and quotients here are therefore exact fractions, rounded once.
interface Q { n: bigint; d: bigint }
const B0 = BigInt(0);
const B1 = BigInt(1);
const B2 = BigInt(2);
const B10 = BigInt(10);

/** The exact decimal a figure is written as (its shortest form: 0.145, 13194.9). */
function q(x: number): Q {
  const s = String(x);
  if (!/^-?\d+(\.\d+)?$/.test(s)) throw new Error(`not a plain decimal: ${s}`);
  const [ip, fp = ""] = s.split(".");
  return { n: BigInt(ip + fp), d: B10 ** BigInt(fp.length) };
}
const mul = (a: Q, b: Q): Q => ({ n: a.n * b.n, d: a.d * b.d });
const add = (a: Q, b: Q): Q => ({ n: a.n * b.d + b.n * a.d, d: a.d * b.d });
const div = (a: Q, b: Q): Q => ({ n: a.n * b.d, d: a.d * b.n });

/** Round half up (away from zero) to `places` decimals. */
function round(x: Q, places = 2): number {
  const scale = B10 ** BigInt(places);
  const neg = x.n < B0 !== x.d < B0;
  const n = (x.n < B0 ? -x.n : x.n) * scale;
  const d = x.d < B0 ? -x.d : x.d;
  let units = n / d;
  if ((n % d) * B2 >= d) units += B1;
  const v = Number(units) / Number(scale);
  return neg ? -v : v;
}

/** a x b x ..., exactly, rounded half up to the cent. */
function cents(...xs: number[]): number {
  return round(xs.map(q).reduce(mul));
}

/** Tax on taxable income, the form way: (income - bracket floor) x rate, plus the floor's cumulative tax. */
export function taxOn(bands: Bands, ti: number): number {
  let lower = 0;
  let cum: Q = q(0);
  for (const [upper, rate] of bands) {
    if (upper === null || ti <= upper) return r2(cents(r2(ti - lower), rate) + round(cum));
    cum = add(cum, mul(q(upper - lower), q(rate)));
    lower = upper;
  }
  throw new Error("unreachable: the last band has no limit");
}

/** The bracket a taxable income's top dollar sits in. */
function bandRate(bands: Bands, ti: number): number {
  return bands.find(([upper]) => upper === null || ti <= upper)![1];
}

/** Basic personal amount on net income, phased down linearly between the 29% and 33% thresholds (Federal Worksheet line 30000). */
export function bpa(y: Fed, ni: number): number {
  const t29 = y.bands.value[2][0]!;
  const t33 = y.bands.value[3][0]!;
  const { max, min } = y.bpa.value;
  if (ni <= t29) return max;
  if (ni >= t33) return min;
  const supp = max - min;
  const reduction = round(div(mul(q(supp), q(r2(ni - t29))), q(t33 - t29)));
  return r2(min + Math.max(0, supp - reduction));
}

export interface Cpp {
  base: number;
  first_additional: number;
  cpp2: number;
  ei: number;
  deduction: number;
  credit_amount: number;
}

/** The first additional CPP rate: the employee rate less the base rate (5.95% - 4.95% = 1%). */
function firstAdditionalRate(y: Fed): number {
  return pyRound(y.eeRate.value - CPP_BASE_RATE.value, 6);
}

/** Employee CPP/CPP2/EI for a full year with one employer, split as Schedule 8 splits it. */
export function employeeCpp(y: Fed, e: number): Cpp {
  const pens = r2(Math.max(Math.min(e, y.ympe.value) - y.exempt.value, 0));
  const base = cents(pens, CPP_BASE_RATE.value);
  const first = cents(pens, firstAdditionalRate(y));
  const cpp2 = cents(r2(Math.max(Math.min(e, y.yampe.value) - y.ympe.value, 0)), y.cpp2.value);
  const ei = cents(r2(Math.min(e, y.mie.value)), y.ei.value);
  return { base, first_additional: first, cpp2, ei, deduction: r2(first + cpp2), credit_amount: base };
}

/** Self-employed CPP (both halves), split into the line 22200 deduction and the line 31000 credit. */
export function selfEmployedCpp(y: Fed, se: number): Cpp {
  const pens = r2(Math.max(Math.min(se, y.ympe.value) - y.exempt.value, 0));
  const base = cents(pens, CPP_BASE_RATE.value, 2);
  const first = cents(pens, firstAdditionalRate(y), 2);
  const cpp2 = cents(r2(Math.max(Math.min(se, y.yampe.value) - y.ympe.value, 0)), y.cpp2.value, 2);
  const half = cents(base, 0.5);
  return { base, first_additional: first, cpp2, ei: 0, deduction: r2(half + first + cpp2), credit_amount: r2(base - half) };
}

export interface FederalTax {
  tax: number;
  bpa: number;
  canada_employment_amount: number;
  credits: number;
  basic_federal_tax: number;
}

/** Federal Step 5: tax on taxable income less non-refundable credits (BPA, CPP base, EI, Canada employment amount). */
export function federalTax(year: string, ti: number, ni: number, e: number, cpp: Cpp | null): FederalTax {
  const y = FED[year];
  const tax = taxOn(y.bands.value, ti);
  const b = bpa(y, ni);
  const cea = Math.min(CEA.value[year], e);
  const credits = cents(r2(b + (cpp?.credit_amount ?? 0) + (cpp?.ei ?? 0) + cea), y.credit.value);
  return { tax, bpa: b, canada_employment_amount: cea, credits, basic_federal_tax: Math.max(0, r2(tax - credits)) };
}

/** What one more dollar of RRSP deduction saves in federal tax: the bracket rate, plus the BPA it gives back in the phase-down. */
export function federalRrspSaving(year: string, ti: number, ni: number, basic: number): number {
  const y = FED[year];
  if (basic <= 0) return 0;
  const t29 = y.bands.value[2][0]!;
  const t33 = y.bands.value[3][0]!;
  let rate = q(bandRate(y.bands.value, ti));
  if (ni > t29 && ni <= t33) rate = add(rate, div(mul(q(y.credit.value), q(y.bpa.value.max - y.bpa.value.min)), q(t33 - t29)));
  return round(rate, 4);
}

/** Ontario Health Premium on taxable income (ON428 line 89 chart). */
export function healthPremium(ti: number): number {
  let floor = 0;
  for (const [top, base, rate] of ON_OHP.value) {
    if (top === null || ti <= top) return rate === 0 ? base : r2(base + cents(r2(ti - floor), rate));
    floor = top;
  }
  throw new Error("unreachable: the last step has no limit");
}

export interface ProvincialInput {
  ti: number;
  ni: number;
  employment_income: number;
  /** Credit amounts other than the basic personal amount (CPP base, EI; a test may add a spouse amount). */
  other_credit_amounts: number;
  /** Credits already worked out at their own rates (a test may add a donations credit). */
  other_credits?: number;
}

/** Provincial tax for ON, BC or AB, form line by form line. null = a figure the skill does not settle (Alberta 2026 supplemental base). */
export function provincialTax(prov: string, year: string, p: ProvincialInput): { tax: number; lines: Record<string, number> } | null {
  const P = PROV[`${prov}-${year}`];
  const tax = taxOn(P.bands.value, p.ti);
  const credits = r2(cents(r2(P.bpa.value + p.other_credit_amounts), P.credit.value) + (p.other_credits ?? 0));
  const basic = Math.max(0, r2(tax - credits));
  if (prov === "ON") {
    const [s1, s2] = (year === "2026" ? ON_SURTAX_26 : ON_SURTAX_25).value;
    const surtax = r2(cents(Math.max(0, r2(basic - s1)), 0.2) + cents(Math.max(0, r2(basic - s2)), 0.36));
    const l73 = r2(basic + surtax);
    const red = (year === "2026" ? ON_REDUCTION_26 : ON_REDUCTION_25).value;
    const reduction = Math.min(l73, Math.max(0, r2(2 * red - l73)));
    const l83 = r2(l73 - reduction);
    const L = ON_LIFT.value;
    const liftFull = Math.max(0, r2(Math.min(L.max, cents(p.employment_income, L.rate)) - cents(Math.max(0, r2(p.ni - L.threshold)), L.clawback)));
    const lift = Math.min(l83, liftFull);
    const premium = healthPremium(p.ti);
    const total = r2(l83 - lift + premium);
    return { tax: total, lines: { tax_on_taxable_income: tax, non_refundable_credits: credits, basic_tax: basic, surtax, tax_reduction: reduction, lift_credit: lift, health_premium: premium, provincial_tax: total } };
  }
  if (prov === "BC") {
    const R = (year === "2026" ? BC_REDUCTION_26 : BC_REDUCTION_25).value;
    const reduction = Math.min(basic, Math.max(0, r2(R.basic - cents(Math.max(0, r2(p.ni - R.threshold)), R.rate))));
    const total = r2(basic - reduction);
    return { tax: total, lines: { tax_on_taxable_income: tax, non_refundable_credits: credits, basic_tax: basic, tax_reduction: reduction, provincial_tax: total } };
  }
  // Alberta: the supplemental credit gives back 25% of the credits above the base. The 2026 base is
  // not printed yet; the skill says 2026 amounts rise by 2%, so it is above the 2025 base, and credits
  // at or below the 2025 base get no supplemental credit in either year.
  const S = AB_SUPP_25.value;
  const supplemental = cents(Math.max(0, r2(credits - S.base)), S.rate);
  if (year === "2026" && supplemental > 0) return null;
  const total = Math.max(0, r2(basic - supplemental));
  return { tax: total, lines: { tax_on_taxable_income: tax, non_refundable_credits: credits, basic_tax: basic, supplemental_credit: supplemental, provincial_tax: total } };
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const year = f.string("tax_year");
  const prov = f.string("province", undefined, PROVINCES);
  const e = f.number("employment_income", 0);
  const se = f.number("self_employment_net_income", 0);
  const other = f.number("other_income", 0);
  const eligDiv = f.number("eligible_dividends", 0);
  const otherDiv = f.number("other_dividends", 0);
  const rrsp = f.number("rrsp_deduction", 0);
  const withheld = f.number("tax_withheld", 0);
  const spouse = f.bool("has_spouse_or_partner", false);
  const dependants = f.number("dependants", 0);
  const senior = f.bool("age_65_or_over", false);
  const used = {
    province: prov, employment_income: e, self_employment_net_income: se, other_income: other,
    eligible_dividends: eligDiv, other_dividends: otherDiv, rrsp_deduction: rrsp, tax_withheld: withheld,
    has_spouse_or_partner: spouse, dependants, age_65_or_over: senior, tax_year: year,
  };
  const y = FED[year];

  if (prov === "QC") {
    return missingRule(spec.name, `Quebec income tax for ${year}`,
      "A Quebec resident files a separate Quebec return (TP-1) with its own taxable income (worker deduction, line 248 QPP and QPIP deduction), pays QPP and QPIP instead of CPP and part of EI, owes the health services fund contribution and the drug insurance premium on the TP-1, and takes the 16.5% Quebec abatement on federal tax. " +
      (year === "2026"
        ? "qc-individual-return says the 2026 line 248 factors are not published and the 2025 ones must not be used for 2026; "
        : "") +
      "this engine computes none of the Quebec return.",
      [], { inputsUsed: used });
  }
  if (eligDiv > 0 || otherDiv > 0) {
    return missingRule(spec.name, "dividends",
      "ca-fed-t1-return states the federal gross-up and dividend tax credit, but this engine does not yet carry dividends through the federal and provincial forms (gross-up, credits, Ontario surtax and Health Premium order).", [], { inputsUsed: used });
  }
  if (spouse || dependants > 0 || senior) {
    return missingRule(spec.name, "credits for a spouse or partner, dependants, or age 65 or over",
      "This engine computes a single person under 65 with no dependants. Spouse, eligible dependant, caregiver, age and pension credits, the Ontario LIFT family test and the Ontario tax reduction for dependants are not implemented.", [], { inputsUsed: used });
  }
  if (e > 0 && se > 0) {
    return missingRule(spec.name, "CPP on both employment and self-employment income (Schedule 8, Part 5)",
      "With both kinds of earnings the self-employed CPP is reduced by what the employer deducted; this engine does not implement that part of Schedule 8 yet.", [], { inputsUsed: used });
  }

  const P = PROV[`${prov}-${year}`];
  const consts: Rule[] = [y.bands, y.bpa, y.credit, ...y.extra];
  const steps: string[] = [];

  let cpp: Cpp | null = null;
  if (e > 0) {
    cpp = employeeCpp(y, e);
    consts.push(y.ympe, y.exempt, y.eeRate, y.yampe, y.cpp2, y.mie, y.ei, CPP_BASE_RATE, CPP2_DEDUCTIBLE, EI_CREDIT, CEA);
    steps.push(
      `Employee CPP: base ${pct(CPP_BASE_RATE.value)} and first additional ${pct(firstAdditionalRate(y))} of earnings between CAD ${money(y.exempt.value)} and YMPE CAD ${money(y.ympe.value)} = CAD ${money(cpp.base)} + CAD ${money(cpp.first_additional)}; CPP2 ${pct(y.cpp2.value)} up to YAMPE CAD ${money(y.yampe.value)} = CAD ${money(cpp.cpp2)}; EI ${pct(y.ei.value)} up to CAD ${money(y.mie.value)} = CAD ${money(cpp.ei)} (deducted from pay)`,
      `Line 22215 deduction (first additional + CPP2) = CAD ${money(cpp.deduction)}; credit amounts: base CPP CAD ${money(cpp.credit_amount)} (line 30800), EI CAD ${money(cpp.ei)} (line 31200)`,
    );
  } else if (se > 0) {
    cpp = selfEmployedCpp(y, se);
    consts.push(y.ympe, y.exempt, y.eeRate, y.yampe, y.cpp2, y.se, CPP_BASE_RATE, CPP2_DEDUCTIBLE, SE_SPLIT);
    steps.push(
      `Self-employed CPP (both halves): base CAD ${money(cpp.base)} + first additional CAD ${money(cpp.first_additional)} + CPP2 CAD ${money(cpp.cpp2)} = CAD ${money(cpp.base + cpp.first_additional + cpp.cpp2)}, payable with the return`,
      `Line 22200 deduction (half of base + first additional + CPP2) = CAD ${money(cpp.deduction)}; line 31000 credit amount (other half of base) = CAD ${money(cpp.credit_amount)}`,
    );
  }
  const deduction = cpp?.deduction ?? 0;
  const total = r2(e + se + other);
  const ni = r2(total - rrsp - deduction);
  if (ni < 0) throw new NeedsInput("input 'rrsp_deduction' is more than income less the CPP deduction: an RRSP deduction cannot make net income negative");
  const ti = ni;
  const t29 = y.bands.value[2][0]!;
  const t33 = y.bands.value[3][0]!;
  if (ni > t29 && ni < t33) consts.push(BPA_PHASE);

  const otherAmounts = r2((cpp?.credit_amount ?? 0) + (cpp?.ei ?? 0));
  const both = (n: number) => {
    const fed = federalTax(year, n, n, e, cpp);
    const pv = provincialTax(prov, year, { ti: n, ni: n, employment_income: e, other_credit_amounts: otherAmounts });
    return { fed, pv };
  };
  const { fed, pv } = both(ni);
  if (!pv) {
    return missingRule(spec.name, "Alberta supplemental tax credit base for 2026",
      "The credits are above the 2025 base of $4,800, so the 2026 supplemental credit applies; ab-individual-return says the 2026 base ($4,896) is worked out from the escalator and not yet printed by CRA or Alberta.",
      [...consts, AB_SUPP_26_UNCONFIRMED], { inputsUsed: used });
  }
  consts.push(P.bands, P.credit, P.bpa, ...P.rules);

  const totalTax = r2(fed.basic_federal_tax + pv.tax);
  const cppWithReturn = se > 0 && cpp ? r2(cpp.base + cpp.first_additional + cpp.cpp2) : 0;
  const balance = r2(totalTax + cppWithReturn - withheld);
  const step = Math.min(1_000, ni);
  const lower = both(r2(ni - step));
  const saving1000 = r2(totalTax - (lower.fed.basic_federal_tax + lower.pv!.tax));
  const fedSaving = federalRrspSaving(year, ti, ni, fed.basic_federal_tax);
  const pl = pv.lines;

  steps.push(
    `Total income CAD ${money(total)} less RRSP CAD ${money(rrsp)} less CPP deduction CAD ${money(deduction)} = net income CAD ${money(ni)} = taxable income (no other deductions)`,
    `Federal tax on CAD ${money(ti)} at the ${year} brackets (top dollar at ${pct(bandRate(y.bands.value, ti))}) = CAD ${money(fed.tax)}`,
    `Federal credits = (BPA CAD ${money(fed.bpa)}${cpp ? ` + CPP/EI CAD ${money(otherAmounts)}` : ""}${e > 0 ? ` + Canada employment amount CAD ${money(fed.canada_employment_amount)}` : ""}) x ${pct(y.credit.value)} = CAD ${money(fed.credits)}; basic federal tax CAD ${money(fed.basic_federal_tax)}`,
    `${NAMES[prov]} tax on CAD ${money(ti)} at the ${year} brackets = CAD ${money(pl.tax_on_taxable_income)}; credits (BPA CAD ${money(P.bpa.value)}${cpp ? ` + CPP/EI CAD ${money(otherAmounts)}` : ""}) x ${pct(P.credit.value)} = CAD ${money(pl.non_refundable_credits)}; basic ${NAMES[prov]} tax CAD ${money(pl.basic_tax)}`,
    ...(prov === "ON"
      ? [`Ontario surtax CAD ${money(pl.surtax)}; tax reduction CAD ${money(pl.tax_reduction)}; LIFT credit CAD ${money(pl.lift_credit)}; Health Premium on taxable income CAD ${money(pl.health_premium)}`]
      : prov === "BC"
        ? [`BC tax reduction CAD ${money(pl.tax_reduction)}`]
        : [`Alberta supplemental tax credit CAD ${money(pl.supplemental_credit)}`]),
    `${NAMES[prov]} tax = CAD ${money(pv.tax)}; total income tax = CAD ${money(totalTax)}`,
    ...(se > 0 ? [`Plus self-employed CPP payable with the return CAD ${money(cppWithReturn)}`] : []),
    `Less tax already paid CAD ${money(withheld)} = ${balance >= 0 ? "balance owing" : "refund"} CAD ${money(Math.abs(balance))}`,
    `CAD ${money(step)} more RRSP deduction would save CAD ${money(saving1000)} of income tax (federal alone: CAD ${fedSaving} per dollar at this income)`,
  );

  return ok(
    spec.name,
    { label: `Balance owing for ${year} (negative = refund), ${NAMES[prov]} resident`, value: balance, currency: "CAD" },
    {
      total_income: total,
      ...(cpp ? { cpp: { base: cpp.base, first_additional: cpp.first_additional, cpp2: cpp.cpp2 } } : {}),
      ...(e > 0 && cpp ? { ei_premium: cpp.ei } : {}),
      cpp_deduction: deduction,
      rrsp_deduction: rrsp,
      net_income: ni,
      taxable_income: ti,
      federal_tax_on_taxable_income: fed.tax,
      federal_basic_personal_amount: fed.bpa,
      canada_employment_amount: fed.canada_employment_amount,
      federal_non_refundable_credits: fed.credits,
      basic_federal_tax: fed.basic_federal_tax,
      provincial: pl,
      provincial_tax: pv.tax,
      total_income_tax: totalTax,
      cpp_payable_with_return: cppWithReturn,
      tax_withheld: withheld,
      balance_owing: balance,
      rrsp_saving_next_1000: saving1000,
      federal_saving_per_extra_rrsp_dollar: fedSaving,
    },
    steps,
    consts,
    used,
    {
      assumptions: [
        `Resident in ${NAMES[prov]} on 31 December ${year} and in Canada all year; single, under 65, no dependants; not bankrupt`,
        "Taxable income equals net income: no loss carryovers, capital gains or other deductions",
        "Credits are the basic personal amount, CPP/EI and the Canada employment amount only (no medical, tuition, donation, disability or other credits)",
        ...(e > 0 ? ["One employer for the whole year; CPP and EI are the statutory annual amounts, assumed deducted from pay"] : []),
        ...(se > 0 ? ["Age 18 to 70 for CPP; not opted into EI special benefits as a self-employed person"] : []),
        ...(prov === "ON" ? ["Ontario LIFT uses net income as adjusted net income (no UCCB or RDSP amounts)"] : []),
      ],
      anchors,
      notes: [
        `${year} return due 30 April ${Number(year) + 1} (15 June if self-employed); any balance is payable by 30 April ${Number(year) + 1}`,
        ...(year === "2026" ? ["The 2026 provincial forms are not published yet: the tax on lower bands is worked out from the 2026 brackets the way the 2025 forms print it"] : []),
      ],
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
