import test from "node:test";
import assert from "node:assert/strict";
import { estimateDivision296 } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const member = { incomeYear: "2026-27", protectedOfficeOrFund: false, childRecipient: false, structuredSettlementContribution: false, diedOnOrBeforeYearEnd: false };
const estimate = (balance, earnings, flags = {}) =>
  estimateDivision296({ ...member, totalSuperBalanceAtYearEnd: balance, totalSuperEarnings: earnings, ...flags });
const figures = (result) => [
  result.largeBalanceSharePercent,
  result.veryLargeBalanceSharePercent,
  result.taxableSuperannuationEarnings,
  result.veryLargeBalanceEarningsComponent,
  result.taxOnTaxableEarnings,
  result.taxOnVeryLargeComponent,
  result.division296TaxEstimate,
];
const calculated = ["incomeYear", "liable", "largeBalanceSharePercent", "veryLargeBalanceSharePercent", "taxableSuperannuationEarnings",
  "veryLargeBalanceEarningsComponent", "taxOnTaxableEarnings", "taxOnVeryLargeComponent", "division296TaxEstimate"];

// Explanatory Memorandum to the Treasury Laws Amendment (Building a Stronger and Fairer Super System)
// Bill 2026, Examples 1.1 (Jordan) and 1.2 (Kelly).
test("EM Example 1.1: $4 million and $100,000 of earnings give $3,750", () => {
  const result = estimate("4000000", "100000");
  assert.equal(result.verdict, "estimate_calculated");
  assert.deepEqual(result.reason_codes, ["caller_attested_inputs", "liable"]);
  assert.equal(result.liable, true);
  assert.deepEqual(figures(result), ["25.00", "0.00", "25000.00", "0.00", "3750.00", "0.00", "3750.00"]);
  assert.equal(result.reason_codes.length, result.reasons.length);
  assert.doesNotThrow(() => JSON.stringify(result));
});

test("EM Example 1.2: $12 million and $500,000 of earnings give $56,250 + $8,335 = $64,585", () => {
  assert.deepEqual(figures(estimate("12000000", "500000")), ["75.00", "16.67", "375000.00", "83350.00", "56250.00", "8335.00", "64585.00"]);
});

test("the thresholds and rates are those of ss 296-30, 296-35 and Imposition Act s 5", () => {
  assert.equal(rules.years["2026-27"].large_threshold, "3000000");
  assert.equal(rules.years["2026-27"].very_large_threshold, "10000000");
  assert.deepEqual([rules.rates.taxable_superannuation_earnings_percent, rules.rates.very_large_component_percent], [15, 10]);
});

// ss 296-40(3) and 296-45(3): $150 over $3 million is 0.004999...% and $150.01 is 0.005000...%;
// $500.02 over $10 million is 0.004999...% and $500.03 is 0.005000...%; $32 million is 90.625% and 68.75%.
test("each share rounds to 2 places, up from a third decimal place of 5", () => {
  const nil = estimate("3000150", "100000");
  assert.deepEqual([nil.largeBalanceSharePercent, nil.reason_codes[1], nil.liable, nil.division296TaxEstimate], ["0.00", "share_rounds_to_nil", true, "0.00"]);
  assert.equal(estimate("3000150.01", "100000").largeBalanceSharePercent, "0.01");
  assert.equal(estimate("10000500.02", "100000").veryLargeBalanceSharePercent, "0.00");
  assert.deepEqual(figures(estimate("10000500.03", "100000")), ["70.00", "0.01", "70000.00", "10.00", "10500.00", "1.00", "10501.00"]);
  assert.deepEqual(figures(estimate("32000000", "100000")), ["90.63", "68.75", "90630.00", "68750.00", "13594.50", "6875.00", "20469.50"]);
});

test("a balance must be greater than each threshold, not equal to it", () => {
  for (const balance of ["0", "2999999.99", "3000000"]) {
    const result = estimate(balance, "100000");
    assert.deepEqual([result.reason_codes[1], result.liable, result.division296TaxEstimate], ["balance_not_above_threshold", false, "0.00"], balance);
  }
  assert.equal(estimate("3000000.01", "100000").reason_codes[1], "share_rounds_to_nil");
  for (const balance of ["9999999.99", "10000000", "10000000.01"]) {
    const result = estimate(balance, "100000");
    assert.deepEqual([result.veryLargeBalanceSharePercent, result.division296TaxEstimate], ["0.00", "10500.00"], balance);
  }
});

test("each amount rounds to the cent from exact values, half away from zero", () => {
  assert.deepEqual(figures(estimate("4000000", "0.38")), ["25.00", "0.00", "0.10", "0.00", "0.01", "0.00", "0.01"]);
  assert.equal(estimate("6000000", "0.20").division296TaxEstimate, "0.02");
  assert.equal(estimate("12000000", "-0.03").veryLargeBalanceEarningsComponent, "-0.01");
});

// $12 million and 4 cents: each part is 0.45 of a cent, rounded to nil, though their exact sum is 0.9 of a cent.
test("the total is the sum of the 2 tax amounts shown", () => {
  const small = estimate("12000000", "0.04");
  assert.deepEqual([small.taxOnTaxableEarnings, small.taxOnVeryLargeComponent, small.division296TaxEstimate], ["0.00", "0.00", "0.00"]);
  const toCents = (amount) => BigInt(amount.replace(".", ""));
  for (const balance of ["10000500.03", "12000000", "12345678.91", "32000000"]) {
    for (const earnings of ["0.01", "0.04", "0.07", "1.13", "99999.99", "123456.78"]) {
      const result = estimate(balance, earnings);
      assert.equal(toCents(result.division296TaxEstimate), toCents(result.taxOnTaxableEarnings) + toCents(result.taxOnVeryLargeComponent), `${balance} ${earnings}`);
    }
  }
});

test("earnings of nil or less give no tax, and the very large component keeps their sign", () => {
  for (const [earnings, component] of [["0", "0.00"], ["-0", "0.00"], ["-0.00", "0.00"], ["-50000", "-8335.00"], ["-999999999999999.99", "-166700000000000.00"]]) {
    const result = estimate("12000000", earnings);
    assert.deepEqual([result.reason_codes[1], result.liable, result.taxableSuperannuationEarnings, result.veryLargeBalanceEarningsComponent, result.division296TaxEstimate],
      ["earnings_not_above_nil", false, "0.00", component, "0.00"], earnings);
  }
  assert.equal(estimate("10000000.01", "-50000").veryLargeBalanceEarningsComponent, "0.00");
});

test("each exception removes the liability, not the earnings, and death makes the balance nil", () => {
  const child = estimate("4000000", "100000", { childRecipient: true });
  assert.deepEqual([child.reason_codes[1], child.liable], ["child_recipient", false]);
  assert.deepEqual(figures(child), ["25.00", "0.00", "25000.00", "0.00", "0.00", "0.00", "0.00"]);
  const settlement = estimate("12000000", "500000", { structuredSettlementContribution: true });
  assert.deepEqual([settlement.reason_codes[1], settlement.liable, settlement.taxableSuperannuationEarnings, settlement.division296TaxEstimate],
    ["structured_settlement_contribution", false, "375000.00", "0.00"]);
  const died = estimate("12000000", "500000", { diedOnOrBeforeYearEnd: true });
  assert.deepEqual([died.reason_codes[1], died.liable], ["died_on_or_before_year_end", false]);
  assert.deepEqual(figures(died), ["0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00"]);
  const both = estimate("4000000", "100000", { childRecipient: true, diedOnOrBeforeYearEnd: true });
  assert.deepEqual([both.reason_codes[1], both.taxableSuperannuationEarnings], ["child_recipient", "0.00"]);
});

for (const [label, input, verdict, code] of [
  ["a later year", { ...member, incomeYear: "2027-28", totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "refused", "unsupported_year"],
  ["an earlier year", { ...member, incomeYear: "2025-26", totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "refused", "unsupported_year"],
  ["an inherited property name as the year", { ...member, incomeYear: "toString", totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "refused", "unsupported_year"],
  ["a missing year", { ...member, incomeYear: undefined, totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "refused", "unsupported_year"],
  ["a negative balance", { ...member, totalSuperBalanceAtYearEnd: "-0.01", totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["a missing balance", { ...member, totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["missing earnings", { ...member, totalSuperBalanceAtYearEnd: "4000000" }, "unknown", "invalid_money"],
  ["a number, not a string", { ...member, totalSuperBalanceAtYearEnd: 4000000, totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["3 decimal places", { ...member, totalSuperBalanceAtYearEnd: "4000000.001", totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["grouped digits", { ...member, totalSuperBalanceAtYearEnd: "4,000,000", totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["exponent notation", { ...member, totalSuperBalanceAtYearEnd: "4e6", totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["16 whole digits", { ...member, totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "1000000000000000" }, "unknown", "invalid_money"],
  ["a leading zero", { ...member, totalSuperBalanceAtYearEnd: "04000000", totalSuperEarnings: "100000" }, "unknown", "invalid_money"],
  ["a protected office or fund", { ...member, protectedOfficeOrFund: true, totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "refused", "protected_office_or_fund"],
  ["an unanswered protected office or fund question", { ...member, protectedOfficeOrFund: undefined, totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "unknown", "exception_unanswered"],
  ["an unanswered exception", { ...member, childRecipient: undefined, totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "unknown", "exception_unanswered"],
  ["an exception answered as text", { ...member, diedOnOrBeforeYearEnd: "no", totalSuperBalanceAtYearEnd: "4000000", totalSuperEarnings: "100000" }, "unknown", "exception_unanswered"],
]) {
  test(`no calculated figure for ${label}`, () => {
    const result = estimateDivision296(input);
    assert.deepEqual([result.verdict, result.reason_codes], [verdict, [code]]);
    for (const key of calculated) assert.equal(result[key], null, key);
  });
}

test("invalid records return a structured result", () => {
  for (const input of [null, undefined, [], "4000000", 4000000]) assert.equal(estimateDivision296(input).reason_codes[0], "invalid_input");
});

test("no mutation of the rules through a result", () => {
  const result = estimate("4000000", "100000");
  result.sources.push("x");
  result.limits.length = 0;
  assert.notEqual(rules.sources.at(-1), "x");
  assert.ok(rules.limits.length > 0);
});
