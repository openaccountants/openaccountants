// Does a skill still say what an engine quotes? Used by scripts/check-engine-quotes.ts, the
// daily drift check that stops an engine silently keeping a figure its skill no longer states.
//
// Both sides are normalised the same way, so only typography is forgiven: whitespace, markdown
// emphasis and links, thousands separators, non-breaking spaces, dash and quote-mark variants,
// spacing around table pipes, and letter case. Figures, words and their order must match.
//
// A quote may skip text with "..." (or "…"): each piece must then appear, in order, on ONE line
// of the skill (a table row or a paragraph), so "SBITO | ... cap $1,000" still has to be the
// SBITO row and cannot be satisfied by a "cap $1,000" anywhere else in the skill.
//
// A quote of several lines (a table with its header row, or a rule and its worked example)
// matches when each of its lines matches a line of the skill, in the same order.

const ELLIPSIS = /\s*(?:\.\.\.|\u2026)\s*/;

/** Normalise one line of text (no newlines in the result). */
export function normaliseText(s: string): string {
  return (
    s
      // Thousands separators between digit groups: "12,345", "12 345" (nbsp / narrow nbsp / thin space).
      .replace(/(\d)[,\u00a0\u202f\u2009\u2007](?=\d{3}(?!\d))/g, "$1")
      .normalize("NFKC")
      // Markdown links keep their text; emphasis and code marks go.
      .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
      .replace(/[*_`]/g, "")
      .replace(/\\\|/g, "|")
      // Quote marks.
      .replace(/[\u2018\u2019\u201a\u2032]/g, "'")
      .replace(/[\u201c\u201d\u201e\u2033]/g, '"')
      // Dashes, minus signs and "--" become one hyphen, with the spaces around it dropped.
      .replace(/\s*(?:-{2,3}|[\u2010\u2011\u2012\u2013\u2014\u2015\u2212-])\s*/g, "-")
      // Table cells: same spacing around every pipe.
      .replace(/\s*\|\s*/g, " | ")
      .replace(/\s+/g, " ")
      .trim()
      .toLowerCase()
  );
}

/** The skill's text as normalised lines, ready for quoteFound. */
export function normaliseLines(text: string): string[] {
  return text.split(/\r?\n/).map(normaliseText).filter(Boolean);
}

/**
 * Where piece p occurs in line from position `from`, never splitting a number: "5.95%" is not
 * found inside "15.95%", nor "$1000" inside "$1000000" or "12" inside "12.5".
 */
function indexOfWhole(line: string, p: string, from: number): number {
  const digitStart = /^[\d.]/.test(p);
  const digitEnd = /\d$/.test(p);
  for (let i = line.indexOf(p, from); i >= 0; i = line.indexOf(p, i + 1)) {
    const before = line.slice(Math.max(0, i - 1), i);
    const after = line.slice(i + p.length, i + p.length + 2);
    if (digitStart && /\d/.test(before)) continue;
    if (digitEnd && /^(\d|[.,]\d)/.test(after)) continue;
    return i;
  }
  return -1;
}

/** True when every piece of one quote line appears, in order, on this skill line. */
function lineMatches(pieces: string[], line: string): boolean {
  let at = 0;
  for (const p of pieces) {
    const i = indexOfWhole(line, p, at);
    if (i < 0) return false;
    at = i + p.length;
  }
  return true;
}

/** True when each line of the quote is found on a line of the skill, in order. */
export function quoteFound(quote: string, lines: string[]): boolean {
  const quoteLines = quote
    .split(/\r?\n/)
    .map((q) => q.split(ELLIPSIS).map(normaliseText).filter(Boolean))
    .filter((pieces) => pieces.length > 0);
  if (quoteLines.length === 0) return false;
  let from = 0;
  for (const pieces of quoteLines) {
    let hit = -1;
    for (let i = from; i < lines.length; i++) {
      if (lineMatches(pieces, lines[i])) {
        hit = i;
        break;
      }
    }
    if (hit < 0) return false;
    from = hit + 1;
  }
  return true;
}
