// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's div7a-loan-review calculation contract:
// https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review
// Pure, offline calculation. No clock, network, floating-point money or rate overrides.
import rules from "./rules.json" with { type: "json" };

const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const termPattern = /^(0|[1-9]\d?)(?:\.(\d{1,6}))?$/;

function cents(value) {
  if (typeof value !== "string" || value.length > 18) return null;
  const match = moneyPattern.exec(value);
  return match && match[0] === value ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

function termYears(value) {
  if (typeof value !== "string" || value.length > 9) return null;
  const match = termPattern.exec(value);
  if (!match || match[0] !== value) return null;
  const scaled = BigInt(match[1]) * 1000000n + BigInt((match[2] ?? "").padEnd(6, "0"));
  if (scaled <= 0n || scaled > 25000000n) return null;
  return Number((scaled + 999999n) / 1000000n);
}

function yearStart(value) {
  if (typeof value !== "string" || value.length !== 7 || !/^\d{4}-\d{2}$/.test(value)) return null;
  const start = Number(value.slice(0, 4));
  return value.slice(5) === String((start + 1) % 100).padStart(2, "0") ? start : null;
}

const formatMoney = (value) => `${value / 100n}.${String(value % 100n).padStart(2, "0")}`;

/**
 * @param {object} input
 * @param {string} input.incomeYear Supported year, e.g. "2026-27".
 * @param {string} input.loanIncomeYear Year this amalgamated loan was made; must be earlier.
 * @param {true} input.standardIncomeYear Confirms a 30 June income year.
 * @param {"complying_amalgamated"|"not_complying"|"unknown"} input.loanStatus
 *   Caller-reviewed existing s 109N/amalgamated loan, without refinancing or term adjustments.
 * @param {true} input.repaymentsReviewed Confirms the supplied amount was checked under s 109R.
 * @param {string} input.openingBalance Statutory previous-year outstanding amount, AUD decimal.
 * @param {string} input.remainingTermYears Actual-term-minus-elapsed-years under s 109E(6).
 * @param {string} input.eligibleRepayments AUD decimal; explicit "0" is valid, missing is unknown.
 * @returns {object} JSON-safe review result; all monetary results are decimal strings or null.
 */
export function assessDiv7aRepayment(input) {
  const base = {
    as_of: rules.as_of,
    currency: rules.currency,
    sources: [...rules.sources],
    limits: [...rules.limits],
    rounding: rules.rounding,
    benchmarkRatePercent: null,
    openingBalance: null,
    remainingTermYearsSupplied: null,
    remainingTermYearsUsed: null,
    minimumYearlyRepaymentEstimate: null,
    repaymentTarget: null,
    eligibleRepayments: null,
    shortfall: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const currentYear = yearStart(input.incomeYear);
  if (currentYear === null || !Object.hasOwn(rules.benchmark_rates, input.incomeYear)) {
    return stop("refused", "unsupported_year", "Select a supported income year; no benchmark is assumed for another year.");
  }
  const rate = rules.benchmark_rates[input.incomeYear];
  if (input.standardIncomeYear !== true) {
    return stop(input.standardIncomeYear === false ? "refused" : "unknown", "income_year_basis", "A confirmed 30 June income year is required; substituted periods are outside scope.");
  }
  if (input.loanStatus !== "complying_amalgamated") {
    return stop(input.loanStatus === "not_complying" ? "refused" : "unknown", "loan_status", "Establish an existing complying amalgamated loan and review any refinancing or term changes first.");
  }
  const loanYear = yearStart(input.loanIncomeYear);
  if (loanYear === null) return stop("unknown", "loan_year_missing", "Supply the income year in which the amalgamated loan was made.");
  if (loanYear >= currentYear) return stop("refused", "not_later_year", "The minimum yearly repayment applies to a loan made in an earlier income year.");
  if (input.repaymentsReviewed !== true) {
    return stop("unknown", "repayments_not_reviewed", "Establish eligible repayments under s 109R, including its exceptions; a bank payment alone is insufficient.");
  }
  const opening = cents(input.openingBalance);
  const repayments = cents(input.eligibleRepayments);
  const term = termYears(input.remainingTermYears);
  if (opening === null || repayments === null) {
    return stop("unknown", "invalid_money", "Supply non-negative AUD decimal strings, at most 15 whole digits and 2 decimal places; missing is not zero.");
  }
  if (term === null || term + (currentYear - loanYear - 1) > 25) {
    return stop("refused", "invalid_term", "Supply a positive remaining term consistent with the actual constituent-loan terms, chronology and maximum 25-year scope.");
  }

  // Exact equivalent of P*r / (1 - (1/(1+r))**n), expressed in cents.
  const r = BigInt(rate.basis_points);
  const d = 10000n;
  const growth = (d + r) ** BigInt(term);
  const numerator = opening * r * growth;
  const denominator = d * (growth - d ** BigInt(term));
  const estimate = (2n * numerator + denominator) / (2n * denominator);
  const target = (numerator + denominator - 1n) / denominator;
  const shortfall = target > repayments ? target - repayments : 0n;
  return {
    ...base,
    verdict: shortfall > 0n ? "shortfall_indicated" : "no_shortfall_indicated",
    reason_codes: ["caller_attested_inputs", shortfall > 0n ? "repayment_shortfall" : "repayments_cover_formula"],
    reasons: [
      "Loan compliance, balance, remaining term and repayment eligibility are caller-attested; this calculator has not verified them.",
      shortfall > 0n ? "Eligible repayments are below the formula amount; review the shortfall and separate dividend conditions." : "Supplied eligible repayments cover the formula amount; this does not establish overall Division 7A compliance.",
    ],
    benchmarkRatePercent: rate.percent,
    openingBalance: formatMoney(opening),
    remainingTermYearsSupplied: input.remainingTermYears,
    remainingTermYearsUsed: term,
    minimumYearlyRepaymentEstimate: formatMoney(estimate),
    repaymentTarget: formatMoney(target),
    eligibleRepayments: formatMoney(repayments),
    shortfall: formatMoney(shortfall),
  };
}
