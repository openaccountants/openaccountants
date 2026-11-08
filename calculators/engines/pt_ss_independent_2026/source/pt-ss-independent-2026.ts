// Portugal self-employed (trabalhador independente), quarterly regime: monthly social security
// contribution, 2026. Skill: pt-social-contributions.
import { FactReader, taxYearFact, factsSchema, money, ok, pct, pyRound, r2, rule, type Engine, type EngineSpec, type NeedsInputOutput } from "./types";

const S = "pt-social-contributions";
export const IAS = rule("IAS_2026", 537.13, S, "Rates, bands and thresholds", "IAS | EUR 537.13 | 2026 | Portaria 480-A/2025/1");
export const RATE = rule("SELF_EMPLOYED_RATE", 0.214, S, "Rates, bands and thresholds", "Self-employed rate | 21.4% | 2026 | Code art. 168(1)");
export const RATE_ENI = rule("ENI_EIRL_RATE", 0.252, S, "Rates, bands and thresholds", "Empresário em nome individual, EIRL holder and their spouses | 25.2% | 2026 | Code art. 168(4)");
export const SERV = rule("SERVICES_FACTOR", 0.7, S, "Rates, bands and thresholds", "Relevant income: services | 70% of the quarter's service income | 2026 | Code art. 162(1)(a)");
export const GOODS = rule("GOODS_FACTOR", 0.2, S, "The taxable base", "Segurança Social computes relevant income: 70% of services plus 20% of goods (art. 162(1))");
export const BASE = rule("MONTHLY_BASE_FRACTION", 1 / 3, S, "Rates, bands and thresholds", "Monthly base | 1/3 of the quarter's relevant income, for the declaration month and the next two | 2026 | Code art. 163(1)");
export const CEIL = rule("BASE_CEILING", 6_445.56, S, "Rates, bands and thresholds", "Ceiling on the monthly base | 12 x IAS = EUR 6,445.56 | 2026 | Code art. 163(5)");
export const MIN = rule("MIN_CONTRIBUTION", 20.0, S, "Rates, bands and thresholds", "Minimum contribution | EUR 20.00 a month when there is no income or the result is below EUR 20 | 2026 | Code art. 163(2)");
const CONSTS = [IAS, RATE, RATE_ENI, SERV, GOODS, BASE, CEIL, MIN];

export const spec: EngineSpec = {
  name: "pt_ss_independent_2026",
  version: "1.2.0",
  jurisdiction: "PT",
  tax_years: ["2026"],
  summary:
    "Portugal 2026: monthly social security contribution of a self-employed worker (quarterly regime) from the quarter's declared service/goods income; applies to the declaration month and the next two.",
  topics: /social security|seguran[cç]a social|contribui[cç]|trabalhador independente|recibos verdes|self.?employed contribution/,
  facts: {
    quarter_services_income: { type: "number", required: true, description: "EUR" },
    quarter_goods_income: { type: "number", required: false, default: 0, description: "EUR" },
    is_eni_or_eirl: { type: "boolean", required: false, default: false, description: "empresário em nome individual or EIRL holder (or their spouse)" },
    base_adjustment_pct: { type: "number", required: false, default: 0, description: "between -25 and 25 (art. 164 option)" },
    exempt: { type: "boolean", required: false, default: false, description: "first 12 months, employment exemption, pension, etc." },
    tax_year: taxYearFact(["2026"]),
  },
  outputs: { relevant_income: "EUR", monthly_base: "EUR", rate: "fraction", monthly_contribution: "EUR", three_months_total: "EUR" },
};

export const anchors = [
  "pt-social-contributions Example 1: EUR 9,000 services in a quarter -> relevant EUR 6,300, base EUR 2,100, EUR 449.40 a month",
  "Ceiling 12 x IAS = EUR 6,445.56",
];

export function monthly(services: number, goods: number, eni = false, adj = 0.0): [number, number, number] {
  const relevant = services * SERV.value + goods * GOODS.value;
  const base = Math.min(relevant * BASE.value * (1 + adj / 100), CEIL.value);
  return [relevant, base, Math.max(MIN.value, pyRound(base * (eni ? RATE_ENI.value : RATE.value), 2))];
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const s = f.number("quarter_services_income");
  const g = f.number("quarter_goods_income", 0);
  const eni = f.bool("is_eni_or_eirl", false);
  // base_adjustment_pct may be negative, so it is read raw (as the Python engine does).
  const rawAdj = f.get("base_adjustment_pct");
  const adj = rawAdj || 0;
  const exempt = f.bool("exempt", false);
  const used = { quarter_services_income: s, quarter_goods_income: g, is_eni_or_eirl: eni, base_adjustment_pct: adj, exempt };
  if (typeof adj !== "number" || !Number.isFinite(adj) || adj < -25 || adj > 25) {
    const out: NeedsInputOutput = { status: "needs_input", engine: spec.name, what: "base_adjustment_pct must be between -25 and 25", schema: factsSchema(spec) };
    return out;
  }
  if (exempt) {
    return ok(spec.name, { label: "Monthly contribution", value: 0.0, currency: "EUR" }, { monthly_contribution: 0.0, reason: "exempt" },
      ["Exempt from contributions: EUR 0.00 a month"], CONSTS, used, { anchors });
  }
  const [relevant, base, m] = monthly(s, g, eni, adj);
  const rate = eni ? RATE_ENI.value : RATE.value;
  const steps = [
    `Relevant income = ${pct(SERV.value)} of services EUR ${money(s)} + ${pct(GOODS.value)} of goods EUR ${money(g)} = EUR ${money(relevant)}`,
    `Monthly base = one third of relevant income${adj ? `, adjusted by ${adj}%` : ""}, capped at EUR ${money(CEIL.value)} = EUR ${money(base)}`,
    `Monthly contribution = ${pct(rate)} x EUR ${money(base)} = EUR ${money(m)} (minimum EUR ${money(MIN.value)})`,
    `For the declaration month and the next two: EUR ${money(m * 3)}`,
  ];
  return ok(
    spec.name,
    { label: "Monthly contribution for the declaration month and the next two", value: m, currency: "EUR" },
    { relevant_income: r2(relevant), monthly_base: r2(base), rate, monthly_contribution: m, three_months_total: r2(m * 3) },
    steps,
    CONSTS,
    used,
    {
      assumptions: ["Quarterly regime (simplified regime, not organised accounts)", "Paid between the 10th and 20th of the following month (art. 155(2))"],
      anchors,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
