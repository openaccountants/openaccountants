import test from "node:test";
import assert from "node:assert/strict";
import { assessBaseRateEntity } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };

const figures = (aggregatedTurnover, assessableIncome, baseRateEntityPassiveIncome) => ({ aggregatedTurnover, assessableIncome, baseRateEntityPassiveIncome });
const check = (year, previousYear, incomeYear = "2026-27") => assessBaseRateEntity({ incomeYear, entityType: "company", ...year, previousYear });
const prior = (...amounts) => ({ existed: true, ...figures(...amounts) });
const trading = figures("8000000", "8240000", "40000");
const unknownFields = ["incomeYear", "baseRateEntity", "limbs", "companyTaxRatePercent", "imputation"];

function assertNoRate(result, verdict, code) {
  assert.equal(result.verdict, verdict);
  assert.deepEqual(result.reason_codes, [code]);
  assert.equal(result.reasons.length, 1);
  for (const field of unknownFields) assert.equal(result[field], null, field);
}

test("rules.json carries the Rates Act figures for 2021-22 to 2026-27", () => {
  assert.deepEqual(rules.income_years.first, "2021-22");
  assert.deepEqual(rules.income_years.last, "2026-27");
  assert.equal(rules.base_rate_entity.turnover_threshold, "50000000");
  assert.equal(rules.base_rate_entity.passive_income_limit_percent, 80);
  assert.deepEqual([rules.rates.base_rate_entity_percent, rules.rates.other_percent], [25, 30]);
});

// ATO, Changes to company tax rates (last updated 4 September 2026), read 18 November 2026. Each
// example says only that turnover is under $50 million, except Hats 4 Cats; turnovers below $50
// million and Hats 4 Cats' assessable income are invented.
for (const [name, year, rate, codes] of [
  ["Happy Feet: 3.8% interest", figures("104000", "104000", "4000"), 25, ["base_rate_entity"]],
  ["Coffee and Cake: 28.6% trust rent", figures("700000", "700000", "200000"), 25, ["base_rate_entity"]],
  ["Best Equity: 100% interest and dividends", figures("5000000", "5000000", "5000000"), 30, ["passive_income_over_80_percent"]],
  ["SoftDev: 85% net capital gain", figures("1000000", "1000000", "850000"), 30, ["passive_income_over_80_percent"]],
  ["Hats 4 Cats: $170 million with a foreign affiliate", figures("170000000", "20000000", "0"), 30, ["turnover_not_under_threshold"]],
]) {
  test(`ATO example 2025-26, ${name}: ${rate}%`, () => {
    const result = check(year, undefined, "2025-26");
    assert.equal(result.verdict, "rate_calculated");
    assert.equal(result.companyTaxRatePercent, rate);
    assert.equal(result.baseRateEntity, rate === 25);
    assert.deepEqual(result.reason_codes, ["caller_established_figures", ...codes, "previous_year_not_supplied"]);
    assert.equal(result.reason_codes.length, result.reasons.length);
    assert.equal(result.imputation, null);
    assert.doesNotThrow(() => JSON.stringify(result));
  });
}

test("au-company-tax Example 1: $8.0m turnover, 0.49% BREPI, 25%", () => {
  const result = check(trading);
  assert.deepEqual([result.companyTaxRatePercent, result.limbs], [25, { passiveIncome: true, aggregatedTurnover: true }]);
});

test("passive income limb: exactly 80% passes, 1 cent more fails (s 23AA(a))", () => {
  assert.equal(check(figures("1", "1000000", "800000")).companyTaxRatePercent, 25);
  assert.equal(check(figures("1", "1000000", "800000.00")).companyTaxRatePercent, 25);
  assert.equal(check(figures("1", "1000000", "800000.01")).companyTaxRatePercent, 30);
  // au-company-tax decision case: the unresolved $1 receipt as a royalty.
  assert.equal(check(figures("1", "1000000", "800001")).companyTaxRatePercent, 30);
  assert.equal(check(figures("1", "0.05", "0.04")).companyTaxRatePercent, 25);
  assert.equal(check(figures("1", "0.04", "0.04")).companyTaxRatePercent, 30);
});

test("turnover limb: $49,999,999.99 passes, exactly $50 million fails (s 23AA(b))", () => {
  assert.equal(check(figures("49999999.99", "100", "0")).companyTaxRatePercent, 25);
  const atThreshold = check(figures("50000000", "100", "0"));
  assert.equal(atThreshold.companyTaxRatePercent, 30);
  assert.deepEqual(atThreshold.limbs, { passiveIncome: true, aggregatedTurnover: false });
});

test("failing both limbs gives both reasons and 30%", () => {
  const result = check(figures("60000000", "100", "100"));
  assert.equal(result.companyTaxRatePercent, 30);
  assert.deepEqual(result.reason_codes.slice(1, 3), ["passive_income_over_80_percent", "turnover_not_under_threshold"]);
});

// LCR 2019/5 Example 2.2 (Swan Co, paragraph 64): nil assessable income and nil base rate entity
// passive income is 'no more than 80%'.
test("no assessable income and no passive income meets the passive income limb", () => {
  const result = check(figures("0", "0", "0"));
  assert.deepEqual([result.companyTaxRatePercent, result.limbs.passiveIncome], [25, true]);
});

test("LCR 2019/5 Swan Co: a dormant company with nil figures last year franks at 25%", () => {
  const result = check(figures("60000000", "100", "100"), prior("0", "0", "0"));
  assert.deepEqual(result.imputation.limbs, { passiveIncome: true, aggregatedTurnover: true });
  assert.equal(result.imputation.corporateTaxRateForImputationPurposesPercent, 25);
});

test("au-company-tax Example 4: taxed at 25% but franks at 30% from last year's $55m turnover", () => {
  const result = check(figures("30000000", "30000000", "1000"), prior("55000000", "30000000", "1000"));
  assert.equal(result.companyTaxRatePercent, 25);
  assert.deepEqual(result.imputation, {
    basis: "previous_year_figures",
    limbs: { passiveIncome: true, aggregatedTurnover: false },
    corporateTaxRateForImputationPurposesPercent: 30,
    maximumFrankingCredit: { numerator: 3, denominator: 7 },
  });
  assert.deepEqual(result.reason_codes, ["caller_established_figures", "base_rate_entity", "imputation_previous_year_figures"]);
});

test("au-company-tax Example 4 reverse: a 100% BREPI company taxed at 30% franks at 25%", () => {
  const result = check(figures("2000000", "2000000", "2000000"), prior("2000000", "2000000", "100000"));
  assert.equal(result.companyTaxRatePercent, 30);
  assert.equal(result.imputation.corporateTaxRateForImputationPurposesPercent, 25);
  assert.deepEqual(result.imputation.maximumFrankingCredit, { numerator: 1, denominator: 3 });
});

// ATO, Allocating franking credits, example 2 (2019-20; the same test in a covered year): last
// year's turnover was $52 million, this year's is expected to be $45 million.
test("Dillmore Manufacture: the imputation rate uses last year's turnover, not this year's", () => {
  const result = check(figures("45000000", "45000000", "0"), prior("52000000", "52000000", "0"));
  assert.deepEqual([result.companyTaxRatePercent, result.imputation.corporateTaxRateForImputationPurposesPercent], [25, 30]);
});

test("the imputation test applies both limbs to last year's figures", () => {
  const passiveFails = check(trading, prior("1", "100", "80.01"));
  assert.deepEqual(passiveFails.imputation.limbs, { passiveIncome: false, aggregatedTurnover: true });
  assert.equal(passiveFails.imputation.corporateTaxRateForImputationPurposesPercent, 30);
  const turnoverEdge = check(trading, prior("49999999.99", "100", "80"));
  assert.equal(turnoverEdge.imputation.corporateTaxRateForImputationPurposesPercent, 25);
});

test("au-company-tax Test 6: a company that did not exist last year franks at 25%", () => {
  const result = check(figures("60000000", "100", "100"), { existed: false });
  assert.equal(result.companyTaxRatePercent, 30);
  assert.deepEqual(result.imputation, {
    basis: "did_not_exist",
    limbs: null,
    corporateTaxRateForImputationPurposesPercent: 25,
    maximumFrankingCredit: { numerator: 1, denominator: 3 },
  });
  assert.equal(result.reason_codes.at(-1), "imputation_did_not_exist");
});

test("the first covered year tests 2020-21 figures against the 2021-22 law", () => {
  const result = check(trading, prior("40000000", "100", "10"), "2021-22");
  assert.equal(result.imputation.corporateTaxRateForImputationPurposesPercent, 25);
});

test("each current-year figure is required; a missing or malformed one gives no rate", () => {
  for (const key of ["aggregatedTurnover", "assessableIncome", "baseRateEntityPassiveIncome"]) {
    for (const bad of [undefined, null, "", 1000, "-1", "1.001", "1e6", "01", "1,000", " 1"]) {
      const result = check({ ...trading, [key]: bad });
      assertNoRate(result, "unknown", "figures");
      assert.match(result.reasons[0], new RegExp(key));
    }
  }
  assertNoRate(check(figures("1", "100", "100.01")), "unknown", "passive_exceeds_assessable");
});

test("previous-year inputs: a stated existence, then each figure, are required", () => {
  for (const previousYear of [null, "yes", [], {}, { existed: "yes" }]) {
    assertNoRate(check(trading, previousYear), "unknown", "previous_year");
  }
  for (const key of ["aggregatedTurnover", "assessableIncome", "baseRateEntityPassiveIncome"]) {
    assertNoRate(check(trading, { existed: false, [key]: "1" }), "unknown", "previous_year");
    const { [key]: _, ...rest } = trading;
    assertNoRate(check(trading, { existed: true, ...rest }), "unknown", "previous_year_figures");
  }
  assertNoRate(check(trading, { existed: true, ...figures("1", "100", "101") }), "unknown", "previous_year_passive_exceeds_assessable");
});

test("income years outside 2021-22 to 2026-27 are refused; malformed years are unknown", () => {
  assert.equal(check(trading, undefined, "2021-22").verdict, "rate_calculated");
  assertNoRate(check(trading, undefined, "2020-21"), "refused", "earlier_income_year");
  assertNoRate(check(trading, undefined, "2017-18"), "refused", "earlier_income_year");
  assertNoRate(check(trading, undefined, "2027-28"), "refused", "later_income_year");
  for (const year of [undefined, "2026", "2026-28", "2026/27", "2026-2027", 2026]) {
    assertNoRate(assessBaseRateEntity({ incomeYear: year, entityType: "company", ...trading }), "unknown", "income_year");
  }
});

test("special-rate entities, trustees and public trading trusts are refused by name", () => {
  const refused = Object.keys(rules.entity_types.refused);
  assert.deepEqual(refused, ["company_as_trustee", "rsa_provider", "pooled_development_fund", "life_insurance_company",
    "non_profit_company", "recognised_medium_credit_union", "public_trading_trust"]);
  for (const entityType of refused) {
    const result = assessBaseRateEntity({ incomeYear: "2026-27", entityType, ...trading });
    assertNoRate(result, "refused", "entity_type_refused");
    assert.equal(result.reasons[0], rules.entity_types.refused[entityType]);
  }
  // s 23(6) and (7) cap the tax; the rate itself still comes from s 23(2).
  for (const entityType of ["non_profit_company", "recognised_medium_credit_union"]) {
    assert.match(rules.entity_types.refused[entityType], /rate is 25% or 30% under s 23\(2\)/);
  }
  for (const entityType of [undefined, "Company", "trust", "toString", "constructor"]) {
    assertNoRate(assessBaseRateEntity({ incomeYear: "2026-27", entityType, ...trading }), "unknown", "entity_type");
  }
});

test("a non-record input is unknown", () => {
  for (const input of [undefined, null, "2026-27", [trading]]) assertNoRate(assessBaseRateEntity(input), "unknown", "invalid_input");
});
