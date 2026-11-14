// Shared types and helpers for the calculation engines behind the MCP `compute` tool.
//
// An engine is a pure function run(facts) -> EngineOutput. It decides the tax rules
// itself and asks the caller only for facts. Every figure it uses is a Rule taken from
// an OpenAccountants skill (slug, section and the quoted line), and when a skill does
// not serve a figure the engine refuses with status "missing_rule" instead of guessing.
//
// Ported from the tested Python engines of the 6 Nov 2026 A/B test (common.py). Output
// numbers must match the Python engines to the cent: see pyRound and the parity test.

/** A constant taken from a skill, with where it came from. */
export interface Rule<T = unknown> {
  name: string;
  value: T;
  slug: string;
  section: string;
  quote: string;
}

export function rule<T>(name: string, value: T, slug: string, section: string, quote: string): Rule<T> {
  return { name, value, slug, section, quote };
}

export type FactType = "number" | "boolean" | "string";

export interface FactSpec {
  type: FactType;
  description: string;
  required: boolean;
  default?: number | boolean | string;
  choices?: string[];
}

export interface EngineSpec {
  name: string;
  /** Bumped whenever a constant or the method changes; part of every receipt. */
  version: string;
  /** ISO country code the engine serves (matches start()'s resolved jurisdiction). */
  jurisdiction: string;
  /** The tax year(s) its constants are for ("2026" or "2026-27"). Any other year is refused. */
  tax_years: string[];
  summary: string;
  /** Lower-case question words that point a computation question at this engine. */
  topics: RegExp;
  facts: Record<string, FactSpec>;
  outputs: Record<string, string>;
  /** For return engines: the item categories the caller sorts items into. */
  categories?: Record<string, string>;
}

export interface OkOutput {
  status: "ok";
  engine: string;
  headline: { label: string; value: number; currency: string };
  lines: Record<string, unknown>;
  steps: string[];
  inputs_used: Record<string, unknown>;
  constants_used: Rule[];
  assumptions: string[];
  skill_anchors_reproduced: string[];
  notes: string[];
  /** Optional facts the caller left out, with the default the engine used (set by the registry). */
  defaults_assumed?: Record<string, unknown>;
  /** The tax year the figures are for, as checked by the registry's year guard. */
  tax_year?: string;
}

export interface MissingRuleOutput {
  status: "missing_rule";
  engine: string;
  what: string;
  why: string;
  partial: Record<string, unknown>;
  inputs_used: Record<string, unknown>;
  constants_used: Rule[];
  instruction: string;
  defaults_assumed?: Record<string, unknown>;
  tax_year?: string;
}

export interface NeedsInputOutput {
  status: "needs_input";
  engine: string;
  what: string;
  schema: Record<string, unknown>;
}

export type EngineOutput = OkOutput | MissingRuleOutput | NeedsInputOutput;

export interface Engine {
  spec: EngineSpec;
  /** The skill worked examples this engine reproduces (asserted in the tests). */
  anchors: string[];
  /** Every Rule the engine uses, so the quote drift check can read them without running facts. */
  rules: Rule[];
  run(facts: Record<string, unknown>): EngineOutput;
}

/** The tax_year fact every engine takes (required; checked by the registry's year guard). */
export function taxYearFact(years: string[]): FactSpec {
  const split = years.every((y) => /^\d{4}-\d{2}$/.test(y));
  return {
    type: "string",
    required: true,
    choices: years,
    description: `the tax year the question is about${split ? ", written YYYY-YY" : ""}. This engine has figures for ${years.join(" and ")} only; any other year is refused`,
  };
}

/** Thrown by FactReader; the registry turns it into a needs_input response. */
export class NeedsInput extends Error {}

const MISSING_INSTRUCTION =
  "No OpenAccountants skill serves this figure. Do not invent it: say it is missing, or cite an official source you fetched yourself and label it as not from OpenAccountants.";

/**
 * Python's round(x, nd): rounds the EXACT binary value of x half-to-even. Math.round
 * and toFixed round ties up, so they differ from the Python engines on values such as
 * 0.125. toFixed(100) yields the exact decimal expansion of a double (it is exact for
 * every magnitude these engines meet), and the half-even step is done on its digits.
 */
export function pyRound(x: number, nd = 0): number {
  if (!Number.isFinite(x) || x === 0) return x + 0;
  if (Math.abs(x) >= 1e21) return x;
  const neg = x < 0;
  const [ip, fp] = Math.abs(x).toFixed(100).split(".");
  let digits = BigInt(ip + fp.slice(0, nd));
  const rest = fp.slice(nd);
  const first = rest.charCodeAt(0) - 48;
  const tailNonZero = /[1-9]/.test(rest.slice(1));
  if (first > 5 || (first === 5 && (tailNonZero || digits % BigInt(2) === BigInt(1)))) digits += BigInt(1);
  const s = digits.toString().padStart(nd + 1, "0");
  const v = Number(nd > 0 ? `${s.slice(0, -nd)}.${s.slice(-nd)}` : s);
  return neg ? -v : v + 0;
}

/** Round to the cent, as the Python engines do (round(x + 0.0, 2)). */
export function r2(x: number): number {
  return pyRound(x + 0, 2);
}

/** "12,345.67" for steps. Display only; the figure itself is r2(x). */
export function money(x: number): string {
  return r2(x).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

/** "25.8%" for steps. */
export function pct(rate: number): string {
  return `${Number((rate * 100).toFixed(4))}%`;
}

function pyList(items: string[]): string {
  return `[${items.map((c) => `'${c}'`).join(", ")}]`;
}

/**
 * Reads and validates facts with the same rules and messages as the Python `need()`:
 * a fact that is absent or null takes its default; with no default it is missing.
 * Numbers must be finite and not negative; booleans must be true or false.
 */
export class FactReader {
  constructor(private readonly raw: Record<string, unknown>) {}

  private present(key: string): boolean {
    return Object.prototype.hasOwnProperty.call(this.raw, key) && this.raw[key] !== null && this.raw[key] !== undefined;
  }

  number(key: string, dflt?: number): number;
  number(key: string, dflt: null): number | null;
  number(key: string, dflt?: number | null): number | null {
    if (!this.present(key)) {
      if (dflt === undefined) throw new NeedsInput(`missing input '${key}'`);
      return dflt;
    }
    const v = this.raw[key];
    if (typeof v !== "number" || !Number.isFinite(v)) throw new NeedsInput(`input '${key}' must be a number`);
    if (v < 0) throw new NeedsInput(`input '${key}' must not be negative`);
    return v + 0;
  }

  bool(key: string, dflt?: boolean): boolean {
    if (!this.present(key)) {
      if (dflt === undefined) throw new NeedsInput(`missing input '${key}'`);
      return dflt;
    }
    const v = this.raw[key];
    if (typeof v !== "boolean") throw new NeedsInput(`input '${key}' must be true or false`);
    return v;
  }

  string(key: string, dflt?: string, choices?: string[]): string {
    if (!this.present(key)) {
      if (dflt === undefined) throw new NeedsInput(`missing input '${key}'`);
      return dflt;
    }
    const v = this.raw[key];
    // Stricter than the Python engines, which str() any value: a fact that is not
    // text is asked for again rather than coerced.
    if (typeof v !== "string") throw new NeedsInput(`input '${key}' must be text`);
    if (choices && !choices.includes(v)) throw new NeedsInput(`input '${key}' must be one of ${pyList(choices)}`);
    return v;
  }

  /** The raw value, unvalidated (for the few facts the Python engines read with .get()). */
  get(key: string): unknown {
    return this.raw[key];
  }
}

export function ok(
  engine: string,
  headline: { label: string; value: number; currency: string },
  lines: Record<string, unknown>,
  steps: string[],
  consts: Rule[],
  inputsUsed: Record<string, unknown>,
  opts: { assumptions?: string[]; anchors?: string[]; notes?: string[] } = {},
): OkOutput {
  return {
    status: "ok",
    engine,
    headline,
    lines,
    steps,
    inputs_used: inputsUsed,
    constants_used: consts,
    assumptions: opts.assumptions ?? [],
    skill_anchors_reproduced: opts.anchors ?? [],
    notes: opts.notes ?? [],
  };
}

export function missingRule(
  engine: string,
  what: string,
  why: string,
  consts: Rule[] = [],
  opts: { partial?: Record<string, unknown>; inputsUsed?: Record<string, unknown> } = {},
): MissingRuleOutput {
  return {
    status: "missing_rule",
    engine,
    what,
    why,
    partial: opts.partial ?? {},
    inputs_used: opts.inputsUsed ?? {},
    constants_used: consts,
    instruction: MISSING_INSTRUCTION,
  };
}

/** JSON-Schema form of an engine's facts, returned with needs_input. */
export function factsSchema(spec: EngineSpec): Record<string, unknown> {
  const properties: Record<string, unknown> = {};
  for (const [k, f] of Object.entries(spec.facts)) {
    properties[k] = {
      type: f.type,
      description: f.description,
      ...(f.choices ? { enum: f.choices } : {}),
      ...(f.default !== undefined ? { default: f.default } : {}),
    };
  }
  return {
    type: "object",
    properties,
    required: Object.entries(spec.facts).filter(([, f]) => f.required).map(([k]) => k),
  };
}
