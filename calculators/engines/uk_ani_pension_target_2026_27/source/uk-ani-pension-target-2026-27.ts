// UK: relief-at-source pension contribution needed to bring adjusted net income (ANI) down
// to a target limit, 2026-27. Skill: uk-income-tax-sa100 (ANI definition, RAS gross-up, PA
// taper limit, HICBC limits). The Tax-Free Childcare income limit is NOT served by any
// OpenAccountants skill: that target always returns missing_rule, and no caller-supplied
// limit is accepted.
import { FactReader, taxYearFact, missingRule, money, ok, r2, rule, type Engine, type EngineSpec } from "./types";

const S = "uk-income-tax-sa100";
export const GROSS_UP = rule("RAS_NET_TO_GROSS", 0.8, S, "Worked examples / Example 2: Personal Allowance taper and the Child Benefit charge, England, 2026-27", "pension_gross: pension_net / 0.8");
export const ANI_DEF = rule(
  "ANI_DEFINITION",
  "total taxable income less reliefs, less grossed-up Gift Aid and grossed-up relief-at-source pension contributions",
  S,
  "The taxable base / Step 3: adjusted net income (ITA 2007 s.58)",
  "deduct grossed-up Gift Aid and grossed-up relief-at-source pension contributions",
);
export const PA_TAPER = rule("PA_TAPER_START", 100_000, S, "Rates, bands and thresholds", "Personal Allowance taper (ITA 2007 s.35(2)) | Reduced by half the adjusted net income over GBP 100,000");
export const HICBC_START = rule("HICBC_START", 60_000, S, "Rates, bands and thresholds", "High Income Child Benefit Charge (ITEPA 2003 s.681C) | 1% of Child Benefit per GBP 200 of adjusted net income over GBP 60,000; 100% at GBP 80,000");
const LIMITS: Record<string, typeof PA_TAPER> = { personal_allowance_taper: PA_TAPER, child_benefit_charge_nil: HICBC_START };
const CONSTS = [GROSS_UP, ANI_DEF, PA_TAPER, HICBC_START];
const TARGETS = ["personal_allowance_taper", "child_benefit_charge_nil", "tax_free_childcare"];

export const spec: EngineSpec = {
  name: "uk_ani_pension_target_2026_27",
  version: "1.2.0",
  jurisdiction: "GB",
  tax_years: ["2026-27"],
  summary:
    "UK 2026-27: how much to pay (net) into a relief-at-source personal pension to bring adjusted net income down to a limit. Targets: personal_allowance_taper (GBP 100,000), child_benefit_charge_nil (GBP 60,000), tax_free_childcare (limit not served by any skill: always returns missing_rule until a skill serves it).",
  topics: /adjusted net income|pension contribution|pay into (a|my) pension|childcare|child benefit|personal allowance (taper|back)|60% (tax )?trap|£?100,?000 (trap|taper)/,
  facts: {
    total_taxable_income: { type: "number", required: true, description: "GBP" },
    existing_gross_ras_contributions: { type: "number", required: false, default: 0, description: "GBP" },
    gross_gift_aid: { type: "number", required: false, default: 0, description: "GBP" },
    target: { type: "string", required: true, choices: TARGETS, description: "personal_allowance_taper|child_benefit_charge_nil|tax_free_childcare" },
    tax_year: taxYearFact(["2026-27"]),
  },
  outputs: {
    adjusted_net_income_now: "GBP", limit: "GBP", gross_contribution_needed: "GBP",
    net_payment_needed: "GBP", basic_rate_relief_added_by_provider: "GBP",
  },
};

export const anchors = [
  "uk-income-tax-sa100 Example 2: net GBP 4,000 -> gross GBP 5,000; ANI GBP 107,000; further gross GBP 7,000 restores the allowance at GBP 100,000",
];

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const income = f.number("total_taxable_income");
  const existing = f.number("existing_gross_ras_contributions", 0);
  const ga = f.number("gross_gift_aid", 0);
  const target = f.string("target", undefined, TARGETS);
  const ani = income - existing - ga;
  const used: Record<string, unknown> = { total_taxable_income: income, existing_gross_ras_contributions: existing, gross_gift_aid: ga, target };
  if (target === "tax_free_childcare") {
    // No skill serves this limit, and the caller may not supply one (a model would invent
    // it): always refuse until a skill serves it.
    return missingRule(
      spec.name,
      "Tax-Free Childcare adjusted net income limit (UK, 2026-27)",
      "No OpenAccountants skill states the Tax-Free Childcare income limit. The method is served (gross needed = ANI - limit; net paid = gross x 0.8) but not the limit.",
      CONSTS,
      { partial: { adjusted_net_income_now: r2(ani), formula: "gross_needed = ANI - limit; net_payment = gross_needed x 0.8" }, inputsUsed: used },
    );
  }
  const c = LIMITS[target];
  const limit = c.value;
  const limitSrc = `${c.slug} / ${c.section}`;
  const origin = "OpenAccountants skill";
  const gross = Math.max(ani - limit, 0);
  const net = gross * GROSS_UP.value;
  Object.assign(used, { limit, limit_source: limitSrc, limit_origin: origin });
  const steps = [
    `Adjusted net income now = GBP ${money(income)} less gross pension contributions GBP ${money(existing)} less gross Gift Aid GBP ${money(ga)} = GBP ${money(ani)}`,
    `Limit = GBP ${money(limit)} (${origin})`,
    `Gross contribution needed = GBP ${money(gross)}; the person pays ${GROSS_UP.value * 100}% of that = GBP ${money(net)} and the provider adds GBP ${money(gross - net)} basic rate relief`,
  ];
  return ok(
    spec.name,
    { label: `Net relief-at-source payment needed to reach ANI limit (${target})`, value: r2(net), currency: "GBP" },
    { adjusted_net_income_now: r2(ani), limit, gross_contribution_needed: r2(gross), net_payment_needed: r2(net), basic_rate_relief_added_by_provider: r2(gross - net) },
    steps,
    CONSTS,
    used,
    {
      assumptions: [
        "No other ANI deductions beyond those entered",
        "Contribution within the annual allowance (not checked)",
        "Exactly at the limit; whether the test is 'over' or 'at or over' the limit is not decided here",
      ],
      anchors,
      notes: [`limit origin: ${origin}`],
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
