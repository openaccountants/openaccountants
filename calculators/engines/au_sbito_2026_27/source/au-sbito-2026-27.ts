// Australia small business income tax offset (SBITO), 2026-27.
// Skills: au-rates-2026-27, au-individual-return.
import { BRACKETS, taxOn } from "./au-resident-tax-2026-27";
import { FactReader, taxYearFact, money, ok, pct, pyRound, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "au-rates-2026-27";
export const RATE = rule("SBITO_RATE", 0.16, S, "Individual income tax / Offsets and deductions", "SBITO | For eligible individuals with positive taxable income: 16% x (total net small business income / taxable income) x basic income tax liability");
export const CAP = rule("SBITO_CAP", 1_000, S, "Individual income tax / Offsets and deductions", "SBITO | ... capped at $1,000");
export const TURNOVER = rule("SBITO_TURNOVER_LIMIT", 5_000_000, S, "Individual income tax / Offsets and deductions", "SBITO | ... aggregated turnover must be < $5m");
export const METHOD = rule(
  "TAX_ON_NET_SBI_METHOD",
  "basic income tax liability x (net small business income / taxable income)",
  "au-individual-return",
  "Section 1 -- Quick Reference / Small Business Income Tax Offset (SBITO) [T1]; Section 4 -- Worked Examples / Example 1 -- Standard Sole Trader (Graphic Designer)",
  "Rate | 16% of income tax on business income\nbusiness is 100% of income, so 16% x 15,070",
);
const CONSTS = [BRACKETS, RATE, CAP, TURNOVER, METHOD];

export const spec: EngineSpec = {
  name: "au_sbito_2026_27",
  version: "1.4.0",
  jurisdiction: "AU",
  tax_years: ["2026-27"],
  summary:
    "Australia 2026-27 small business income tax offset for an individual resident: 16% of the tax on net small business income, capped at $1,000, aggregated turnover under $5m.",
  topics: /small business (income )?tax offset|\bsbito\b|small business offset/,
  facts: {
    taxable_income: { type: "number", required: true, description: "AUD (all income less deductions)" },
    net_small_business_income: { type: "number", required: true, description: "AUD" },
    aggregated_turnover: { type: "number", required: true, description: "AUD" },
    tax_year: taxYearFact(["2026-27"]),
  },
  outputs: {
    basic_income_tax_liability: "AUD", net_sbi_share_of_taxable_income: "fraction",
    tax_on_net_small_business_income: "AUD", sbito_before_cap: "AUD", sbito: "AUD",
  },
};

export const anchors = ["au-individual-return Example 1: tax $15,070, business 100% of income -> 16% = $2,411, capped at $1,000"];

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const ti = f.number("taxable_income");
  const sbi = f.number("net_small_business_income");
  const turnover = f.number("aggregated_turnover");
  const used = { taxable_income: ti, net_small_business_income: sbi, aggregated_turnover: turnover };
  const head = (v: number) => ({ label: "SBITO 2026-27", value: v, currency: "AUD" });
  if (turnover >= TURNOVER.value) {
    return ok(spec.name, head(0.0), { sbito: 0.0, reason: "turnover not under $5m" },
      [`Aggregated turnover AUD ${money(turnover)} is not under AUD ${money(TURNOVER.value)}: no offset`], CONSTS, used, { anchors });
  }
  if (ti <= 0 || sbi <= 0) {
    return ok(spec.name, head(0.0), { sbito: 0.0 }, ["No taxable income or no net small business income: no offset"], CONSTS, used, { anchors });
  }
  const basic = taxOn(ti);
  const share = Math.min(sbi / ti, 1.0);
  const taxOnSbi = basic * share;
  const off = Math.min(taxOnSbi * RATE.value, CAP.value);
  const steps = [
    `Basic income tax liability on AUD ${money(ti)} at the 2026-27 resident rates = AUD ${money(basic)}`,
    `Share of taxable income that is net small business income = ${pyRound(share, 6)}`,
    `Tax on net small business income = AUD ${money(taxOnSbi)}`,
    `Offset = ${pct(RATE.value)} x AUD ${money(taxOnSbi)} = AUD ${money(taxOnSbi * RATE.value)}, capped at AUD ${money(CAP.value)} = AUD ${money(off)}`,
  ];
  return ok(
    spec.name,
    head(r2(off)),
    {
      basic_income_tax_liability: r2(basic), net_sbi_share_of_taxable_income: pyRound(share, 6),
      tax_on_net_small_business_income: r2(taxOnSbi), sbito_before_cap: r2(taxOnSbi * RATE.value), sbito: r2(off),
    },
    steps,
    CONSTS,
    used,
    {
      assumptions: [
        "Tax on net small business income = basic income tax liability (before offsets) x net small business income / taxable income, the income share capped at 1 (au-rates-2026-27 SBITO row)",
        "Basic income tax liability uses the 2026-27 resident brackets (no Medicare levy)",
      ],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
