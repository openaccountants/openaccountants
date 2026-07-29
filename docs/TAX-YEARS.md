# Tax years: how a figure knows which year it belongs to

Most tax data goes wrong in the same boring way: a number that was right last
year is served this year with nothing saying which year it came from. The fix
is not to keep chasing values. It is to make every figure carry its year, and
to make the server prefer the right one.

## Facts are not stale. They are dated.

A 2025 figure is *correct* for 2025. People file 2025 returns throughout 2026,
so deleting last year's numbers would break real work. What breaks trust is an
**undated** number, because nothing stops a model combining a 2025 threshold
with a 2026 rate into a total that is true for no year at all.

So every figure carries a validity window, and the server:

1. **Labels it.** Every rule rendered by `search_rules` shows its period —
   `TY2026` for a calendar-year jurisdiction, `2025/26` for a fiscal one.
2. **Warns on mixtures.** If one response carries figures from more than one
   tax year, the header says so by name and forbids combining them.
3. **Prefers the current year.** Year coverage outranks text relevance, so the
   figure for the year you asked about surfaces first. Prior-year figures still
   serve, clearly labeled.
4. **Serves two years.** The current tax year and the one before it, because
   that is the filing window. Older vintages stay in the database and serve
   only when you ask for that year by name.

## The tax year is not the calendar year

This is where most tax datasets quietly break. A figure stamped
`1 Jan – 31 Dec` is wrong at both ends for most of the world:

| Jurisdiction | Tax year |
|---|---|
| United Kingdom | 6 April – 5 April |
| India, Hong Kong, New Zealand | 1 April – 31 March |
| Australia, Pakistan, Bangladesh | 1 July – 30 June |
| South Africa (individuals) | 1 March – end February |
| United States, Ireland, Singapore | calendar year |

A UK figure for **2025/26** covers 6 April 2025 to 5 April 2026. Stamp it as
calendar 2025 and two things go wrong: it is labeled "TY2025", which a British
accountant reads as a different year, and a question asked in February 2026
about the current year misses it, because the filter tests the wrong boundary.

Watch the exceptions. Ireland and Singapore are commonly assumed to run fiscal
years for individuals and do not. Japan's *corporate* year is April to March
while individual income tax is the calendar year, so a blanket rule corrupts
it. Getting these wrong is worse than leaving them alone.

## Where the current value actually comes from

We do not want to be the place a rate lives. Rates move, and a database of
rates is a promise to chase them forever in 190 jurisdictions.

Instead a **slot** records where a figure is *published*: the authority, the
document family, the stable official URL, the publication cadence, and the
checks to run. The value itself is fetched live from that primary source at
answer time, under the research protocol, and machine-checked with
`verify_citations` before it reaches anyone.

A source map does not go stale on 1 January. A rate table does.

Where we do cache a value, it is dated and cited: *"$24,500, per IRS Notice
2025-67, verified 29 July 2026."* Never a bare number. A model that cannot
fetch still gets an honest, dated answer rather than a confident guess.

## Adding a figure

- Put the year in `valid_from` / `valid_to`, **never** in the item text. A
  year baked into a title is how last year's figure passes for this year's.
- Use the jurisdiction's real tax-year boundaries, not 1 January.
- Cite the primary source with a URL, and record the date you read it.
- Add the new year as a **new row**. Never overwrite the prior year: someone
  is still filing it.
