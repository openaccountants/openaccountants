// US self-employment tax (Schedule SE, regular method), 2025 and 2026.
// Skills: us-federal-return-assembly (2026 wage base, worked Case A),
// us-schedule-c-and-se-computation (2025 rows, examples).
import { FactReader, taxYearFact, missingRule, money, ok, pct, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "us-federal-return-assembly";
export const NEF = rule("NET_EARNINGS_FACTOR", 0.9235, S, "Self-employment tax", "Net earnings | Schedule C net profit × 92.35%");
export const MINNE = rule("MIN_NET_EARNINGS", 400, S, "Self-employment tax", "No SE tax | If net earnings (Schedule SE line 4c) are less than $400");
export const SS = rule("SS_RATE", 0.124, S, "Self-employment tax", "Social security part | 12.4% of net earnings, up to the wage base minus social security wages already taxed");
export const BASE = rule<Record<string, number>>("WAGE_BASE", { "2025": 176_100, "2026": 184_500 }, S, "Self-employment tax", "Wage base | $176,100 for 2025; $184,500 for 2026");
export const MED = rule("MEDICARE_RATE", 0.029, S, "Self-employment tax", "Medicare part | 2.9% of all net earnings, with no cap");
export const HALF = rule("DEDUCTIBLE_SHARE", 0.5, S, "Self-employment tax", "Deduction | Half of SE tax (Schedule SE line 13) goes to Schedule 1 line 15");
const CONSTS = [NEF, MINNE, SS, BASE, MED, HALF];

export const spec: EngineSpec = {
  name: "us_se_tax",
  version: "1.2.0",
  jurisdiction: "US",
  tax_years: ["2025", "2026"],
  summary:
    "US self-employment tax (Schedule SE regular method) for tax year 2025 or 2026: 92.35% of net profit, 12.4% social security up to the wage base less W-2 SS wages, 2.9% Medicare uncapped. Excludes the 0.9% Additional Medicare Tax (Form 8959).",
  topics: /self.?employment tax|schedule se\b|\bse tax\b|seca\b/,
  facts: {
    schedule_c_net_profit: { type: "number", required: true, description: "USD (total of all Schedule C/F)" },
    w2_social_security_wages: { type: "number", required: false, default: 0, description: "USD" },
    tax_year: taxYearFact(["2025", "2026"]),
  },
  outputs: { net_earnings_from_se: "USD", social_security_part: "USD", medicare_part: "USD", se_tax: "USD", deductible_half: "USD" },
};

export const anchors = [
  "us-federal-return-assembly Case A: profit $120,000 -> SE tax $16,955.46 (2025), half $8,477.73",
  "us-schedule-c-and-se-computation Example 2: $102,500 -> $14,483",
];

export function se(profit: number, wages: number, year: string): [number, number, number] {
  const ne = profit * NEF.value;
  if (ne < MINNE.value) return [ne, 0.0, 0.0];
  return [ne, Math.min(ne, Math.max(BASE.value[year] - wages, 0)) * SS.value, ne * MED.value];
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const p = f.number("schedule_c_net_profit");
  const w = f.number("w2_social_security_wages", 0);
  const rawYear = f.get("tax_year");
  const y = rawYear === undefined ? "2026" : String(rawYear);
  const used = { schedule_c_net_profit: p, w2_social_security_wages: w, tax_year: y };
  if (!Object.prototype.hasOwnProperty.call(BASE.value, y)) {
    return missingRule(spec.name, `social security wage base for ${y}`, "Only 2025 and 2026 are served.", CONSTS, { inputsUsed: used });
  }
  const [ne, ss, m] = se(p, w, y);
  const tot = r2(ss + m);
  const steps = [
    `Net earnings from self-employment = ${pct(NEF.value)} x USD ${money(p)} = USD ${money(ne)}`,
    ne < MINNE.value
      ? `Net earnings under USD ${money(MINNE.value)}: no SE tax`
      : `Social security part = ${pct(SS.value)} x min(net earnings, wage base USD ${money(BASE.value[y])} less W-2 wages USD ${money(w)}) = USD ${money(ss)}`,
    `Medicare part = ${pct(MED.value)} x net earnings = USD ${money(m)}`,
    `SE tax = USD ${money(tot)}; deductible half = USD ${money(tot * HALF.value)}`,
  ];
  return ok(
    spec.name,
    { label: `Self-employment tax ${y}`, value: tot, currency: "USD" },
    { net_earnings_from_se: r2(ne), social_security_part: r2(ss), medicare_part: r2(m), se_tax: tot, deductible_half: r2(tot * HALF.value) },
    steps,
    CONSTS,
    used,
    { assumptions: ["Regular Schedule SE method; no church employee income, no optional methods", "Additional Medicare Tax (0.9%, Form 8959) not included"], anchors },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
