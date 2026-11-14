// Running one engine: the year guard, fact validation and the defaults the engine assumed.
// Kept apart from registry.ts (which imports every engine) so one engine can be bundled on
// its own with exactly this code: scripts/export-engines.mjs publishes each engine to the
// public repository with this file, and the export test checks the bundle gives the same
// output as runEngine here.
import { NeedsInput, factsSchema, missingRule, type Engine, type EngineOutput } from "./types";

export type YearCheck =
  | { ok: true; year: string }
  | { ok: false; status: "needs_input" | "missing_rule"; what: string };

/**
 * The year guard. An engine's constants are for the tax year(s) in spec.tax_years and are
 * never applied to another year (a California engine that used 2025 rates for 2026 was
 * wrong 3 times out of 3). A year written in a form we cannot read is needs_input; a clear
 * year the engine has no figures for is missing_rule.
 */
export function checkTaxYear(engine: Engine, raw: unknown): YearCheck {
  const years = engine.spec.tax_years;
  const split = years.every((y) => /^\d{4}-\d{2}$/.test(y));
  const example = years[years.length - 1];
  const badForm = { ok: false as const, status: "needs_input" as const, what: `input 'tax_year' must be a tax year written like '${example}'` };
  if (raw === undefined || raw === null || raw === "") return { ok: false, status: "needs_input", what: "missing input 'tax_year'" };
  let s: string;
  if (typeof raw === "number" && Number.isInteger(raw)) s = String(raw);
  else if (typeof raw === "string") s = raw.trim();
  else return badForm;
  let year: string;
  const one = /^(\d{4})$/.exec(s);
  const two = /^(\d{4})\s*[-/]\s*(\d{2}|\d{4})$/.exec(s);
  if (split) {
    if (one) {
      return { ok: false, status: "needs_input", what: `tax_year '${s}' is ambiguous for a tax year that spans two calendar years: ask which one, and write it like '${example}'` };
    }
    if (!two) return badForm;
    const start = Number(two[1]);
    const end = Number(two[2]) % 100;
    if (end !== (start + 1) % 100) return badForm;
    year = `${start}-${String((start + 1) % 100).padStart(2, "0")}`;
  } else {
    if (two) return { ok: false, status: "needs_input", what: `input 'tax_year' must be a calendar year written like '${example}'` };
    if (!one) return badForm;
    year = s;
  }
  if (!years.includes(year)) {
    return { ok: false, status: "missing_rule", what: `no OpenAccountants figures for tax year ${year}` };
  }
  return { ok: true, year };
}

/** Run one engine. A missing or invalid fact comes back as needs_input, never a throw. */
export function runEngine(engine: Engine, facts: unknown): EngineOutput {
  if (!facts || typeof facts !== "object" || Array.isArray(facts)) {
    return { status: "needs_input", engine: engine.spec.name, what: "facts must be an object of named facts", schema: factsSchema(engine.spec) };
  }
  const year = checkTaxYear(engine, (facts as Record<string, unknown>).tax_year);
  if (!year.ok) {
    if (year.status === "needs_input") return { status: "needs_input", engine: engine.spec.name, what: year.what, schema: factsSchema(engine.spec) };
    const out = missingRule(
      engine.spec.name,
      year.what,
      `This engine holds figures for tax year ${engine.spec.tax_years.join(" and ")} only. It never applies one year's figures to another year.`,
      [],
      { inputsUsed: { tax_year: (facts as Record<string, unknown>).tax_year } },
    );
    return out;
  }
  try {
    // The engine sees the year as the guard read it ("2026/27" -> "2026-27", 2026 -> "2026").
    const out = engine.run({ ...(facts as Record<string, unknown>), tax_year: year.year });
    if (out.status !== "needs_input") {
      out.defaults_assumed = defaultsAssumed(engine, facts as Record<string, unknown>);
      out.tax_year = year.year;
    }
    return out;
  } catch (e) {
    if (e instanceof NeedsInput) {
      return { status: "needs_input", engine: engine.spec.name, what: e.message, schema: factsSchema(engine.spec) };
    }
    throw e;
  }
}

/**
 * Every optional fact the caller did not give, with the default the engine used. A default
 * can change the answer (W-2 wages 0, not an ENI holder, no HELP debt), so the compute tool
 * states each one as an assumption instead of applying it silently. Facts that decide which
 * regime applies (UK region, Canadian province, Irish status, German assessment) have no
 * default: the engine asks for them.
 */
export function defaultsAssumed(engine: Engine, facts: Record<string, unknown>): Record<string, unknown> {
  const out: Record<string, unknown> = {};
  for (const [k, f] of Object.entries(engine.spec.facts)) {
    if (f.default !== undefined && (facts[k] === undefined || facts[k] === null)) out[k] = f.default;
  }
  return out;
}

