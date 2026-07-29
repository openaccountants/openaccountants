# Research guardrails: what we certify, and what we don't

Frontier models already get most tax questions substantively right. What they
fail is everything that makes an answer defensible: a pinpoint citation, the
authority that outranks the blog post, an honest confidence level, and a named
human when the position is unsettled.

That layer is what OpenAccountants serves.

## The doctrine, in one line

**We certify the process and the people. We never certify the value.**

The model fetches figures from primary sources itself. We make it hard to do
that sloppily, and we put a named professional behind the method. So a stored
figure of ours can be out of date without anyone being misled, because nothing
we serve is presented as truth-by-assertion.

This is a deliberate trade. Selling verified figures means owning every wrong
figure, in every jurisdiction, forever. Selling the guardrails means the
primary source carries itself and the accountant carries the method.

## What arrives with an analysis question

When a question needs judgment rather than a lookup — *can I deduct this*,
*how is this taxed*, *am I still resident* — the response carries a research
protocol:

1. **Authority hierarchy.** Statute beats regulation beats case law beats
   official guidance beats commentary, plus the jurisdiction's actual primary
   sources. Where sources conflict, the higher tier wins.
2. **Citation discipline.** Every figure anchored to a pinpoint citation with
   its official URL and effective date, fetched in this session rather than
   recalled. Stale recall is the single most common failure mode.
3. **A confidence ladder.** US questions get the real practice standards
   (will / should / more likely than not / substantial authority / reasonable
   basis). Elsewhere, High / Medium / Low with the reason it is not higher.
4. **A memo contract.** The sections a reviewer expects, ending in an
   authorities table and a scope note.

Then the part that is not advice: `verify_citations` takes the model's own
`{url, figure, quote}` claims, fetches each cited page, and confirms the figure
actually appears there. Not against our database — **against the source the
model cited**. Confidence stops being self-reported.

Unsettled points route to a named, licensed accountant rather than a
disclaimer.

## Why check citations rather than serve verified numbers

The failure that damages people is not a sloppy answer they can spot. It is a
**confidently wrong** one: a well-structured memo, correct-looking citations,
built on law that changed. We measured this — an unaided model produced a memo
scoring 0.95 on citation form and 0.10 on substance, because it applied
superseded law with perfect formatting.

A citation check is mechanical, verifiable, and carries no opinion: *the page
you cited does contain that figure*. A verified-figure claim is a tax opinion,
and it decays.

Verdicts are `verified`, `not_found`, or `unfetchable` — never "false". PDFs,
paywalls and JavaScript pages fetch badly, and an honest "could not check"
beats a confident verdict either way.

## Limits, stated plainly

- **We cannot make a model obey.** Everything above is served as guidance. A
  model that ignores it produces an ordinary AI answer. We measure how often
  that happens rather than pretending it doesn't.
- **Some models have no web access.** For those, a dated cached value with its
  source is the honest fallback, never a bare number.
- **A gap is a gap.** Where no accountant has written a method for a job, we
  say so and point at the primary authorities, rather than inventing coverage.
