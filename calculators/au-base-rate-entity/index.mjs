// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's company tax module (ryanduguid.github.io, assets/company-tax.mjs at
// 4b7cfc9790b5914dfd77b40b7a704ff80f85f2c4).
// Pure, offline calculation. No clock, network, floating-point money or rate overrides.
import rules from "./rules.json" with { type: "json" };

const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const figures = ["aggregatedTurnover", "assessableIncome", "baseRateEntityPassiveIncome"];

function cents(value) {
  if (typeof value !== "string" || value.length > 18) return null;
  const match = moneyPattern.exec(value);
  return match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

function yearStart(value) {
  if (typeof value !== "string" || !/^\d{4}-\d{2}$/.test(value)) return null;
  const start = Number(value.slice(0, 4));
  return value.slice(5) === String((start + 1) % 100).padStart(2, "0") ? start : null;
}

const threshold = cents(rules.base_rate_entity.turnover_threshold);
const passiveLimit = BigInt(rules.base_rate_entity.passive_income_limit_percent);
const firstYear = yearStart(rules.income_years.first);
const lastYear = yearStart(rules.income_years.last);
const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));

// One year's figures in cents, or the reason they cannot be used.
function readFigures(record, label) {
  const values = figures.map((key) => cents(record[key]));
  const missing = values.indexOf(null);
  if (missing >= 0) {
    return { code: "figures", reason: `Supply ${label} ${figures[missing]} as dollars with up to 2 decimal places, such as "1250000.00".` };
  }
  const [turnover, assessable, passive] = values;
  if (passive > assessable) {
    return { code: "passive_exceeds_assessable", reason: `Base rate entity passive income cannot exceed assessable income (${label} figures).` };
  }
  return { turnover, assessable, passive };
}

// Income Tax Rates Act 1986 s 23AA: paragraph (a) passive income, paragraph (b) aggregated turnover.
function baseRateTest({ turnover, assessable, passive }) {
  const passiveIncome = passive * 100n <= passiveLimit * assessable;
  const aggregatedTurnover = turnover < threshold;
  return { baseRateEntity: passiveIncome && aggregatedTurnover, limbs: { passiveIncome, aggregatedTurnover } };
}

// s 23(2) for the tax rate; s 995-1 'corporate tax rate' for the imputation rate.
const ratePercent = (baseRateEntity) => (baseRateEntity ? rules.rates.base_rate_entity_percent : rules.rates.other_percent);

// s 202-60(2): 1 over the gross-up rate (100% - rate) / rate, that is rate / (100 - rate), in lowest terms.
function maximumFrankingCredit(rate) {
  const divisor = gcd(rate, 100 - rate);
  return { numerator: rate / divisor, denominator: (100 - rate) / divisor };
}

/**
 * @param {object} input
 * @param {string} input.incomeYear "YYYY-YY", 2021-22 to 2026-27.
 * @param {"company"} input.entityType Caller-attested: a company, not acting as a trustee, to which
 *   only s 23(2) applies. The refused types in rules.json are refused by name.
 * @param {string} input.aggregatedTurnover This year's aggregated turnover (ITAA 1997 s 328-115), dollars.
 * @param {string} input.assessableIncome This year's assessable income, dollars.
 * @param {string} input.baseRateEntityPassiveIncome This year's base rate entity passive income (s 23AB), dollars.
 * @param {{existed: boolean, aggregatedTurnover?: string, assessableIncome?: string,
 *   baseRateEntityPassiveIncome?: string}} [input.previousYear] For the corporate tax rate for imputation
 *   purposes: whether the company existed in the previous income year and, if it did, that year's figures.
 * @returns {object} JSON-safe result; rates are whole percentages or null.
 */
export function assessBaseRateEntity(input) {
  const base = {
    as_of: rules.as_of,
    income_years: { first: rules.income_years.first, last: rules.income_years.last },
    sources: [...rules.sources],
    limits: [...rules.limits],
    incomeYear: null,
    baseRateEntity: null,
    limbs: null,
    companyTaxRatePercent: null,
    imputation: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const start = yearStart(input.incomeYear);
  if (start === null) return stop("unknown", "income_year", "Supply the income year as YYYY-YY, such as \"2026-27\".");
  if (start < firstYear) return stop("refused", "earlier_income_year", rules.income_years.earlier);
  if (start > lastYear) return stop("refused", "later_income_year", rules.income_years.later);
  const refusedType = Object.hasOwn(rules.entity_types.refused, input.entityType) ? rules.entity_types.refused[input.entityType] : null;
  if (refusedType) return stop("refused", "entity_type_refused", refusedType);
  if (input.entityType !== "company") {
    return stop("unknown", "entity_type", `entityType must be company, or one of the refused types: ${Object.keys(rules.entity_types.refused).join(", ")}.`);
  }
  const current = readFigures(input, "this year's");
  if (current.code) return stop("unknown", current.code, current.reason);

  const reason_codes = ["caller_established_figures"];
  const reasons = ["The figures and the entity type are caller-established; this calculator has not verified them."];
  const add = (code, reason) => {
    reason_codes.push(code);
    reasons.push(reason);
  };
  const year = baseRateTest(current);
  if (year.baseRateEntity) add("base_rate_entity", "Both limbs of s 23AA are met: the 25% rate applies (s 23(2)(a)).");
  if (!year.limbs.passiveIncome) add("passive_income_over_80_percent", "Base rate entity passive income is more than 80% of assessable income (s 23AA(a)): the 30% rate applies.");
  if (!year.limbs.aggregatedTurnover) add("turnover_not_under_threshold", "Aggregated turnover is not less than $50 million (s 23AA(b)): the 30% rate applies.");

  let imputation = null;
  const previous = input.previousYear;
  if (previous === undefined) {
    add("previous_year_not_supplied", "No previous-year inputs, so no corporate tax rate for imputation purposes: it is never taken from this year's result.");
  } else {
    if (!previous || typeof previous !== "object" || Array.isArray(previous) || typeof previous.existed !== "boolean") {
      return stop("unknown", "previous_year", "previousYear must state existed as true or false, or be omitted.");
    }
    if (!previous.existed && figures.some((key) => previous[key] !== undefined)) {
      return stop("unknown", "previous_year", "A company that did not exist in the previous income year has no figures for it; omit them.");
    }
    let before = null;
    if (previous.existed) {
      const figuresBefore = readFigures(previous, "the previous year's");
      if (figuresBefore.code) return stop("unknown", `previous_year_${figuresBefore.code}`, figuresBefore.reason);
      before = baseRateTest(figuresBefore);
    }
    const rate = before ? ratePercent(before.baseRateEntity) : rules.rates.base_rate_entity_percent;
    imputation = {
      basis: before ? "previous_year_figures" : "did_not_exist",
      limbs: before ? before.limbs : null,
      corporateTaxRateForImputationPurposesPercent: rate,
      maximumFrankingCredit: maximumFrankingCredit(rate),
    };
    add(`imputation_${imputation.basis}`, before
      ? "The corporate tax rate for imputation purposes applies s 23AA to the previous year's figures (s 995-1)."
      : "The company did not exist in the previous income year, so it franks at the s 23(2)(a) rate (s 995-1).");
  }
  return {
    ...base,
    verdict: "rate_calculated",
    reason_codes,
    reasons,
    incomeYear: input.incomeYear,
    baseRateEntity: year.baseRateEntity,
    limbs: year.limbs,
    companyTaxRatePercent: ratePercent(year.baseRateEntity),
    imputation,
  };
}
