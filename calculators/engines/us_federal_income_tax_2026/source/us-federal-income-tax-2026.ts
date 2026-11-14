// US federal individual income tax (Form 1040) for tax years 2025 and 2026, with the
// estimated-tax safe harbour for the same year.
//
// Skills: us-federal-income-tax-return-1040 (2026 rate schedules, standard deduction, child
// tax credit, AMT exemption, the 2026 itemized deduction limit), us-form-1040-individual-return
// (2025 brackets, standard deduction, child tax credit and its phase-out start, AMT, Additional
// Medicare), us-capital-gains (0%/15%/20% ceilings, net investment income tax),
// us-qbi-deduction (20% rate, QBI, Form 8995, 2026 thresholds and minimum; 2025 thresholds),
// us-schedule-c-and-se-computation (2026 Additional Medicare), us-quarterly-estimated-tax (2026
// safe harbour and due dates, instalments, the zero-tax exception; 2025 due dates),
// us-form-1040-individual-return (2025 safe harbour), us-2026-federal-tax-changes (child tax
// credit made permanent). Self-employment tax is the us_se_tax engine's, imported.
//
// The engine refuses (missing_rule) whatever no skill states: a 2025 married-filing-separately
// return (no skill prints that schedule), the QBI deduction above the threshold (Form 8995-A),
// the child tax credit above its phase-out start (no skill states the reduction rate), and the
// alternative minimum tax whenever it cannot be shown to be zero.
import { FactReader, NeedsInput, missingRule, money, ok, pct, r2, rule, taxYearFact, type Engine, type EngineSpec, type Rule } from "./types";
import { BASE, HALF, MED, MINNE, NEF, SS, se } from "./us-se-tax";

const F26 = "us-federal-income-tax-return-1040";
const F25 = "us-form-1040-individual-return";
const CG = "us-capital-gains";
const SE = "us-schedule-c-and-se-computation";
const QB = "us-qbi-deduction";
const ET = "us-quarterly-estimated-tax";
const CH = "us-2026-federal-tax-changes";

export const STATUSES = ["single", "married_filing_jointly", "married_filing_separately", "head_of_household"] as const;
export type Status = (typeof STATUSES)[number];
type ByStatus<T> = Record<Status, T>;
const byStatus = <T>(single: T, mfj: T, mfs: T, hoh: T): ByStatus<T> => ({
  single, married_filing_jointly: mfj, married_filing_separately: mfs, head_of_household: hoh,
});

/** A rate schedule: [upper limit of the band (null = no limit), rate]. */
export type Schedule = [number | null, number][];
const RATES = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37];
const sched = (...tops: number[]): Schedule => RATES.map((r, i) => [i < tops.length ? tops[i] : null, r]);

// ---- 2026 rate schedules (Rev. Proc. 2025-32, as the skill prints them) ----
const SEC_R26 = "Tax year 2026 rate schedules";
export const SCHED_MFJ_2026 = rule("RATE_SCHEDULE_MFJ_2026", sched(24_800, 100_800, 211_400, 403_550, 512_450, 768_700), F26, SEC_R26,
  "Married filing jointly and surviving spouses, up to USD 24,800 | 10% of taxable income\n" +
  "Married filing jointly, over USD 24,800 up to USD 100,800 | USD 2,480 plus 12% of the excess over USD 24,800\n" +
  "Married filing jointly, over USD 100,800 up to USD 211,400 | USD 11,600 plus 22% of the excess over USD 100,800\n" +
  "Married filing jointly, over USD 211,400 up to USD 403,550 | USD 35,932 plus 24% of the excess over USD 211,400\n" +
  "Married filing jointly, over USD 403,550 up to USD 512,450 | USD 82,048 plus 32% of the excess over USD 403,550\n" +
  "Married filing jointly, over USD 512,450 up to USD 768,700 | USD 116,896 plus 35% of the excess over USD 512,450\n" +
  "Married filing jointly, over USD 768,700 | USD 206,583.50 plus 37% of the excess over USD 768,700");
export const SCHED_HOH_2026 = rule("RATE_SCHEDULE_HOH_2026", sched(17_700, 67_450, 105_700, 201_750, 256_200, 640_600), F26, SEC_R26,
  "Head of household, up to USD 17,700 | 10% of taxable income\n" +
  "Head of household, over USD 17,700 up to USD 67,450 | USD 1,770 plus 12% of the excess over USD 17,700\n" +
  "Head of household, over USD 67,450 up to USD 105,700 | USD 7,740 plus 22% of the excess over USD 67,450\n" +
  "Head of household, over USD 105,700 up to USD 201,750 | USD 16,155 plus 24% of the excess over USD 105,700\n" +
  "Head of household, over USD 201,750 up to USD 256,200 | USD 39,207 plus 32% of the excess over USD 201,750\n" +
  "Head of household, over USD 256,200 up to USD 640,600 | USD 56,631 plus 35% of the excess over USD 256,200\n" +
  "Head of household, over USD 640,600 | USD 191,171 plus 37% of the excess over USD 640,600");
const SHARED_26 =
  "Single, and married filing separately, up to USD 12,400 | 10% of taxable income\n" +
  "Single, and married filing separately, over USD 12,400 up to USD 50,400 | USD 1,240 plus 12% of the excess over USD 12,400\n" +
  "Single, and married filing separately, over USD 50,400 up to USD 105,700 | USD 5,800 plus 22% of the excess over USD 50,400\n" +
  "Single, and married filing separately, over USD 105,700 up to USD 201,775 | USD 17,966 plus 24% of the excess over USD 105,700\n" +
  "Single, and married filing separately, over USD 201,775 up to USD 256,225 | USD 41,024 plus 32% of the excess over USD 201,775\n";
export const SCHED_SINGLE_2026 = rule("RATE_SCHEDULE_SINGLE_2026", sched(12_400, 50_400, 105_700, 201_775, 256_225, 640_600), F26, SEC_R26,
  SHARED_26 +
  "Single only, over USD 256,225 up to USD 640,600 | USD 58,448 plus 35% of the excess over USD 256,225\n" +
  "Single only, over USD 640,600 | USD 192,979.25 plus 37% of the excess over USD 640,600");
export const SCHED_MFS_2026 = rule("RATE_SCHEDULE_MFS_2026", sched(12_400, 50_400, 105_700, 201_775, 256_225, 384_350), F26, SEC_R26,
  SHARED_26 +
  "Married filing separately only, over USD 256,225 up to USD 384,350 | USD 58,448 plus 35% of the excess over USD 256,225\n" +
  "Married filing separately only, over USD 384,350 | USD 103,291.75 plus 37% of the excess over USD 384,350");

// ---- 2025 brackets (single, MFJ, HoH only: no skill prints the 2025 MFS schedule) ----
const SEC_R25 = "2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent)";
const T25_S = [11_925, 48_475, 103_350, 197_300, 250_525, 626_350];
const T25_J = [23_850, 96_950, 206_700, 394_600, 501_050, 751_600];
const T25_H = [17_000, 64_850, 103_350, 197_300, 250_500, 626_350];
export const SCHED_SINGLE_2025 = rule("RATE_SCHEDULE_SINGLE_2025", sched(...T25_S), F25, SEC_R25,
  "Single (2025) tax brackets\nRate | Taxable income\n10% | $0 – $11,925\n12% | $11,925 – $48,475\n22% | $48,475 – $103,350\n" +
  "24% | $103,350 – $197,300\n32% | $197,300 – $250,525\n35% | $250,525 – $626,350\n37% | over $626,350");
export const SCHED_MFJ_2025 = rule("RATE_SCHEDULE_MFJ_2025", sched(...T25_J), F25, SEC_R25,
  "MFJ (2025) tax brackets\nRate | Taxable income\n10% | $0 – $23,850\n12% | $23,850 – $96,950\n22% | $96,950 – $206,700\n" +
  "24% | $206,700 – $394,600\n32% | $394,600 – $501,050\n35% | $501,050 – $751,600\n37% | over $751,600");
export const SCHED_HOH_2025 = rule("RATE_SCHEDULE_HOH_2025", sched(...T25_H), F25, SEC_R25,
  "HoH (2025) tax brackets\nRate | Taxable income\n10% | $0 – $17,000\n12% | $17,000 – $64,850\n22% | $64,850 – $103,350\n" +
  "24% | $103,350 – $197,300\n32% | $197,300 – $250,500\n35% | $250,500 – $626,350\n37% | over $626,350");

export const SCHEDULES: Record<string, Partial<ByStatus<Rule<Schedule>>>> = {
  "2026": byStatus(SCHED_SINGLE_2026, SCHED_MFJ_2026, SCHED_MFS_2026, SCHED_HOH_2026),
  "2025": { single: SCHED_SINGLE_2025, married_filing_jointly: SCHED_MFJ_2025, head_of_household: SCHED_HOH_2025 },
};

// ---- Deductions ----
const SEC_D26 = "Tax year 2026 deductions, credits and other amounts";
export const STD_2026 = rule("STANDARD_DEDUCTION_2026", byStatus(16_100, 32_200, 16_100, 24_150), F26, SEC_D26,
  "Standard deduction, married filing jointly and surviving spouses | USD 32,200\n" +
  "Standard deduction, head of household | USD 24,150\n" +
  "Standard deduction, single and married filing separately | USD 16,100");
export const STD_2025 = rule("STANDARD_DEDUCTION_2025", byStatus(15_750, 31_500, 15_750, 23_625), F25, "2.1 Standard deduction (§63(c))",
  "Filing status | 2025 amount\nSingle | $15,750\nMarried filing jointly (MFJ) | $31,500\nMarried filing separately (MFS) | $15,750\nHead of household (HoH) | $23,625");
const SEC_ACT = "Changes made by Public Law 119-21 that apply to a tax year 2026 return";
export const CASH_GIFTS_2026 = rule("NON_ITEMIZER_CASH_GIFTS_2026", { other: 1_000, joint: 2_000 }, F26, SEC_ACT,
  "Charitable deduction for a taxpayer who does not itemize, taxable years beginning after 31 December 2025 | up to USD 1,000 (USD 2,000 joint)");
export const LIMIT_68_2026 = rule("ITEMIZED_LIMIT_37_PERCENT_BAND_2026", 2 / 37, F26, SEC_ACT,
  "Limit on itemized deductions in the 37% bracket, taxable years beginning after 31 December 2025 | itemized deductions reduced by 2/37 of the lesser of (1) the itemized deductions, or (2) taxable income, computed before this reduction and increased by those itemized deductions, above the dollar amount at which the 37% bracket begins for the taxpayer");

// ---- QBI (section 199A), simplified computation only ----
export const QBI_RATE = rule("QBI_RATE", 0.2, QB, "Rates, bands and thresholds",
  "The final One Big Beautiful Bill Act (Public Law 119-21, section 70105) kept the 20% rate, removed the end-2025 expiry\n" +
  "Deduction rate on QBI | 20% (the 23% in the House-passed bill was not enacted)");
export const QBI_METHOD = rule("QBI_SIMPLIFIED_METHOD", true, QB, "Rates, bands and thresholds; Step 3: where taxable income sits",
  "Overall cap | 20% of (taxable income before the QBI deduction minus net capital gain, with qualified dividends added to net capital gain)\n" +
  "At or below the threshold ... | 20% of QBI for every business, SSTB or not; no wage or UBIA limit | Form 8995");
export const QBI_DEFINITION = rule("QBI_DEFINITION", true, QB, "Step 1: qualified business income for each business; Step 2: taxable income before the QBI deduction",
  "QBI = Schedule C line 31 minus the deductible half of self-employment tax (Schedule 1) minus the self-employed health insurance deduction minus the deduction for contributions to SEP, SIMPLE or solo 401(k) plans for the owner.\n" +
  "Use Form 1040 line 11a (adjusted gross income) minus the standard or itemized deduction and the other deductions the 2026 draft Form 8995 instructions list for line 11");
export const QBI_THRESHOLD_2026 = rule("QBI_THRESHOLD_2026", byStatus(201_750, 403_500, 201_775, 201_750), QB, "Rates, bands and thresholds",
  "Threshold amount, all other returns (single, head of household, qualifying surviving spouse) | USD 201,750\n" +
  "Threshold amount, married filing separately | USD 201,775\nThreshold amount, married filing jointly | USD 403,500");
export const QBI_THRESHOLD_2025 = rule("QBI_THRESHOLD_2025", byStatus(197_300, 394_600, 197_300, 197_300), QB, "Section 3 — Year-specific figures table for tax year 2025",
  "Taxable income threshold (single / HoH / QSS) | $197,300\nTaxable income threshold (MFJ) | $394,600\nTaxable income threshold (MFS) | $197,300");
export const QBI_MINIMUM_2026 = rule("QBI_MINIMUM_2026", { minimum: 400, qbi_needed: 1_000 }, QB, "Rates, bands and thresholds; Step 7: combine, cap, then the minimum",
  "Minimum deduction, taxable years beginning after 31 December 2025 | USD 400\n" +
  "QBI needed for the minimum, from active businesses (material participation, section 469(h)) | USD 1,000\n" +
  "Minimum (new for 2026): if aggregate QBI from all businesses the taxpayer materially participated in is at least USD 1,000, the deduction is the greater of the step 3 result and USD 400");

// ---- Capital gains and qualified dividends ----
export interface CgBands { rates: [number, number, number]; ceilings: ByStatus<[number, number]> }
const CG_HEAD = "0% up to taxable income of | 15% up to taxable income of | 20% above";
export const CG_2026 = rule<CgBands>("CAPITAL_GAIN_RATES_2026", { rates: [0, 0.15, 0.2], ceilings: byStatus([49_450, 545_500], [98_900, 613_700], [49_450, 306_850], [66_200, 579_600]) },
  CG, "Rates, bands and thresholds",
  "Long-term gain and qualified dividends: maximum zero rate amount, married filing jointly and surviving spouse | USD 98,900\n" +
  "Maximum 15 percent rate amount, married filing jointly and surviving spouse (20% above) | USD 613,700\n" +
  "Maximum zero rate amount, married filing separately | USD 49,450\nMaximum 15 percent rate amount, married filing separately | USD 306,850\n" +
  "Maximum zero rate amount, head of household | USD 66,200\nMaximum 15 percent rate amount, head of household | USD 579,600\n" +
  "Maximum zero rate amount, all other individuals (single) | USD 49,450\nMaximum 15 percent rate amount, all other individuals (single) | USD 545,500\n" +
  "Rates on adjusted net capital gain | 0%, 15%, 20%");
export const CG_2025 = rule<CgBands>("CAPITAL_GAIN_RATES_2025", { rates: [0, 0.15, 0.2], ceilings: byStatus([48_350, 533_400], [96_700, 600_050], [48_350, 300_000], [64_750, 566_700]) },
  CG, "2025 returns (tax year 2025, extended deadline 15 October 2026)",
  `Filing status (2025) | ${CG_HEAD}\nSingle | USD 48,350 | USD 533,400 | USD 533,400\nMarried filing jointly, surviving spouse | USD 96,700 | USD 600,050 | USD 600,050\n` +
  "Married filing separately | USD 48,350 | USD 300,000 | USD 300,000\nHead of household | USD 64,750 | USD 566,700 | USD 566,700");
export const CG_STACKING = rule("CAPITAL_GAIN_STACKING", true, CG, "Step 5: split the long-term gain into rate groups; Step 6: stack the gain on top of ordinary income",
  "0/15/20 group: all other net capital gain, plus qualified dividends.\n" +
  "Ordinary taxable income fills the brackets first; the preferential gain sits on top.\n" +
  "Use the Qualified Dividends and Capital Gain Tax Worksheet in the Form 1040 instructions.");

// ---- Child tax credit ----
export const CTC_2026 = rule("CHILD_TAX_CREDIT_2026", { per_child: 2_200, refundable_per_child: 1_700 }, F26, SEC_D26,
  "Child tax credit, maximum per qualifying child | USD 2,200\nChild tax credit, refundable amount per child | USD 1,700");
export const CTC_2025 = rule("CHILD_TAX_CREDIT_2025", { per_child: 2_200, refundable_per_child: 1_700 }, F25, "2.9 Other OBBBA changes",
  "Child Tax Credit — $2,200 per qualifying child under 17 (§24(h)), refundable portion $1,700 in 2025");
export const CTC_PHASEOUT_START = rule("CHILD_TAX_CREDIT_PHASEOUT_START", { joint: 400_000, other: 200_000 }, F25, "2.9 Other OBBBA changes",
  "Child Tax Credit — $2,200 per qualifying child under 17 (§24(h)), ... made permanent by OBBBA §70104. Phaseout begins $400k MFJ / $200k other.");
export const CTC_PERMANENT = rule("CHILD_TAX_CREDIT_PERMANENT", true, CH, "Boundary and exception table / Families",
  "Child tax credit (permanent). USD 2,200 per child, USD 1,700 refundable (section 70104, taxable years beginning after 31 December 2024).");

// ---- Alternative minimum tax: only used to show that it is zero ----
export const AMT_2026 = rule("AMT_EXEMPTION_2026", { exemption: byStatus(90_100, 140_200, 70_100, 90_100), phaseout_start: byStatus(500_000, 1_000_000, 500_000, 500_000) }, F26, SEC_D26,
  "Alternative minimum tax exemption, married filing jointly and surviving spouses | USD 140,200\n" +
  "Alternative minimum tax exemption, unmarried (not surviving spouse) | USD 90,100\n" +
  "Alternative minimum tax exemption, married filing separately | USD 70,100\n" +
  "Alternative minimum tax exemption, phase-out starts and ends, joint returns | USD 1,000,000; USD 1,280,400\n" +
  "Alternative minimum tax exemption, phase-out starts and ends, unmarried | USD 500,000; USD 680,200\n" +
  "Alternative minimum tax exemption, phase-out starts and ends, married filing separately | USD 500,000; USD 640,200");
export const AMT_2025 = rule("AMT_EXEMPTION_2025", { exemption: byStatus(88_100, 137_000, 68_500, 88_100), phaseout_start: byStatus(626_350, 1_252_700, 626_350, 626_350) }, F25, "2.4 AMT exemption — §55(d) (post-TCJA, OBBBA-permanent)",
  "Filing status | Exemption | Phaseout begins | Fully phased out\nSingle / HoH | $88,100 | $626,350 | $978,750\nMFJ / QSS | $137,000 | $1,252,700 | $1,800,700\nMFS | $68,500 | $626,350 | $900,350");
export const AMT_TOP_RATE = rule("AMT_TOP_RATE", 0.28, F25, "2.4 AMT exemption — §55(d) (post-TCJA, OBBBA-permanent)",
  "AMT rates — 26% on AMTI up to ... 28% above.");
export const AMT_STEPS = rule("AMT_COMPUTATION_STEPS", true, F25, "9.2 AMT computation flow",
  "AMT computation steps — 1. Start with regular taxable income (Line 15). 2. Add back the standard deduction (if claimed). 3. Add AMT adjustments and preferences (Form 6251 Lines 2a-2t). 4. Subtract the AMT exemption (with phaseout if AMTI > threshold). 5. Apply 26%/28% AMT rates. 6. Subtract AMT foreign tax credit. 7. Compare to regular tax.");

// ---- Taxes on higher income ----
export const ADDL_MEDICARE_2026 = rule("ADDITIONAL_MEDICARE_2026", { rate: 0.009, threshold: byStatus(200_000, 250_000, 125_000, 200_000) }, SE, "Rates, bands and thresholds; Form 8959: Additional Medicare Tax on self-employment income",
  "Additional Medicare Tax on self-employment income | 0.9%\n" +
  "Additional Medicare Tax threshold, single, head of household, qualifying surviving spouse | USD 200,000\n" +
  "Additional Medicare Tax threshold, married filing jointly | USD 250,000\nAdditional Medicare Tax threshold, married filing separately | USD 125,000\n" +
  "Take the threshold for the filing status (USD 200,000, 250,000 or 125,000). Reduce it, not below zero, by the person's Medicare wages. Self-employment income (Schedule SE line 6) above the reduced threshold is taxed at 0.9%.");
export const ADDL_MEDICARE_2025 = rule("ADDITIONAL_MEDICARE_2025", { rate: 0.009, threshold: byStatus(200_000, 250_000, 125_000, 200_000) }, F25, "2.6 Additional Medicare Tax — §3101(b)(2) and §1401(b)(2)",
  "Additional Medicare Tax thresholds\nFiling status | Threshold\nSingle / HoH | $200,000\nMFJ | $250,000\nMFS | $125,000\nAdditional Medicare Tax rate — 0.9% on wages/SE income over threshold");
export const NIIT = rule("NET_INVESTMENT_INCOME_TAX", { rate: 0.038, threshold: byStatus(200_000, 250_000, 125_000, 200_000) }, CG, "Rates, bands and thresholds; Step 8: the net investment income tax",
  "Net investment income tax rate | 3.8%\nNIIT threshold, joint return or surviving spouse | USD 250,000\n" +
  "NIIT threshold, married filing separately (half the joint amount) | USD 125,000\nNIIT threshold, any other case (single, head of household) | USD 200,000\n" +
  "On Form 8960: 3.8% of the lesser of (A) net investment income or (B) modified adjusted gross income over the threshold");
export const NII_ITEMS = rule("NET_INVESTMENT_INCOME_ITEMS", true, CG, "Step 8: the net investment income tax",
  "Net investment income includes capital gains, interest, dividends, ... It excludes wages, most self-employment income");
export const NIIT_2025 = rule("NIIT_SAME_FOR_2025", true, CG, "2025 returns (tax year 2025, extended deadline 15 October 2026)",
  "The NIIT thresholds, the 3.8% rate and the USD 3,000 / USD 1,500 loss limit are the same as for 2026.");

// ---- Estimated tax safe harbour ----
export interface SafeHarbour { current: number; prior: number; prior_high: number; agi_limit: number; agi_limit_mfs: number }
const SH = { current: 0.9, prior: 1, prior_high: 1.1, agi_limit: 150_000, agi_limit_mfs: 75_000 };
export const SH_2026 = rule<SafeHarbour>("SAFE_HARBOUR_2026", SH, ET, "Rates, bands and thresholds; Boundary and exception table",
  "Current-year safe harbour: share of the 2026 tax | 90%\nPrior-year safe harbour: share of the 2025 tax | 100%\n" +
  "Prior-year safe harbour where 2025 AGI exceeds the limit below | 110%\n2025 AGI limit for 100% (110% above it) | USD 150,000\n" +
  "2025 AGI limit, married filing separately for 2026 | USD 75,000\n" +
  "2025 return not filed, or 2025 a short year | Prior-year safe harbour not available: only 90% of 2026 tax");
export const DATES_2026 = rule("ESTIMATED_TAX_DUE_DATES_2026", ["2026-04-15", "2026-06-15", "2026-09-15", "2027-01-15"], ET, "Rates, bands and thresholds",
  "1st installment due | 15 April 2026\n2nd installment due | 15 June 2026\n3rd installment due | 15 September 2026\n4th installment due | 15 January 2027");
export const SH_2025 = rule<SafeHarbour>("SAFE_HARBOUR_2025", SH, F25, "15. Estimated tax — §6654",
  "Safe harbors — 90% of current year tax, OR 100% of prior year tax (110% if prior-year AGI > $150,000 / $75,000 MFS)");
export const DATES_2025 = rule("ESTIMATED_TAX_DUE_DATES_2025", ["2025-04-15", "2025-06-16", "2025-09-15", "2026-01-15"], ET, "Section 1 -- Quick reference",
  "1st | April 15, 2025\n2nd | June 16, 2025\n3rd | September 15, 2025\n4th | January 15, 2026");
export const INSTALMENT = rule("QUARTERLY_INSTALMENT_SHARE", 0.25, ET, "Rates, bands and thresholds",
  "Each regular installment | 25% of the required annual payment");
export const ZERO_PRIOR_TAX = rule("ZERO_PRIOR_YEAR_TAX", true, ET, "Step 1: is anything required?",
  "The zero-tax exception: no payments are required if the person was a US citizen or resident alien for all of 2025, the 2025 tax year was 12 months, and they had no tax liability for 2025");

const SE_RULES = [NEF, MINNE, SS, BASE, MED, HALF];
const CONSTS: Rule[] = [
  SCHED_SINGLE_2026, SCHED_MFJ_2026, SCHED_MFS_2026, SCHED_HOH_2026, SCHED_SINGLE_2025, SCHED_MFJ_2025, SCHED_HOH_2025,
  STD_2026, STD_2025, CASH_GIFTS_2026, LIMIT_68_2026,
  QBI_RATE, QBI_METHOD, QBI_DEFINITION, QBI_THRESHOLD_2026, QBI_THRESHOLD_2025, QBI_MINIMUM_2026,
  CG_2026, CG_2025, CG_STACKING,
  CTC_2026, CTC_2025, CTC_PHASEOUT_START, CTC_PERMANENT,
  AMT_2026, AMT_2025, AMT_TOP_RATE, AMT_STEPS,
  ADDL_MEDICARE_2026, ADDL_MEDICARE_2025, NIIT, NII_ITEMS, NIIT_2025,
  SH_2026, DATES_2026, SH_2025, DATES_2025, INSTALMENT, ZERO_PRIOR_TAX,
  ...SE_RULES,
];

const STATES =
  "alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|maryland|massachusetts|michigan|minnesota|mississippi|missouri|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming|district of columbia";

export const spec: EngineSpec = {
  name: "us_federal_income_tax_2026",
  version: "1.1.0",
  jurisdiction: "US",
  tax_years: ["2025", "2026"],
  summary:
    "US federal individual income tax on Form 1040 for tax year 2025 or 2026: AGI, standard or itemized deduction, the simplified QBI deduction, bracket tax with the 0%/15%/20% rates on qualified dividends and long-term gains, the child tax credit, self-employment tax, Additional Medicare Tax and net investment income tax, plus the estimated-tax safe harbour and due dates. Refuses the alternative minimum tax when it cannot be shown to be zero, QBI above the threshold, the child tax credit above its phase-out start, and 2025 married filing separately.",
  // Personal federal tax only. A question about self-employment tax alone stays with us_se_tax;
  // state, corporate, payroll, sales, property, estate and gift questions never reach it.
  topics: new RegExp(
    "^(?![\\s\\S]*\\b(?:corporat\\w*|c[- ]?corp\\w*|s[- ]?corp\\w*|compan(?:y|y's|ies)|1120s?|1065|partnership return|state (?:income )?tax(?:es)?|state return|franchise tax|sales tax|use tax|property tax|payroll|estate tax|gift tax|excise)\\b)" +
      `(?![\\s\\S]*\\b(?:${STATES})\\b(?![\\s\\S]*\\bfederal\\b))` +
      "(?=[\\s\\S]*(?:\\bfederal (?:income )?tax|\\bincome tax|\\btax brackets?\\b|\\bmarginal (?:tax )?rate|\\beffective tax rate|\\btaxable income|\\b(?:form )?1040\\b(?!-?es)|\\bhow much (?:federal )?tax\\b|\\bhow much (?:do|will|would) (?:i|we) owe\\b|(?<!employment )(?<!\\bse )\\btax (?:bill|liability)\\b|\\bcapital gains? tax|\\bqualified dividends?\\b|\\bchild tax credit|\\bstandard deduction|\\bestimated tax|\\b1040-?es\\b|\\bquarterly (?:tax|estimated|payments?)\\b|\\bsafe harbou?r))",
  ),
  facts: {
    filing_status: { type: "string", required: true, choices: [...STATUSES], description: "filing status at the end of the year (a qualifying surviving spouse is not covered)" },
    wages: { type: "number", required: false, default: 0, description: "USD, Form W-2 box 1 (taxable wages)" },
    w2_social_security_wages: { type: "number", required: false, description: "USD, Form W-2 box 3. Left out, it is taken as equal to wages. Used only for the self-employment tax wage base" },
    w2_medicare_wages: { type: "number", required: false, description: "USD, Form W-2 box 5. Left out, it is taken as equal to wages. Used only for the Additional Medicare Tax" },
    self_employment_net_profit: { type: "number", required: false, default: 0, description: "USD, Schedule C line 31 net profit (all Schedule C businesses together; a loss is not covered)" },
    self_employed_retirement_and_health_deductions: { type: "number", required: false, default: 0, description: "USD, Schedule 1 lines 16 and 17 for that business: SEP, SIMPLE or solo 401(k) deduction plus self-employed health insurance. They reduce AGI and QBI" },
    other_adjustments: { type: "number", required: false, default: 0, description: "USD, other Schedule 1 adjustments not tied to the business (HSA, IRA, student loan interest, educator expenses)" },
    interest: { type: "number", required: false, default: 0, description: "USD, taxable interest (Form 1040 line 2b)" },
    ordinary_dividends: { type: "number", required: false, default: 0, description: "USD, ordinary dividends (line 3b), qualified dividends included" },
    qualified_dividends: { type: "number", required: false, default: 0, description: "USD, qualified dividends (line 3a), part of ordinary_dividends" },
    short_term_capital_gains: { type: "number", required: false, default: 0, description: "USD, net short-term capital gain (taxed as ordinary income). If short-term losses exceed short-term gains, subtract the net loss from long_term_capital_gains and enter 0" },
    long_term_capital_gains: { type: "number", required: false, default: 0, description: "USD, net long-term capital gain on assets held more than one year, after any net short-term loss, with no 28% collectibles or 25% section 1250 gain. A net capital loss is not covered" },
    other_ordinary_income: { type: "number", required: false, default: 0, description: "USD, other taxable income that is not investment income (unemployment compensation, taxable pensions and IRA distributions, prizes). Rents, royalties and passive income are not covered" },
    itemized_deductions: { type: "number", required: false, description: "USD, Schedule A total after the SALT cap and every other Schedule A limit. Left out, the standard deduction is used; given, the larger of the two is used" },
    itemized_state_and_local_taxes: { type: "number", required: false, description: "USD, the state and local taxes included in itemized_deductions (after the cap). Used only to show the alternative minimum tax is zero; left out, all itemized deductions are treated as taxes (the cautious reading)" },
    cash_charitable_gifts: { type: "number", required: false, default: 0, description: "USD, cash gifts to public charities. Used only in 2026 when the standard deduction is taken (up to USD 1,000, or USD 2,000 married filing jointly); an itemizer includes gifts in itemized_deductions" },
    dependents_under_17: { type: "number", required: false, default: 0, description: "qualifying children under 17 at the end of the year, each with a social security number (child tax credit)" },
    materially_participates: { type: "boolean", required: false, description: "2026 only, asked when it changes the answer: the taxpayer materially participates in the Schedule C business (for the USD 400 minimum QBI deduction)" },
    prior_year_tax: { type: "number", required: false, description: "USD, total tax on last year's return (Form 1040 line 24), for the estimated-tax safe harbour. Left out, no safe harbour is computed" },
    prior_year_agi: { type: "number", required: false, description: "USD, last year's AGI (Form 1040 line 11b), needed with prior_year_tax for the 100% or 110% test" },
    tax_year: taxYearFact(["2025", "2026"]),
  },
  outputs: {
    agi: "USD, adjusted gross income",
    deduction_used: "standard or itemized",
    deduction: "USD",
    qbi_deduction: "USD",
    taxable_income: "USD",
    ordinary_tax: "USD, bracket tax on ordinary taxable income",
    preferential_tax: "USD, tax on qualified dividends and long-term gains at 0%/15%/20%",
    income_tax: "USD, Form 1040 line 16",
    child_tax_credit: "USD, the non-refundable part used",
    se_tax: "USD",
    additional_medicare_tax: "USD",
    net_investment_income_tax: "USD",
    total_tax: "USD, Form 1040 line 24",
    estimated_tax: "required annual payment, instalment and due dates (when prior_year_tax is given)",
  },
};

export const anchors = [
  "us-form-1040-individual-return Example A (2025, single): taxable income $83,400, tax $12,716",
  "us-form-1040-individual-return Example B (2025, MFJ, itemized $67,300, two children): tax $37,852, CTC $4,400, NIIT $236, Additional Medicare $270, total tax $33,958",
  "us-form-1040-individual-return Example D (2025, single): regular tax $40,840, NIIT about $1,210 (the ISO AMT is outside this engine)",
  "us-federal-return-assembly Case A (2025): AGI $86,922.27, QBI deduction $14,234.45, taxable income $56,937.82, SE tax $16,955.46",
  "us-federal-return-assembly Case C (2026): QBI $1,500 -> $400 minimum; QBI $999 -> $199.80",
  "us-federal-income-tax-return-1040 worked decision (2026, MFJ, AGI $200,000): standard route $34,200 -> tax $25,900; itemized $30,000 -> $26,824",
  "us-capital-gains Case 1 (2026, single, taxable income $70,000 with $40,000 gain): $3,082.50 on the gain",
  "us-capital-gains Case 2 (2026, MFJ, MAGI $300,000, NII $80,000): NIIT $1,900",
  "us-capital-gains Case 7 (2025, MFJ, taxable income $120,000 with $30,000 gain): $3,495 on the gain",
  "us-quarterly-estimated-tax Examples 1 and 2: required annual payment $18,000 (quarterly $4,500); $46,200 (quarterly $11,550)",
];

/** Tax on taxable income from one rate schedule. */
export function scheduleTax(s: Schedule, x: number): number {
  let tax = 0;
  let lower = 0;
  for (const [upper, rate] of s) {
    if (x <= lower) break;
    tax += rate * (Math.min(x, upper ?? Infinity) - lower);
    lower = upper ?? Infinity;
  }
  return tax;
}

export interface CgResult { ordinaryIncome: number; at0: number; at15: number; at20: number; ordinaryTax: number; preferentialTax: number; tax: number }

/** Qualified Dividends and Capital Gain Tax Worksheet (lines 1 to 25). */
export function capitalGainWorksheet(s: Schedule, cg: CgBands, status: Status, ti: number, preferential: number): CgResult {
  const [zeroTop, fifteenTop] = cg.ceilings[status];
  const l10 = Math.min(ti, preferential);
  const l5 = Math.max(0, ti - preferential);
  const at0 = Math.min(ti, zeroTop) - Math.min(l5, Math.min(ti, zeroTop));
  const at15 = Math.min(l10 - at0, Math.max(0, Math.min(ti, fifteenTop) - (l5 + at0)));
  const at20 = l10 - at0 - at15;
  const t15 = r2(at15 * cg.rates[1]);
  const t20 = r2(at20 * cg.rates[2]);
  const ordinaryTax = r2(scheduleTax(s, l5));
  const worksheet = r2(ordinaryTax + t15 + t20);
  const allOrdinary = r2(scheduleTax(s, ti));
  return { ordinaryIncome: r2(l5), at0: r2(at0), at15: r2(at15), at20: r2(at20), ordinaryTax, preferentialTax: r2(t15 + t20), tax: Math.min(worksheet, allOrdinary) };
}

/** QBI deduction below the threshold (Form 8995), with the 2026 minimum. null = above the threshold. */
export function qbiDeduction(year: string, status: Status, qbi: number, tiBeforeQbi: number, netCapitalGain: number, materiallyParticipates: () => boolean): number | null {
  if (qbi <= 0) return 0;
  const threshold = (year === "2026" ? QBI_THRESHOLD_2026 : QBI_THRESHOLD_2025).value[status];
  if (tiBeforeQbi > threshold) return null;
  const normal = r2(Math.min(QBI_RATE.value * qbi, QBI_RATE.value * Math.max(0, tiBeforeQbi - netCapitalGain)));
  const m = QBI_MINIMUM_2026.value;
  if (year === "2026" && qbi >= m.qbi_needed && normal < m.minimum && materiallyParticipates()) return m.minimum;
  return normal;
}

/** Additional Medicare Tax (Form 8959): wages over the threshold, then SE income over the threshold less wages. */
export function additionalMedicare(rate: number, threshold: number, medicareWages: number, seIncome: number): number {
  return r2(rate * (Math.max(0, medicareWages - threshold) + Math.max(0, seIncome - Math.max(0, threshold - medicareWages))));
}

/** Required annual estimated-tax payment: lesser of 90% of this year's tax and 100%/110% of last year's. */
export function safeHarbour(sh: SafeHarbour, status: Status, currentTax: number, priorTax: number, priorAgi: number | null) {
  const priorPct = priorTax === 0 ? null : (priorAgi as number) > (status === "married_filing_separately" ? sh.agi_limit_mfs : sh.agi_limit) ? sh.prior_high : sh.prior;
  const priorAmount = priorPct === null ? 0 : r2(priorPct * priorTax);
  const ninety = r2(sh.current * currentTax);
  const required = Math.min(ninety, priorAmount);
  return { priorPct, priorAmount, ninety, required, instalment: r2(required * INSTALMENT.value) };
}

const pick = <T>(year: string, y26: Rule<T>, y25: Rule<T>) => (year === "2026" ? y26 : y25);

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const year = f.string("tax_year");
  const status = f.string("filing_status", undefined, [...STATUSES]) as Status;
  const wages = f.number("wages", 0);
  const ssWagesGiven = f.number("w2_social_security_wages", null);
  const mcWagesGiven = f.number("w2_medicare_wages", null);
  const profit = f.number("self_employment_net_profit", 0);
  const seDeductions = f.number("self_employed_retirement_and_health_deductions", 0);
  const otherAdj = f.number("other_adjustments", 0);
  const interest = f.number("interest", 0);
  const ordDiv = f.number("ordinary_dividends", 0);
  const qualDiv = f.number("qualified_dividends", 0);
  const stGain = f.number("short_term_capital_gains", 0);
  const ltGain = f.number("long_term_capital_gains", 0);
  const otherInc = f.number("other_ordinary_income", 0);
  const itemized = f.number("itemized_deductions", null);
  const saltGiven = f.number("itemized_state_and_local_taxes", null);
  const gifts = f.number("cash_charitable_gifts", 0);
  const kids = f.number("dependents_under_17", 0);
  const priorTax = f.number("prior_year_tax", null);
  if (!Number.isInteger(kids)) throw new NeedsInput("input 'dependents_under_17' must be a whole number");
  if (qualDiv > ordDiv) throw new NeedsInput("input 'qualified_dividends' cannot be more than 'ordinary_dividends' (qualified dividends are part of ordinary dividends)");
  if (saltGiven !== null && (itemized === null || saltGiven > itemized)) throw new NeedsInput("input 'itemized_state_and_local_taxes' needs 'itemized_deductions' and cannot be more than it");

  const used: Record<string, unknown> = {
    filing_status: status, wages, self_employment_net_profit: profit, self_employed_retirement_and_health_deductions: seDeductions,
    other_adjustments: otherAdj, interest, ordinary_dividends: ordDiv, qualified_dividends: qualDiv, short_term_capital_gains: stGain,
    long_term_capital_gains: ltGain, other_ordinary_income: otherInc, itemized_deductions: itemized, cash_charitable_gifts: gifts,
    dependents_under_17: kids, tax_year: year,
  };
  const consts: Rule[] = [];
  const steps: string[] = [];
  const assumptions: string[] = [];
  const notes: string[] = [];
  const lines: Record<string, unknown> = {};
  const refuse = (what: string, why: string) => missingRule(spec.name, what, why, consts, { partial: { ...lines }, inputsUsed: used });

  const schedule = SCHEDULES[year][status];
  if (!schedule) {
    return refuse("2025 rate schedule for married filing separately",
      "No OpenAccountants skill prints the 2025 married-filing-separately rate schedule (us-form-1040-individual-return gives single, MFJ and HoH only).");
  }

  // 1. Schedule SE (the us_se_tax engine's method and figures).
  const ssWages = ssWagesGiven ?? wages;
  const [ne, ssPart, medPart] = se(profit, ssWages, year);
  const seTax = r2(ssPart + medPart);
  const halfSe = r2(seTax * HALF.value);
  if (profit > 0) {
    consts.push(...SE_RULES);
    used.w2_social_security_wages = ssWages;
    if (ssWagesGiven === null && wages > 0 && ne >= MINNE.value) assumptions.push("Social security wages (W-2 box 3) taken as equal to wages; give w2_social_security_wages if they differ");
    steps.push(ne < MINNE.value
      ? `Net earnings from self-employment ${pct(NEF.value)} x USD ${money(profit)} = USD ${money(ne)}, under USD ${money(MINNE.value)}: no SE tax`
      : `SE tax: ${pct(SS.value)} x min(net earnings USD ${money(ne)}, wage base USD ${money(BASE.value[year])} less W-2 social security wages USD ${money(ssWages)}) + ${pct(MED.value)} x net earnings = USD ${money(seTax)}; deductible half USD ${money(halfSe)}`);
  }
  if (seDeductions > profit - halfSe) {
    throw new NeedsInput("input 'self_employed_retirement_and_health_deductions' cannot be more than the Schedule C net profit less the deductible half of self-employment tax");
  }

  // 2. AGI.
  const totalIncome = r2(wages + interest + ordDiv + stGain + ltGain + otherInc + profit);
  const agi = r2(totalIncome - halfSe - seDeductions - otherAdj);
  steps.push(`Total income USD ${money(totalIncome)} less adjustments (half SE tax USD ${money(halfSe)}, self-employed retirement and health USD ${money(seDeductions)}, other USD ${money(otherAdj)}) = AGI USD ${money(agi)}`);
  Object.assign(lines, { total_income: totalIncome, deductible_half_se_tax: halfSe, agi });

  // 3. Deduction and QBI.
  const std = pick(year, STD_2026, STD_2025);
  consts.push(std);
  let standardRoute = std.value[status];
  let giftsAllowed = 0;
  if (year === "2026" && gifts > 0) {
    giftsAllowed = Math.min(gifts, status === "married_filing_jointly" ? CASH_GIFTS_2026.value.joint : CASH_GIFTS_2026.value.other);
    standardRoute += giftsAllowed;
  }
  const qbi = r2(profit - halfSe - seDeductions);
  const ncg = qualDiv + ltGain;
  const askParticipation = () => {
    const mp = f.bool("materially_participates");
    used.materially_participates = mp;
    return mp;
  };
  const qbiFor = (tibq: number) => qbiDeduction(year, status, qbi, tibq, ncg, askParticipation);
  const thresholdRule = year === "2026" ? QBI_THRESHOLD_2026 : QBI_THRESHOLD_2025;
  const qbiRefusal = (tibq: number) => {
    consts.push(QBI_RATE, QBI_DEFINITION, QBI_METHOD, thresholdRule);
    return refuse("qualified business income deduction above the threshold (Form 8995-A)",
      `Taxable income before the QBI deduction (USD ${money(tibq)}) is above the ${year} threshold of USD ${money(thresholdRule.value[status])}. Above it the deduction depends on W-2 wages, qualified property and whether the business is a specified service business (Form 8995-A), which this engine does not compute.`);
  };

  let deductionUsed: "standard" | "itemized" = "standard";
  let deduction = standardRoute;
  let qbiDed: number | null = null;
  let limitReduction = 0;
  if (itemized !== null && itemized > standardRoute) {
    const tibq = r2(agi - itemized);
    const q = qbiFor(tibq);
    if (q === null) return qbiRefusal(tibq);
    let allowed = itemized;
    if (year === "2026") {
      // The 37% band starts where the 35% band ends on the filing status's schedule.
      const start37 = schedule.value[5][0] as number;
      const tiWithout = agi - itemized - q;
      limitReduction = r2(LIMIT_68_2026.value * Math.min(itemized, Math.max(0, tiWithout + itemized - start37)));
      allowed = r2(itemized - limitReduction);
    }
    if (allowed > standardRoute) {
      deductionUsed = "itemized";
      deduction = allowed;
      qbiDed = q;
    }
  }
  if (deductionUsed === "standard") {
    const tibq = r2(agi - standardRoute);
    const q = qbiFor(tibq);
    if (q === null) return qbiRefusal(tibq);
    qbiDed = q;
  }
  if (limitReduction > 0) {
    consts.push(LIMIT_68_2026);
    steps.push(`Itemized deductions USD ${money(itemized as number)} reduced by 2/37 of the part in the 37% band: USD ${money(limitReduction)}, leaving USD ${money(r2((itemized as number) - limitReduction))}`);
  }
  if (giftsAllowed > 0) consts.push(CASH_GIFTS_2026);
  steps.push(deductionUsed === "itemized"
    ? `Itemized deductions USD ${money(deduction)} are more than the standard deduction USD ${money(standardRoute)}: itemize`
    : `Standard deduction USD ${money(std.value[status])}${giftsAllowed > 0 ? ` plus cash gifts USD ${money(giftsAllowed)} (non-itemizer, 2026)` : ""}${itemized !== null ? `, more than itemized USD ${money(itemized)}` : ""}`);
  const qbiDeductionAmount = qbiDed as number;
  if (qbi > 0) {
    consts.push(QBI_RATE, QBI_DEFINITION, QBI_METHOD, thresholdRule);
    if (used.materially_participates === true && qbiDeductionAmount === QBI_MINIMUM_2026.value.minimum) consts.push(QBI_MINIMUM_2026);
    assumptions.push("The Schedule C business is a qualified trade or business carried on in the United States, and there is no QBI loss carried forward, no REIT dividends and no publicly traded partnership income");
    steps.push(`QBI = net profit USD ${money(profit)} less half SE tax and self-employed retirement and health deductions = USD ${money(qbi)}; QBI deduction (Form 8995, at or below the threshold) = USD ${money(qbiDeductionAmount)}`);
  }
  const ti = r2(Math.max(0, agi - deduction - qbiDeductionAmount));
  steps.push(`Taxable income = AGI USD ${money(agi)} less deduction USD ${money(deduction)} less QBI deduction USD ${money(qbiDeductionAmount)} = USD ${money(ti)}`);
  Object.assign(lines, { standard_deduction: std.value[status], deduction_used: deductionUsed, deduction: r2(deduction), qbi: Math.max(0, qbi), qbi_deduction: r2(qbiDeductionAmount), taxable_income: ti });

  // 4. Tax: rate schedule, with the capital gain worksheet when there are qualified dividends or long-term gains.
  consts.unshift(schedule);
  const cg = pick(year, CG_2026, CG_2025);
  let cgr: CgResult;
  if (ncg > 0) {
    consts.push(cg, CG_STACKING);
    cgr = capitalGainWorksheet(schedule.value, cg.value, status, ti, ncg);
    steps.push(`Ordinary taxable income USD ${money(cgr.ordinaryIncome)} taxed on the ${year} schedule: USD ${money(cgr.ordinaryTax)}`);
    steps.push(`Qualified dividends and long-term gains stacked on top: USD ${money(cgr.at0)} at 0%, USD ${money(cgr.at15)} at 15%, USD ${money(cgr.at20)} at 20% = USD ${money(cgr.preferentialTax)}`);
    if (cgr.tax < r2(cgr.ordinaryTax + cgr.preferentialTax)) steps.push(`Tax on all taxable income at the regular rates is lower (USD ${money(cgr.tax)}), so that is the tax (worksheet line 25)`);
  } else {
    const t = r2(scheduleTax(schedule.value, ti));
    cgr = { ordinaryIncome: ti, at0: 0, at15: 0, at20: 0, ordinaryTax: t, preferentialTax: 0, tax: t };
    steps.push(`Tax on USD ${money(ti)} from the ${year} ${status.replace(/_/g, " ")} schedule = USD ${money(t)}`);
  }
  const incomeTax = cgr.tax;
  Object.assign(lines, {
    ordinary_taxable_income: cgr.ordinaryIncome, ordinary_tax: cgr.ordinaryTax, taxed_at_0: cgr.at0, taxed_at_15: cgr.at15, taxed_at_20: cgr.at20,
    preferential_tax: cgr.preferentialTax, income_tax: incomeTax,
  });

  // 5. AMT: computed nowhere; the return is refused unless the AMT is certainly zero.
  const amt = pick(year, AMT_2026, AMT_2025);
  consts.push(amt, AMT_TOP_RATE, AMT_STEPS);
  const salt = saltGiven ?? itemized ?? 0;
  const amtiUpper = deductionUsed === "itemized" ? agi - ((itemized as number) - salt) : agi;
  const exemption = amt.value.exemption[status];
  const tmtRaw = AMT_TOP_RATE.value * Math.max(0, amtiUpper - exemption);
  const tmtUpper = r2(tmtRaw);
  if (amtiUpper > amt.value.phaseout_start[status] || tmtRaw > incomeTax) {
    return refuse("alternative minimum tax",
      amtiUpper > amt.value.phaseout_start[status]
        ? `Alternative minimum taxable income may be above the ${year} exemption phase-out start (USD ${money(amt.value.phaseout_start[status])}). No OpenAccountants skill serves the AMT rate bands for this case, so the AMT cannot be shown to be zero.`
        : `At most 28% x (USD ${money(amtiUpper)} - exemption USD ${money(exemption)}) = USD ${money(tmtUpper)} of tentative minimum tax, more than the regular tax USD ${money(incomeTax)}, so the AMT cannot be ruled out. No OpenAccountants skill serves the full AMT computation.`);
  }
  steps.push(`AMT is zero: alternative minimum taxable income is at most USD ${money(amtiUpper)}, and even 28% of it above the exemption USD ${money(exemption)} (USD ${money(tmtUpper)}) is not more than the regular tax`);
  lines.alternative_minimum_tax = 0;

  // 6. Child tax credit (non-refundable part only).
  let ctcUsed = 0;
  let ctcUnused = 0;
  const ctc = pick(year, CTC_2026, CTC_2025);
  if (kids > 0) {
    consts.push(ctc, CTC_PHASEOUT_START);
    if (year === "2026") consts.push(CTC_PERMANENT);
    const start = status === "married_filing_jointly" ? CTC_PHASEOUT_START.value.joint : CTC_PHASEOUT_START.value.other;
    if (agi > start) {
      return refuse("child tax credit phase-out above the threshold",
        `AGI USD ${money(agi)} is above the phase-out start of USD ${money(start)}. No OpenAccountants skill states how fast the credit is reduced above it, so the credit is not computed.`);
    }
    const full = kids * ctc.value.per_child;
    ctcUsed = Math.min(full, incomeTax);
    ctcUnused = r2(full - ctcUsed);
    steps.push(`Child tax credit ${kids} x USD ${money(ctc.value.per_child)} = USD ${money(full)} (AGI under USD ${money(start)}); used against tax: USD ${money(ctcUsed)}`);
    if (ctcUnused > 0) {
      notes.push(`USD ${money(ctcUnused)} of the child tax credit is more than the income tax. Up to USD ${money(ctc.value.refundable_per_child)} per child may be refundable as the additional child tax credit (Schedule 8812), which this engine does not compute: no OpenAccountants skill serves its earned-income formula. It is a payment, so it does not change total tax.`);
    }
  }
  Object.assign(lines, { child_tax_credit: r2(ctcUsed), child_tax_credit_unused: ctcUnused, se_tax: seTax });

  // 7. Schedule 2 taxes on higher income.
  const addl = pick(year, ADDL_MEDICARE_2026, ADDL_MEDICARE_2025);
  const mcWages = mcWagesGiven ?? wages;
  used.w2_medicare_wages = mcWages;
  const seIncome = ne >= MINNE.value ? ne : 0;
  const addlTax = additionalMedicare(addl.value.rate, addl.value.threshold[status], mcWages, seIncome);
  if (mcWagesGiven === null && wages > 0) assumptions.push("Medicare wages (W-2 box 5) taken as equal to wages; give w2_medicare_wages if they differ");
  if (addlTax > 0 || mcWages + seIncome > 0) consts.push(addl);
  if (addlTax > 0) steps.push(`Additional Medicare Tax ${pct(addl.value.rate)} on wages USD ${money(mcWages)} and SE income USD ${money(seIncome)} above USD ${money(addl.value.threshold[status])} = USD ${money(addlTax)}`);
  const nii = interest + ordDiv + stGain + ltGain;
  const niit = r2(NIIT.value.rate * Math.min(nii, Math.max(0, agi - NIIT.value.threshold[status])));
  if (nii > 0) {
    consts.push(NIIT, NII_ITEMS);
    if (year === "2025") consts.push(NIIT_2025);
  }
  if (niit > 0) steps.push(`Net investment income tax ${pct(NIIT.value.rate)} x min(net investment income USD ${money(nii)}, AGI over USD ${money(NIIT.value.threshold[status])}) = USD ${money(niit)}`);
  const total = r2(incomeTax - ctcUsed + seTax + addlTax + niit);
  steps.push(`Total tax = income tax USD ${money(incomeTax)} - child tax credit USD ${money(ctcUsed)} + SE tax USD ${money(seTax)} + Additional Medicare USD ${money(addlTax)} + NIIT USD ${money(niit)} = USD ${money(total)}`);
  Object.assign(lines, { additional_medicare_tax: addlTax, net_investment_income_tax: niit, total_tax: total });

  // 8. Estimated tax safe harbour for the same year.
  lines.estimated_tax = null;
  if (priorTax !== null) {
    const priorAgi = priorTax === 0 ? f.number("prior_year_agi", null) : f.number("prior_year_agi");
    used.prior_year_tax = priorTax;
    used.prior_year_agi = priorAgi;
    const sh = pick(year, SH_2026, SH_2025);
    const dates = pick(year, DATES_2026, DATES_2025);
    consts.push(sh, dates, INSTALMENT);
    if (priorTax === 0) consts.push(ZERO_PRIOR_TAX);
    const h = safeHarbour(sh.value, status, total, priorTax, priorAgi);
    let required = h.required;
    if (ctcUnused > 0) {
      // A refundable credit lowers this year's tax for the 90% test; the engine knows only its ceiling.
      const low = r2(sh.value.current * Math.max(0, total - Math.min(ctcUnused, kids * ctc.value.refundable_per_child)));
      if (h.priorAmount > low) {
        return refuse("refundable additional child tax credit (needed for the 90% estimated tax test)",
          "This year's tax for the 90% test is after the refundable additional child tax credit, which no OpenAccountants skill lets this engine compute, and here it could decide which test is lower.");
      }
      required = h.priorAmount;
    }
    const instalment = r2(required * INSTALMENT.value);
    lines.estimated_tax = {
      current_year_tax: total, ninety_percent_of_current_year_tax: h.ninety, prior_year_percentage: h.priorPct, prior_year_amount: h.priorAmount,
      required_annual_payment: required, instalment, due_dates: dates.value,
    };
    steps.push(`Estimated tax: lesser of 90% of USD ${money(total)} (USD ${money(h.ninety)}) and ${h.priorPct === null ? "USD 0.00 (no tax last year)" : `${pct(h.priorPct)} of last year's USD ${money(priorTax)} (USD ${money(h.priorAmount)})`} = USD ${money(required)}; four instalments of USD ${money(instalment)} due ${dates.value.join(", ")}`);
    notes.push("Withholding counts toward the required annual payment. No estimated tax is required if the tax owed after withholding and credits is under USD 1,000.");
    assumptions.push("Last year's return covered 12 months, and less than two-thirds of gross income is from farming or fishing");
  }

  assumptions.push(
    "Federal income tax only: no state or local tax",
    "Nobody on the return is 65 or older or blind, the filer cannot be claimed as a dependent, and there are no Schedule 1-A deductions (tips, overtime, car loan interest, senior deduction)",
    "Taxable income is taxed with the rate schedules. Form 1040 uses the IRS Tax Table below USD 100,000 of taxable income, which can differ by a few dollars",
    "No credits other than the child tax credit (no credit for other dependents, earned income credit, education or energy credits)",
    "No alternative minimum tax adjustments or preference items other than state and local taxes (no incentive stock options, private activity bond interest or depreciation differences)",
    "Modified AGI equals AGI (no foreign earned income or possessions exclusion)",
  );
  if (status === "married_filing_separately") assumptions.push("The spouse does not itemize (if they do, this return must itemize too)");

  return ok(
    spec.name,
    { label: `US federal total tax ${year} (Form 1040 line 24)`, value: total, currency: "USD" },
    lines,
    steps,
    consts,
    used,
    { assumptions, anchors, notes },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
