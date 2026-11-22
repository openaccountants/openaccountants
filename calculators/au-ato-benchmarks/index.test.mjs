import test from "node:test";
import assert from "node:assert/strict";
import { compareWithAtoBenchmarks } from "./index.mjs";
import rules from "./rules.json" with { type: "json" };
import dataset from "./benchmarks-2023-24.json" with { type: "json" };
import pages from "./ato-pages-2023-24.json" with { type: "json" };

const year = "2023-24";
const check = (input) => compareWithAtoBenchmarks({ benchmarkYear: year, ...input });
const ratio = (result, name) => result.ratios.find((r) => r.ratio === name);
const bands = (name) => dataset.industries[name].bands.map((band, i) => ({ ...band, ...pages.industries[name].bands[i] }));

// ATO, 'How to compare your business performance manually' (QC47938, last updated 16 March 2026).
test("ATO example: Elizabeth's coffee shop is within both key ranges", () => {
  const result = check({
    industry: "Coffee shops",
    totalBusinessIncome: 705200,
    costOfSales: 253300,
    salaryAndWagesInCostOfSales: false,
    totalExpenses: 675500,
    paymentsToAssociatedPersons: 50000,
  });
  assert.equal(result.verdict, "compared");
  assert.equal(result.band.label, "More than $600,000");
  assert.equal(result.keyRatio, "cost_of_sales");
  assert.deepEqual(ratio(result, "cost_of_sales"), { ratio: "cost_of_sales", key: true, amount: 253300, percent: 35.92, range: { min: 33, max: 38 }, position: "within" });
  assert.deepEqual(ratio(result, "total_expenses"), { ratio: "total_expenses", key: false, amount: 625500, percent: 88.7, range: { min: 86, max: 93 }, position: "within" });
  assert.equal(result.reason_codes.length, result.reasons.length);
  assert.doesNotThrow(() => JSON.stringify(result));
});

// ATO, 'What it means to be outside the benchmark range' (QC47939, last updated 16 March 2026).
test("ATO example: Robert's plumbing business is above, then within once his own wages come out", () => {
  const before = check({ industry: "Plumbing services", totalBusinessIncome: 704500, totalExpenses: 845650, paymentsToAssociatedPersons: 0 });
  assert.equal(before.turnoverBasis, "total_business_income");
  assert.equal(before.keyRatio, "total_expenses");
  assert.deepEqual(ratio(before, "total_expenses"), { ratio: "total_expenses", key: true, amount: 845650, percent: 120.04, range: { min: 75, max: 86 }, position: "above" });
  const after = check({ industry: "Plumbing services", totalBusinessIncome: 704500, totalExpenses: 605650, paymentsToAssociatedPersons: 0 });
  assert.equal(ratio(after, "total_expenses").percent, 85.97);
  assert.equal(ratio(after, "total_expenses").position, "within");
});

test("ATO example: Belinda's footwear business is below the cost of sales range", () => {
  const result = check({ industry: "Footwear retailing", totalBusinessIncome: 230000, costOfSales: 92000, salaryAndWagesInCostOfSales: false });
  assert.equal(result.band.label, "$180,001 - $600,000");
  assert.deepEqual(ratio(result, "cost_of_sales"), { ratio: "cost_of_sales", key: true, amount: 92000, percent: 40, range: { min: 51, max: 59 }, position: "below" });
});

test("ATO example: Steff's cost of sales to turnover is 30.21%", () => {
  const result = check({ industry: "Coffee shops", totalBusinessIncome: 456790, salesOfGoodsAndServices: 456790, costOfSales: 137983, salaryAndWagesInCostOfSales: false });
  assert.equal(ratio(result, "cost_of_sales").percent, 30.21);
});

test("bakeries match the ATO's industry page (QC43659) for every band and ratio", () => {
  assert.deepEqual(bands("Bakeries and hot bread shops").map((b) => [b.from, b.to, b.cost_of_sales, b.total_expenses, b.labour, b.rent, b.motor_vehicle]), [
    [65000, 400000, [31, 38], [69, 81], [14, 25], [10, 17], [2, 4]],
    [400001, 750000, [34, 39], [75, 86], [15, 28], [8, 12], [1, 2]],
    [750001, null, [29, 36], [82, 90], [25, 34], [5, 8], [1, 1]],
  ]);
});

for (const [label, turnover, band] of [
  ["the lowest published turnover", 65000, "$65,000 - $400,000"],
  ["the top of the low band", 400000, "$65,000 - $400,000"],
  ["the first dollar of the medium band", 400001, "$400,001 - $750,000"],
  ["the top of the medium band", 750000, "$400,001 - $750,000"],
  ["the first dollar more than $750,000", 750001, "More than $750,000"],
]) {
  test(`turnover band: ${label}`, () => {
    assert.equal(check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: turnover, rentExpenses: 0 }).band.label, band);
  });
}

test("a 2-band industry's top band is open-ended", () => {
  const result = check({ industry: "Barber and men's hairdressing", totalBusinessIncome: 150001, totalExpenses: 100000, paymentsToAssociatedPersons: 0 });
  assert.deepEqual(result.band, { label: "More than $150,000", from: 150001, to: null });
});

test("turnover below the lowest band is refused with no comparison", () => {
  const result = check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 64999, rentExpenses: 0 });
  assert.equal(result.verdict, "refused");
  assert.deepEqual(result.reason_codes, ["turnover_below_bands"]);
  assert.equal(result.ratios, null);
});

for (const [label, sales, turnover, basis] of [
  ["sales of exactly 50% of total business income are turnover", 50000, 50000, "sales_of_goods_and_services"],
  ["sales a dollar under 50% give way to total business income", 49999, 100000, "total_business_income"],
  ["zero sales give way to total business income", 0, 100000, "total_business_income"],
  ["blank sales give way to total business income", undefined, 100000, "total_business_income"],
]) {
  test(`turnover: ${label}`, () => {
    const result = check({ industry: "Plumbing services", totalBusinessIncome: 100000, salesOfGoodsAndServices: sales, motorVehicleExpenses: 0 });
    assert.equal(result.turnover, turnover);
    assert.equal(result.turnoverBasis, basis);
  });
}

// Bakery low band: total expenses 69% to 81% of turnover 100,000, compared at 2 places, half up.
for (const [expenses, position] of [[68994, "below"], [68995, "within"], [81004, "within"], [81005, "above"]]) {
  test(`a ratio at ${expenses / 1000}% of turnover is ${position} a 69% to 81% range`, () => {
    const result = check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 100000, totalExpenses: expenses, paymentsToAssociatedPersons: 0 });
    assert.equal(ratio(result, "total_expenses").position, position);
  });
}

// Coffee shops low band: total expenses 73% to 86% of turnover 250,000; 215,010 is 86.004%.
test("the position follows the percentage shown, to 2 places", () => {
  const result = check({ industry: "Coffee shops", totalBusinessIncome: 250000, totalExpenses: 215010, paymentsToAssociatedPersons: 0 });
  assert.equal(ratio(result, "total_expenses").percent, 86);
  assert.equal(ratio(result, "total_expenses").position, "within");
  const above = check({ industry: "Coffee shops", totalBusinessIncome: 250000, totalExpenses: 215013, paymentsToAssociatedPersons: 0 });
  assert.deepEqual([ratio(above, "total_expenses").percent, ratio(above, "total_expenses").position], [86.01, "above"]);
});

test("a single published figure is both bounds", () => {
  const at = (motorVehicleExpenses) => ratio(check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 800000, motorVehicleExpenses }), "motor_vehicle").position;
  assert.deepEqual([at(7959), at(7960), at(8039), at(8040)], ["below", "within", "within", "above"]);
});

test("a 0% range holds only expenses under 0.005% of turnover", () => {
  const at = (motorVehicleExpenses) => ratio(check({ industry: "Pharmacy", totalBusinessIncome: 4000000, motorVehicleExpenses }), "motor_vehicle");
  assert.deepEqual(at(199).range, { min: 0, max: 0 });
  assert.deepEqual([at(0).position, at(199).position, at(200).position], ["within", "within", "above"]);
});

test("payments to associated persons come out of total expenses and labour", () => {
  const result = check({
    industry: "Bakeries and hot bread shops",
    totalBusinessIncome: 100000,
    totalExpenses: 90000,
    paymentsToAssociatedPersons: 15000,
    totalSalaryAndWages: 30000,
    contractorExpenses: 5000,
    w1: 30000,
  });
  assert.equal(ratio(result, "total_expenses").amount, 75000);
  assert.equal(ratio(result, "labour").amount, 20000);
  assert.ok(!result.reason_codes.includes("w1_not_supplied"));
});

test("W1 replaces total salary and wages for labour only where it is greater", () => {
  const labour = (w1) => ratio(check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 100000, totalSalaryAndWages: 20000, contractorExpenses: 0, paymentsToAssociatedPersons: 0, w1 }), "labour").amount;
  assert.deepEqual([labour(25000), labour(15000), labour(undefined)], [25000, 20000, 20000]);
  const result = check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 100000, totalSalaryAndWages: 20000, contractorExpenses: 0, paymentsToAssociatedPersons: 0 });
  assert.ok(result.reason_codes.includes("w1_not_supplied"));
});

test("salary and wages coded C come out of cost of sales", () => {
  const cos = (salaryAndWagesInCostOfSales) => ratio(check({ industry: "Bakeries and hot bread shops", totalBusinessIncome: 100000, costOfSales: 50000, totalSalaryAndWages: 15000, rentExpenses: 0, salaryAndWagesInCostOfSales }), "cost_of_sales").amount;
  assert.deepEqual([cos(true), cos(false), cos(undefined)], [35000, 50000, null]);
});

test("a cost of sales key range falls back to total expenses where no cost of sales is reported", () => {
  const base = { industry: "Bakeries and hot bread shops", totalBusinessIncome: 100000, totalExpenses: 75000, paymentsToAssociatedPersons: 0 };
  for (const extra of [{}, { costOfSales: 0, salaryAndWagesInCostOfSales: false }]) {
    const result = check({ ...base, ...extra });
    assert.equal(result.keyRatio, "total_expenses");
    assert.ok(result.reason_codes.includes("key_total_expenses_no_cost_of_sales"));
    assert.equal(ratio(result, "total_expenses").key, true);
  }
  const reported = check({ ...base, costOfSales: 1, salaryAndWagesInCostOfSales: false });
  assert.equal(reported.keyRatio, "cost_of_sales");
  assert.ok(reported.reason_codes.includes("cost_of_sales_small_unquantified"));
});

test("a ratio the industry does not publish, or the caller does not supply, is not compared", () => {
  const result = check({ industry: "Plumbing services", totalBusinessIncome: 700000, rentExpenses: 10000 });
  assert.equal(ratio(result, "rent").position, "no_published_range");
  assert.equal(ratio(result, "rent").range, null);
  assert.equal(ratio(result, "labour").position, "not_supplied");
});

test("the result is a comparison, never a compliance finding", () => {
  const result = check({ industry: "Plumbing services", totalBusinessIncome: 704500, totalExpenses: 845650, paymentsToAssociatedPersons: 0 });
  assert.doesNotMatch(JSON.stringify(result), /complian|non-compliant|breach|evasion/i);
  assert.equal(result.guidance.ato_use, pages.ato_guidance.ato_use);
  assert.match(result.attribution, /Creative Commons Attribution 2\.5 Australia/);
  assert.match(result.attribution, /under the ATO's copyright notice \(QC17043/);
});

for (const [label, input, verdict, code] of [
  ["a year the data does not hold", { benchmarkYear: "2024-25", industry: "Coffee shops", totalBusinessIncome: 100000 }, "refused", "benchmark_year"],
  ["an industry the ATO does not publish", { industry: "Coffee shop", totalBusinessIncome: 100000 }, "refused", "industry"],
  ["the industry whose 2 ATO sources disagree", { industry: "Hardware and building supplies retailing", totalBusinessIncome: 500000 }, "refused", "industry_excluded"],
  ["an inherited property name", { industry: "constructor", totalBusinessIncome: 100000 }, "refused", "industry"],
  ["cents", { industry: "Coffee shops", totalBusinessIncome: 100000.5, rentExpenses: 1 }, "unknown", "invalid_amount"],
  ["a negative amount", { industry: "Coffee shops", totalBusinessIncome: 100000, rentExpenses: -1 }, "unknown", "invalid_amount"],
  ["an amount as text", { industry: "Coffee shops", totalBusinessIncome: "100000", rentExpenses: 1 }, "unknown", "invalid_amount"],
  ["a misspelt input", { industry: "Coffee shops", totalBusinessIncome: 100000, rentExpense: 1 }, "unknown", "unknown_input"],
  ["a wages code that is not a boolean", { industry: "Coffee shops", totalBusinessIncome: 100000, salaryAndWagesInCostOfSales: "C" }, "unknown", "invalid_input"],
  ["no total business income", { industry: "Coffee shops", rentExpenses: 1 }, "unknown", "total_business_income"],
  ["zero total business income", { industry: "Coffee shops", totalBusinessIncome: 0, rentExpenses: 1 }, "unknown", "total_business_income"],
  ["associated payments larger than total expenses", { industry: "Coffee shops", totalBusinessIncome: 100000, totalExpenses: 1000, paymentsToAssociatedPersons: 1001 }, "unknown", "negative_amount"],
  ["no ratio's amounts", { industry: "Coffee shops", totalBusinessIncome: 100000 }, "unknown", "no_ratio"],
]) {
  test(`refuses ${label}`, () => {
    const result = compareWithAtoBenchmarks({ benchmarkYear: year, ...input });
    assert.equal(result.verdict, verdict);
    assert.deepEqual(result.reason_codes, [code]);
    assert.equal(result.ratios, null);
  });
}

for (const input of [null, [], "Coffee shops"]) {
  test(`refuses ${JSON.stringify(input)} as input`, () => {
    assert.deepEqual(compareWithAtoBenchmarks(input).reason_codes, ["invalid_input"]);
  });
}

test("every industry's bands adjoin from its lowest band and end open, with each range in order", () => {
  assert.deepEqual([dataset.benchmark_year, pages.benchmark_year], [rules.benchmark_year, rules.benchmark_year]);
  assert.deepEqual(Object.keys(dataset.industries), Object.keys(pages.industries));
  const industries = Object.entries(pages.industries);
  assert.equal(industries.length + Object.keys(rules.data.excluded).length, 100);
  for (const [name, industry] of industries) {
    assert.ok(["cost_of_sales", "total_expenses"].includes(industry.key), name);
    assert.ok([2, 3].includes(industry.bands.length), name);
    assert.equal(dataset.industries[name].bands.length, industry.bands.length, name);
    // Each field sits in the file of its source: cost of sales in the dataset only where it is the key range.
    const keyCostOfSales = industry.key === "cost_of_sales" ? ["cost_of_sales"] : [];
    const pageCostOfSales = industry.key === "cost_of_sales" ? [] : ["cost_of_sales"];
    dataset.industries[name].bands.forEach((band, i) => {
      assert.deepEqual(Object.keys(band), ["label", "from", "to", "total_expenses", ...keyCostOfSales], name);
      assert.deepEqual(Object.keys(industry.bands[i]), [...pageCostOfSales, "labour", "rent", "motor_vehicle"], name);
    });
    assert.deepEqual(Object.keys(dataset.industries[name]), ["bands"], name);
    assert.deepEqual(Object.keys(industry), ["page", "key", "bands"], name);
    bands(name).forEach((band, i, all) => {
      if (i > 0) assert.equal(band.from, all[i - 1].to + 1, name);
      assert.equal(band.to === null, i === all.length - 1, name);
      assert.notEqual(band[industry.key], null, name);
      for (const r of ["total_expenses", "cost_of_sales", "labour", "rent", "motor_vehicle"]) {
        const range = band[r];
        if (range !== null) assert.ok(Number.isInteger(range[0]) && range[0] <= range[1] && range[1] <= 100, `${name} ${r}`);
      }
    });
  }
});
