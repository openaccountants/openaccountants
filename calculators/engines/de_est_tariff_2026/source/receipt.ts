// The receipt returned with every computed answer: a fingerprint anyone can recompute from
// the engine name, engine version, the facts and the result, so the same facts on the same
// engine version always give the same id. Not stored anywhere yet (no table in this change).
import { createHash } from "crypto";

/** JSON with object keys sorted at every level, so key order never changes the hash. */
export function canonicalJson(value: unknown): string {
  if (value === null || typeof value !== "object") return JSON.stringify(value) ?? "null";
  if (Array.isArray(value)) return `[${value.map((v) => canonicalJson(v === undefined ? null : v)).join(",")}]`;
  const obj = value as Record<string, unknown>;
  const keys = Object.keys(obj).filter((k) => obj[k] !== undefined).sort();
  return `{${keys.map((k) => `${JSON.stringify(k)}:${canonicalJson(obj[k])}`).join(",")}}`;
}

export interface Receipt {
  id: string;
  engine_version: string;
  computed_at: string;
}

/** id = sha256(engine name, engine version, canonical facts, canonical result), newline-joined. */
export function receiptId(engine: string, version: string, facts: unknown, result: unknown): string {
  return createHash("sha256")
    .update([engine, version, canonicalJson(facts), canonicalJson(result)].join("\n"))
    .digest("hex");
}

export function makeReceipt(engine: string, version: string, facts: unknown, result: unknown, now: Date = new Date()): Receipt {
  return { id: receiptId(engine, version, facts, result), engine_version: version, computed_at: now.toISOString() };
}
