// Dutch corporate income tax (Vpb) on a taxable amount, 2026. Skill: nl-corporate-tax.
import { FactReader, taxYearFact, money, ok, pct, pyRound, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "nl-corporate-tax";
export const BRACKET = rule("BRACKET", 200_000, S, "Rates, bands and thresholds", "Vpb on taxable amount up to and including EUR 200,000 (Wet Vpb art. 22) | 19%");
export const LOW = rule("LOW_RATE", 0.19, S, "Rates, bands and thresholds", "up to and including EUR 200,000 ... 19% | 2026");
export const HIGH = rule("HIGH_RATE", 0.258, S, "Rates, bands and thresholds", "above EUR 200,000 (art. 22: EUR 38,000 plus 25.8% of the excess) | 25.8% | 2026");
const CONSTS = [BRACKET, LOW, HIGH];

export const spec: EngineSpec = {
  name: "nl_vpb_2026",
  version: "1.2.0",
  jurisdiction: "NL",
  tax_years: ["2026"],
  summary:
    "Netherlands corporate income tax (vennootschapsbelasting) for 2026 on a BV/NV's taxable amount (after loss offset and exemptions).",
  topics: /corporate (income )?tax|\bvpb\b|vennootschapsbelasting|\bcit\b|corporation tax/,
  facts: {
    taxable_amount: { type: "number", required: true, description: "EUR, taxable amount after losses/participation exemption/innovation box" },
    tax_year: taxYearFact(["2026"]),
  },
  outputs: { tax_at_19pct: "EUR", tax_at_25_8pct: "EUR", vpb_total: "EUR", effective_rate: "fraction" },
};

export const anchors = [
  "Rates table: tax at EUR 200,000 = EUR 38,000",
  "Example 1: EUR 425,000 -> EUR 96,050",
  "Example 2: EUR 2,020,000 -> EUR 507,560",
];

export function vpb(x: number): number {
  return Math.min(x, BRACKET.value) * LOW.value + Math.max(x - BRACKET.value, 0) * HIGH.value;
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const x = f.number("taxable_amount");
  const low = Math.min(x, BRACKET.value) * LOW.value;
  const high = Math.max(x - BRACKET.value, 0) * HIGH.value;
  const total = r2(low + high);
  const steps = [
    `${pct(LOW.value)} on the first EUR ${money(Math.min(x, BRACKET.value))} = EUR ${money(low)}`,
    `${pct(HIGH.value)} on the excess over EUR ${money(BRACKET.value)} (EUR ${money(Math.max(x - BRACKET.value, 0))}) = EUR ${money(high)}`,
    `Vpb payable = EUR ${money(total)}`,
  ];
  return ok(
    spec.name,
    { label: "Vpb payable for 2026", value: total, currency: "EUR" },
    { tax_at_19pct: r2(low), tax_at_25_8pct: r2(high), vpb_total: total, effective_rate: x ? pyRound(total / x, 6) : 0 },
    steps,
    CONSTS,
    { taxable_amount: x },
    {
      assumptions: ["Calendar-year 2026 financial year", "Input is the taxable amount after loss offset, participation exemption and innovation box"],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
