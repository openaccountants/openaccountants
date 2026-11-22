// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's division-293 and income-tests worksheets in australian-tax-calculators:
// https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators
// Pure, offline calculation. No clock, network, floating-point money or threshold overrides.
import rules from "./rules.json" with { type: "json" };

const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;

// A non-negative AUD decimal string in cents, otherwise null.
function cents(value) {
  if (typeof value !== "string") return null;
  const match = moneyPattern.exec(value);
  return match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

const formatMoney = (value) => `${value / 100n}.${String(value % 100n).padStart(2, "0")}`;
const positive = (value) => (value > 0n ? value : 0n);

// The amounts supplied, in cents; each is required and "0" when there is none.
const amounts = [
  "taxableIncomeForSurchargePurposes",
  "reportableFringeBenefitsTotal",
  "netFinancialInvestmentLoss",
  "netRentalPropertyLoss",
  "lowTaxContributedAmounts",
  "excessConcessionalContributions",
];

// Each flag that puts the case outside Subdivision 293-B alone: its reason code and why.
const exclusions = [
  ["definedBenefitInterest", "defined_benefit_interest", "A defined benefit interest changes the low tax contributions (ITAA 1997 Subdivision 293-D); this calculator does not cover it."],
  ["constitutionallyProtectedFund", "constitutionally_protected_fund", "An interest in a constitutionally protected fund can change or remove the tax (ITAA 1997 Subdivision 293-E and Imposition Act 2013 s 6); this calculator does not cover it."],
  ["stateHigherLevelOfficeHolder", "state_higher_level_office_holder", "A State higher level office holder may be outside Division 293 tax under Imposition Act 2013 s 6, and Subdivision 293-E changes the tax for one with a constitutionally protected fund interest; this calculator does not cover them."],
  ["commonwealthJustice", "commonwealth_justice", "A justice or judge in ITAA 1997 s 293-190 has modified defined benefit contributions and threshold (Subdivision 293-F); this calculator does not cover it."],
  ["departingAustraliaSuperannuationPayment", "departing_australia_payment", "A departing Australia superannuation payment can bring a refund that stops all Division 293 tax liabilities (ITAA 1997 ss 293-230 and 293-240); this calculator does not cover it."],
];

const outcomes = {
  liable: "Liable under ITAA 1997 s 293-15: Division 293 income and low tax contributions together exceed $250,000.",
  not_above_threshold: "Not liable: Division 293 income and low tax contributions together do not exceed $250,000 (ITAA 1997 s 293-20(1)).",
  no_low_tax_contributions: "Not liable: the low tax contributions are nil (ITAA 1997 s 293-20(2)).",
};

/**
 * @param {object} input
 * @param {string} input.incomeYear A supported income year, e.g. "2026-27".
 * @param {string} input.taxableIncomeForSurchargePurposes s 995-1 'income for surcharge purposes' (a): taxable income
 *   worked out disregarding the assessable FHSS released amount and ITAA 1936 Sch 2F s 271-105(1).
 * @param {string} input.reportableFringeBenefitsTotal FBTAA s 135N.
 * @param {string} input.netFinancialInvestmentLoss s 995-1 'total net investment loss' (a).
 * @param {string} input.netRentalPropertyLoss s 995-1 'total net investment loss' (b).
 * @param {string} input.lowTaxContributedAmounts s 293-30.
 * @param {string} input.excessConcessionalContributions s 291-20(1).
 * @param {boolean} input.definedBenefitInterest true is refused.
 * @param {boolean} input.constitutionallyProtectedFund true is refused.
 * @param {boolean} input.stateHigherLevelOfficeHolder Of a kind declared for Subdivision 293-E; true is refused.
 * @param {boolean} input.commonwealthJustice true is refused.
 * @param {boolean} input.departingAustraliaSuperannuationPayment true is refused.
 * @returns {object} JSON-safe estimate; money is decimal strings or null.
 */
export function estimateDivision293(input) {
  const base = {
    as_of: rules.as_of,
    currency: rules.currency,
    sources: [...rules.sources],
    limits: [...rules.limits],
    rounding: rules.rounding,
    incomeYear: null,
    liable: null,
    division293Income: null,
    lowTaxContributions: null,
    combinedAmount: null,
    excessOverThreshold: null,
    taxableContributions: null,
    division293TaxEstimate: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  if (!rules.supported_years.includes(input.incomeYear)) {
    return stop("refused", "unsupported_year", `Select one of ${rules.supported_years.join(", ")}; the law for another year has not been checked.`);
  }
  for (const [key, code, reason] of exclusions) {
    if (input[key] === true) return stop("refused", code, reason);
    if (input[key] !== false) return stop("unknown", code, `State ${key} as true or false.`);
  }
  const value = Object.fromEntries(amounts.map((key) => [key, cents(input[key])]));
  if (Object.values(value).includes(null)) {
    return stop("unknown", "invalid_money", `Supply ${amounts.join(", ")} as non-negative AUD decimal strings with at most 2 decimal places; "0" when there is none, as missing is not zero.`);
  }
  if (value.excessConcessionalContributions > value.lowTaxContributedAmounts) {
    return stop("unknown", "components_inconsistent", "The excess concessional contributions exceed the low tax contributed amounts, so ITAA 1997 s 293-25 gives a negative amount, which this calculator does not work with; check both.");
  }

  // s 995-1 'income for surcharge purposes' (a), (b) and (d). Its s 301-20(3) reduction is nil from 2024-25:
  // nobody is then both under 60 and at preservation age (SISR reg 6.01(2)), as s 301-20(1) requires.
  const income = value.taxableIncomeForSurchargePurposes + value.reportableFringeBenefitsTotal
    + value.netFinancialInvestmentLoss + value.netRentalPropertyLoss;
  const contributions = value.lowTaxContributedAmounts - value.excessConcessionalContributions;
  const combined = income + contributions;
  const excess = positive(combined - BigInt(rules.threshold) * 100n);
  const taxable = contributions < excess ? contributions : excess;
  // Cents times a whole-percent rate are hundredths of a cent: round half away from zero (taxable is not negative).
  const tax = (2n * taxable * BigInt(rules.rate_percent) + 100n) / 200n;
  const code = contributions === 0n ? "no_low_tax_contributions" : excess === 0n ? "not_above_threshold" : "liable";
  return {
    ...base,
    verdict: "estimate_calculated",
    reason_codes: ["caller_supplied_inputs", code],
    reasons: [
      "Every amount and answer is caller-supplied; this calculator has not verified them. The ATO assesses the tax from the tax return and what funds report.",
      outcomes[code],
    ],
    incomeYear: input.incomeYear,
    liable: code === "liable",
    division293Income: formatMoney(income),
    lowTaxContributions: formatMoney(contributions),
    combinedAmount: formatMoney(combined),
    excessOverThreshold: formatMoney(excess),
    taxableContributions: formatMoney(taxable),
    division293TaxEstimate: formatMoney(tax),
  };
}
