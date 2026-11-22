// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's FBT car calculator (ryanduguid.github.io, assets/business-calculators.mjs, fbtCar).
// Pure, offline calculation. No clock, network, floating-point money or rate overrides.
import rules from "./rules.json" with { type: "json" };

const msPerDay = 86400000;
const moneyPattern = /^(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const datePattern = /^(\d{4})-(\d{2})-(\d{2})$/;
const methods = new Set(["statutory", "operating_cost"]);

function cents(value) {
  if (typeof value !== "string" || value.length > 18) return null;
  const match = moneyPattern.exec(value);
  return match ? BigInt(match[1]) * 100n + BigInt((match[2] ?? "").padEnd(2, "0")) : null;
}

function dayNumber(value) {
  const match = typeof value === "string" ? datePattern.exec(value) : null;
  if (!match) return null;
  const day = Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])) / msPerDay;
  return new Date(day * msPerDay).toISOString().slice(0, 10) === value ? day : null;
}

const count = (value) => (Number.isSafeInteger(value) && value >= 0 ? value : null);
const decimal2 = (hundredths) => `${hundredths / 100n}.${String(hundredths % 100n).padStart(2, "0")}`;

// numerator / denominator cents less the payment, nil if not positive, as a numerator over the same denominator.
function net(numerator, denominator, payment) {
  const excess = numerator - payment * denominator;
  return excess <= 0n ? 0n : excess;
}

// numerator / denominator cents rounded half up to the cent.
const roundCents = (numerator, denominator) => (2n * numerator + denominator) / (2n * denominator);

// ss 10A and 10B: true or false when every condition the reduction needs is stated, otherwise null.
function businessUseEntitled(input) {
  const conditions = ["odometerRecordsMaintained"];
  if (input.logBookYear === true) conditions.push("logBookRecordsMaintained");
  if (input.providerIsEmployer === false) conditions.push("recordsGivenBeforeDeclarationDate");
  const stated = [...conditions, "logBookYear", "providerIsEmployer"].every((key) => typeof input[key] === "boolean");
  return stated ? conditions.every((key) => input[key]) : null;
}

/**
 * @param {object} input
 * @param {number} input.fbtYear FBT year by its ending 31 March, e.g. 2027.
 * @param {"statutory"|"operating_cost"} input.method "operating_cost" when the employer elects s 10.
 * @param {boolean} input.commitmentBefore10May2011 The last commitment by the employer, the employee or an
 *   associate to the car's application or availability for the period was made before 7.30 pm AEST on
 *   10 May 2011 (Tax Laws Amendment (2011 Measures No. 5) Act 2011, Sch 5 item 8(2)); true is refused.
 * @param {string} input.carValue AUD decimal: cost price if the provider or an associate owned the car at
 *   the earliest holding time, otherwise its leased car value at that time.
 * @param {string} input.earliestHoldingDate "YYYY-MM-DD": the provider or an associate first held the car.
 * @param {string} input.laterAccessoriesCost AUD decimal: non-business accessories under s 9(2)(a)(iii); "0" if none.
 * @param {number} input.privateUseDays Days in the year on which car fringe benefits were provided.
 * @param {string} input.recipientsPayment AUD decimal under ss 9(2)(e) and 10(3)(c); "0" if none.
 * @param {string} [input.operatingCost] AUD decimal, s 10(3)(a); required for "operating_cost".
 * @param {number} [input.businessKilometres] Estimated business kilometres in the holding period (s 162F).
 * @param {number} [input.totalKilometres] Total kilometres in the holding period.
 * @param {boolean} [input.logBookYear] Required with business kilometres, as are the next 2.
 * @param {boolean} [input.odometerRecordsMaintained] Odometer records were maintained for the holding period.
 * @param {boolean} [input.providerIsEmployer] The employer held the car.
 * @param {boolean} [input.logBookRecordsMaintained] Required in a log book year (s 10A(a)).
 * @param {boolean} [input.recordsGivenBeforeDeclarationDate] Required where the provider is not the employer.
 * @returns {object} JSON-safe result; money is AUD decimal strings or null.
 */
export function assessCarFringeBenefit(input) {
  const base = {
    as_of: rules.as_of,
    sources: [...rules.sources],
    limits: [...rules.limits],
    rounding: rules.rounding,
    fbtYear: null,
    method: null,
    baseValue: null,
    statutoryValue: null,
    operatingCostValue: null,
    businessUsePercentage: null,
    taxableValue: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  if (!Number.isInteger(input.fbtYear) || !Object.hasOwn(rules.years, String(input.fbtYear))) {
    return stop("refused", "unsupported_year", `Covered FBT years end 31 March ${Object.keys(rules.years).join(", ")}; no figure is assumed for another year.`);
  }
  const year = rules.years[String(input.fbtYear)];
  if (!methods.has(input.method)) return stop("unknown", "method", "method must be statutory or operating_cost.");
  if (input.commitmentBefore10May2011 !== false) {
    return input.commitmentBefore10May2011 === true
      ? stop("refused", "pre_2011_commitment", "A commitment made before 7.30 pm AEST on 10 May 2011 keeps statutory percentages this calculator does not apply.")
      : stop("unknown", "pre_2011_commitment", "State commitmentBefore10May2011 as true or false.");
  }
  const value = cents(input.carValue);
  const accessories = cents(input.laterAccessoriesCost);
  const payment = cents(input.recipientsPayment);
  if (value === null || accessories === null || payment === null || value === 0n) {
    return stop("unknown", "invalid_money", "Supply carValue above nil, and laterAccessoriesCost and recipientsPayment, as AUD decimal strings with at most 2 decimal places; missing is not zero.");
  }
  const held = dayNumber(input.earliestHoldingDate);
  if (held === null) return stop("unknown", "earliest_holding_date", "Supply earliestHoldingDate as YYYY-MM-DD.");
  const [start, end] = [dayNumber(year.start), dayNumber(year.end)];
  if (held > end) return stop("refused", "not_held_in_year", `The car was first held after ${year.end}, the end of the FBT year.`);
  const days = count(input.privateUseDays);
  const heldDays = end - Math.max(start, held) + 1;
  if (days === null || days > heldDays) {
    return stop("unknown", "private_use_days", `privateUseDays must be a whole number from 0 to ${heldDays}, the days from ${start >= held ? year.start : input.earliestHoldingDate} to ${year.end}.`);
  }

  const reason_codes = ["caller_attested_inputs"];
  const reasons = ["Every input is caller-supplied; this calculator has not verified them, nor whether a car benefit arises or is exempt."];
  const add = (code, reason) => {
    reason_codes.push(code);
    reasons.push(reason);
  };
  // s 9(2)(a): the base value in units of 1/denominator cent, so 2/3 of a cost price stays exact.
  const [y, m, d] = input.earliestHoldingDate.split("-").map(Number);
  const reduced = start > Date.UTC(y + 4, m - 1, d) / msPerDay;
  const { numerator, denominator } = rules.statutory_formula.reduction;
  const share = reduced ? BigInt(numerator) : BigInt(denominator);
  const baseValue = value * share + accessories * BigInt(denominator);
  if (reduced) add("base_value_reduced", "The year begins after the fourth anniversary of the earliest holding time, so the cost price or leased car value is reduced by one-third (s 9(2)(a)).");
  const statutoryDenominator = BigInt(denominator) * 100n * BigInt(year.days);
  const statutory = net(baseValue * BigInt(rules.statutory_formula.percent) * BigInt(days), statutoryDenominator, payment);

  let operating = null;
  let operatingDenominator = 1n;
  let businessUse = null;
  if (input.method === "operating_cost") {
    const cost = cents(input.operatingCost);
    if (cost === null || cost === 0n) {
      return stop("unknown", "operating_cost", "Supply operatingCost above nil as an AUD decimal string; it includes deemed depreciation and interest or lease charges, so nil means they were left out.");
    }
    const [business, total] = [count(input.businessKilometres), count(input.totalKilometres)];
    if (business === null || total === null || business > total) {
      return stop("unknown", "kilometres", "Supply businessKilometres and totalKilometres as whole numbers, business no more than total.");
    }
    const entitled = business === 0 ? false : businessUseEntitled(input);
    if (entitled === null) {
      return stop("unknown", "business_use_records", "For a business use reduction, state logBookYear, odometerRecordsMaintained and providerIsEmployer, plus logBookRecordsMaintained in a log book year and recordsGivenBeforeDeclarationDate where the provider is not the employer, each as true or false.");
    }
    if (business > 0 && !entitled) add("no_business_use_reduction", "The records ss 10A and 10B require are not all held, so the business use percentage is nil.");
    const [privateKm, allKm] = entitled ? [total - business, total] : [1, 1];
    businessUse = entitled ? (BigInt(business) * 20000n + BigInt(total)) / (2n * BigInt(total)) : 0n;
    operatingDenominator = BigInt(allKm);
    operating = net(cost * BigInt(privateKm), operatingDenominator, payment);
  }
  // s 10(5) compares the exact values, before rounding to the cent.
  const lowerStatutory = operating !== null && operating * statutoryDenominator > statutory * operatingDenominator;
  const method = operating === null || lowerStatutory ? "statutory" : "operating_cost";
  if (lowerStatutory) add("statutory_lower", "The operating cost value exceeds the statutory formula value, so the election is treated as not made (s 10(5)).");
  add(method, method === "statutory" ? "Valued by the statutory formula (s 9)." : "Valued by the operating cost method (s 10).");
  return {
    ...base,
    verdict: "taxable_value_calculated",
    reason_codes,
    reasons,
    fbtYear: input.fbtYear,
    method,
    baseValue: decimal2(roundCents(baseValue, BigInt(denominator))),
    statutoryValue: decimal2(roundCents(statutory, statutoryDenominator)),
    operatingCostValue: operating === null ? null : decimal2(roundCents(operating, operatingDenominator)),
    businessUsePercentage: businessUse === null ? null : decimal2(businessUse),
    taxableValue: decimal2(method === "statutory" ? roundCents(statutory, statutoryDenominator) : roundCents(operating, operatingDenominator)),
  };
}
