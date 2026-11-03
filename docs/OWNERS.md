# Owners

Who owns each jurisdiction for the [GOAL.md](GOAL.md) push. The owner drives the pack to complete and verified; they do not have to write every line themselves. James Wallach works with Jeff on the US. Change this file by PR.

**Every owner and every writer, human or AI, builds skills to one standard: [docs/skill-template.md](skill-template.md) ("How to write a skill: the standard").** Primary sources only, one independent review before merge, nothing unconfirmed in the skill.

**Agents starting European work: read [Europe writing assignments](#europe-writing-assignments) first.** It records the allocation as of 31 October 2026.

| Owner | Regions | Jurisdictions | Thin (7 or fewer skills) |
|---|---|---|---|
| Jeff Watts | Americas: US federal and states, Canada and provinces, Latin America, Caribbean | 105 | 91 |
| Ryan Duguid | Asia-Pacific, Africa | 94 | 73 |
| Michael Cutajar | Europe, Middle East; merges and final review | 67 | 12 |

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

Michael set this allocation on 23 October 2026 and remains the accountable owner for Europe. A writing allocation does not transfer professional responsibility, and it does not make a skill Accountant-reviewed.

**Claude: 32 jurisdictions. ChatGPT: 23.** A country allocation covers every topic, including existing skills. One active writer per country.

### 23 and 24 October 2026

- 23 October: Michael split the 55 European jurisdictions between Claude (22) and ChatGPT (33).
- 24 October: Michael handed Bulgaria (BG), Croatia (HR), Estonia (EE), Latvia (LV), Lithuania (LT), Slovakia (SK) and Slovenia (SI) from ChatGPT to Claude. That made Claude 29 and ChatGPT 26. The follow-ups recorded at that handover were fixed on 30 October: the Lithuania formation VAT test (#947) and the Slovenia income tax conflict noted on #769 (#943). The older overview, formation and optimisation skills in these packs were refreshed the same day.
- 24 October: Michael replaced the consolidated PR #514 with one PR per country. The [split register](research/2026-10-24-country-pr-split.md) maps each replacement PR. #514 and its branch stay as historical review evidence.

### 30-31 October 2026

On 30 October Michael said to finish Europe and "max out the agents". 116 PRs merged on 30 and 31 October (to 08:33 UTC on 31 October).

- **Claude's 29 countries:** Claude refreshed every remaining pre-2026 file in them, one PR per skill.
- **Taken by Claude:** Bosnia (BA), Ukraine (UA), Andorra (AD) and Spain (ES). They were ChatGPT allocations with no open PR. A handover comment was posted on each country issue (#381, #428, #376, #391) before the work started.
- **Stale ChatGPT country PRs:** Claude reviewed, fixed and merged #782 IS, #783 IM, #784 XK, #786 ME, #787 NO, #790 SM, #793 MD, #807 MK and #915 IT. Each got an independent review, and a second review where the first reviewer rebuilt files. The remaining old files in those countries were then rewritten and reviewed.
- **Liechtenstein:** PR #785 is being finished the same way.
- **Germany #921 and Slovakia #907** stay with ChatGPT.
- **Spain closeout (31 October):** Michael asked ChatGPT to finish the remaining scope. The handover is recorded on #391. Preserve Claude’s merged formation/optimisation refreshes and the #905 tax pack; one active writer, one country batch. The reviewed withholding and foreign-assignment additions leave two crypto computations open, not six whole ordinary domains.
- **EU-wide VAT:** the EU VAT base and directive skills were brought to 2026 (#1017, #1018).

State on main at 31 October:

- 50 of the 55 European packs have every skill on `tax_year: 2026`. Five are still on 2025, all ChatGPT allocations: Liechtenstein (PR #785), Azerbaijan (draft PR #797), Belarus (draft PR #835), Georgia and Turkey (no open PR). The `references.md` files and the UK `crypto-accounting` skill carry no tax year.
- Accountant review is zero for every pack worked on 30-31 October. An independent AI review and a merge do not make a skill Accountant-reviewed.

### Publishing

- Read this section, the country issue, the skills on main and the open PRs before starting. Reuse existing work whoever wrote it.
- Every skill gets an independent review against the law before merge. Most of the 30-31 October work used one PR per skill. A country batch reviewed together can go in one country PR.
- Keep each pack's applicable domains, `partial:` entries and gaps in its README. Merging a skill does not prove the pack is complete.

### Country allocation

Writer is who holds the country now. Tax year is the year on every skill on main at 31 October. Issue state and PRs as of 31 October.

| Code | Country or territory | Writer | Tax year | Status |
|---|---|---|---|---|
| AD | Andorra | Claude (from ChatGPT, 30 Oct) | 2026 | Overview and formation refreshed (#954, #958, #992). Issue #376 open. |
| AL | Albania | Claude | 2026 | Issue #377 closed. |
| AM | Armenia | ChatGPT | 2026 | Issue #378 closed. |
| AT | Austria | Claude | 2026 | Issue #379 closed. |
| AZ | Azerbaijan | ChatGPT | 2025 | Draft PR #797 open. Issue #380 open. |
| BA | Bosnia and Herzegovina | Claude (from ChatGPT, 30 Oct) | 2026 | All ten skills rebuilt or refreshed (#964, #971, #976 to #979, #981, #985, #989, #993). Issue #381 open. |
| BE | Belgium | Claude | 2026 | Issue #382 closed. |
| BG | Bulgaria | Claude | 2026 | Issue #383 closed. |
| BY | Belarus | ChatGPT | 2025 | Draft PR #835 open. Issue #384 open. |
| CH | Switzerland | Claude | 2026 | Issue #385 closed. |
| CY | Cyprus | Claude | 2026 | Issue #386 closed. |
| CZ | Czech Republic | Claude | 2026 | Issue #387 closed. |
| DE | Germany | Claude | 2026 | ChatGPT PR #921 open; it stays with ChatGPT. Issue #388 open. |
| DK | Denmark | Claude | 2026 | Issue #389 closed. |
| EE | Estonia | Claude | 2026 | Issue #390 closed. |
| ES | Spain | ChatGPT closeout (from Claude, 31 Oct) | 2026 | #905 and Claude's #972/#980 preserved. Reviewed closeout additions are on `codex/spain-closeout-2026`; #391 stays open for Navarra multi-lot crypto cost and Álava blocked crypto-loss release. |
| FI | Finland | ChatGPT | 2026 | Issue #392 closed. |
| FO | Faroe Islands | ChatGPT | 2026 | Draft PR #776 open. Issue #393 open. |
| FR | France | Claude | 2026 | Issue #394 closed. |
| GB | United Kingdom | Claude | 2026 | Issue #395 closed. |
| GE | Georgia | ChatGPT | 2025 | No open PR. Issue #396 open. |
| GG | Guernsey | ChatGPT | 2026 | No open PR. Issue #397 open. |
| GI | Gibraltar | ChatGPT | 2026 | PR #778 open. Issue #398 open. |
| GR | Greece | Claude | 2026 | Issue #399 closed. |
| HR | Croatia | Claude | 2026 | Issue #400 closed. |
| HU | Hungary | Claude | 2026 | Issue #401 closed. |
| IE | Ireland | Claude | 2026 | Issue #402 closed. |
| IM | Isle of Man | ChatGPT; Claude finished the open work | 2026 | #783 merged 30 Oct; CIT, overview, formation, VAT and payroll rebuilt (#1013, #1015, #1016, #1020, #1021). Issue #403 open. |
| IS | Iceland | ChatGPT; Claude finished the open work | 2026 | #782 merged 30 Oct; optimisation, overview and formation refreshed (#1012, #1014, #1019). Issue #404 open. |
| IT | Italy | Claude | 2026 | ChatGPT PR #915 reviewed, fixed and merged 30 Oct. Issue #405 closed. |
| LI | Liechtenstein | ChatGPT; Claude finishing PR #785 | 2025 | Draft PR #785 open. Issue #406 open. |
| LT | Lithuania | Claude | 2026 | Issue #407 closed. |
| LU | Luxembourg | Claude | 2026 | Issue #408 closed. |
| LV | Latvia | Claude | 2026 | Issue #409 closed. |
| MC | Monaco | ChatGPT | 2026 | #796 merged 27 Oct. Issue #410 closed. |
| MD | Moldova | ChatGPT; Claude finished the open work | 2026 | #793 merged 31 Oct; remaining skills rebuilt or refreshed (#1008 to #1011, #1024 to #1029). Issue #411 open. |
| ME | Montenegro | ChatGPT; Claude finished the open work | 2026 | #786 merged 30 Oct; overview and formation refreshed (#1001 to #1003). Issue #412 open. |
| MK | North Macedonia | ChatGPT; Claude finished the open work | 2026 | #807 merged 30 Oct. Issue #413 open. |
| MT | Malta | Claude | 2026 | Issue #414 closed. |
| NL | Netherlands | Claude | 2026 | PR #939 (VAT return merge) open. Issue #415 closed. |
| NO | Norway | ChatGPT; Claude finished the open work | 2026 | #787 merged 30 Oct; CIT, personal income tax, social contributions, VAT, overview, formation and exit skills rebuilt or refreshed, README maps all seven domains (#997 to #1000, #1004 to #1007, #1023). Issue #416 open. |
| PL | Poland | Claude | 2026 | Issue #417 closed. |
| PT | Portugal | Claude | 2026 | Issue #418 closed. |
| RO | Romania | Claude | 2026 | Issue #419 closed. |
| RS | Serbia | Claude | 2026 | Issue #420 closed. |
| SE | Sweden | Claude | 2026 | Issue #422 closed. |
| SI | Slovenia | Claude | 2026 | Issue #423 closed. |
| SJ | Svalbard | ChatGPT | 2026 | Draft PR #846 open. Issue #424 open. |
| SK | Slovakia | Claude | 2026 | ChatGPT draft PR #907 open; it stays with ChatGPT. Issue #425 open. |
| SM | San Marino | ChatGPT; Claude finished the open work | 2026 | #790 merged 30 Oct. Issue #426 open. |
| TR | Turkey | ChatGPT | 2025 | No open PR. Issue #427 open. |
| UA | Ukraine | Claude (from ChatGPT, 30 Oct) | 2026 | Rebuilt or refreshed, with new TP and cross-border skills (#959, #966, #974, #984, #986, #987, #994 to #996). Issue #428 open. |
| VA | Vatican City | ChatGPT | 2026 | No open PR. Issue #429 open. |
| XK | Kosovo | ChatGPT; Claude finished the open work | 2026 | #784 merged 30 Oct. Issue #430 open. |

### Handover rules

- One active writer per country. Before another writer starts, record a handover on the country issue with the topic, branch or PR, unfinished scope and next action. Inactivity or a merged PR alone does not transfer a country.
- An independent review does not transfer writing. Keep author and reviewer records. Accountant review is separate and is the only way a skill becomes Accountant-reviewed.

This allocation covers only the 55 jurisdictions labelled `europe` below. Ryan's Asia-Pacific and Africa allocation, Jeff's Americas allocation and Michael's Middle East accountability are unchanged. Caribbean and Middle East drafts in the #514 split are preserved contributions, not a new regional assignment. Assign Jersey or Åland work here before adding it to this table.

## By jurisdiction

Generated from `python3 scripts/coverage-report.py --markdown` on 2026-10-31 (tax domains); the issue for each row is the live status. Stale counts skills with no `last_updated` or one more than 365 days old. Regenerate with the same command when owners change.

| Owner | Region | Code | Name | Skills | Reviewed | Stale | Missing domains |
|---|---|---|---|---|---|---|---|
| jeff | americas | AG | Antigua And Barbuda | 3 | 0 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | AR | Argentina | 8 | 0 | 0 | PR, TP, XB |
| jeff | americas | AW | Aruba | 3 | 0 | 0 | IT-CORP, VAT, PR, TP, XB |
| jeff | americas | BB | Barbados | 6 | 0 | 0 | TP, XB |
| jeff | americas | BL | Saint Barthelemy | 2 | 0 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | BM | Bermuda | 7 | 0 | 0 | TP, XB |
| jeff | americas | BO | Bolivia | 5 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | BR | Brazil | 14 | 0 | 0 | IT-CORP, SC, XB |
| jeff | americas | BS | Bahamas | 6 | 0 | 0 | TP, XB |
| jeff | americas | BZ | Belize | 6 | 0 | 0 | TP, XB |
| jeff | americas | CA | Canada | 51 | 1 | 0 | none |
| jeff | americas | CA-AB | Alberta (Canada) | 2 | 0 | 0 | IT-CORP, VAT, SC, PR, TP |
| jeff | americas | CL | Chile | 8 | 0 | 0 | PR, TP, XB |
| jeff | americas | CO | Colombia | 8 | 0 | 0 | PR, TP, XB |
| jeff | americas | CR | Costa Rica | 5 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | CU | Cuba | 6 | 0 | 0 | TP, XB |
| jeff | americas | CW | Cura Ao | 6 | 0 | 0 | TP, XB |
| jeff | americas | DM | Dominica | 4 | 0 | 0 | TP, XB |
| jeff | americas | DO | Dominican Republic | 22 | 0 | 0 | none |
| jeff | americas | EC | Ecuador | 8 | 0 | 0 | VAT, TP, XB |
| jeff | americas | GD | Grenada | 3 | 0 | 0 | IT-IND, IT-CORP, PR, TP, XB |
| jeff | americas | GF | French Guiana | 2 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | GL | Greenland | 2 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, TP, XB |
| jeff | americas | GP | Guadeloupe | 1 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | GT | Guatemala | 7 | 0 | 0 | VAT, TP, XB |
| jeff | americas | GY | Guyana | 6 | 0 | 0 | TP, XB |
| jeff | americas | HN | Honduras | 7 | 0 | 0 | VAT, TP, XB |
| jeff | americas | HT | Haiti | 6 | 0 | 0 | VAT, SC, TP, XB |
| jeff | americas | JM | Jamaica | 6 | 0 | 0 | VAT, TP, XB |
| jeff | americas | KN | Saint Kitts And Nevis | 2 | 0 | 0 | IT-IND, IT-CORP, VAT, PR, TP, XB |
| jeff | americas | KY | Cayman Islands | 6 | 0 | 0 | TP, XB |
| jeff | americas | LC | Saint Lucia | 5 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | MF | Saint Martin | 3 | 0 | 0 | IT-IND, VAT, SC, PR, TP, XB |
| jeff | americas | MQ | Martinique | 1 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | MS | Montserrat | 3 | 0 | 0 | VAT, TP |
| jeff | americas | MX | Mexico | 12 | 0 | 0 | IT-CORP, SC, PR, XB |
| jeff | americas | NI | Nicaragua | 7 | 0 | 0 | VAT, TP, XB |
| jeff | americas | PA | Panama | 4 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | PE | Peru | 7 | 0 | 0 | VAT, TP, XB |
| jeff | americas | PM | Saint Pierre And Miquelon | 2 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | PR | Puerto Rico | 3 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | PY | Paraguay | 4 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | SR | Suriname | 6 | 0 | 0 | TP, XB |
| jeff | americas | SV | El Salvador | 5 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | SX | Sint Maarten | 3 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | TC | Turks And Caicos | 3 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | TT | Trinidad And Tobago | 6 | 0 | 0 | TP, XB |
| jeff | americas | US | United States (federal) | 103 | 21 | 0 | SC, TP |
| jeff | americas | US-AK | Alaska (US) | 1 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AL | Alabama (US) | 4 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AR | Arkansas (US) | 4 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-AZ | Arizona (US) | 4 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-CA | California (US) | 16 | 0 | 0 | IT-CORP, SC, TP |
| jeff | americas | US-CO | Colorado (US) | 6 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-CT | Connecticut (US) | 3 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-DC | District of Columbia (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-DE | Delaware (US) | 4 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-FL | Florida (US) | 7 | 0 | 0 | SC, PR, TP, XB |
| jeff | americas | US-GA | Georgia (US) | 10 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-HI | Hawaii (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-IA | Iowa (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-ID | Idaho (US) | 2 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-IL | Illinois (US) | 6 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-IN | Indiana (US) | 3 | 0 | 0 | IT-IND, IT-CORP, SC, TP, XB |
| jeff | americas | US-KS | Kansas (US) | 7 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-KY | Kentucky (US) | 3 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-LA | Louisiana (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MA | Massachusetts (US) | 7 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-MD | Maryland (US) | 3 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-ME | Maine (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MI | Michigan (US) | 9 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-MN | Minnesota (US) | 5 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-MO | Missouri (US) | 4 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-MS | Mississippi (US) | 3 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-MT | Montana (US) | 1 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-NC | North Carolina (US) | 7 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-ND | North Dakota (US) | 6 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-NE | Nebraska (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NH | New Hampshire (US) | 2 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-NJ | New Jersey (US) | 5 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-NM | New Mexico (US) | 3 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NV | Nevada (US) | 5 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-NY | New York (US) | 16 | 0 | 0 | SC, TP |
| jeff | americas | US-NY-NYC | New York City (US) | 1 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| jeff | americas | US-OH | Ohio (US) | 6 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-OK | Oklahoma (US) | 3 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-OR | Oregon (US) | 3 | 0 | 0 | IT-CORP, VAT, SC, TP, XB |
| jeff | americas | US-PA | Pennsylvania (US) | 5 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-RI | Rhode Island (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-SC | South Carolina (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-SD | South Dakota (US) | 1 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-TN | Tennessee (US) | 1 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-TX | Texas (US) | 8 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-UT | Utah (US) | 3 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-VA | Virginia (US) | 4 | 0 | 0 | SC, TP, XB |
| jeff | americas | US-VT | Vermont (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WA | Washington (US) | 5 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WI | Wisconsin (US) | 4 | 0 | 0 | IT-CORP, SC, TP, XB |
| jeff | americas | US-WV | West Virginia (US) | 2 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| jeff | americas | US-WY | Wyoming (US) | 3 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| jeff | americas | UY | Uruguay | 7 | 0 | 0 | VAT, TP, XB |
| jeff | americas | VC | Saint Vincent And The Grenadines | 3 | 0 | 0 | SC, PR, TP, XB |
| jeff | americas | VE | Venezuela | 5 | 0 | 0 | IT-CORP, VAT, TP, XB |
| jeff | americas | VG | British Virgin Islands | 6 | 0 | 0 | TP, XB |
| jeff | americas | VI | Us Virgin Islands | 3 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| michael | europe | AD | Andorra | 8 | 0 | 0 | IT-IND |
| michael | europe | AL | Albania | 8 | 0 | 0 | none |
| michael | europe | AM | Armenia | 10 | 0 | 0 | none |
| michael | europe | AT | Austria | 10 | 0 | 0 | none |
| michael | europe | AZ | Azerbaijan | 8 | 0 | 0 | TP, XB |
| michael | europe | BA | Bosnia | 10 | 0 | 0 | IT-IND, SC, PR, TP, XB |
| michael | europe | BE | Belgium | 15 | 0 | 0 | none |
| michael | europe | BG | Bulgaria | 10 | 0 | 0 | none |
| michael | europe | BY | Belarus | 8 | 0 | 0 | TP, XB |
| michael | europe | CH | Switzerland | 14 | 0 | 0 | none |
| michael | europe | CY | Cyprus | 9 | 0 | 0 | none |
| michael | europe | CZ | Czech Republic | 13 | 0 | 0 | none |
| michael | europe | DE | Germany | 31 | 0 | 0 | none |
| michael | europe | DK | Denmark | 10 | 0 | 0 | none |
| michael | europe | EE | Estonia | 10 | 0 | 0 | none |
| michael | europe | ES | Spain | 30 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, XB |
| michael | europe | FI | Finland | 14 | 0 | 0 | none |
| michael | europe | FO | Faroe Islands | 5 | 0 | 0 | IT-CORP, TP |
| michael | europe | FR | France | 23 | 0 | 0 | none |
| michael | europe | GB | Uk | 35 | 0 | 0 | none |
| michael | europe | GE | Georgia | 8 | 3 | 0 | TP, XB |
| michael | europe | GG | Guernsey | 10 | 0 | 0 | IT-IND, IT-CORP, SC, PR, TP, XB |
| michael | europe | GI | Gibraltar | 5 | 0 | 0 | VAT, TP, XB |
| michael | europe | GR | Greece | 15 | 0 | 0 | none |
| michael | europe | HR | Croatia | 10 | 0 | 0 | none |
| michael | europe | HU | Hungary | 11 | 0 | 0 | none |
| michael | europe | IE | Ireland | 18 | 0 | 0 | none |
| michael | europe | IM | Im | 8 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| michael | europe | IS | Iceland | 10 | 0 | 0 | none |
| michael | europe | IT | Italy | 22 | 0 | 0 | none |
| michael | europe | LI | Liechtenstein | 6 | 0 | 0 | TP, XB |
| michael | europe | LT | Lithuania | 9 | 0 | 0 | none |
| michael | europe | LU | Luxembourg | 8 | 0 | 0 | none |
| michael | europe | LV | Latvia | 10 | 0 | 0 | none |
| michael | europe | MC | Monaco | 8 | 0 | 0 | none |
| michael | europe | MD | Moldova | 10 | 0 | 0 | PR, XB |
| michael | europe | ME | Montenegro | 10 | 0 | 0 | IT-IND |
| michael | europe | MK | North Macedonia | 10 | 0 | 0 | XB |
| michael | europe | MT | Malta | 34 | 0 | 0 | none |
| michael | europe | NL | Netherlands | 30 | 0 | 0 | none |
| michael | europe | NO | Norway | 12 | 0 | 0 | none |
| michael | europe | PL | Poland | 12 | 0 | 0 | none |
| michael | europe | PT | Portugal | 19 | 0 | 0 | none |
| michael | europe | RO | Romania | 13 | 0 | 0 | none |
| michael | europe | RS | Serbia | 10 | 0 | 0 | none |
| michael | europe | SE | Sweden | 15 | 0 | 0 | none |
| michael | europe | SI | Slovenia | 10 | 0 | 0 | none |
| michael | europe | SJ | Svalbard | 3 | 0 | 0 | IT-CORP, VAT, SC, TP, XB |
| michael | europe | SK | Slovakia | 10 | 0 | 0 | none |
| michael | europe | SM | San Marino | 8 | 0 | 0 | IT-CORP, VAT, SC |
| michael | europe | TR | Turkey | 8 | 0 | 0 | TP, XB |
| michael | europe | UA | Ukraine | 17 | 0 | 0 | none |
| michael | europe | VA | Vatican City | 1 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| michael | europe | XK | Kosovo | 8 | 0 | 0 | SC, PR |
| michael | middle-east | AE | Uae | 9 | 0 | 0 | TP, XB |
| michael | middle-east | BH | Bahrain | 6 | 0 | 0 | TP, XB |
| michael | middle-east | EG | Egypt | 17 | 0 | 0 | XB |
| michael | middle-east | IL | Israel | 10 | 0 | 0 | SC, TP, XB |
| michael | middle-east | IQ | Iraq | 7 | 0 | 0 | TP, XB |
| michael | middle-east | IR | Iran | 6 | 0 | 0 | TP, XB |
| michael | middle-east | JO | Jordan | 6 | 0 | 0 | TP, XB |
| michael | middle-east | KW | Kuwait | 6 | 0 | 0 | TP, XB |
| michael | middle-east | LB | Lebanon | 6 | 0 | 0 | TP, XB |
| michael | middle-east | OM | Oman | 6 | 0 | 0 | TP, XB |
| michael | middle-east | QA | Qatar | 8 | 0 | 0 | none |
| michael | middle-east | SA | Saudi Arabia | 12 | 0 | 0 | SC, TP, XB |
| ryan | africa | AO | Angola | 6 | 0 | 0 | TP, XB |
| ryan | africa | BF | Burkina Faso | 8 | 0 | 0 | TP, XB |
| ryan | africa | BI | Burundi | 6 | 0 | 0 | TP, XB |
| ryan | africa | BJ | Benin | 6 | 0 | 0 | TP, XB |
| ryan | africa | BW | Botswana | 6 | 0 | 0 | TP, XB |
| ryan | africa | CD | Dr Congo | 6 | 0 | 0 | TP, XB |
| ryan | africa | CF | Central African Republic | 6 | 0 | 0 | TP, XB |
| ryan | africa | CG | Republic Of Congo | 6 | 0 | 0 | TP, XB |
| ryan | africa | CI | Ivory Coast | 4 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | CM | Cameroon | 4 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | CV | Cape Verde | 6 | 0 | 0 | TP, XB |
| ryan | africa | DJ | Djibouti | 6 | 0 | 0 | TP, XB |
| ryan | africa | DZ | Algeria | 4 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | ER | Eritrea | 6 | 0 | 0 | TP, XB |
| ryan | africa | ET | Ethiopia | 7 | 0 | 0 | TP, XB |
| ryan | africa | GA | Gabon | 5 | 0 | 0 | TP, XB |
| ryan | africa | GH | Ghana | 7 | 0 | 0 | TP, XB |
| ryan | africa | GM | Gambia | 6 | 0 | 0 | TP, XB |
| ryan | africa | GN | Guinea | 6 | 0 | 0 | TP, XB |
| ryan | africa | GQ | Equatorial Guinea | 6 | 0 | 0 | TP, XB |
| ryan | africa | GW | Guinea Bissau | 6 | 0 | 0 | TP, XB |
| ryan | africa | KE | Kenya | 14 | 0 | 0 | SC, PR, TP |
| ryan | africa | KM | Comoros | 3 | 0 | 0 | IT-CORP, VAT, SC, PR, TP, XB |
| ryan | africa | LR | Liberia | 6 | 0 | 0 | TP, XB |
| ryan | africa | LS | Lesotho | 6 | 0 | 0 | TP, XB |
| ryan | africa | LY | Libya | 6 | 0 | 0 | TP, XB |
| ryan | africa | MA | Morocco | 16 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | MG | Madagascar | 6 | 0 | 0 | TP, XB |
| ryan | africa | ML | Mali | 6 | 0 | 0 | TP, XB |
| ryan | africa | MR | Mauritania | 6 | 0 | 0 | TP, XB |
| ryan | africa | MU | Mauritius | 6 | 0 | 0 | TP, XB |
| ryan | africa | MW | Malawi | 6 | 0 | 0 | TP, XB |
| ryan | africa | MZ | Mozambique | 4 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | NA | Namibia | 6 | 0 | 0 | TP, XB |
| ryan | africa | NE | Niger | 5 | 0 | 0 | TP, XB |
| ryan | africa | NG | Nigeria | 14 | 0 | 0 | SC, TP, XB |
| ryan | africa | RE | Reunion | 1 | 0 | 0 | IT-IND, IT-CORP, VAT, SC, PR, TP, XB |
| ryan | africa | RW | Rwanda | 8 | 0 | 0 | TP, XB |
| ryan | africa | SC | Seychelles | 5 | 0 | 0 | TP, XB |
| ryan | africa | SD | Sudan | 6 | 0 | 0 | TP, XB |
| ryan | africa | SH | Saint Helena | 4 | 0 | 0 | IT-CORP, VAT, SC, TP, XB |
| ryan | africa | SL | Sierra Leone | 6 | 0 | 0 | TP, XB |
| ryan | africa | SN | Senegal | 7 | 0 | 0 | TP, XB |
| ryan | africa | SO | Somalia | 6 | 0 | 0 | TP, XB |
| ryan | africa | SS | South Sudan | 6 | 0 | 0 | TP, XB |
| ryan | africa | ST | S O Tom And Pr Ncipe | 6 | 0 | 0 | TP, XB |
| ryan | africa | SZ | Eswatini | 6 | 0 | 0 | TP, XB |
| ryan | africa | TD | Chad | 6 | 0 | 0 | TP, XB |
| ryan | africa | TG | Togo | 6 | 0 | 0 | TP, XB |
| ryan | africa | TN | Tunisia | 7 | 0 | 0 | TP, XB |
| ryan | africa | TZ | Tanzania | 6 | 0 | 0 | IT-CORP, TP, XB |
| ryan | africa | UG | Uganda | 6 | 0 | 0 | TP, XB |
| ryan | africa | YT | Mayotte | 2 | 0 | 0 | IT-IND, IT-CORP, SC, TP, XB |
| ryan | africa | ZA | South Africa | 20 | 0 | 0 | IT-CORP, SC, PR |
| ryan | africa | ZM | Zambia | 6 | 0 | 0 | TP, XB |
| ryan | africa | ZW | Zimbabwe | 6 | 0 | 0 | TP, XB |
| ryan | apac | AF | Afghanistan | 6 | 0 | 0 | TP, XB |
| ryan | apac | AU | Australia | 61 | 0 | 0 | none |
| ryan | apac | BD | Bangladesh | 18 | 0 | 0 | TP, XB |
| ryan | apac | BN | Brunei | 7 | 0 | 0 | TP, XB |
| ryan | apac | BT | Bhutan | 6 | 0 | 0 | TP, XB |
| ryan | apac | CN | China | 14 | 0 | 0 | TP |
| ryan | apac | FJ | Fiji | 6 | 0 | 0 | TP, XB |
| ryan | apac | HK | Hong Kong | 7 | 0 | 0 | SC, PR, TP, XB |
| ryan | apac | ID | Indonesia | 13 | 0 | 0 | SC, TP, XB |
| ryan | apac | IN | India | 22 | 0 | 0 | IT-CORP, SC |
| ryan | apac | JP | Japan | 19 | 0 | 0 | IT-CORP, XB |
| ryan | apac | KG | Kyrgyzstan | 6 | 0 | 0 | TP, XB |
| ryan | apac | KH | Cambodia | 6 | 0 | 0 | TP, XB |
| ryan | apac | KR | South Korea | 6 | 0 | 0 | IT-CORP, PR, TP, XB |
| ryan | apac | KZ | Kazakhstan | 17 | 0 | 0 | TP, XB |
| ryan | apac | LA | Laos | 5 | 0 | 0 | TP, XB |
| ryan | apac | LK | Sri Lanka | 10 | 0 | 0 | SC, TP, XB |
| ryan | apac | MM | Myanmar | 11 | 0 | 0 | IT-CORP, TP, XB |
| ryan | apac | MN | Mongolia | 5 | 0 | 0 | TP, XB |
| ryan | apac | MO | Macau | 5 | 0 | 0 | TP, XB |
| ryan | apac | MV | Maldives | 6 | 0 | 0 | TP, XB |
| ryan | apac | MY | Malaysia | 8 | 1 | 0 | VAT, SC, PR, TP, XB |
| ryan | apac | NP | Nepal | 5 | 0 | 0 | SC, TP, XB |
| ryan | apac | NZ | New Zealand | 11 | 0 | 0 | IT-CORP, SC, PR, TP, XB |
| ryan | apac | PG | Papua New Guinea | 6 | 0 | 0 | TP, XB |
| ryan | apac | PH | Philippines | 7 | 7 | 0 | SC, TP, XB |
| ryan | apac | PK | Pakistan | 19 | 0 | 0 | TP, XB |
| ryan | apac | SG | Singapore | 10 | 0 | 0 | IT-CORP, SC, PR, XB |
| ryan | apac | TH | Thailand | 7 | 0 | 0 | TP, XB |
| ryan | apac | TJ | Tajikistan | 6 | 0 | 0 | TP, XB |
| ryan | apac | TL | Timor Leste | 6 | 0 | 0 | TP, XB |
| ryan | apac | TM | Turkmenistan | 6 | 0 | 0 | TP, XB |
| ryan | apac | TO | Tonga | 6 | 0 | 0 | TP, XB |
| ryan | apac | TW | Taiwan | 6 | 0 | 0 | SC, PR, TP, XB |
| ryan | apac | UZ | Uzbekistan | 8 | 0 | 0 | TP, XB |
| ryan | apac | VN | Vietnam | 8 | 0 | 0 | TP, XB |
| ryan | apac | VU | Vanuatu | 6 | 0 | 0 | TP, XB |
| ryan | apac | WS | Samoa | 6 | 0 | 0 | TP, XB |
