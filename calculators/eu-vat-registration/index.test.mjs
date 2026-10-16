import { test } from "node:test";
import assert from "node:assert/strict";
import { assessEuVatRegistration as run, rules } from "./index.mjs";

// The three worked cases from skills/cross-border/eu-oss-digital.md, plus the branches
// that decide registrations: B2B, stock abroad, non-EU goods, missing numbers.

test("EU seller under the EUR 10,000 threshold in both years charges home VAT", () => {
  const r = run({ seller: "eu", supply: "digital_services", customers: "consumers", b2cCrossBorderEurThisYear: 8000, b2cCrossBorderEurLastYear: 6000 });
  assert.equal(r.verdict, "home_vat");
  assert.match(r.headline, /own country's VAT/);
  assert.ok(r.figures.includes("eu_b2c_threshold_eur"));
  assert.ok(r.sources.includes(rules.figures.eu_b2c_threshold_eur.source));
});

test("EU seller over the threshold this year charges destination VAT and is pointed at Union OSS", () => {
  const r = run({ seller: "eu", supply: "digital_services", customers: "consumers", b2cCrossBorderEurThisYear: 12000, b2cCrossBorderEurLastYear: 6000 });
  assert.equal(r.verdict, "destination_vat");
  assert.match(r.actions[0], /Union OSS/);
});

test("the threshold also bites when LAST year was over it", () => {
  const r = run({ seller: "eu", supply: "goods", customers: "consumers", b2cCrossBorderEurThisYear: 2000, b2cCrossBorderEurLastYear: 15000 });
  assert.equal(r.verdict, "destination_vat");
});

test("non-EU seller of digital services has no threshold", () => {
  const r = run({ seller: "non_eu", supply: "digital_services", customers: "consumers", b2cCrossBorderEurThisYear: 500 });
  assert.equal(r.verdict, "destination_vat");
  assert.match(r.headline, /from the first sale/);
  assert.match(r.actions[0], /non-Union OSS/);
});

test("non-EU seller shipping goods into the EU is sent to IOSS with the EUR 150 line", () => {
  const r = run({ seller: "non_eu", supply: "goods", customers: "consumers", goodsShippedFromOutsideEu: true });
  assert.equal(r.verdict, "import_scheme");
  assert.match(r.headline, /EUR 150/);
  assert.ok(r.figures.includes("ioss_consignment_limit_eur"));
});

test("business customers only: the customer accounts for the VAT", () => {
  const r = run({ seller: "eu", supply: "other_services", customers: "businesses" });
  assert.equal(r.verdict, "customer_accounts");
  assert.match(r.reasons[0], /reverse charge/);
});

test("stock held in another member state means local registration, whatever the turnover", () => {
  const r = run({ seller: "eu", supply: "goods", customers: "consumers", b2cCrossBorderEurThisYear: 100, stockInOtherEuCountry: true, viaMarketplace: true });
  assert.equal(r.verdict, "local_registration");
  assert.match(r.reasons.join(" "), /warehouses/);
});

test("without the sales figures the check asks for them instead of guessing", () => {
  const r = run({ seller: "eu", supply: "goods", customers: "consumers" });
  assert.equal(r.verdict, "check_with_accountant");
  assert.equal(r.confidence, "low");
});

test("string inputs from a web form are accepted", () => {
  const r = run({ seller: "eu", supply: "goods", customers: "consumers", b2cCrossBorderEurThisYear: "9999", b2cCrossBorderEurLastYear: "", viaMarketplace: "on" });
  assert.equal(r.verdict, "home_vat");
});

test("every result carries the as-of date, limits and at least one official source", () => {
  for (const input of [
    { seller: "eu", supply: "goods", customers: "consumers", b2cCrossBorderEurThisYear: 1 },
    { seller: "non_eu", supply: "other_services", customers: "consumers" },
    { seller: "eu", supply: "other_services", customers: "consumers" },
  ]) {
    const r = run(input);
    assert.equal(r.as_of, rules.as_of);
    assert.ok(r.limits.length >= 2);
    assert.ok(r.sources.length >= 1 || r.verdict === "check_with_accountant");
  }
});
