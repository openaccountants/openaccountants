// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's Division 296 tax calculator on ryanduguid.github.io:
// https://github.com/ryanduguid/ryanduguid.github.io/blob/main/assets/division-296.mjs
// Pure, offline calculation. No clock, network, floating-point money or threshold overrides.
import rules from "./rules.json" with { type: "json" };

const moneyPattern = /^(-?)(0|[1-9]\d{0,14})(?:\.(\d{1,2}))?$/;
const exceptions = [
  ["childRecipient", "child_recipient", "Not liable: a child recipient of a superannuation income stream at any time in the year (ITAA 1997 s 296-20)."],
  ["structuredSettlementContribution", "structured_settlement_contribution", "Not liable: a structured settlement contribution was made for the person in 2026-27 or an earlier year (ITAA 1997 s 296-25)."],
  ["diedOnOrBeforeYearEnd", "died_on_or_before_year_end", "Not liable: the person died on or before 30 June 2027 (ITTPA 1997 s 296-1(3)); the balance is also nil after death (ITAA 1997 s 296-50)."],
];
const outcomes = {
  balance_not_above_threshold: "Not liable: the balance at 30 June 2027 is not greater than the large superannuation balance threshold (ITAA 1997 s 296-40(1)(a)).",
  earnings_not_above_nil: "Not liable: total superannuation earnings are not greater than nil (ITAA 1997 s 296-40(1)(b)).",
  share_rounds_to_nil: "Liable under ITAA 1997 s 296-15, but the share above the large threshold rounds to 0.00% under s 296-40(3), so the tax is nil.",
  liable: "Liable under ITAA 1997 s 296-15: the balance at 30 June 2027 is greater than the large superannuation balance threshold and total superannuation earnings are greater than nil.",
};

// Cents for an AUD decimal string with at most 15 whole digits and 2 decimal places, otherwise null.
function cents(value, allowNegative) {
  if (typeof value !== "string") return null;
  const match = moneyPattern.exec(value);
  if (!match || (match[1] && !allowNegative)) return null;
  const amount = BigInt(match[2]) * 100n + BigInt((match[3] ?? "").padEnd(2, "0"));
  return match[1] ? -amount : amount;
}

// ss 296-40(2), (3) and 296-45(2), (3): the share of the balance above the threshold, in hundredths of
// 1%, rounded up from a third decimal place of 5; nil when the balance is not greater than the threshold.
const shareAbove = (balance, threshold) =>
  balance > threshold ? (2n * (balance - threshold) * 10000n + balance) / (2n * balance) : 0n;

// value / scale hundredths, rounded half away from zero.
function round(value, scale = 1n) {
  const magnitude = value < 0n ? -value : value;
  const rounded = (2n * magnitude + scale) / (2n * scale);
  return value < 0n ? -rounded : rounded;
}

// value / scale hundredths, rounded half away from zero, as a decimal string with 2 places.
function decimal(value, scale = 1n) {
  const rounded = round(value, scale);
  const magnitude = rounded < 0n ? -rounded : rounded;
  return `${rounded < 0n ? "-" : ""}${magnitude / 100n}.${String(magnitude % 100n).padStart(2, "0")}`;
}

/**
 * @param {object} input
 * @param {string} input.incomeYear Supported year: "2026-27".
 * @param {string} input.totalSuperBalanceAtYearEnd Total superannuation balance at 30 June 2027 with
 *   LRBA amounts left out (s 296-260), AUD decimal string, caller-attested.
 * @param {string} input.totalSuperEarnings Total superannuation earnings for the year, AUD decimal
 *   string that may be negative, caller-attested.
 * @param {boolean} input.protectedOfficeOrFund At any time in the year: an interest in, or a death
 *   benefit income stream from, a constitutionally protected fund; an office or death benefit in
 *   s 296-55(3) items 2 to 5; or a State higher level office, held now or before. True is refused.
 *   Caller-attested.
 * @param {boolean} input.childRecipient s 296-20, caller-attested.
 * @param {boolean} input.structuredSettlementContribution s 296-25, caller-attested.
 * @param {boolean} input.diedOnOrBeforeYearEnd ITTPA s 296-1(3), caller-attested.
 * @returns {object} JSON-safe estimate; shares and money are decimal strings or null.
 */
export function estimateDivision296(input) {
  const base = {
    as_of: rules.as_of,
    currency: rules.currency,
    sources: [...rules.sources],
    limits: [...rules.limits],
    rounding: rules.rounding,
    incomeYear: null,
    liable: null,
    largeBalanceSharePercent: null,
    veryLargeBalanceSharePercent: null,
    taxableSuperannuationEarnings: null,
    veryLargeBalanceEarningsComponent: null,
    taxOnTaxableEarnings: null,
    taxOnVeryLargeComponent: null,
    division296TaxEstimate: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  if (typeof input.incomeYear !== "string" || !Object.hasOwn(rules.years, input.incomeYear)) {
    return stop("refused", "unsupported_year", "Only 2026-27 is supported; later thresholds are indexed and not yet published.");
  }
  const year = rules.years[input.incomeYear];
  const balance = cents(input.totalSuperBalanceAtYearEnd, false);
  const earnings = cents(input.totalSuperEarnings, true);
  if (balance === null || earnings === null) {
    return stop("unknown", "invalid_money", "Supply the balance as a non-negative and the earnings as a signed AUD decimal string, at most 15 whole digits and 2 decimal places.");
  }
  if (typeof input.protectedOfficeOrFund !== "boolean" || exceptions.some(([key]) => typeof input[key] !== "boolean")) {
    return stop("unknown", "exception_unanswered", "Answer each question with true or false: protectedOfficeOrFund, childRecipient, structuredSettlementContribution and diedOnOrBeforeYearEnd.");
  }
  if (input.protectedOfficeOrFund) {
    return stop("refused", "protected_office_or_fund", "Not covered: for a constitutionally protected fund member, a judge in ITAA 1997 s 296-55(3), a State higher level office holder or a death beneficiary of one, s 296-55(3) and Imposition Act s 6 can reduce or remove the tax. Obtain professional advice.");
  }

  const reference = input.diedOnOrBeforeYearEnd ? 0n : balance;
  const large = BigInt(year.large_threshold) * 100n;
  const share = shareAbove(reference, large);
  const veryLargeShare = shareAbove(reference, BigInt(year.very_large_threshold) * 100n);
  const hasTaxableEarnings = reference > large && earnings > 0n;
  // Cents times hundredths of 1% are cents / 10000; times a whole-percent rate, cents / 1000000.
  const taxable = hasTaxableEarnings ? earnings * share : 0n;
  const component = earnings * veryLargeShare;
  const exception = exceptions.find(([key]) => input[key]);
  let code;
  if (exception) code = exception[1];
  else if (reference <= large) code = "balance_not_above_threshold";
  else if (earnings <= 0n) code = "earnings_not_above_nil";
  else code = share === 0n ? "share_rounds_to_nil" : "liable";
  const liable = code === "liable" || code === "share_rounds_to_nil";
  // When liable the earnings are positive, so the very large component is not negative.
  // Each tax amount is rounded to the cent and the total is their sum, so the parts shown add up.
  const tax = liable ? round(taxable * BigInt(rules.rates.taxable_superannuation_earnings_percent), 1000000n) : 0n;
  const veryLargeTax = liable ? round(component * BigInt(rules.rates.very_large_component_percent), 1000000n) : 0n;
  return {
    ...base,
    verdict: "estimate_calculated",
    reason_codes: ["caller_attested_inputs", code],
    reasons: [
      "The balance, the earnings and the exception answers are caller-attested; this calculator has not verified them. The ATO assesses the tax from what funds report.",
      exception ? exception[2] : outcomes[code],
    ],
    incomeYear: input.incomeYear,
    liable,
    largeBalanceSharePercent: decimal(share),
    veryLargeBalanceSharePercent: decimal(veryLargeShare),
    taxableSuperannuationEarnings: decimal(taxable, 10000n),
    veryLargeBalanceEarningsComponent: decimal(component, 10000n),
    taxOnTaxableEarnings: decimal(tax),
    taxOnVeryLargeComponent: decimal(veryLargeTax),
    division296TaxEstimate: decimal(tax + veryLargeTax),
  };
}
