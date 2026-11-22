// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026 Ryan Duguid
// Adapted from the author's ato-benchmark-compare ratio and band rules:
// https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare
// Pure, offline comparison. No clock or network.
import rules from "./rules.json" with { type: "json" };
// The ATO's figures sit in 2 files because the ATO released them on 2 sets of terms (see README):
// the dataset's bands, total expenses and key cost of sales ranges, and the pages' other ranges.
import dataset from "./benchmarks-2023-24.json" with { type: "json" };
import pages from "./ato-pages-2023-24.json" with { type: "json" };

const industries = Object.fromEntries(
  Object.entries(pages.industries).map(([name, page]) => [
    name,
    { key: page.key, bands: dataset.industries[name].bands.map((band, i) => ({ ...band, ...page.bands[i] })) },
  ]),
);

const ratioOrder = ["total_expenses", "cost_of_sales", "labour", "rent", "motor_vehicle"];
const amountKeys = [
  "totalBusinessIncome",
  "salesOfGoodsAndServices",
  "totalExpenses",
  "paymentsToAssociatedPersons",
  "costOfSales",
  "totalSalaryAndWages",
  "contractorExpenses",
  "w1",
  "rentExpenses",
  "motorVehicleExpenses",
];
const knownKeys = new Set(["benchmarkYear", "industry", "salaryAndWagesInCostOfSales", ...amountKeys]);

// The amount a ratio divides by turnover, or null when an input it needs is missing.
function numerator(ratio, a, wagesInCostOfSales) {
  const has = (...keys) => keys.every((key) => a[key] !== undefined);
  switch (ratio) {
    case "total_expenses":
      return has("totalExpenses", "paymentsToAssociatedPersons") ? a.totalExpenses - a.paymentsToAssociatedPersons : null;
    case "cost_of_sales":
      if (!has("costOfSales") || wagesInCostOfSales === undefined) return null;
      if (!wagesInCostOfSales) return a.costOfSales;
      return has("totalSalaryAndWages") ? a.costOfSales - a.totalSalaryAndWages : null;
    case "labour": {
      if (!has("totalSalaryAndWages", "contractorExpenses", "paymentsToAssociatedPersons")) return null;
      const wages = a.w1 !== undefined && a.w1 > a.totalSalaryAndWages ? a.w1 : a.totalSalaryAndWages;
      return wages + a.contractorExpenses - a.paymentsToAssociatedPersons;
    }
    case "rent":
      return has("rentExpenses") ? a.rentExpenses : null;
    default:
      return has("motorVehicleExpenses") ? a.motorVehicleExpenses : null;
  }
}

// The ratio in hundredths of a percent, half up: the 2 places the ATO's examples work to (35.92%).
const hundredths = (amount, turnover) => Number((BigInt(amount) * 20000n + BigInt(turnover)) / (2n * BigInt(turnover)));

// That figure against the whole-percentage bounds, inclusive, as the ATO's examples compare it.
function position(hundredthsOfPercent, [min, max]) {
  if (hundredthsOfPercent < min * 100) return "below";
  if (hundredthsOfPercent > max * 100) return "above";
  return "within";
}

/**
 * @param {object} input
 * @param {string} input.benchmarkYear "2023-24", the only year held.
 * @param {string} input.industry An industry name exactly as in ato-pages-2023-24.json `industries`.
 * @param {number} input.totalBusinessIncome Whole dollars, more than 0.
 * @param {number} [input.salesOfGoodsAndServices] Whole dollars; omitted means blank.
 * @param {boolean} [input.salaryAndWagesInCostOfSales] The total salary and wages code is C.
 * Other amounts (whole dollars, 0 or more, each optional): totalExpenses,
 * paymentsToAssociatedPersons, costOfSales, totalSalaryAndWages, contractorExpenses, w1,
 * rentExpenses, motorVehicleExpenses. A ratio whose amounts are not all supplied is not compared.
 * @returns {object} JSON-safe result.
 */
export function compareWithAtoBenchmarks(input) {
  const base = {
    as_of: rules.as_of,
    benchmarkYear: rules.benchmark_year,
    attribution: `${dataset.attribution} ${pages.attribution}`,
    guidance: { ...pages.ato_guidance },
    sources: [...rules.sources],
    limits: [...rules.limits],
    industry: null,
    turnover: null,
    turnoverBasis: null,
    band: null,
    keyRatio: null,
    ratios: null,
  };
  const stop = (verdict, code, reason) => ({ ...base, verdict, reason_codes: [code], reasons: [reason] });
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    return stop("unknown", "invalid_input", "Supply a record with the documented inputs.");
  }
  const unknownKey = Object.keys(input).find((key) => !knownKeys.has(key));
  if (unknownKey !== undefined) return stop("unknown", "unknown_input", `${unknownKey} is not an input of this calculator.`);
  if (input.benchmarkYear !== rules.benchmark_year) {
    return stop("refused", "benchmark_year", `Only the ATO's ${rules.benchmark_year} benchmarks are held.`);
  }
  if (typeof input.industry === "string" && Object.hasOwn(rules.data.excluded, input.industry)) {
    return stop("refused", "industry_excluded", rules.data.excluded[input.industry]);
  }
  if (typeof input.industry !== "string" || !Object.hasOwn(industries, input.industry)) {
    return stop("refused", "industry", "Name an industry exactly as the ATO's benchmarks list it in ato-pages-2023-24.json.");
  }
  const badAmount = amountKeys.find((key) => input[key] !== undefined && !(Number.isSafeInteger(input[key]) && input[key] >= 0));
  if (badAmount !== undefined) return stop("unknown", "invalid_amount", `${badAmount} must be whole dollars, 0 or more.`);
  const wagesFlag = input.salaryAndWagesInCostOfSales;
  if (wagesFlag !== undefined && typeof wagesFlag !== "boolean") {
    return stop("unknown", "invalid_input", "salaryAndWagesInCostOfSales must be true, false or omitted.");
  }
  const income = input.totalBusinessIncome;
  if (!income) return stop("unknown", "total_business_income", "Supply total business income, more than 0.");

  const sales = input.salesOfGoodsAndServices ?? 0;
  const useSales = sales > 0 && sales * 2 >= income;
  const turnover = useSales ? sales : income;
  const industry = industries[input.industry];
  const band = industry.bands.find((b) => turnover >= b.from && (b.to === null || turnover <= b.to));
  if (!band) {
    return stop("refused", "turnover_below_bands", `The ATO publishes no range for turnover under $${industry.bands[0].from.toLocaleString("en-AU")} in this industry.`);
  }
  const amounts = Object.fromEntries(ratioOrder.map((ratio) => [ratio, numerator(ratio, input, wagesFlag)]));
  if (Object.values(amounts).some((amount) => amount !== null && amount < 0)) {
    return stop("unknown", "negative_amount", "A deduction exceeds the amount it comes out of; check the inputs.");
  }
  if (Object.values(amounts).every((amount) => amount === null)) {
    return stop("unknown", "no_ratio", "Supply the amounts for at least one ratio.");
  }

  const reasonCodes = ["caller_supplied_amounts", useSales ? "turnover_sales" : "turnover_total_business_income"];
  const reasons = [
    "Amounts and the industry are the caller's; this calculator has not verified them.",
    useSales
      ? "Turnover is sales of goods and services."
      : "Turnover is total business income: sales are blank, zero or less than 50% of total business income.",
  ];
  let keyRatio = industry.key;
  if (keyRatio === "cost_of_sales") {
    if (!input.costOfSales) {
      keyRatio = "total_expenses";
      reasonCodes.push("key_total_expenses_no_cost_of_sales");
      reasons.push("No cost of sales is reported, so total expenses to turnover is the key range, as the ATO directs.");
    } else {
      reasonCodes.push("cost_of_sales_small_unquantified");
      reasons.push("The ATO says to use total expenses as the key range where cost of sales is only a small amount and does not say how small. Keeping cost of sales as the key range is this calculator's assumption; both are shown.");
    }
  }
  if (amounts.labour !== null && input.w1 === undefined) {
    reasonCodes.push("w1_not_supplied");
    reasons.push("W1 was not supplied: the ATO uses it for labour where it exceeds total salary and wages.");
  }
  const ratios = ratioOrder.map((ratio) => {
    const amount = amounts[ratio];
    const range = band[ratio];
    const shown = amount === null ? null : hundredths(amount, turnover);
    return {
      ratio,
      key: ratio === keyRatio,
      amount,
      percent: shown === null ? null : shown / 100,
      range: range === null ? null : { min: range[0], max: range[1] },
      position: shown === null ? "not_supplied" : range === null ? "no_published_range" : position(shown, range),
    };
  });
  return {
    ...base,
    verdict: "compared",
    reason_codes: reasonCodes,
    reasons,
    industry: input.industry,
    turnover,
    turnoverBasis: useSales ? "sales_of_goods_and_services" : "total_business_income",
    band: { label: band.label, from: band.from, to: band.to },
    keyRatio,
    ratios,
  };
}
