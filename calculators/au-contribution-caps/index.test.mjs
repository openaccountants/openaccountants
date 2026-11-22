import test from "node:test";
import assert from "node:assert/strict";
import { assessContributionCaps } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const years = (rows) => rows.map(([incomeYear, concessionalContributions, totalSuperBalanceBeforeYear]) => (
  totalSuperBalanceBeforeYear === undefined
    ? { incomeYear, concessionalContributions }
    : { incomeYear, concessionalContributions, totalSuperBalanceBeforeYear }
));
const base = {
  incomeYear: "2026-27",
  totalSuperBalanceBeforeYear: "1000000",
  concessionalContributions: "0",
  nonConcessionalContributions: "0",
  under75AtAnyTimeInYear: true,
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  earlierBringForwardCoversYear: false,
};
const check = (changes = {}) => assessContributionCaps({ ...base, ...changes });
const remaining = (result) => Object.fromEntries(result.carryForward.years.map((row) => [row.incomeYear, row.remaining]));
const stopped = (result, verdict, code) => {
  assert.equal(result.verdict, verdict);
  assert.deepEqual(result.reason_codes, [code]);
  for (const key of ["incomeYear", "totalSuperBalanceBeforeYear", "concessional", "carryForward", "nonConcessional"]) assert.equal(result[key], null);
};

// The ATO's 'Concessional contributions cap' page (last updated 2 July 2026), Sam's
// table 1. The page gives his balance only as below $500,000.
const sam = years([["2019-20", "11000"], ["2020-21", "12000"], ["2021-22", "13000"], ["2022-23", "14000"], ["2023-24", "15000"]]);

test("ATO example: Sam's unused caps raise his 2024-25 cap to $97,500 with no excess", () => {
  const result = check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "450000", concessionalContributions: "97500", earlierYears: sam });
  assert.equal(result.verdict, "caps_calculated");
  assert.deepEqual(result.carryForward.years.map((row) => row.unusedCap), ["14000.00", "13000.00", "14500.00", "13500.00", "12500.00"]);
  assert.equal(result.concessional.unusedCapCarriedIn, "67500.00");
  assert.equal(result.concessional.capIncrease, "67500.00");
  assert.equal(result.concessional.cap, "97500.00");
  assert.equal(result.concessional.excess, "0.00");
  assert.ok(result.carryForward.years.every((row) => row.remaining === "0.00" && row.appliedThisYear === row.unusedCap));
  assert.equal(result.carryForward.expiringAtEndOfYear, "0.00");
  assert.equal(result.carryForward.years[0].expiresAtEndOf, "2024-25");
  assert.deepEqual(result.reason_codes, ["caller_supplied_inputs", "carry_forward_applied"]);
  assert.doesNotThrow(() => JSON.stringify(result));
});

test("ATO contributions caps table 2: unused amounts accrued from 2018-19, and 2018-19's lapse", () => {
  const earlierYears = years([["2018-19", "3000"], ["2019-20", "3000"], ["2020-21", "0"], ["2021-22", "0"], ["2022-23", "27500"], ["2023-24", "27500"]]);
  const result = check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "490000", concessionalContributions: "30000", earlierYears });
  assert.deepEqual(result.carryForward.years.map((row) => [row.incomeYear, row.unusedCap]), [
    ["2019-20", "22000.00"], ["2020-21", "25000.00"], ["2021-22", "27500.00"], ["2022-23", "0.00"], ["2023-24", "0.00"],
  ]);
  assert.equal(result.concessional.unusedCapCarriedIn, "74500.00");
  assert.equal(result.concessional.capIncrease, "0.00");
  assert.equal(result.concessional.balanceBelowCarryForwardThreshold, true);
  assert.equal("carryForwardAllowed" in result.concessional, false);
  assert.deepEqual(result.reason_codes, ["caller_supplied_inputs"]);
  assert.equal(result.carryForward.expiringAtEndOfYear, "22000.00");
});

test("below $500,000 with no unused cap: only the balance condition is met and the cap is not increased", () => {
  const full = years([["2019-20", "25000"], ["2020-21", "25000"], ["2021-22", "27500"], ["2022-23", "27500"], ["2023-24", "27500"]]);
  const result = check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "400000", concessionalContributions: "40000", earlierYears: full, excessConcessionalReleased: false });
  assert.equal(result.concessional.balanceBelowCarryForwardThreshold, true);
  assert.equal(result.concessional.unusedCapCarriedIn, "0.00");
  assert.equal(result.concessional.capIncrease, "0.00");
  assert.equal(result.concessional.cap, "30000.00");
  assert.equal(result.concessional.excess, "10000.00");
  assert.equal(result.reason_codes.includes("carry_forward_applied"), false);
});

// Hand-worked: 2021-22 to 2025-26 at $20,000 leave $7,500, $7,500, $7,500, $10,000 and
// $10,000 unused; $50,000 in 2026-27 is $17,500 over the $32,500 cap.
const fiveYears = years([["2021-22", "20000"], ["2022-23", "20000"], ["2023-24", "20000"], ["2024-25", "20000"], ["2025-26", "20000"]]);

test("$499,999.99 just before the year: the excess is covered earliest year first, partly from 2023-24", () => {
  const result = check({ totalSuperBalanceBeforeYear: "499999.99", concessionalContributions: "50000", earlierYears: fiveYears });
  assert.equal(result.concessional.balanceBelowCarryForwardThreshold, true);
  assert.equal(result.concessional.unusedCapCarriedIn, "42500.00");
  assert.equal(result.concessional.capIncrease, "17500.00");
  assert.equal(result.concessional.cap, "50000.00");
  assert.equal(result.concessional.excess, "0.00");
  assert.deepEqual(result.carryForward.years.map((row) => row.appliedThisYear), ["7500.00", "7500.00", "2500.00", "0.00", "0.00"]);
  assert.deepEqual(remaining(result), { "2021-22": "0.00", "2022-23": "0.00", "2023-24": "5000.00", "2024-25": "10000.00", "2025-26": "10000.00" });
  assert.equal(result.carryForward.expiringAtEndOfYear, "0.00");
});

test("$500,000.00 just before the year: no increase, the amounts still age and 2021-22's lapses", () => {
  const result = check({ totalSuperBalanceBeforeYear: "500000.00", concessionalContributions: "50000", earlierYears: fiveYears, excessConcessionalReleased: false });
  assert.equal(result.concessional.balanceBelowCarryForwardThreshold, false);
  assert.equal(result.concessional.capIncrease, "0.00");
  assert.equal(result.concessional.cap, "32500.00");
  assert.equal(result.concessional.excess, "17500.00");
  assert.deepEqual(remaining(result), { "2021-22": "7500.00", "2022-23": "7500.00", "2023-24": "7500.00", "2024-25": "10000.00", "2025-26": "10000.00" });
  assert.equal(result.carryForward.expiringAtEndOfYear, "7500.00");
  assert.equal(result.carryForward.years[0].expiresAtEndOf, "2026-27");
  assert.equal(result.nonConcessional.contributionsCounted, "17500.00");
});

test("earlier years are needed below $500,000 and optional at or above it", () => {
  stopped(check({ totalSuperBalanceBeforeYear: "499999.99", concessionalContributions: "20000" }), "unknown", "earlier_years_missing");
  const result = check({ totalSuperBalanceBeforeYear: "500000", concessionalContributions: "20000" });
  assert.equal(result.carryForward, null);
  assert.equal(result.concessional.unusedCapCarriedIn, null);
  assert.equal(result.concessional.unusedCapThisYear, "12500.00");
});

// Hand-worked to 2024-25: 2022-23's $50,000 is $22,500 over its $27,500 cap with a balance
// below $500,000, so 2018-19's $20,000 and then $2,500 of 2020-21's $10,000 are applied.
const history = [["2018-19", "5000"], ["2019-20", "25000"], ["2020-21", "15000"], ["2021-22", "27500"], ["2022-23", "50000", "300000"], ["2023-24", "7500"]];

test("an earlier year over its cap uses the unused cap of its own previous 5 years first", () => {
  const result = check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "400000", concessionalContributions: "30000", earlierYears: years(history) });
  assert.deepEqual(result.carryForward.years.map((row) => [row.incomeYear, row.unusedCap, row.carriedIn]), [
    ["2019-20", "0.00", "0.00"], ["2020-21", "10000.00", "7500.00"], ["2021-22", "0.00", "0.00"], ["2022-23", "0.00", "0.00"], ["2023-24", "20000.00", "20000.00"],
  ]);
  assert.equal(result.concessional.unusedCapCarriedIn, "27500.00");
  assert.equal(result.concessional.excess, "0.00");
});

test("an earlier year over its cap at $500,000 applies nothing; without its balance there is no figure", () => {
  const atLimit = history.map((row) => (row[0] === "2022-23" ? ["2022-23", "50000", "500000"] : row));
  const result = check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "400000", concessionalContributions: "30000", earlierYears: years(atLimit) });
  assert.equal(result.concessional.unusedCapCarriedIn, "30000.00");
  const noBalance = history.map((row) => row.slice(0, 2));
  stopped(check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "400000", earlierYears: years(noBalance) }), "unknown", "earlier_balance_missing");
  stopped(check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "400000", earlierYears: years(history.slice(1)) }), "unknown", "earlier_years_short");
});

test("earlier years must run without a gap from 5 years before to the year before, from 2018-19", () => {
  const invalid = [
    fiveYears.slice(1),
    fiveYears.slice(0, 4),
    [...fiveYears.slice(0, 2), ...fiveYears.slice(3)],
    [...fiveYears, fiveYears[2]],
    [...fiveYears, { incomeYear: "2026-27", concessionalContributions: "0" }],
    [...fiveYears.slice(0, 4), { incomeYear: "2025-26", concessionalContributions: "-1" }],
    [...fiveYears.slice(0, 4), { incomeYear: "2025-27", concessionalContributions: "0" }],
    [...fiveYears.slice(0, 4), null],
    [],
    "2021-22",
  ];
  for (const earlierYears of invalid) stopped(check({ totalSuperBalanceBeforeYear: "100000", earlierYears }), "unknown", "earlier_years_invalid");
  const before = years([["2017-18", "0"], ["2018-19", "0"], ["2019-20", "0"], ["2020-21", "0"], ["2021-22", "0"], ["2022-23", "0"], ["2023-24", "0"]]);
  stopped(check({ incomeYear: "2024-25", totalSuperBalanceBeforeYear: "100000", earlierYears: before }), "refused", "year_before_2018_19");
  const unordered = [...fiveYears].reverse();
  assert.equal(check({ totalSuperBalanceBeforeYear: "100000", earlierYears: unordered }).verdict, "caps_calculated");
});

// The ATO's 'Non-concessional contributions cap' page (last updated 7 May 2026): first-year
// caps by total super balance on 30 June of the previous year.
const bands = {
  "2026-27": [["1839999.99", "390000.00"], ["1840000.00", "260000.00"], ["1969999.99", "260000.00"], ["1970000.00", null]],
  "2025-26": [["1759999.99", "360000.00"], ["1760000.00", "240000.00"], ["1879999.99", "240000.00"], ["1880000.00", null]],
  "2024-25": [["1659999.99", "360000.00"], ["1660000.00", "240000.00"], ["1779999.99", "240000.00"], ["1780000.00", null]],
};
const general = { "2024-25": "120000.00", "2025-26": "120000.00", "2026-27": "130000.00" };
const transfer = { "2024-25": "1900000.00", "2025-26": "2000000.00", "2026-27": "2100000.00" };

for (const [incomeYear, rows] of Object.entries(bands)) {
  test(`bring forward bands for ${incomeYear} match the ATO's table at each boundary`, () => {
    for (const [balance, bringForwardCap] of rows) {
      const result = check({ incomeYear, totalSuperBalanceBeforeYear: balance, nonConcessionalContributions: "400000" });
      assert.equal(result.nonConcessional.generalCap, general[incomeYear]);
      assert.equal(result.nonConcessional.firstYearCapIfBringForwardStarts, bringForwardCap, `${incomeYear} at ${balance}`);
      assert.equal(result.nonConcessional.cap, bringForwardCap ?? general[incomeYear]);
      assert.equal(result.nonConcessional.bringForwardYears, bringForwardCap === null ? null : Number(BigInt(bringForwardCap.slice(0, -3)) / BigInt(general[incomeYear].slice(0, -3))));
    }
    const nearCap = (cents) => `${BigInt(transfer[incomeYear].slice(0, -3)) - 1n}.${cents}`;
    assert.equal(check({ incomeYear, totalSuperBalanceBeforeYear: nearCap("99"), nonConcessionalContributions: "1" }).nonConcessional.cap, general[incomeYear]);
    const atCap = check({ incomeYear, totalSuperBalanceBeforeYear: transfer[incomeYear], nonConcessionalContributions: "1" });
    assert.equal(atCap.nonConcessional.cap, "0.00");
    assert.equal(atCap.nonConcessional.firstYearCapIfBringForwardStarts, null);
    assert.equal(atCap.nonConcessional.excess, "1.00");
  });
}

test("bring forward starts only above the general cap, and only under 75", () => {
  const atCap = check({ nonConcessionalContributions: "130000" });
  assert.equal(atCap.nonConcessional.bringForwardTriggered, false);
  assert.equal(atCap.nonConcessional.cap, "130000.00");
  // Not started: no output may read as a bring forward cap; the conditional figure says so.
  assert.equal("bringForwardCap" in atCap.nonConcessional, false);
  assert.equal(atCap.nonConcessional.firstYearCapIfBringForwardStarts, "390000.00");
  assert.equal(atCap.nonConcessional.bringForwardYears, null);
  assert.equal(atCap.nonConcessional.remaining, "0.00");
  const over = check({ nonConcessionalContributions: "130000.01" });
  assert.equal(over.nonConcessional.bringForwardTriggered, true);
  assert.equal(over.nonConcessional.bringForwardYears, 3);
  assert.equal(over.nonConcessional.cap, "390000.00");
  assert.equal(over.nonConcessional.remaining, "259999.99");
  assert.deepEqual(over.reason_codes, ["caller_supplied_inputs", "bring_forward_triggered"]);
  const aged = check({ nonConcessionalContributions: "200000", under75AtAnyTimeInYear: false });
  assert.equal(aged.nonConcessional.firstYearCapIfBringForwardStarts, null);
  assert.equal(aged.nonConcessional.cap, "130000.00");
  assert.equal(aged.nonConcessional.excess, "70000.00");
  const excess = check({ nonConcessionalContributions: "400000" });
  assert.equal(excess.nonConcessional.excess, "10000.00");
  assert.deepEqual(excess.reason_codes, ["caller_supplied_inputs", "bring_forward_triggered", "excess_non_concessional"]);
});

test("an unreleased concessional excess counts as non-concessional and can start bring forward", () => {
  const facts = { totalSuperBalanceBeforeYear: "600000", concessionalContributions: "40000", nonConcessionalContributions: "125000", excessConcessionalReleased: false };
  const result = check(facts);
  assert.equal(result.concessional.excess, "7500.00");
  assert.equal(result.nonConcessional.excessConcessionalCounted, "7500.00");
  assert.equal(result.nonConcessional.contributionsCounted, "132500.00");
  assert.equal(result.nonConcessional.bringForwardTriggered, true);
  assert.equal(result.nonConcessional.excess, "0.00");
  assert.equal(check({ ...facts, under75AtAnyTimeInYear: false }).nonConcessional.excess, "2500.00");
  stopped(check({ ...facts, excessConcessionalReleased: true }), "refused", "excess_released");
  stopped(check({ ...facts, excessConcessionalReleased: undefined }), "unknown", "excess_release_unknown");
  assert.equal(check({ ...facts, concessionalContributions: "32500", excessConcessionalReleased: undefined }).verdict, "caps_calculated");
});

test("each exclusion is refused when true and has no figure when not stated", () => {
  for (const [key, code] of [
    ["definedBenefitInterest", "defined_benefit_interest"],
    ["constitutionallyProtectedFund", "constitutionally_protected_fund"],
    ["earlierBringForwardCoversYear", "bring_forward_later_year"],
  ]) {
    stopped(check({ [key]: true }), "refused", code);
    stopped(check({ [key]: undefined }), "unknown", code);
    stopped(check({ [key]: "false" }), "unknown", code);
  }
  stopped(check({ under75AtAnyTimeInYear: undefined }), "unknown", "age_test");
});

test("unsupported years and malformed inputs give no figure", () => {
  for (const incomeYear of ["2023-24", "2027-28", "2026-28", "2026/27", 2026, undefined]) stopped(check({ incomeYear }), "refused", "unsupported_year");
  for (const value of [undefined, "", "-1", "1.234", "1e6", "01", 1000, "1,000"]) {
    stopped(check({ concessionalContributions: value }), "unknown", "invalid_money");
    stopped(check({ totalSuperBalanceBeforeYear: value }), "unknown", "invalid_money");
    stopped(check({ nonConcessionalContributions: value }), "unknown", "invalid_money");
  }
  for (const input of [null, [], "facts"]) stopped(assessContributionCaps(input), "unknown", "invalid_input");
});

test("rules: caps are the ATO's published figures and the non-concessional cap is 4 times the concessional", () => {
  assert.deepEqual(rules.concessional_caps.amounts, {
    "2018-19": "25000", "2019-20": "25000", "2020-21": "25000", "2021-22": "27500", "2022-23": "27500",
    "2023-24": "27500", "2024-25": "30000", "2025-26": "30000", "2026-27": "32500",
  });
  for (const incomeYear of rules.supported_years) {
    assert.equal(check({ incomeYear }).nonConcessional.generalCap, general[incomeYear]);
    assert.equal(check({ incomeYear }).nonConcessional.generalTransferBalanceCap, transfer[incomeYear]);
  }
});
