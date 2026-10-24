# Owners

Who owns each jurisdiction for the [GOAL.md](GOAL.md) push. The owner drives the pack to complete and verified; they do not have to write every line themselves. James Wallach works with Jeff on the US. Change this file by PR.

**Agents starting European work: read [Europe writing assignments](#europe-writing-assignments) first.** Michael updated the allocation on 24 October 2026. Coordination [PR #773](https://github.com/openaccountants/openaccountants/pull/773) carries this allocation until merged. The [country PR split register](docs/research/2026-10-24-country-pr-split.md) supersedes consolidated PR [#514](https://github.com/openaccountants/openaccountants/pull/514) for new publication; preserve that PR and its branch as historical review evidence.

| Owner | Regions | Jurisdictions | Thin (7 or fewer skills) |
|---|---|---|---|
| Jeff Watts | Americas: US federal and states, Canada and provinces, Latin America, Caribbean | 105 | 91 |
| Ryan Duguid | Asia-Pacific, Africa | 94 | 73 |
| Michael Cutajar | Europe, Middle East; merges and final review | 67 | 29 |

Cross-cutting: Ryan owns source reachability, the repo audit and the pentest. Michael owns the website sync, licensing and marketing. Jeff owns the board and issue triage. The GLOBAL, INTL and EU-wide skills are not jurisdictions; Michael maintains them.

## Roles

Owning a region means driving its packs. These roles cut across regions. Each one exists because of something we measured on 23 October 2026 across the 2,169 skills on main:

- 11% have a `## Sources` section, and 1.5% record when each source was read.
- 74% are still labelled tax year 2025 or earlier, or carry no year.
- 2% have a worked example the checker recomputes.
- 1.5% (33) are Accountant-reviewed.
- Independent reviews this week found at least one wrong or outdated figure in most older skills they checked.

CI checks that a skill is well formed. It does not check that a skill is right. These roles close that gap.

| Role | What it does | Why we need it | Who |
|---|---|---|---|
| Data lead | Owns the quality numbers and the checks behind them. Runs a weekly job for broken source links, contradictions between skills and skills still on last year's figures, and opens an issue for each failure. Sets the provenance standard (official sources, "Read on" dates, a "Not yet confirmed" line) and puts the honest counts in the weekly report: reviewed, current-year, fully sourced. | Nothing today opens a source link or compares skills against each other, and `detect-contradictions.py` is not in CI. File counts look like coverage when they are not. | Proposed: Ryan Duguid, who already owns source reachability and the repo audit. To confirm with Ryan. |
| Country writers | Write and re-verify skills for the countries assigned to them, one writer per country, each skill followed by an independent review against the law before merge. | Keeps work from being duplicated and puts a second check on every figure. | Europe: Claude and ChatGPT, as assigned below (Michael accountable). Other regions: the region owner. |
| Re-verification queue | Picks the old skills that AIs load most (from the platform usage digest) and sends them back through write and review, most-used first. | Most of the library is older drafts; fixing the ones people actually use first gives the most accuracy per hour. | Data lead sets the queue; country writers do the work. |
| Reviewing accountants | A named, credentialed accountant reviews a country's pack and signs it off as Accountant-reviewed (`tier: 1`). | This is the third test in [GOAL.md](GOAL.md) and the slowest. 33 skills have it today. | Open. One per country; region owners recruit. |
| Tooling | Builds and maintains the checks: link checker, contradiction gate, provenance required on changed skills, the coverage report and its `partial:` rule. | Every rule we rely on should run without a person remembering it. | Open; the data lead decides what is built first. |
| Merger and final review | Merges PRs, holds the line on the two quality states and the copy rules. | Humans merge; one person keeps it consistent. | Michael Cutajar. |
| Board and triage | Keeps the issue board current and routes new issues and contributors. | Contributors need a clear place to start. | Jeff Watts. |

To take an open role, comment on the coverage report issue or open a PR changing this table.

## Europe writing assignments

Approved by Michael on 23 October 2026 and updated by his explicit handover on 24 October 2026. Michael remains the accountable owner for Europe. Writing allocation does not transfer professional responsibility or certify a Guide.

**Claude: 29 jurisdictions. ChatGPT: 26 jurisdictions.** Country allocations cover all topics, including existing Guides. One active writer per country.

### Recorded seven-country handover, 24 October 2026

Michael handed **Bulgaria (BG), Croatia (HR), Estonia (EE), Latvia (LV), Lithuania (LT), Slovakia (SK) and Slovenia (SI) to Claude**. This supersedes their former ChatGPT allocation and the old instruction for Claude to leave those packs untouched.

| Country | Country issue | Handover status and next action |
|---|---|---|
| Bulgaria | [#383](https://github.com/openaccountants/openaccountants/issues/383) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged law-based drafts and independent review records. |
| Croatia | [#400](https://github.com/openaccountants/openaccountants/issues/400) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged drafts and review records. |
| Estonia | [#390](https://github.com/openaccountants/openaccountants/issues/390) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged drafts and review records. |
| Latvia | [#409](https://github.com/openaccountants/openaccountants/issues/409) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged drafts and review records. |
| Slovakia | [#425](https://github.com/openaccountants/openaccountants/issues/425) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged drafts and review records. |
| Slovenia | [#423](https://github.com/openaccountants/openaccountants/issues/423) | Michael reports the 2026 tax-domain work complete and issue closed. Preserve merged drafts and review records. |
| Lithuania | [#407](https://github.com/openaccountants/openaccountants/issues/407) | Still open. Payroll/social draft [#772](https://github.com/openaccountants/openaccountants/pull/772), branch `fix/LT-payroll-sc-2026`, needs a fresh independent review because its earlier review was stopped. Reconcile main, fix findings, pass checks, then merge and close the issue under Michael's direction. |

The source handover is Michael's message and `HANDOVER-wave3.md`, supplied on 24 October. He reports 37 merged PRs, all Source-cited drafts and no accountant review. Closed coverage issues and independent source review do not grant `tier: 1`. Retain the recorded follow-ups: Lithuania formation's old rolling VAT test, Slovenia optimisation's contradiction noted on #769, and older non-domain overview/formation/optimisation summaries across these packs. Do not reopen completed tax-domain work merely to regenerate it.

### Current country work

| Writer | Current work and next action | Preserve or leave parked |
|---|---|---|
| Claude | Continue within the 29-country allocation below. Lithuania #407 / PR #772 is the outstanding Wave 3 review/merge item. Check country issues, existing merged work and open PRs before writing. | The seven-country transfer above is explicit. All other ChatGPT countries require a separate recorded handover. |
| ChatGPT, primary chat | Armenia under [#378](https://github.com/openaccountants/openaccountants/issues/378), branch `codex/armenia-country-completion`; corporate/individual/VAT and new TP/XB draft checkpoints `08ece09e` / `947a3d9f`. Resume payroll/social after reconciling current country work and the PR split. | Montenegro source `86bab4f9` received independent review and correction closure, published to historical shared head `571c00a3`; 46 controls, seven domains partial, zero professional reviews. Bosnia is parked at `63d8b8b5`; Norway is parked at `79c46e49`. |
| ChatGPT, support chat | Monaco was taken on [#410](https://github.com/openaccountants/openaccountants/issues/410), branch `codex/monaco-country-completion`, before writing. Primary-law retrievals and a private country card exist; no Monaco Guide edits or content publication yet. Pause drafting for Michael's requested ownership correction and one-PR-per-country split. Resume Monaco in a fresh session with the preserved evidence. | San Marino reviewed source `b5e11396`, published batch `669a1cca`, all five exact-head checks green. Liechtenstein reviewed source `ede184f9` / batch `ee349c5d`; Finland reviewed source `c83ca9f5` / batch `af8d6057`. These remain partial Source-cited drafts. Iceland, Norway, Guernsey, Gibraltar and Bosnia remain parked. |

### Country publication rule

Prepare the whole country batch locally, obtain independent review, fix findings, then push **once for that country**. Michael's 24 October instruction replaces the consolidated-PR rule: use **one PR per country**, not one PR per Guide. Split existing #514 contents without changing their legal substance or claiming a new review. Preserve original Guide paths, attribution, calculation blocks, source records and review limits. The [split register](docs/research/2026-10-24-country-pr-split.md) maps every replacement PR and shared provenance. Keep unresolved domains and professional review separate from publication/CI status.

Continue within your allocation without waiting for another country-by-country instruction. Before taking work, fetch origin and check the current main files, issue and open PRs. Start each new wave in a fresh session as Michael directed; use this file and the split register for the handover.

### Country allocation

| Code | Country or territory | Assigned writer |
|---|---|---|
| AD | Andorra | ChatGPT |
| AL | Albania | Claude |
| AM | Armenia | ChatGPT |
| AT | Austria | Claude |
| AZ | Azerbaijan | ChatGPT |
| BA | Bosnia and Herzegovina | ChatGPT |
| BE | Belgium | Claude |
| BG | Bulgaria | Claude |
| BY | Belarus | ChatGPT |
| CH | Switzerland | Claude |
| CY | Cyprus | Claude |
| CZ | Czech Republic | Claude |
| DE | Germany | Claude |
| DK | Denmark | Claude |
| EE | Estonia | Claude |
| ES | Spain | ChatGPT |
| FI | Finland | ChatGPT |
| FO | Faroe Islands | ChatGPT |
| FR | France | Claude |
| GB | United Kingdom | Claude |
| GE | Georgia | ChatGPT |
| GG | Guernsey | ChatGPT |
| GI | Gibraltar | ChatGPT |
| GR | Greece | Claude |
| HR | Croatia | Claude |
| HU | Hungary | Claude |
| IE | Ireland | Claude |
| IM | Isle of Man | ChatGPT |
| IS | Iceland | ChatGPT |
| IT | Italy | Claude |
| LI | Liechtenstein | ChatGPT |
| LT | Lithuania | Claude |
| LU | Luxembourg | Claude |
| LV | Latvia | Claude |
| MC | Monaco | ChatGPT |
| MD | Moldova | ChatGPT |
| ME | Montenegro | ChatGPT |
| MK | North Macedonia | ChatGPT |
| MT | Malta | Claude |
| NL | Netherlands | Claude |
| NO | Norway | ChatGPT |
| PL | Poland | Claude |
| PT | Portugal | Claude |
| RO | Romania | Claude |
| RS | Serbia | Claude |
| RU | Russia | ChatGPT |
| SE | Sweden | Claude |
| SI | Slovenia | Claude |
| SJ | Svalbard | ChatGPT |
| SK | Slovakia | Claude |
| SM | San Marino | ChatGPT |
| TR | Turkey | ChatGPT |
| UA | Ukraine | ChatGPT |
| VA | Vatican City | ChatGPT |
| XK | Kosovo | ChatGPT |

### Working and handover rules

- Read this assignment, the country issue, current main Guides, research and open PRs before starting. Reuse existing work regardless of its author.
- Claude owns all topics for the 29 countries in the table; ChatGPT owns all topics for the remaining 26. Michael remains accountable for both allocations.
- One active writer per country. Record a handover on GitHub with its country/topic, branch/PR, unfinished scope and next action before another writer starts. Inactivity or a merged PR alone does not transfer ownership.
- Independent review does not confer writing ownership. Preserve author/reviewer provenance; obtain named professional review separately.
- Guide presence, arithmetic checks, source preparation and merge status alone do not prove comprehensive coverage. Preserve each pack's explicit applicability and evidence gaps.
- Use one reviewed country batch and one country PR. Historical #514 and its branch remain evidence; its replacement PRs are listed in the split register.

This allocation applies only to the 55 jurisdictions labelled `europe` below. Ryan's Asia-Pacific/Africa allocation, Jeff's Americas allocation and Michael's Middle East accountability remain unchanged. Existing Caribbean/Middle East drafts in the split are preserved contributions, not a claim of a new regional assignment. Reconcile and explicitly assign Jersey or Åland work before adding it to this table.

## By jurisdiction

Generated from `python3 scripts/coverage-report.py` on 2026-10-22 (tax domains); the issue for each row is the live status. Regenerate with the same command when owners change.

| Owner | Region | Code | Name | Skills | Reviewed | Missing domains |
|---|---|---|---|---|---|---|
| jeff | americas | AG | Antigua And Barbuda | 3 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | AR | Argentina | 8 | 0 | PR, TP, XB |
| jeff | americas | AW | Aruba | 3 | 0 | IT-CORP, VAT, PR, TP, XB |
| jeff | americas | BB | Barbados | 6 | 0 | TP, XB |
| jeff | americas | BL | Saint Barthelemy | 2 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | BM | Bermuda | 7 | 0 | TP, XB |
| jeff | americas | BO | Bolivia | 5 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | BR | Brazil | 14 | 0 | IT-CORP, SC, XB |
| jeff | americas | BS | Bahamas | 6 | 0 | TP, XB |
| jeff | americas | BZ | Belize | 6 | 0 | TP, XB |
| jeff | americas | CA | Canada | 51 | 1 | none |
| jeff | americas | CA-AB | Alberta (Canada) | 2 | 0 | IT-CORP, VAT, SC, PR, TP |
| jeff | americas | CL | Chile | 8 | 0 | PR, TP, XB |
| jeff | americas | CO | Colombia | 8 | 0 | PR, TP, XB |
| jeff | americas | CR | Costa Rica | 5 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | CU | Cuba | 6 | 0 | TP, XB |
| jeff | americas | CW | Cura Ao | 6 | 0 | TP, XB |
| jeff | americas | DM | Dominica | 4 | 0 | TP, XB |
| jeff | americas | DO | Dominican Republic | 22 | 0 | none |
| jeff | americas | EC | Ecuador | 8 | 0 | VAT, TP, XB |
| jeff | americas | GD | Grenada | 3 | 0 | IT-IND, IT-CORP, PR, TP, XB |
| jeff | americas | GF | French Guiana | 2 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | GL | Greenland | 2 | 0 | IT-IND, IT-CORP, VAT, SC, TP, XB |
| jeff | americas | GP | Guadeloupe | 1 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | GT | Guatemala | 7 | 0 | VAT, TP, XB |
| jeff | americas | GY | Guyana | 6 | 0 | TP, XB |
| jeff | americas | HN | Honduras | 7 | 0 | VAT, TP, XB |
| jeff | americas | HT | Haiti | 6 | 0 | VAT, SC, TP, XB |
| jeff | americas | JM | Jamaica | 6 | 0 | VAT, TP, XB |
| jeff | americas | KN | Saint Kitts And Nevis | 2 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | KY | Cayman Islands | 6 | 0 | TP, XB |
| jeff | americas | LC | Saint Lucia | 5 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | MF | Saint Martin | 3 | 0 | IT-IND, VAT, SC, PR, TP, XB |
| jeff | americas | MQ | Martinique | 1 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | MS | Montserrat | 3 | 0 | VAT, TP |
| jeff | americas | MX | Mexico | 12 | 0 | IT-CORP, SC, PR, XB |
| jeff | americas | NI | Nicaragua | 7 | 0 | VAT, TP, XB |
| jeff | americas | PA | Panama | 4 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | PE | Peru | 7 | 0 | VAT, TP, XB |
| jeff | americas | PM | Saint Pierre And Miquelon | 2 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | PR | Puerto Rico | 3 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | PY | Paraguay | 4 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | SR | Suriname | 6 | 0 | TP, XB |
| jeff | americas | SV | El Salvador | 5 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | SX | Sint Maarten | 3 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | TC | Turks And Caicos | 3 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | TT | Trinidad And Tobago | 6 | 0 | TP, XB |
| jeff | americas | US | United States (federal) | 103 | 21 | SC, TP |
| jeff | americas | US-AK | Alaska (US) | 1 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AL | Alabama (US) | 4 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AR | Arkansas (US) | 4 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AZ | Arizona (US) | 4 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-CA | California (US) | 16 | 0 | IT-CORP, SC, TP |
| jeff | americas | US-CO | Colorado (US) | 6 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-CT | Connecticut (US) | 3 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-DC | District of Columbia (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-DE | Delaware (US) | 4 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-FL | Florida (US) | 7 | 0 | SC, PR, TP, XB |
| jeff | americas | US-GA | Georgia (US) | 10 | 0 | SC, TP, XB |
| jeff | americas | US-HI | Hawaii (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-IA | Iowa (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-ID | Idaho (US) | 2 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-IL | Illinois (US) | 6 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-IN | Indiana (US) | 3 | 0 | IT-IND, IT-CORP, SC, TP, XB |
| jeff | americas | US-KS | Kansas (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-KY | Kentucky (US) | 3 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-LA | Louisiana (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MA | Massachusetts (US) | 7 | 0 | SC, TP, XB |
| jeff | americas | US-MD | Maryland (US) | 3 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-ME | Maine (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MI | Michigan (US) | 9 | 0 | SC, TP, XB |
| jeff | americas | US-MN | Minnesota (US) | 5 | 0 | SC, TP, XB |
| jeff | americas | US-MO | Missouri (US) | 4 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-MS | Mississippi (US) | 3 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MT | Montana (US) | 1 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-NC | North Carolina (US) | 7 | 0 | SC, TP, XB |
| jeff | americas | US-ND | North Dakota (US) | 6 | 0 | SC, TP, XB |
| jeff | americas | US-NE | Nebraska (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NH | New Hampshire (US) | 2 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-NJ | New Jersey (US) | 5 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-NM | New Mexico (US) | 3 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NV | Nevada (US) | 5 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NY | New York (US) | 16 | 0 | SC, TP |
| jeff | americas | US-NY-NYC | New York City (US) | 1 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-OH | Ohio (US) | 6 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-OK | Oklahoma (US) | 3 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-OR | Oregon (US) | 3 | 0 | IT-CORP, VAT, SC, TP, XB |
| jeff | americas | US-PA | Pennsylvania (US) | 5 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-RI | Rhode Island (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-SC | South Carolina (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-SD | South Dakota (US) | 1 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-TN | Tennessee (US) | 1 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-TX | Texas (US) | 8 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-UT | Utah (US) | 3 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-VA | Virginia (US) | 4 | 0 | SC, TP, XB |
| jeff | americas | US-VT | Vermont (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WA | Washington (US) | 5 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WI | Wisconsin (US) | 4 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-WV | West Virginia (US) | 2 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WY | Wyoming (US) | 3 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | UY | Uruguay | 7 | 0 | VAT, TP, XB |
| jeff | americas | VC | Saint Vincent And The Grenadines | 3 | 0 | SC, PR, TP, XB |
| jeff | americas | VE | Venezuela | 5 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | VG | British Virgin Islands | 6 | 0 | TP, XB |
| jeff | americas | VI | Us Virgin Islands | 3 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| michael | europe | AD | Andorra | 6 | 0 | VAT, TP, XB |
| michael | europe | AL | Albania | 5 | 0 | IT-CORP, TP, XB |
| michael | europe | AM | Armenia | 8 | 0 | TP, XB |
| michael | europe | AT | Austria | 7 | 0 | PR, TP, XB |
| michael | europe | AZ | Azerbaijan | 8 | 0 | TP, XB |
| michael | europe | BA | Bosnia | 8 | 0 | TP, XB |
| michael | europe | BE | Belgium | 10 | 0 | IT-CORP, TP, XB |
| michael | europe | BG | Bulgaria | 8 | 0 | TP, XB |
| michael | europe | BY | Belarus | 8 | 0 | TP, XB |
| michael | europe | CH | Switzerland | 11 | 0 | SC, PR, TP, XB |
| michael | europe | CY | Cyprus | 6 | 0 | IT-CORP, TP, XB |
| michael | europe | CZ | Czech Republic | 8 | 0 | PR, TP, XB |
| michael | europe | DE | Germany | 23 | 0 | IT-CORP |
| michael | europe | DK | Denmark | 5 | 0 | IT-CORP, SC, PR, TP, XB |
| michael | europe | EE | Estonia | 8 | 0 | TP, XB |
| michael | europe | ES | Spain | 24 | 0 | none |
| michael | europe | FI | Finland | 7 | 0 | PR, TP, XB |
| michael | europe | FO | Faroe Islands | 5 | 0 | IT-CORP, TP |
| michael | europe | FR | France | 21 | 0 | IT-CORP |
| michael | europe | GB | Uk | 31 | 0 | IT-CORP, SC |
| michael | europe | GE | Georgia | 8 | 3 | TP, XB |
| michael | europe | GG | Guernsey | 3 | 0 | VAT, TP, XB |
| michael | europe | GI | Gibraltar | 5 | 0 | VAT, TP, XB |
| michael | europe | GR | Greece | 8 | 0 | SC, PR, TP, XB |
| michael | europe | HR | Croatia | 8 | 0 | TP, XB |
| michael | europe | HU | Hungary | 5 | 0 | IT-CORP, PR, TP, XB |
| michael | europe | IE | Ireland | 14 | 0 | SC, TP, XB |
| michael | europe | IM | Im | 6 | 0 | TP, XB |
| michael | europe | IS | Iceland | 8 | 0 | TP, XB |
| michael | europe | IT | Italy | 15 | 0 | IT-CORP, XB |
| michael | europe | LI | Liechtenstein | 6 | 0 | TP, XB |
| michael | europe | LT | Lithuania | 7 | 0 | TP, XB |
| michael | europe | LU | Luxembourg | 5 | 0 | IT-CORP, TP, XB |
| michael | europe | LV | Latvia | 8 | 0 | TP, XB |
| michael | europe | MC | Monaco | 6 | 0 | TP, XB |
| michael | europe | MD | Moldova | 8 | 0 | TP, XB |
| michael | europe | ME | Montenegro | 8 | 0 | TP, XB |
| michael | europe | MK | North Macedonia | 8 | 0 | TP, XB |
| michael | europe | MT | Malta | 30 | 0 | IT-CORP, XB |
| michael | europe | NL | Netherlands | 22 | 0 | SC, XB |
| michael | europe | NO | Norway | 9 | 0 | PR, TP |
| michael | europe | PL | Poland | 7 | 0 | IT-CORP, PR, TP, XB |
| michael | europe | PT | Portugal | 15 | 0 | TP |
| michael | europe | RO | Romania | 10 | 0 | TP, XB |
| michael | europe | RS | Serbia | 7 | 0 | IT-CORP, TP, XB |
| michael | europe | RU | Russia | 14 | 0 | IT-CORP, TP, XB |
| michael | europe | SE | Sweden | 9 | 0 | IT-CORP, TP, XB |
| michael | europe | SI | Slovenia | 8 | 0 | TP, XB |
| michael | europe | SJ | Svalbard | 3 | 0 | IT-CORP, VAT, SC, TP, XB |
| michael | europe | SK | Slovakia | 8 | 0 | TP, XB |
| michael | europe | SM | San Marino | 6 | 0 | TP, XB |
| michael | europe | TR | Turkey | 8 | 0 | TP, XB |
| michael | europe | UA | Ukraine | 15 | 0 | TP, XB |
| michael | europe | VA | Vatican City | 1 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| michael | europe | XK | Kosovo | 5 | 0 | IT-CORP, TP, XB |
| michael | middle-east | AE | Uae | 9 | 0 | TP, XB |
| michael | middle-east | BH | Bahrain | 6 | 0 | TP, XB |
| michael | middle-east | EG | Egypt | 17 | 0 | XB |
| michael | middle-east | IL | Israel | 10 | 0 | SC, TP, XB |
| michael | middle-east | IQ | Iraq | 7 | 0 | TP, XB |
| michael | middle-east | IR | Iran | 6 | 0 | TP, XB |
| michael | middle-east | JO | Jordan | 6 | 0 | TP, XB |
| michael | middle-east | KW | Kuwait | 6 | 0 | TP, XB |
| michael | middle-east | LB | Lebanon | 6 | 0 | TP, XB |
| michael | middle-east | OM | Oman | 6 | 0 | TP, XB |
| michael | middle-east | QA | Qatar | 6 | 0 | TP, XB |
| michael | middle-east | SA | Saudi Arabia | 12 | 0 | SC, TP, XB |
| ryan | africa | AO | Angola | 6 | 0 | TP, XB |
| ryan | africa | BF | Burkina Faso | 8 | 0 | TP, XB |
| ryan | africa | BI | Burundi | 6 | 0 | TP, XB |
| ryan | africa | BJ | Benin | 6 | 0 | TP, XB |
| ryan | africa | BW | Botswana | 6 | 0 | TP, XB |
| ryan | africa | CD | Dr Congo | 6 | 0 | TP, XB |
| ryan | africa | CF | Central African Republic | 6 | 0 | TP, XB |
| ryan | africa | CG | Republic Of Congo | 6 | 0 | TP, XB |
| ryan | africa | CI | Ivory Coast | 4 | 0 | IT-CORP, TP, XB |
| ryan | africa | CM | Cameroon | 4 | 0 | IT-CORP, TP, XB |
| ryan | africa | CV | Cape Verde | 6 | 0 | TP, XB |
| ryan | africa | DJ | Djibouti | 6 | 0 | TP, XB |
| ryan | africa | DZ | Algeria | 4 | 0 | IT-CORP, TP, XB |
| ryan | africa | ER | Eritrea | 6 | 0 | TP, XB |
| ryan | africa | ET | Ethiopia | 7 | 0 | TP, XB |
| ryan | africa | GA | Gabon | 5 | 0 | TP, XB |
| ryan | africa | GH | Ghana | 7 | 0 | TP, XB |
| ryan | africa | GM | Gambia | 6 | 0 | TP, XB |
| ryan | africa | GN | Guinea | 6 | 0 | TP, XB |
| ryan | africa | GQ | Equatorial Guinea | 6 | 0 | TP, XB |
| ryan | africa | GW | Guinea Bissau | 6 | 0 | TP, XB |
| ryan | africa | KE | Kenya | 14 | 0 | SC, PR, TP |
| ryan | africa | KM | Comoros | 3 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| ryan | africa | LR | Liberia | 6 | 0 | TP, XB |
| ryan | africa | LS | Lesotho | 6 | 0 | TP, XB |
| ryan | africa | LY | Libya | 6 | 0 | TP, XB |
| ryan | africa | MA | Morocco | 16 | 0 | IT-CORP, TP, XB |
| ryan | africa | MG | Madagascar | 6 | 0 | TP, XB |
| ryan | africa | ML | Mali | 6 | 0 | TP, XB |
| ryan | africa | MR | Mauritania | 6 | 0 | TP, XB |
| ryan | africa | MU | Mauritius | 6 | 0 | TP, XB |
| ryan | africa | MW | Malawi | 6 | 0 | TP, XB |
| ryan | africa | MZ | Mozambique | 4 | 0 | IT-CORP, TP, XB |
| ryan | africa | NA | Namibia | 6 | 0 | TP, XB |
| ryan | africa | NE | Niger | 5 | 0 | TP, XB |
| ryan | africa | NG | Nigeria | 14 | 0 | SC, TP, XB |
| ryan | africa | RE | Reunion | 1 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| ryan | africa | RW | Rwanda | 8 | 0 | TP, XB |
| ryan | africa | SC | Seychelles | 5 | 0 | TP, XB |
| ryan | africa | SD | Sudan | 6 | 0 | TP, XB |
| ryan | africa | SH | Saint Helena | 4 | 0 | IT-CORP, VAT, SC, TP, XB |
| ryan | africa | SL | Sierra Leone | 6 | 0 | TP, XB |
| ryan | africa | SN | Senegal | 7 | 0 | TP, XB |
| ryan | africa | SO | Somalia | 6 | 0 | TP, XB |
| ryan | africa | SS | South Sudan | 6 | 0 | TP, XB |
| ryan | africa | ST | S O Tom And Pr Ncipe | 6 | 0 | TP, XB |
| ryan | africa | SZ | Eswatini | 6 | 0 | TP, XB |
| ryan | africa | TD | Chad | 6 | 0 | TP, XB |
| ryan | africa | TG | Togo | 6 | 0 | TP, XB |
| ryan | africa | TN | Tunisia | 7 | 0 | TP, XB |
| ryan | africa | TZ | Tanzania | 6 | 0 | IT-CORP, TP, XB |
| ryan | africa | UG | Uganda | 6 | 0 | TP, XB |
| ryan | africa | YT | Mayotte | 2 | 0 | IT-IND, IT-CORP, SC, TP, XB |
| ryan | africa | ZA | South Africa | 20 | 0 | IT-CORP, SC, PR |
| ryan | africa | ZM | Zambia | 6 | 0 | TP, XB |
| ryan | africa | ZW | Zimbabwe | 6 | 0 | TP, XB |
| ryan | apac | AF | Afghanistan | 6 | 0 | TP, XB |
| ryan | apac | AU | Australia | 60 | 0 | none |
| ryan | apac | BD | Bangladesh | 18 | 0 | TP, XB |
| ryan | apac | BN | Brunei | 7 | 0 | TP, XB |
| ryan | apac | BT | Bhutan | 6 | 0 | TP, XB |
| ryan | apac | CN | China | 14 | 0 | TP |
| ryan | apac | FJ | Fiji | 6 | 0 | TP, XB |
| ryan | apac | HK | Hong Kong | 7 | 0 | SC, PR, TP, XB |
| ryan | apac | ID | Indonesia | 13 | 0 | SC, TP, XB |
| ryan | apac | IN | India | 22 | 0 | IT-CORP, SC |
| ryan | apac | JP | Japan | 19 | 0 | IT-CORP, XB |
| ryan | apac | KG | Kyrgyzstan | 6 | 0 | TP, XB |
| ryan | apac | KH | Cambodia | 6 | 0 | TP, XB |
| ryan | apac | KR | South Korea | 6 | 0 | IT-CORP, PR, TP, XB |
| ryan | apac | KZ | Kazakhstan | 17 | 0 | TP, XB |
| ryan | apac | LA | Laos | 5 | 0 | TP, XB |
| ryan | apac | LK | Sri Lanka | 10 | 0 | SC, TP, XB |
| ryan | apac | MM | Myanmar | 12 | 0 | IT-CORP, TP, XB |
| ryan | apac | MN | Mongolia | 5 | 0 | TP, XB |
| ryan | apac | MO | Macau | 5 | 0 | TP, XB |
| ryan | apac | MV | Maldives | 6 | 0 | TP, XB |
| ryan | apac | MY | Malaysia | 8 | 1 | VAT, SC, PR, TP, XB |
| ryan | apac | NP | Nepal | 5 | 0 | SC, TP, XB |
| ryan | apac | NZ | New Zealand | 11 | 0 | IT-CORP, SC, PR, TP, XB |
| ryan | apac | PG | Papua New Guinea | 6 | 0 | TP, XB |
| ryan | apac | PH | Philippines | 7 | 7 | SC, TP, XB |
| ryan | apac | PK | Pakistan | 19 | 0 | TP, XB |
| ryan | apac | SG | Singapore | 10 | 0 | IT-CORP, SC, PR, XB |
| ryan | apac | TH | Thailand | 7 | 0 | TP, XB |
| ryan | apac | TJ | Tajikistan | 6 | 0 | TP, XB |
| ryan | apac | TL | Timor Leste | 6 | 0 | TP, XB |
| ryan | apac | TM | Turkmenistan | 6 | 0 | TP, XB |
| ryan | apac | TO | Tonga | 6 | 0 | TP, XB |
| ryan | apac | TW | Taiwan | 6 | 0 | SC, PR, TP, XB |
| ryan | apac | UZ | Uzbekistan | 8 | 0 | TP, XB |
| ryan | apac | VN | Vietnam | 8 | 0 | TP, XB |
| ryan | apac | VU | Vanuatu | 6 | 0 | TP, XB |
| ryan | apac | WS | Samoa | 6 | 0 | TP, XB |
