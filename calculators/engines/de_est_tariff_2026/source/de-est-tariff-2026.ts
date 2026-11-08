// Germany: income tax under the 2026 tariff in § 32a EStG (Grundtarif and splitting), before
// Soli and church tax. Skill: germany-income-tax (rates table copies § 32a(1) EStG 2026).
import { FactReader, taxYearFact, money, ok, rule, type Engine, type EngineSpec } from "./types";

const S = "germany-income-tax";
export const Z1 = rule("ZONE1_GRUNDFREIBETRAG", 12_348, S, "Rates, bands and thresholds", "Tariff zone 1 ... EUR 0 to 12,348: no tax");
export const Z2 = rule("ZONE2", { top: 17_799, a: "914.51", b: "1400" }, S, "Rates, bands and thresholds", "EUR 12,349 to 17,799: (914.51 × y + 1,400) × y, y = (x − 12,348) / 10,000");
export const Z3 = rule("ZONE3", { top: 69_878, a: "173.10", b: "2397", c: "1034.87" }, S, "Rates, bands and thresholds", "EUR 17,800 to 69,878: (173.10 × z + 2,397) × z + 1,034.87, z = (x − 17,799) / 10,000");
export const Z4 = rule("ZONE4", { top: 277_825, r: "0.42", c: "11135.63" }, S, "Rates, bands and thresholds", "EUR 69,879 to 277,825: 0.42 × x − 11,135.63");
export const Z5 = rule("ZONE5", { r: "0.45", c: "19470.38" }, S, "Rates, bands and thresholds", "From EUR 277,826: 0.45 × x − 19,470.38");
export const RND = rule("ROUNDING", "floor x and tax to whole euros", S, "Rates, bands and thresholds", "Taxable income x and the tax are both rounded down to whole euros");
export const SPL = rule("SPLITTING", "2 x tariff(x/2)", S, "Rates, bands and thresholds", "Splitting (joint assessment) | Twice the tax on half the joint taxable income | 2026 | Same, § 32a(5)");
const CONSTS = [Z1, Z2, Z3, Z4, Z5, RND, SPL];

export const spec: EngineSpec = {
  name: "de_est_tariff_2026",
  version: "1.2.0",
  jurisdiction: "DE",
  tax_years: ["2026"],
  summary:
    "Germany 2026 income tax from the § 32a EStG tariff on taxable income (zu versteuerndes Einkommen), Grundtarif or splitting. Excludes solidarity surcharge and church tax.",
  topics: /income tax|einkommensteuer|\bzve\b|zu versteuerndes|\best\b|splitting|grundtarif/,
  facts: {
    taxable_income_zve: { type: "number", required: true, description: "EUR" },
    assessment: { type: "string", required: true, choices: ["single", "joint"], description: "single (Grundtarif) or joint (splitting)" },
    tax_year: taxYearFact(["2026"]),
  },
  outputs: { zve: "EUR (whole euros)", zone: "tariff zone 1-5", income_tax: "EUR (whole euros)" },
};

export const anchors = ["germany-income-tax Example 1: zvE EUR 49,844 -> EUR 10,493", "Example 2: zvE EUR 79,964 -> EUR 22,449"];

// Exact decimal arithmetic (value = n / 10^scale), so the tariff matches the Python
// engine's Decimal computation digit for digit. Every product here is short and exact.
interface Dec { n: bigint; scale: number }
const TEN = BigInt(10);
function dec(s: string | number): Dec {
  const [i, fr = ""] = String(s).split(".");
  return { n: BigInt(i + fr), scale: fr.length };
}
function align(a: Dec, b: Dec): [bigint, bigint, number] {
  const scale = Math.max(a.scale, b.scale);
  return [a.n * TEN ** BigInt(scale - a.scale), b.n * TEN ** BigInt(scale - b.scale), scale];
}
const add = (a: Dec, b: Dec): Dec => { const [x, y, scale] = align(a, b); return { n: x + y, scale }; };
const sub = (a: Dec, b: Dec): Dec => { const [x, y, scale] = align(a, b); return { n: x - y, scale }; };
const mul = (a: Dec, b: Dec): Dec => ({ n: a.n * b.n, scale: a.scale + b.scale });
const div10k = (a: Dec): Dec => ({ n: a.n, scale: a.scale + 4 });
function floorDec(a: Dec): number {
  const d = TEN ** BigInt(a.scale);
  let q = a.n / d;
  if (a.n < BigInt(0) && q * d !== a.n) q -= BigInt(1);
  return Number(q);
}

export function tariff(xIn: number): number {
  const x = Math.floor(xIn);
  const X = dec(x);
  let t: Dec;
  if (x <= Z1.value) {
    t = dec(0);
  } else if (x <= Z2.value.top) {
    const y = div10k(sub(X, dec(Z1.value)));
    t = mul(add(mul(dec(Z2.value.a), y), dec(Z2.value.b)), y);
  } else if (x <= Z3.value.top) {
    const z = div10k(sub(X, dec(Z2.value.top)));
    t = add(mul(add(mul(dec(Z3.value.a), z), dec(Z3.value.b)), z), dec(Z3.value.c));
  } else if (x <= Z4.value.top) {
    t = sub(mul(dec(Z4.value.r), X), dec(Z4.value.c));
  } else {
    t = sub(mul(dec(Z5.value.r), X), dec(Z5.value.c));
  }
  return floorDec(t);
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const x = f.number("taxable_income_zve");
  const a = f.string("assessment", undefined, ["single", "joint"]);
  const tax = a === "single" ? tariff(x) : 2 * tariff(Math.floor(x) / 2);
  const tops = [Z1.value, Z2.value.top, Z3.value.top, Z4.value.top, Infinity];
  const probe = a === "single" ? x : x / 2;
  const zone = tops.findIndex((top) => probe <= top) + 1;
  const kind = a === "single" ? "Grundtarif" : "splitting";
  const steps = [
    `zvE rounded down to whole euros = EUR ${money(Math.floor(x))}`,
    a === "single"
      ? `Grundtarif: zone ${zone} formula of § 32a(1) EStG gives EUR ${money(tax)} (rounded down)`
      : `Splitting: twice the tariff on half the joint zvE (EUR ${money(Math.floor(x) / 2)}, zone ${zone}) = EUR ${money(tax)}`,
  ];
  return ok(
    spec.name,
    { label: `Income tax 2026 (§ 32a EStG, ${kind}), before Soli and church tax`, value: tax, currency: "EUR" },
    { zve: Math.floor(x), zone, income_tax: tax },
    steps,
    CONSTS,
    { taxable_income_zve: x, assessment: a },
    { assumptions: ["zvE is given; no deductions computed here"], anchors },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
