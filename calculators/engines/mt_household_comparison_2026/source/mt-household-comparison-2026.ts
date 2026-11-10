// Malta resident married couple, basis years 2025 and 2026: joint against separate computation,
// with and without the 10% part-time final tax on spouse B's part-time self-employment profit.
// Skill: malta-income-tax.
//
// A  joint (article 49): the couple's combined income on the married table for the basis year.
// B  separate (article 49A or 50): each spouse on the article 56(1)(b) single or parent table.
// C  A or B, but spouse B's part-time profit up to the EUR 12,000 cap taxed at the final 10%
//    (article 90A), with any excess left in the return.
// The tables, taxOn and the child test are the mt_income_tax_2026 engine's own, imported, so the
// two engines can never disagree on a figure. Anything the skill does not state is refused.
import {
  MARRIED0_26, MARRIED1_26, MARRIED2_26, MARRIED_25, PARENT0_26, PARENT1_26, PARENT1_ACT, PARENT2_26, PARENT_25, SINGLE_25, SINGLE_26,
  CHILD_NATIONALITY, NO_CHILD_TABLES_2025, qualifyingChildren, taxOn, wholeCount, type Table,
} from "./mt-income-tax-2026";
import { FactReader, NeedsInput, missingRule, money, ok, pct, r2, rule, taxYearFact, type Engine, type EngineSpec, type Rule } from "./types";

const S = "malta-income-tax";
const SEC_WHO = "Who gets which table";
const SEC_PT = "Part-time work final tax";

export const SEPARATE_USES_B_TABLES = rule("SEPARATE_COMPUTATION_TABLES", true, S, SEC_WHO,
  "Married tables (article 56(1)(a)) apply to a married couple resident in Malta and taxed jointly under article 49. If either spouse elected a separate return (article 49A), or the responsible spouse opted for a separate computation (article 50), each spouse uses the article 56(1)(b) tables instead.");
export const PARENT_TABLE_TEST = rule("PARENT_TABLE_TEST", true, S, SEC_WHO,
  "Parent table (article 56(1)(b)(ii)): the individual was a parent who kept a child in custody, or paid maintenance for the child under article 12(1)(t). The child must be not over 18, or not over 23 if in full-time education.");
export const MARRIED_CHILD_CUSTODY = rule("MARRIED_CHILD_TABLES_CUSTODY", true, S, SEC_WHO,
  "for the married tables (a)(ii) and (a)(iii), the couple kept the child (or the two children) in their custody. Maintenance does not count for these tables");
export const PARENT_CHILD_CUSTODY = rule("PARENT_CHILD_TABLES_CUSTODY", true, S, SEC_WHO,
  "for the parent tables (b)(iv) and (b)(v), the individual kept the child in custody (their own child, a spouse's child or a certified cohabitant's child) or paid maintenance for their own child under article 12(1)(t)");
export const CHILD_FALLBACK = rule("CHILD_TABLES_FALLBACK", true, S, SEC_WHO,
  "If any condition fails, fall back to the married (i) or parent (ii) table.");
export const PT_RATE = rule("PART_TIME_FINAL_RATE", 0.1, S, SEC_PT,
  "Rate: 10% from year of assessment 2023 (article 90A(11)). Before that it was 15%. The tax is final, and the income is not declared in the return.");
export const PT_CAP = rule("PART_TIME_SELF_EMPLOYED_CAP", 12_000, S, SEC_PT,
  "Caps (rule 3(2)): the rate covers self-employed profit (article 4(1)(a)) up to €12,000 ... Any excess is declared in the return at normal rates.");
export const PT_SPOUSE = rule("PART_TIME_SPOUSE_EXTENSION", true, S, SEC_PT,
  "Article 90A(9) extends this to a spouse living with a qualifying spouse.");
export const PT_OPT_OUT = rule("PART_TIME_OPT_OUT", true, S, SEC_PT,
  "Opting out: the person may declare all part-time income in the return at progressive rates. Any final tax already paid is then credited or refunded (article 90A(2)).");
export const PT_PAYMENT = rule("PART_TIME_PAYMENT_DATE", "30 April", S, SEC_PT,
  "Paying as a self-employed part-timer: pay the tax by 30 April of the year after the income was earned.");

const IMPORTED: Rule[] = [
  SINGLE_26, MARRIED0_26, PARENT0_26, MARRIED1_26, MARRIED2_26, PARENT1_26, PARENT2_26,
  SINGLE_25, MARRIED_25, PARENT_25, NO_CHILD_TABLES_2025, CHILD_NATIONALITY, PARENT1_ACT,
];
const OWN: Rule[] = [SEPARATE_USES_B_TABLES, PARENT_TABLE_TEST, MARRIED_CHILD_CUSTODY, PARENT_CHILD_CUSTODY, CHILD_FALLBACK, PT_RATE, PT_CAP, PT_SPOUSE, PT_OPT_OUT, PT_PAYMENT];

const ROUTES = ["article_50", "article_49A"];

export const spec: EngineSpec = {
  name: "mt_household_comparison_2026",
  version: "1.0.0",
  jurisdiction: "MT",
  tax_years: ["2025", "2026"],
  summary:
    "Malta resident married couple, basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): compares the joint computation on the married table, separate computation (article 49A or 50) with each spouse on the single or parent table, and either of those with spouse B's part-time self-employment profit taxed at the final 10% (article 90A, up to EUR 12,000), and says which gives the least tax.",
  // A couple (or a separate computation) AND a comparison or the part-time 10% regime; never a
  // company question. A plain married-couple tax question stays with mt_income_tax_2026.
  topics:
    /^(?![\s\S]*\b(?:compan(?:y|y's|ies)|corporat\w*|ltd|limited)\b)(?=[\s\S]*(?:\bcouple\b|spous|married|husband|wife|\bjoint\b|separate (?:computation|return|assessment)|\b49a\b))[\s\S]*(?:compar\w*|\bvs\b|versus|separate|\b49a\b|art(?:icle|\.)? ?50\b|part[- ]time|\b90a\b|\bta22\b|lowest|cheapest|better off|which (?:is|option|one|gives) (?:lower|less|cheaper|better|the least))/,
  facts: {
    spouse_a_chargeable_income: {
      type: "number",
      required: true,
      description: "EUR, spouse A's own chargeable income (after their own expenses and capital allowances), without income taxed at a final rate (15% rent option, property transfers)",
    },
    spouse_b_chargeable_income: {
      type: "number",
      required: true,
      description: "EUR, spouse B's own chargeable income on the same basis, INCLUDING any part-time self-employment profit given in spouse_b_part_time_profit",
    },
    married_resident_living_together: {
      type: "boolean",
      required: true,
      description: "the two spouses were married to each other, both resident in Malta, and living together in the basis year (anything else is refused)",
    },
    children: {
      type: "number",
      required: false,
      description: "how many children the couple kept in their custody in the basis year, each not over 18, or not over 23 and in full-time education (0 if none). Maintenance alone does not count for the married tables",
    },
    eu_eea_or_long_term_resident: {
      type: "boolean",
      required: false,
      description: "needed when there are children in basis year 2026: at least one spouse is an EU/EEA national or holds long-term resident status",
    },
    children_born_and_resident_in_malta: {
      type: "number",
      required: false,
      description: "needed only when neither spouse is an EU/EEA national or long-term resident: how many of those children were born in Malta and are resident in Malta",
    },
    separate_computation_available: {
      type: "boolean",
      required: false,
      description: "needed: the couple can be taxed separately this year (the responsible spouse may opt for a separate computation under article 50, or a separate return election under article 49A is open to them). If false, only the joint options are compared",
    },
    spouse_a_parent: {
      type: "boolean",
      required: false,
      description: "needed for separate computation when there are children: spouse A kept those children in custody (own child, spouse's child or certified cohabitant's child) or paid maintenance for their own child under article 12(1)(t)",
    },
    spouse_b_parent: {
      type: "boolean",
      required: false,
      description: "needed for separate computation when there are children: the same test for spouse B",
    },
    spouse_b_part_time_profit: {
      type: "number",
      required: false,
      default: 0,
      description: "EUR, the part of spouse_b_chargeable_income that is part-time SELF-EMPLOYMENT profit (article 4(1)(a)). Part-time employment income is not handled",
    },
    part_time_eligible: {
      type: "boolean",
      required: false,
      description: "needed when there is part-time profit: spouse B meets the skill's part-time conditions (resident; in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice, or living with a spouse who is; the work registered with Jobsplus, at most two part-time employees, proper books, done for someone other than the full-time employer, VAT-registered unless not required or exempt)",
    },
    separate_route: {
      type: "string",
      required: false,
      choices: ROUTES,
      description: "needed when separate computation and the part-time 10% are both in play: article_50 (the responsible spouse opts for a separate computation) or article_49A (a separate return election)",
    },
    spouse_b_part_time_in_own_right: {
      type: "boolean",
      required: false,
      description: "needed for the article_49A route with part-time profit: spouse B is in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice, and does not qualify only as the spouse of such a person",
    },
    income_or_deductions_to_allocate: {
      type: "boolean",
      required: false,
      default: false,
      description: "either spouse has income other than their own employment or business income (rent, interest, dividends, jointly owned income) or a deduction not tied to one spouse's own income. The skill does not say how these are allocated on separate computation, so the separate options are then refused",
    },
    credits_or_other_deductions: {
      type: "boolean",
      required: false,
      default: false,
      description: "a spouse claims a tax credit (for example a pension or personal retirement scheme credit) or a deduction not already taken off the chargeable incomes above (for example a child or school-fee deduction). Not in the skill, so the whole comparison is refused",
    },
    tax_year: {
      ...taxYearFact(["2025", "2026"]),
      description:
        "the BASIS year: the calendar year the income was earned (2026 income is year of assessment 2027). This engine has figures for basis years 2025 and 2026 only; any other year is refused",
    },
  },
  outputs: {
    options: "each option: status (computed, not_available, missing_rule), the table(s), chargeable income, tax on the return, the 10% final tax, total",
    lowest: "the option key(s) with the least total tax",
    lowest_tax: "EUR",
    saving_against_joint: "EUR, joint total less the lowest total",
  },
};

export const anchors = [
  "malta-income-tax Case 2: married, two children, EUR 40,000 joint -> EUR 3,425 (2026) against EUR 5,450 (2025)",
  "malta-income-tax Case 3: part-time profit EUR 15,000 -> final tax EUR 1,200 on EUR 12,000, EUR 3,000 into the return",
];

type OptionKey = "A_joint" | "B_separate" | "C_joint_10pct" | "C_separate_10pct";
type Option = Record<string, unknown> & { status: "computed" | "not_available" | "missing_rule"; total?: number };
const DESCRIBE: Record<OptionKey, string> = {
  A_joint: "joint computation on the married table",
  B_separate: "separate computation, each spouse on the single or parent table",
  C_joint_10pct: "joint computation with spouse B's part-time profit at the 10% final tax",
  C_separate_10pct: "separate computation with spouse B's part-time profit at the 10% final tax",
};

const tableLabel = (t: Rule<Table>) => `the ${t.name.toLowerCase().replace(/_202[56]$/, "").replace(/_/g, " ")} table`;

export function run(facts: Record<string, unknown>) {
  const f = new FactReader(facts);
  const year = f.string("tax_year");
  const a = f.number("spouse_a_chargeable_income");
  const b = f.number("spouse_b_chargeable_income");
  const couple = f.bool("married_resident_living_together");
  const used: Record<string, unknown> = { spouse_a_chargeable_income: a, spouse_b_chargeable_income: b, married_resident_living_together: couple };
  const ya = Number(year) + 1;

  if (!couple) {
    return missingRule(spec.name, "a couple that is not married, resident in Malta and living together",
      "The skill's married tables and separate computation are for a married couple resident in Malta and living together; it refers non-residents. Use mt_income_tax_2026 for each person on their own.", [], { inputsUsed: used });
  }
  const credits = f.bool("credits_or_other_deductions", false);
  used.credits_or_other_deductions = credits;
  if (credits) {
    return missingRule(spec.name, "tax credits or deductions not already in the chargeable incomes",
      "malta-income-tax does not state the pension or personal retirement scheme credit, child or school-fee deductions, or how a credit or deduction is split between spouses, so the comparison is not computed.", [], { inputsUsed: used });
  }

  const kids = wholeCount(f, "children");
  used.children = kids;
  const child = qualifyingChildren(f, year, kids, used);
  const n = Math.min(child.qualifying, 2);
  const separate = f.bool("separate_computation_available");
  used.separate_computation_available = separate;
  const pt = f.number("spouse_b_part_time_profit", 0);
  used.spouse_b_part_time_profit = pt;
  if (pt > b) throw new NeedsInput("input 'spouse_b_part_time_profit' must not be more than 'spouse_b_chargeable_income', which includes it");
  let eligible = false;
  if (pt > 0) {
    eligible = f.bool("part_time_eligible");
    used.part_time_eligible = eligible;
  }
  const allocate = f.bool("income_or_deductions_to_allocate", false);
  used.income_or_deductions_to_allocate = allocate;

  const consts: Rule[] = [];
  const cite = (...rs: Rule[]) => { for (const r of rs) if (!consts.includes(r)) consts.push(r); };
  const steps: string[] = [`Basis year ${year} is year of assessment ${ya}; status, custody and residence are tested in the basis year`];
  const notes: string[] = [];
  let parent1High = false;

  const taxLine = (who: string, t: Rule<Table>, income: number): number => {
    cite(t);
    const tax = r2(taxOn(t.value, income));
    if (income <= t.value.zero) steps.push(`${who}: EUR ${money(income)} on ${tableLabel(t)} is within the 0% band (up to EUR ${money(t.value.zero)}): EUR 0.00`);
    else {
      const [, rate, sub] = t.value.bands.find(([upper]) => upper === null || income < upper)!;
      steps.push(`${who}: EUR ${money(income)} on ${tableLabel(t)}: EUR ${money(income)} x ${pct(rate)} - EUR ${money(sub)} = EUR ${money(tax)}`);
    }
    if (t === PARENT1_26 && income >= 60_000) parent1High = true;
    return tax;
  };

  // The married table: the 2026 child tables need the couple's custody (kept in `children`).
  const married: Rule<Table> = year === "2025" ? MARRIED_25 : [MARRIED0_26, MARRIED1_26, MARRIED2_26][n];
  if (kids > 0) {
    cite(...child.consts);
    if (year === "2026") {
      cite(MARRIED_CHILD_CUSTODY);
      if (child.qualifying < kids) cite(CHILD_FALLBACK);
    }
  }
  steps.push(year === "2025"
    ? "Joint: basis year 2025 has no qualifying-child tables, so the married table"
    : `Joint: ${kids} child(ren) in the couple's custody, ${child.qualifying} qualifying: ${tableLabel(married)}`);

  const options = {} as Record<OptionKey, Option>;
  const refusals: string[] = [];

  // A: joint.
  const jointTax = taxLine("A, joint", married, a + b);
  options.A_joint = { status: "computed", chargeable_income: r2(a + b), table: married.name, tax_on_return: jointTax, final_tax: 0, total: jointTax };
  if (pt > 0) cite(PT_OPT_OUT);

  // Per-spouse table on separate computation (article 56(1)(b)).
  let tableA: Rule<Table> | null = null;
  let tableB: Rule<Table> | null = null;
  const spouseTable = (key: "spouse_a_parent" | "spouse_b_parent"): Rule<Table> => {
    if (kids === 0) return year === "2025" ? SINGLE_25 : SINGLE_26;
    const parent = f.bool(key);
    used[key] = parent;
    if (!parent) return year === "2025" ? SINGLE_25 : SINGLE_26;
    cite(PARENT_TABLE_TEST);
    if (year === "2025") return PARENT_25;
    cite(PARENT_CHILD_CUSTODY);
    return [PARENT0_26, PARENT1_26, PARENT2_26][n];
  };

  if (!separate) {
    const why = "separate computation is not available to this couple (separate_computation_available is false)";
    options.B_separate = { status: "not_available", reason: why };
  } else if (allocate) {
    const why = "the skill does not say how income other than each spouse's own employment or business income, or a shared deduction, is allocated between spouses on separate computation";
    options.B_separate = { status: "missing_rule", reason: why };
    refusals.push("B_separate");
  } else {
    cite(SEPARATE_USES_B_TABLES);
    tableA = spouseTable("spouse_a_parent");
    tableB = spouseTable("spouse_b_parent");
    steps.push(`Separate: each spouse uses the article 56(1)(b) tables: spouse A ${tableLabel(tableA)}, spouse B ${tableLabel(tableB)}`);
    const ta = taxLine("B, separate, spouse A", tableA, a);
    const tb = taxLine("B, separate, spouse B", tableB, b);
    options.B_separate = {
      status: "computed",
      spouse_a: { chargeable_income: r2(a), table: tableA.name, tax: ta },
      spouse_b: { chargeable_income: r2(b), table: tableB.name, tax: tb },
      final_tax: 0,
      total: r2(ta + tb),
    };
  }

  // C: the part-time 10% final tax on spouse B's profit, up to the cap.
  if (pt === 0 || !eligible) {
    const why = pt === 0 ? "spouse B has no part-time self-employment profit" : "spouse B does not meet the part-time conditions (part_time_eligible is false)";
    options.C_joint_10pct = { status: "not_available", reason: why };
    options.C_separate_10pct = { status: "not_available", reason: why };
  } else {
    cite(PT_SPOUSE, PT_RATE, PT_CAP, PT_PAYMENT);
    const at10 = Math.min(pt, PT_CAP.value);
    const excess = r2(pt - at10);
    const finalTax = r2(at10 * PT_RATE.value);
    steps.push(`Part-time: EUR ${money(at10)} of spouse B's EUR ${money(pt)} part-time profit (cap EUR ${money(PT_CAP.value)}) x ${pct(PT_RATE.value)} = EUR ${money(finalTax)} final tax; EUR ${money(excess)} stays in the return`);
    const cj = taxLine("C, joint", married, a + b - at10);
    options.C_joint_10pct = {
      status: "computed", part_time_at_10pct: r2(at10), final_tax: finalTax, excess_to_return: excess,
      chargeable_income: r2(a + b - at10), table: married.name, tax_on_return: cj, total: r2(cj + finalTax),
    };
    if (!separate) {
      options.C_separate_10pct = { status: "not_available", reason: "separate computation is not available to this couple (separate_computation_available is false)" };
    } else if (allocate) {
      options.C_separate_10pct = { status: "missing_rule", reason: "as for B_separate: the allocation between spouses on separate computation is not stated in the skill" };
      refusals.push("C_separate_10pct");
    } else {
      const route = f.string("separate_route", undefined, ROUTES);
      used.separate_route = route;
      let refuse = false;
      if (route === "article_49A") {
        const own = f.bool("spouse_b_part_time_in_own_right");
        used.spouse_b_part_time_in_own_right = own;
        refuse = !own;
      }
      if (refuse) {
        options.C_separate_10pct = {
          status: "missing_rule",
          reason: "the skill says article 90A(9) extends the part-time regime to a spouse living with a qualifying spouse, but not whether that holds on an article 49A separate return; Cap. 123 article 90A(9) excludes spouses whose separate return election is effective. Not computed",
        };
        refusals.push("C_separate_10pct");
      } else {
        const sa = taxLine("C, separate, spouse A", tableA!, a);
        const sb = taxLine("C, separate, spouse B", tableB!, b - at10);
        options.C_separate_10pct = {
          status: "computed", part_time_at_10pct: r2(at10), final_tax: finalTax, excess_to_return: excess,
          spouse_a: { chargeable_income: r2(a), table: tableA!.name, tax: sa },
          spouse_b: { chargeable_income: r2(b - at10), table: tableB!.name, tax: sb },
          total: r2(sa + sb + finalTax),
        };
      }
    }
  }

  if (parent1High) {
    cite(PARENT1_ACT);
    notes.push("MTCA's 2026 table shows a subtraction of EUR 10,275 for the parent one-child 35% band; the Act (Act III of 2026, article 19) says EUR 10,270, which is used here and gives EUR 5 more tax");
  }

  const computed = (Object.keys(options) as OptionKey[]).filter((k) => options[k].status === "computed");
  if (refusals.length > 0) {
    const what = refusals.includes("C_separate_10pct") && !refusals.includes("B_separate")
      ? "the part-time 10% final tax on an article 49A separate return for a spouse who qualifies only through the other spouse"
      : "how income or deductions are allocated between spouses on separate computation";
    return missingRule(spec.name, what,
      `${refusals.join(" and ")} cannot be computed from the skill (${options[refusals[0] as OptionKey].reason}), so the lowest option cannot be named. The other options are in partial.`,
      consts, { partial: { options }, inputsUsed: used });
  }

  const lowestTax = Math.min(...computed.map((k) => options[k].total!));
  const lowest = computed.filter((k) => options[k].total === lowestTax);
  for (const k of computed) steps.push(`${k} (${DESCRIBE[k]}): total EUR ${money(options[k].total!)}`);
  steps.push(lowest.length > 1
    ? `Lowest: ${lowest.join(" and ")} tie at EUR ${money(lowestTax)}`
    : `Lowest: ${lowest[0]}, EUR ${money(lowestTax)}, EUR ${money(r2(options.A_joint.total! - lowestTax))} less than the joint computation`);
  if (pt > 0 && eligible) notes.push(`The 10% part-time tax is paid by 30 April ${ya} with a statement of accounts; the return and its balance by 30 June ${ya}${year === "2025" ? " (MTCA extended year of assessment 2026 to 31 July 2026)" : ""}`);
  else notes.push(`Return and balance due by 30 June ${ya}${year === "2025" ? " (MTCA extended year of assessment 2026 to 31 July 2026)" : ""}`);

  return ok(
    spec.name,
    { label: `Lowest total tax for the couple, basis year ${year} (year of assessment ${ya}): ${lowest.map((k) => DESCRIBE[k]).join(" or ")}`, value: lowestTax, currency: "EUR" },
    { options, lowest, lowest_tax: lowestTax, saving_against_joint: r2(options.A_joint.total! - lowestTax) },
    steps,
    consts,
    used,
    {
      assumptions: [
        "Each spouse's chargeable income is their own, after their own expenses and capital allowances, and leaves out other final-tax income (15% rent option, property transfers)",
        "The children are the couple's children in their custody; a child outside the household for whom a spouse pays maintenance is not handled",
        "Spouse B's part-time income is self-employment profit; part-time employment income (EUR 10,000 cap) and part-time income of spouse A are not handled",
        "No tax credits; social security contributions are not included; resident, not under a special residence programme, no double tax relief",
      ],
      anchors,
      notes,
    },
  );
}

export const engine: Engine = { spec, anchors, rules: [...IMPORTED, ...OWN], run };
