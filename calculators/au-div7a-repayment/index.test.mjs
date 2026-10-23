import test from "node:test";
import assert from "node:assert/strict";
import { assessDiv7aRepayment } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const facts = {
  incomeYear: "2026-27",
  loanIncomeYear: "2025-26",
  standardIncomeYear: true,
  loanStatus: "complying_amalgamated",
  repaymentsReviewed: true,
  openingBalance: "100000.00",
  remainingTermYears: "7",
  eligibleRepayments: "0",
};
const check = (changes = {}) => assessDiv7aRepayment({ ...facts, ...changes });
const amounts = ["openingBalance", "minimumYearlyRepaymentEstimate", "repaymentTarget", "eligibleRepayments", "shortfall"];

test("seven-year example uses the published rate and preserves its provenance", () => {
  const result = check();
  assert.equal(result.benchmarkRatePercent, "8.77");
  assert.equal(result.minimumYearlyRepaymentEstimate, "19715.97");
  assert.equal(result.repaymentTarget, "19715.97");
  assert.equal(result.shortfall, "19715.97");
  assert.equal(result.verdict, "shortfall_indicated");
  assert.equal(result.as_of, "2026-10-21");
  assert.ok(result.sources.includes(rules.rate_provenance.source));
  assert.doesNotThrow(() => JSON.stringify(result));
});

for (const [year, expected] of Object.entries({
  "2021-22": "104520.00", "2022-23": "104770.00", "2023-24": "108270.00",
  "2024-25": "108770.00", "2025-26": "108370.00", "2026-27": "108770.00",
})) {
  test(`one-year closed-form repayment for ${year}`, () => {
    const start = Number(year.slice(0, 4));
    const prior = `${start - 1}-${String(start % 100).padStart(2, "0")}`;
    assert.equal(check({ incomeYear: year, loanIncomeYear: prior, remainingTermYears: "1" }).repaymentTarget, expected);
  });
}

for (const [year, rate] of Object.entries(rules.benchmark_rates)) {
  test(`two-year result agrees with independent closed form for ${year}`, () => {
    // For n=2 the annuity simplifies to P*(1+r)^2/(2+r).
    const r = BigInt(rate.basis_points);
    const numerator = 10000000n * (10000n + r) ** 2n;
    const denominator = 10000n * (20000n + r);
    const ceil = (numerator + denominator - 1n) / denominator;
    const start = Number(year.slice(0, 4));
    const result = check({ incomeYear: year, loanIncomeYear: `${start - 1}-${String(start % 100).padStart(2, "0")}`, remainingTermYears: "2" });
    assert.equal(result.repaymentTarget, `${ceil / 100n}.${String(ceil % 100n).padStart(2, "0")}`);
  });
}

test("fractional remaining term rounds up before the formula, not to the nearest year", () => {
  assert.equal(check({ remainingTermYears: "6.1" }).repaymentTarget, check().repaymentTarget);
  assert.equal(check({ remainingTermYears: "6.000001" }).remainingTermYearsUsed, 7);
  assert.equal(check({ remainingTermYears: "6.0" }).remainingTermYearsUsed, 6);
  assert.equal(check({ remainingTermYears: "6.0" }).minimumYearlyRepaymentEstimate, "22139.33");
});

test("repayments change only shortfall, including equality and overpayment", () => {
  for (const [paid, shortfall] of [["108770", "0.00"], ["108769.99", "0.01"], ["120000", "0.00"]]) {
    const result = check({ remainingTermYears: "1", eligibleRepayments: paid });
    assert.equal(result.minimumYearlyRepaymentEstimate, "108770.00");
    assert.equal(result.shortfall, shortfall);
    assert.equal(result.verdict, shortfall === "0.00" ? "no_shortfall_indicated" : "shortfall_indicated");
  }
});

test("nearest-cent estimate cannot falsely clear a fraction-of-cent shortfall", () => {
  const result = check({ openingBalance: "10000", remainingTermYears: "6", eligibleRepayments: "2213.93" });
  assert.equal(result.minimumYearlyRepaymentEstimate, "2213.93");
  assert.equal(result.repaymentTarget, "2213.94");
  assert.equal(result.shortfall, "0.01");
  assert.equal(result.verdict, "shortfall_indicated");
  assert.equal(check({ openingBalance: "0.01", remainingTermYears: "1", eligibleRepayments: "0.01" }).repaymentTarget, "0.02");
});

test("explicit zero is supported, missing money is not zero", () => {
  const result = check({ openingBalance: "0", eligibleRepayments: "0" });
  for (const key of amounts) assert.equal(result[key], "0.00");
  assert.equal(result.verdict, "no_shortfall_indicated");
});

const invalid = [
  ["future year", { incomeYear: "2027-28" }, "refused"],
  ["older unsupported year", { incomeYear: "2020-21" }, "refused"],
  ["malformed year", { incomeYear: "2026-28" }, "refused"],
  ["substituted accounting period", { standardIncomeYear: false }, "refused"],
  ["unconfirmed year basis", { standardIncomeYear: undefined }, "unknown"],
  ["non-complying loan", { loanStatus: "not_complying" }, "refused"],
  ["unknown loan", { loanStatus: "unknown" }, "unknown"],
  ["term change outside scope", { loanStatus: "refinanced" }, "unknown"],
  ["missing repayments review", { repaymentsReviewed: undefined }, "unknown"],
  ["truthy review string", { repaymentsReviewed: "true" }, "unknown"],
  ["missing loan year", { loanIncomeYear: undefined }, "unknown"],
  ["loan year itself", { loanIncomeYear: "2026-27" }, "refused"],
  ["future loan year", { loanIncomeYear: "2027-28" }, "refused"],
  ["term exceeds chronology", { loanIncomeYear: "2000-01", remainingTermYears: "1" }, "refused"],
];
for (const value of [undefined, null, "", "-1", "NaN", "Infinity", "1e6", "1.001", " 1", "1\n", "01", "1,000", "1".repeat(10000), 100, NaN, Infinity]) {
  invalid.push([`invalid money ${String(value).slice(0, 20)}`, { openingBalance: value }, "unknown"]);
  invalid.push([`invalid repayments ${String(value).slice(0, 20)}`, { eligibleRepayments: value }, "unknown"]);
}
for (const value of [undefined, "0", "0.0", "-0.2", "26", "25.000001", "6\n", "1e9", "6.0000001", "1".repeat(10000), 7]) {
  invalid.push([`invalid term ${String(value).slice(0, 20)}`, { remainingTermYears: value }, "refused"]);
}
for (const [label, changes, verdict] of invalid) {
  test(`no calculated money for ${label}`, () => {
    const result = check(changes);
    assert.equal(result.verdict, verdict);
    for (const key of amounts) assert.equal(result[key], null);
    assert.equal(result.benchmarkRatePercent, null);
    assert.equal(result.reason_codes.length, result.reasons.length);
  });
}

test("invalid records return a structured result", () => {
  for (const input of [undefined, null, [], 7, "facts"]) assert.equal(assessDiv7aRepayment(input).verdict, "unknown");
});

test("malformed JSON year values never reach property-key coercion", () => {
  for (const value of [null, undefined, true, 2026, [], {}, { toString: null, valueOf: null }, { toString: 42 }, "2026-27\n"]) {
    const result = check({ incomeYear: value });
    assert.equal(result.verdict, "refused");
    for (const key of amounts) assert.equal(result[key], null);
  }
});

test("25-year ceiling and large exact money remain bounded and JSON-safe", () => {
  const result = check({ openingBalance: "999999999999999.99", remainingTermYears: "25" });
  assert.equal(result.verdict, "shortfall_indicated");
  assert.match(result.repaymentTarget, /^\d+\.\d{2}$/);
  assert.doesNotThrow(() => JSON.stringify(result));
});

test("no mutation, rate override, schedule or dividend output", () => {
  const input = Object.freeze({ ...facts, benchmarkRatePercent: "99" });
  const first = assessDiv7aRepayment(input);
  first.sources.push("caller mutation");
  first.limits.length = 0;
  const second = assessDiv7aRepayment(input);
  assert.equal(second.benchmarkRatePercent, "8.77");
  assert.ok(!second.sources.includes("caller mutation"));
  assert.ok(second.limits.length > 0);
  for (const key of ["deemedDividend", "annualInterest", "closingBalance", "schedule"]) assert.ok(!(key in second));
});
