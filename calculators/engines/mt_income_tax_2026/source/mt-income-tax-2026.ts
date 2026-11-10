// Malta resident income tax on chargeable income, basis years 2025 and 2026. Skill: malta-income-tax.
//
// Tax = chargeable income x rate - subtraction, from the table for the person's status in the
// basis year. The engine picks the table from facts (status, children, nationality); the caller
// never names a table. Basis year 2026 is year of assessment 2027 (Act III of 2026, four child
// tables added); basis year 2025 is year of assessment 2026 (Act IX of 2025, three tables only).
import { FactReader, NeedsInput, missingRule, money, ok, pct, r2, rule, taxYearFact, type Engine, type EngineSpec, type Rule } from "./types";

const S = "malta-income-tax";
const SEC26 = "Resident rate tables, basis year 2026 (year of assessment 2027)";
const SEC25 = "2025 income (year of assessment 2026)";
const SEC_WHO = "Who gets which table";
const H26 = "Status in the basis year | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% above (subtract)";
const H25 = "Status (basis year 2025) | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% above (subtract)";

/** zero: top of the 0% band; bands: [upper limit (null = no limit), rate, subtraction]. */
export interface Table {
  zero: number;
  bands: [number | null, number, number][];
}
const t = (zero: number, s15: [number, number], s25: number, s35: number): Table => ({
  zero,
  bands: [[s15[0], 0.15, s15[1]], [60_000, 0.25, s25], [null, 0.35, s35]],
});

export const SINGLE_26 = rule("SINGLE_2026", t(12_000, [16_000, 1_800], 3_400, 9_400), S, SEC26,
  `${H26}\nSingle (other individual), art. 56(1)(b)(i) | €12,000 | over €12,000 and under €16,000 (€1,800) | over €16,000 and under €60,000 (€3,400) | over €60,000 (€9,400)`);
export const MARRIED0_26 = rule("MARRIED_NO_CHILD_2026", t(15_000, [23_000, 2_250], 4_550, 10_550), S, SEC26,
  `${H26}\nMarried, joint, no qualifying child, art. 56(1)(a)(i) | €15,000 | over €15,000 and under €23,000 (€2,250) | over €23,000 and under €60,000 (€4,550) | over €60,000 (€10,550)`);
export const PARENT0_26 = rule("PARENT_2026", t(13_000, [17_500, 1_950], 3_700, 9_700), S, SEC26,
  `${H26}\nParent, art. 56(1)(b)(ii) | €13,000 | over €13,000 and under €17,500 (€1,950) | over €17,500 and under €60,000 (€3,700) | over €60,000 (€9,700)`);
export const MARRIED1_26 = rule("MARRIED_1_CHILD_2026", t(17_500, [26_500, 2_625], 5_275, 11_275), S, SEC26,
  `${H26}\nMarried, 1 qualifying child, art. 56(1)(a)(ii) | €17,500 | over €17,500 and under €26,500 (€2,625) | over €26,500 and under €60,000 (€5,275) | over €60,000 (€11,275)`);
export const MARRIED2_26 = rule("MARRIED_2_CHILDREN_2026", t(22_500, [32_000, 3_375], 6_575, 12_575), S, SEC26,
  `${H26}\nMarried, 2 or more qualifying children, art. 56(1)(a)(iii) | €22,500 | over €22,500 and under €32,000 (€3,375) | over €32,000 and under €60,000 (€6,575) | over €60,000 (€12,575)`);
// 35% band: the Act's EUR 10,270 (Act III of 2026, art. 19); MTCA's table shows EUR 10,275. Michael, 8 Nov 2026: follow the law.
export const PARENT1_26 = rule("PARENT_1_CHILD_2026", t(14_500, [21_000, 2_175], 4_275, 10_270), S, SEC26,
  `${H26}\nParent, 1 qualifying child, art. 56(1)(b)(iv) | €14,500 | over €14,500 and under €21,000 (€2,175) | over €21,000 and under €60,000 (€4,275) | over €60,000 (€10,270; MTCA's table shows €10,275)`);
export const PARENT2_26 = rule("PARENT_2_CHILDREN_2026", t(18_500, [25_500, 2_775], 5_325, 11_325), S, SEC26,
  `${H26}\nParent, 2 or more qualifying children, art. 56(1)(b)(v) | €18,500 | over €18,500 and under €25,500 (€2,775) | over €25,500 and under €60,000 (€5,325) | over €60,000 (€11,325)`);
export const SINGLE_25 = rule("SINGLE_2025", t(12_000, [16_000, 1_800], 3_400, 9_400), S, SEC25,
  `${H25}\nSingle | €12,000 | €12,000 to €16,000 (€1,800) | €16,000 to €60,000 (€3,400) | over €60,000 (€9,400)`);
export const MARRIED_25 = rule("MARRIED_2025", t(15_000, [23_000, 2_250], 4_550, 10_550), S, SEC25,
  `${H25}\nMarried, joint | €15,000 | €15,000 to €23,000 (€2,250) | €23,000 to €60,000 (€4,550) | over €60,000 (€10,550)`);
export const PARENT_25 = rule("PARENT_2025", t(13_000, [17_500, 1_950], 3_700, 9_700), S, SEC25,
  `${H25}\nParent | €13,000 | €13,000 to €17,500 (€1,950) | €17,500 to €60,000 (€3,700) | over €60,000 (€9,700)`);
export const NO_CHILD_TABLES_2025 = rule("NO_CHILD_TABLES_2025", true, S, SEC25,
  "The four qualifying-child tables do not apply to 2025 income.");
export const CHILD_NATIONALITY = rule("QUALIFYING_CHILD_NATIONALITY", true, S, SEC_WHO,
  "a spouse, the individual, or the individual's spouse must be an EU/EEA national or hold long-term resident status;\nif nobody is an EU/EEA national, the child (or each of the two children) must have been born in Malta and be resident in Malta.");
export const PARENT1_ACT = rule("PARENT_1_CHILD_35_ACT_FIGURE", 10_270, S, SEC26,
  "The Act is the law, so compute with €10,270. Tell the user that MTCA's table shows €10,275");

const CONSTS: Rule[] = [
  SINGLE_26, MARRIED0_26, PARENT0_26, MARRIED1_26, MARRIED2_26, PARENT1_26, PARENT2_26,
  SINGLE_25, MARRIED_25, PARENT_25, NO_CHILD_TABLES_2025, CHILD_NATIONALITY, PARENT1_ACT,
];

const STATUSES = ["single", "married_joint", "parent", "single_parent_sole_custody"];

export const spec: EngineSpec = {
  name: "mt_income_tax_2026",
  version: "1.0.0",
  jurisdiction: "MT",
  tax_years: ["2025", "2026"],
  summary:
    "Malta resident income tax on chargeable income for basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): picks the single, married or parent table, including the 2026 qualifying-child tables, from the person's facts.",
  // Personal tax only: a question about a company or corporate tax never reaches this engine.
  topics: /^(?![\s\S]*\b(?:compan(?:y|y's|ies)|corporat\w*|ltd|limited)\b)[\s\S]*(?:income tax|chargeable income|how much tax|tax (?:bill|liability|due|payable|owed?)|married|parent rate|single rate|tax rates?|tax bands?|salary)/,
  facts: {
    chargeable_income: {
      type: "number",
      required: true,
      description:
        "EUR, after allowable expenses and capital allowances, and WITHOUT income taxed at a final rate (part-time 10%, rent on the 15% option, property transfers). For a joint return, the couple's combined chargeable income",
    },
    resident: { type: "boolean", required: true, description: "resident in Malta in the basis year (non-residents are refused)" },
    status: {
      type: "string",
      required: true,
      choices: STATUSES,
      description:
        "status in the basis year: single; married_joint (married, living together, joint return, the default for a couple); parent (has custody of, or pays maintenance for, a child not over 18, or not over 23 in full-time education); single_parent_sole_custody (refused for now). Spouses filing separately (art. 49A or 50): run once per spouse as single or parent",
    },
    children: {
      type: "number",
      required: false,
      description:
        "needed for married_joint and parent: how many children the person or couple had custody of or paid maintenance for, each not over 18, or not over 23 and in full-time education",
    },
    eu_eea_or_long_term_resident: {
      type: "boolean",
      required: false,
      description: "needed when there are children in basis year 2026: the individual or their spouse is an EU/EEA national or holds long-term resident status",
    },
    children_born_and_resident_in_malta: {
      type: "number",
      required: false,
      description: "needed only when nobody is an EU/EEA national or long-term resident: how many of those children were born in Malta and are resident in Malta",
    },
    tax_paid: { type: "number", required: false, default: 0, description: "EUR already paid for the year: FSS tax deducted by employers plus provisional tax" },
    tax_year: {
      ...taxYearFact(["2025", "2026"]),
      description:
        "the BASIS year: the calendar year the income was earned (2026 income is year of assessment 2027). This engine has figures for basis years 2025 and 2026 only; any other year is refused",
    },
  },
  outputs: { chargeable_income: "EUR", table: "rate table used", tax: "EUR", tax_paid: "EUR", balance_due: "EUR (negative = refund)" },
};

export const anchors = [
  "malta-income-tax Case 1: single, chargeable EUR 31,625 -> tax EUR 4,506.25, balance EUR 1,006.25 after EUR 3,500 paid",
  "malta-income-tax Case 2: married, two children, EUR 40,000 -> EUR 3,425 (2026) against EUR 5,450 (2025)",
];

/** Tax on chargeable income with one table. */
export function taxOn(table: Table, income: number): number {
  if (income <= table.zero) return 0;
  const [, rate, sub] = table.bands.find(([upper]) => upper === null || income < upper)!;
  return income * rate - sub;
}

export function wholeCount(f: FactReader, key: string): number {
  const n = f.number(key);
  if (!Number.isInteger(n)) throw new NeedsInput(`input '${key}' must be a whole number`);
  return n;
}

/**
 * How many of `kids` children qualify for the basis-year-2026 child tables: all of them when the
 * individual or a spouse is an EU/EEA national or long-term resident, otherwise those born in and
 * resident in Malta. Basis year 2025 has no child tables (0). Records the facts read in `used`;
 * returns the rules relied on.
 */
export function qualifyingChildren(f: FactReader, year: string, kids: number, used: Record<string, unknown>): { qualifying: number; consts: Rule[] } {
  const consts: Rule[] = [];
  let qualifying = 0;
  if (year === "2025") {
    if (kids > 0) consts.push(NO_CHILD_TABLES_2025);
  } else if (kids > 0) {
    const eu = f.bool("eu_eea_or_long_term_resident");
    used.eu_eea_or_long_term_resident = eu;
    if (eu) qualifying = kids;
    else {
      const born = wholeCount(f, "children_born_and_resident_in_malta");
      used.children_born_and_resident_in_malta = born;
      qualifying = Math.min(born, kids);
    }
    consts.push(CHILD_NATIONALITY);
  }
  return { qualifying, consts };
}

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const year = f.string("tax_year");
  const income = f.number("chargeable_income");
  const resident = f.bool("resident");
  const status = f.string("status", undefined, STATUSES);
  const paid = f.number("tax_paid", 0);
  const used: Record<string, unknown> = { chargeable_income: income, resident, status, tax_paid: paid };
  const ya = Number(year) + 1;

  if (!resident) {
    return missingRule(spec.name, "non-resident rates engine",
      "A non-resident uses the article 56(1)(c) scale or an EU/EEA proviso; the skill says to refer non-resident cases, so this engine does not compute them.", [], { inputsUsed: used });
  }
  if (status === "single_parent_sole_custody") {
    return missingRule(spec.name, "single parent with sole custody (article 56(1)(b)(iii))",
      "That rule taxes on the married table unless a child table gives less, after four conditions; it is not implemented in this engine yet.", [], { inputsUsed: used });
  }

  let table: Rule<Table>;
  const consts: Rule[] = [];
  const steps: string[] = [`Basis year ${year} is year of assessment ${ya}`];
  if (status === "single") {
    table = year === "2026" ? SINGLE_26 : SINGLE_25;
    steps.push("Status single: the single (other individual) table");
  } else {
    const kids = wholeCount(f, "children");
    used.children = kids;
    if (status === "parent" && kids < 1) {
      throw new NeedsInput("status 'parent' needs at least one child in 'children'; with no child use status 'single'");
    }
    const child = qualifyingChildren(f, year, kids, used);
    const qualifying = child.qualifying;
    consts.push(...child.consts);
    const n = Math.min(qualifying, 2);
    if (status === "married_joint") {
      table = year === "2025" ? MARRIED_25 : [MARRIED0_26, MARRIED1_26, MARRIED2_26][n];
    } else {
      table = year === "2025" ? PARENT_25 : [PARENT0_26, PARENT1_26, PARENT2_26][n];
    }
    steps.push(
      year === "2025"
        ? `Status ${status === "married_joint" ? "married, joint" : "parent"}, basis year 2025: the qualifying-child tables do not apply, so the ${status === "married_joint" ? "married" : "parent"} table`
        : `Status ${status === "married_joint" ? "married, joint" : "parent"} with ${kids} child(ren), ${qualifying} qualifying: the ${table.name.toLowerCase().replace(/_2026$/, "").replace(/_/g, " ")} table`,
    );
  }
  consts.unshift(table);
  used.table = table.name;

  const tax = taxOn(table.value, income);
  const tv = table.value;
  const notes: string[] = [];
  if (table === PARENT1_26 && income >= 60_000) {
    consts.push(PARENT1_ACT);
    notes.push("MTCA's 2026 table shows a subtraction of EUR 10,275 for this band; the Act (Act III of 2026, article 19) says EUR 10,270, which is used here and gives EUR 5 more tax");
  }
  if (income <= tv.zero) steps.push(`Chargeable income EUR ${money(income)} is within the 0% band (up to EUR ${money(tv.zero)}): tax EUR 0.00`);
  else {
    const [, rate, sub] = tv.bands.find(([upper]) => upper === null || income < upper)!;
    steps.push(`Tax = EUR ${money(income)} x ${pct(rate)} - EUR ${money(sub)} = EUR ${money(tax)}`);
  }
  const balance = tax - paid;
  steps.push(`Less tax already paid EUR ${money(paid)} = ${balance >= 0 ? "balance due" : "refund"} EUR ${money(Math.abs(balance))}`);

  return ok(
    spec.name,
    { label: `Malta income tax, basis year ${year} (year of assessment ${ya})`, value: r2(tax), currency: "EUR" },
    { chargeable_income: r2(income), table: table.name, tax: r2(tax), tax_paid: r2(paid), balance_due: r2(balance) },
    steps,
    consts,
    used,
    {
      assumptions: [
        "Chargeable income excludes income taxed at a final rate (part-time 10%, 15% rent option, property transfers)",
        "Resident in Malta, not under a special residence programme, no double tax relief",
        "Social security contributions are not included",
      ],
      anchors,
      notes: [`Return and balance due by 30 June ${ya}${year === "2025" ? " (MTCA extended year of assessment 2026 to 31 July 2026)" : ""}`, ...notes],
    },
  );
}

export const engine: Engine = { spec, anchors, rules: CONSTS, run };
