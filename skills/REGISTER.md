# Skills register

Generated from the skill tree on 2026-10-31 by `scripts/build-register.py`. One row per skill in `REGISTER.csv`. This file is the summary.

## Totals

- Skills: 2280
- Jurisdictions: 273 (265 countries or states, the rest pseudo-codes)
- Tax year 2026: 994; still 2025: 1160; no year: 121
- Signed by a named accountant (tier 1): 30, in US (21), PH (7), CA (1), MY (1)
- Scope: 2048 tax skills (deep-tax shape applies), 89 accounting-pack skills (general template), 143 other (routers, templates, patterns)
- Domain from the README `covered_by`: 194; from the slug: 1205; no tax domain: 881
- Pass all 10 checks: 205 of 2048 tax skills
- Duplicates: 396 skills in 142 (country, domain) cells where the README does not name which skill covers the job

## Pass rate per check

Tax skills only (the deep-tax shape applies to them). One column per check in `REGISTER.csv`; the letters are the order in `scripts/skill_checks.py`.

| | Check | Pass | Fail | Pass rate |
|---|---|---:|---:|---:|
| (a) | `tax_year_current` | 902 | 1158 | 44% |
| (b) | `sources_read_dates` | 574 | 1486 | 28% |
| (c) | `rates_rows_sourced` | 247 | 1813 | 12% |
| (d) | `canonical_headings` | 486 | 1574 | 24% |
| (e) | `two_oa_checks` | 510 | 1550 | 25% |
| (f) | `version_numeric` | 1260 | 800 | 61% |
| (g) | `tier_honest` | 1927 | 133 | 94% |
| (h) | `no_em_dash` | 771 | 1289 | 37% |
| (i) | `not_yet_confirmed` | 553 | 1507 | 27% |
| (j) | `reviewed_on` | 1913 | 147 | 93% |

## Rates rows

Tax skills only: 30178 rows, 7704 linked (25.5%), 0 marked unverified (0.0%), 22474 neither. A row marked unverified is not counted as linked.


## By domain

A skill covering two domains counts in both.

| Domain | Skills | Signed |
|---|---:|---:|
| IT-IND | 402 | 4 |
| IT-CORP | 189 | 2 |
| VAT | 305 | 3 |
| SC | 197 | 1 |
| PR | 237 | 2 |
| TP | 65 | 0 |
| XB | 127 | 0 |
| (no tax domain) | 888 | 18 |

## Country by domain

Count of skills in each (country, domain) cell. `*` means at least one is signed by a named accountant; `!` means two or more skills share the cell and the README does not name which one covers it (a duplicate).

| Country | IT-IND | IT-CORP | VAT | SC | PR | TP | XB | All pass | 2026 | Signed | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| US | 36*! | 2! | 4*! |  | 4*! |  | 2! | 0 | 38 | 21 | 102 |
| AU | 7! | 1 | 3! | 1 | 4! | 1 | 4! | 0 | 33 | 0 | 61 |
| CA | 18! | 2! | 1 | 1 | 2! | 1 | 2! | 0 | 5 | 1 | 51 |
| GB | 5! | 1 | 5! | 1 | 2! | 1 | 4! | 15 | 33 | 0 | 35 |
| MT | 6! | 1 | 2! | 1 | 1 | 1 | 1 | 1 | 32 | 0 | 34 |
| DE | 5! | 1 | 2! | 1 | 3! | 1 | 4! | 11 | 28 | 0 | 29 |
| ES | 6! | 2! | 1 | 1 | 2! | 1 | 2! | 20 | 28 | 0 | 29 |
| NL | 4! | 1 | 2! | 1 | 2! | 1 | 1 | 9 | 25 | 0 | 27 |
| FR | 5! | 1 | 1 | 1 | 1 | 1 | 2! | 2 | 22 | 0 | 23 |
| DO | 2! | 1 | 1 | 1 | 2! | 1 | 1 | 0 | 1 | 0 | 22 |
| IT | 1 | 1 | 1 | 2! | 1 | 1 | 1 | 7 | 21 | 0 | 22 |
| IN | 5! |  | 1 | 1 | 1 | 1 | 1 | 0 | 17 | 0 | 21 |
| ZA | 6! |  | 3! |  |  | 1 | 2! | 0 | 2 | 0 | 20 |
| PK | 3! | 1 | 3! | 1 | 3! |  |  | 0 | 8 | 0 | 19 |
| BD | 3! | 1 | 1 | 2! | 2! |  |  | 0 | 11 | 0 | 18 |
| IE | 3! | 1 | 1 | 1 | 3! | 1 | 3! | 11 | 18 | 0 | 18 |
| JP | 3! |  | 2! | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 18 |
| PT | 3! | 1 | 1 | 1 | 1 | 1 | 2! | 2 | 18 | 0 | 18 |
| EG | 3! | 1 | 1 | 1 | 2! | 1 |  | 0 | 11 | 0 | 17 |
| KZ | 3! | 1 | 1 | 2! | 2! |  |  | 0 | 11 | 0 | 17 |
| UA | 3! | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 17 | 0 | 17 |
| MA | 4! |  | 1 | 1 | 1 |  |  | 0 | 6 | 0 | 16 |
| US-CA | 4! |  | 1 |  | 1 |  | 1 | 0 | 10 | 0 | 16 |
| US-NY | 6! | 1 | 2! |  | 1 |  | 1 | 0 | 6 | 0 | 16 |
| CN | 4! | 1 | 1 | 1 | 1 | 1 | 2! | 5 | 9 | 0 | 15 |
| GR | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 2 | 15 | 0 | 15 |
| BE | 3! | 1 | 1 | 1 | 2! | 1 | 1 | 7 | 14 | 0 | 14 |
| BR | 4! |  | 1 | 1 | 1 | 1 |  | 0 | 1 | 0 | 14 |
| CH | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 6 | 14 | 0 | 14 |
| FI | 2! | 2! | 1 | 1 | 1 | 1 | 2! | 0 | 14 | 0 | 14 |
| NG | 4! | 1 | 3! |  | 1 |  |  | 0 | 0 | 0 | 14 |
| SE | 3! | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 13 | 0 | 14 |
| CZ | 2! | 1 | 2! | 2! | 1 | 1 | 1 | 3 | 12 | 0 | 13 |
| ID | 3! | 1 | 1 |  | 2! |  |  | 0 | 1 | 0 | 13 |
| KE | 3! | 1 | 1 |  |  |  | 1 | 1 | 2 | 0 | 13 |
| MX | 3! |  | 1 |  |  | 1 |  | 0 | 0 | 0 | 12 |
| NO | 3! | 1 | 1 | 1 | 1 | 1 | 2! | 0 | 12 | 0 | 12 |
| PL | 2! | 1 | 2! | 1 | 1 | 1 | 1 | 2 | 11 | 0 | 12 |
| RO | 2! | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 11 | 0 | 12 |
| SA | 2! | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 12 |
| HU | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 5 | 11 | 0 | 11 |
| MM | 3! |  | 3! | 1 | 1 |  |  | 0 | 0 | 0 | 11 |
| AM | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| AZ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 | 10 | 0 | 10 |
| BA | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| BG | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| BY | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 | 10 | 0 | 10 |
| EE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| GE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| GG | 1 | 1 | 1 | 1 | 2! | 1 | 1 | 2 | 10 | 0 | 10 |
| HR | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 10 | 0 | 10 |
| IL | 1 | 1 | 1 |  | 1 |  | 1 | 0 | 0 | 0 | 10 |
| IS | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 10 | 0 | 10 |
| LK | 2! | 1 | 1 |  | 2! |  |  | 0 | 0 | 0 | 10 |
| LV | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 10 | 0 | 10 |
| MD | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 | 0 | 10 |
| ME | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 10 | 0 | 10 |
| MK | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 10 | 0 | 10 |
| NZ | 2! |  | 1 | 1 |  |  | 1 | 2 | 9 | 0 | 10 |
| RS | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| SG | 1 |  | 2! | 1 |  | 1 | 1 | 0 | 3 | 0 | 10 |
| SI | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 10 | 0 | 10 |
| SK | 1 | 1 | 2! | 1 | 1 | 1 | 1 | 3 | 9 | 0 | 10 |
| TR | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 9 | 0 | 10 |
| US-GA | 2! | 3! | 1 |  | 1 |  |  | 0 | 3 | 0 | 10 |
| AT | 1 | 1 | 1 | 2! | 1 | 1 | 1 | 2 | 9 | 0 | 9 |
| CY | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | 0 | 9 |
| DK | 2! | 1 | 1 | 1 | 1 | 1 | 1 | 7 | 8 | 0 | 9 |
| LT | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 8 | 0 | 9 |
| US-MI | 3! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 9 |
| AD | 2! | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 8 | 0 | 8 |
| AE | 1 | 2! | 1 | 1 | 1 |  | 1 | 0 | 6 | 0 | 8 |
| AL | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 8 | 0 | 8 |
| AR | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| BF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| BH | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 0 | 8 |
| CL | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| CO | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 8 |
| EC | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| IM | 2! | 1 | 1 | 1 | 1 | 1 | 2! | 0 | 8 | 0 | 8 |
| LI | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 8 | 0 | 8 |
| LU | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 8 | 0 | 8 |
| MC | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 8 | 0 | 8 |
| MY | 1 | 1* | 1 | 1 | 1 |  |  | 0 | 1 | 1 | 8 |
| QA | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 | 8 | 0 | 8 |
| RW | 2! | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| SM | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 8 | 0 | 8 |
| US-TX | 3! | 1 | 2! |  |  |  |  | 0 | 1 | 0 | 8 |
| UZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 8 |
| VN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 8 |
| XK | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | 8 | 0 | 8 |
| BM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| BN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| ET | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| GH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| GT | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| HK |  | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 7 |
| HN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 1 | 0 | 7 |
| IQ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| NI | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| PE | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| PH | 1* | 1* | 1* | 1* | 1* |  |  | 0 | 0 | 7 | 7 |
| SN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 7 |
| TH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| TN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| US-FL | 1 | 1 | 1 |  |  |  |  | 0 | 3 | 0 | 7 |
| US-KS | 1 | 1 | 1 | 1 | 2! | 1 | 1 | 0 | 7 | 0 | 7 |
| US-MA | 1 | 1 | 4! |  | 1 |  |  | 0 | 0 | 0 | 7 |
| US-NC | 2! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 7 |
| UY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 7 |
| AF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| AO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BB | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BI | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BT | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CF | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CV | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| CW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 1 | 0 | 6 |
| DJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ER | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| FJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GN | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GQ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| GY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| HT | 1 | 1 | 1 |  | 2! |  |  | 0 | 6 | 0 | 6 |
| IR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| JM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| JO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KH | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KR | 1 |  | 2! | 1 |  |  |  | 0 | 0 | 0 | 6 |
| KW |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| KY |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LB | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| LY | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ML | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MV | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| MW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| NA | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| OM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| PG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SL | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SR | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ST | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| SZ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TD | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TJ | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TL | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TO | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TT | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| TW | 1 | 1 | 1 | 1 |  |  |  | 0 | 0 | 0 | 6 |
| TZ | 1 |  | 1 | 1 | 2! |  |  | 0 | 2 | 0 | 6 |
| UG | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| US-CO | 1 |  | 3! |  | 1 |  |  | 0 | 1 | 0 | 6 |
| US-IL | 2! |  | 2! |  | 1 |  |  | 0 | 1 | 0 | 6 |
| US-ND | 2! | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 6 |
| US-OH | 1 |  | 2! |  | 1 |  |  | 0 | 4 | 0 | 6 |
| VG |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| VU | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| WS | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ZM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| ZW | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 6 |
| BO | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| CR | 1 |  | 1 | 1 | 1 |  |  | 0 | 2 | 0 | 5 |
| FO | 1 |  | 1 | 1 | 1 |  | 1 | 0 | 5 | 0 | 5 |
| GA |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| GI | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 5 | 0 | 5 |
| LA |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| LC | 1 |  | 2! | 1 |  |  |  | 0 | 4 | 0 | 5 |
| MN |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| MO |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| NE |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| NP | 1 | 1 | 1 |  | 1 |  |  | 0 | 0 | 0 | 5 |
| SC |  | 1 | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| SV | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| US-MN | 1 | 1 | 2! |  | 1 |  |  | 0 | 0 | 0 | 5 |
| US-NJ | 1 |  | 2! |  | 1 |  |  | 0 | 4 | 0 | 5 |
| US-NV |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 5 |
| US-PA | 1 |  | 2! |  | 1 |  |  | 0 | 3 | 0 | 5 |
| US-WA | 1 |  | 2! |  |  |  |  | 0 | 4 | 0 | 5 |
| VE | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 5 |
| CI | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| CM | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| DM | 1 | 1 | 1 | 1 | 1 |  |  | 0 | 4 | 0 | 4 |
| DZ | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| MZ | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| PA | 1 |  | 1 | 1 | 1 |  |  | 0 | 1 | 0 | 4 |
| PY | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 | 4 |
| SH | 3! |  |  |  | 1 |  |  | 0 | 4 | 0 | 4 |
| US-AL | 2! |  | 2! |  |  |  |  | 0 | 0 | 0 | 4 |
| US-AR | 1 |  | 3! |  |  |  |  | 0 | 1 | 0 | 4 |
| US-AZ | 1 |  | 1 |  | 1 |  |  | 0 | 0 | 0 | 4 |
| US-DE | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 4 |
| US-MO | 1 |  | 2! |  | 1 |  |  | 0 | 0 | 0 | 4 |
| US-VA | 1 | 1 | 1 |  | 1 |  |  | 0 | 1 | 0 | 4 |
| US-WI | 1 |  | 2! |  | 1 |  |  | 0 | 1 | 0 | 4 |
| AG |  |  |  | 1 |  |  |  | 0 | 3 | 0 | 3 |
| AW | 1 |  | 1 | 1 |  |  |  | 0 | 3 | 0 | 3 |
| GD |  |  | 1 | 1 |  |  |  | 0 | 3 | 0 | 3 |
| KM | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| MF |  | 1 | 1 |  |  |  |  | 0 | 3 | 0 | 3 |
| MS |  | 1 |  | 1 | 1 |  | 1 | 0 | 3 | 0 | 3 |
| PR | 1 |  |  |  |  |  |  | 0 | 1 | 0 | 3 |
| SJ |  | 1 |  |  | 1 |  | 1 | 0 | 3 | 0 | 3 |
| SX | 1 |  | 1 |  | 1 |  |  | 0 | 3 | 0 | 3 |
| TC |  |  |  | 1 |  |  |  | 0 | 3 | 0 | 3 |
| US-CT | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-IN |  |  | 2! |  | 1 |  |  | 0 | 0 | 0 | 3 |
| US-KY | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-MD | 1 |  | 1 |  | 1 |  |  | 0 | 1 | 0 | 3 |
| US-MS | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-NM | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-OK | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-OR | 1 |  |  |  | 1 |  |  | 0 | 0 | 0 | 3 |
| US-UT | 1 |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| US-WY |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 3 |
| VC |  | 1 | 1 | 1 |  |  |  | 0 | 3 | 0 | 3 |
| VI | 1 |  |  |  |  |  |  | 0 | 3 | 0 | 3 |
| BL |  |  |  | 1 |  |  |  | 0 | 2 | 0 | 2 |
| CA-AB | 1 |  |  |  |  |  | 1 | 0 | 2 | 0 | 2 |
| GF |  |  | 1 |  |  |  |  | 0 | 2 | 0 | 2 |
| GL |  |  |  | 1 | 1 |  |  | 0 | 2 | 0 | 2 |
| KN |  |  |  | 2! |  |  |  | 0 | 2 | 0 | 2 |
| PM | 2! |  |  |  |  |  |  | 0 | 1 | 0 | 2 |
| US-DC | 1 |  | 1 |  |  |  |  | 0 | 1 | 0 | 2 |
| US-HI | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-IA | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-ID |  |  | 2! |  |  |  |  | 0 | 0 | 0 | 2 |
| US-LA | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-ME | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-NE | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-NH |  |  |  |  |  |  |  | 0 | 0 | 0 | 2 |
| US-RI | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-SC | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-VT | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| US-WV | 1 |  | 1 |  |  |  |  | 0 | 0 | 0 | 2 |
| YT |  |  | 1 |  | 1 |  |  | 0 | 2 | 0 | 2 |
| GP |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| MQ |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| RE |  |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| US-AK |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| US-MT | 1 |  |  |  |  |  |  | 0 | 1 | 0 | 1 |
| US-NY-NYC |  |  |  |  |  |  |  | 0 | 0 | 0 | 1 |
| US-SD |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| US-TN |  |  | 1 |  |  |  |  | 0 | 0 | 0 | 1 |
| VA |  |  |  |  |  |  | 1 | 0 | 1 | 0 | 1 |

## Duplicates

Skills that share a (country, domain) cell with another skill and are not named in the pack README's `covered_by`. Fix by naming one in the README or merging the skills.

| Country | Domain | Skill |
|---|---|---|
| AD | IT-IND | `ad-income-tax` |
| AD | IT-IND | `ad-non-resident-income-tax` |
| AE | IT-CORP | `ae-corporate-tax` |
| AE | IT-CORP | `general-uae-corporate-tax-guide` |
| AT | SC | `at-svs-contributions` |
| AU | IT-IND | `amending-an-individual-income-tax-return-in-australia` |
| AU | IT-IND | `au-amending-individual-income-tax-return-period` |
| AU | IT-IND | `au-capital-gains` |
| AU | IT-IND | `au-capital-gains-2` |
| AU | IT-IND | `au-freelance-intake` |
| AU | IT-IND | `au-individual-return` |
| AU | IT-IND | `au-return-assembly` |
| AU | PR | `au-employment-termination-payments` |
| AU | PR | `au-payroll-tax` |
| AU | PR | `au-working-holiday-makers` |
| AU | PR | `australia-payroll` |
| AU | VAT | `au-gst-bas` |
| AU | VAT | `au-gst-property` |
| AU | VAT | `australia-gst` |
| AU | XB | `au-nonresident-cgt` |
| AU | XB | `au-nonresident-cgt-2` |
| AU | XB | `leaving-australia-residency-the-cgt-departure-choice-and-what-follows-you` |
| AU | XB | `leaving-australia-tax-residency-cgt` |
| BD | IT-IND | `bangladesh-pit` |
| BD | IT-IND | `bd-freelance-intake` |
| BD | IT-IND | `bd-return-assembly` |
| BD | PR | `bd-payroll` |
| BD | SC | `bd-social-contributions` |
| BD | SC+PR | `bd-payroll-social` |
| BE | IT-IND | `be-capital-gains` |
| BE | IT-IND | `be-employee-income-tax` |
| BE | IT-IND | `be-income-tax` |
| BE | PR | `be-payroll-withholding` |
| BE | PR | `belgium-payroll` |
| BR | IT-IND | `br-carn-monthly-income-tax-rental-income` |
| BR | IT-IND | `br-freelance-intake` |
| BR | IT-IND | `br-income-tax` |
| BR | IT-IND | `br-return-assembly` |
| CA | IT-CORP | `ab-corporate-tax` |
| CA | IT-CORP | `qc-corporate-tax-co17` |
| CA | IT-IND | `ab-individual-return` |
| CA | IT-IND | `bc-individual-return` |
| CA | IT-IND | `ca-capital-gains` |
| CA | IT-IND | `ca-fed-t1-return` |
| CA | IT-IND | `ca-freelance-intake` |
| CA | IT-IND | `ca-return-assembly` |
| CA | IT-IND | `mb-individual-return` |
| CA | IT-IND | `nb-individual-return` |
| CA | IT-IND | `nl-individual-return` |
| CA | IT-IND | `ns-individual-return` |
| CA | IT-IND | `nt-individual-return` |
| CA | IT-IND | `nu-individual-return` |
| CA | IT-IND | `on-individual-return` |
| CA | IT-IND | `pe-individual-return` |
| CA | IT-IND | `qc-individual-return` |
| CA | IT-IND | `qc-qst-return` |
| CA | IT-IND | `sk-individual-return` |
| CA | IT-IND | `yt-individual-return` |
| CA | PR | `canada-payroll` |
| CA | PR | `nt-payroll-tax` |
| CA | XB | `ca-nonresident-cgt` |
| CA | XB | `leaving-canada-departure-tax` |
| CH | VAT | `ch-vat-return` |
| CH | VAT | `switzerland-vat` |
| CN | IT-IND | `china-pit` |
| CN | IT-IND | `cn-freelance-intake` |
| CN | IT-IND | `cn-return-assembly` |
| CN | XB | `china-to-singapore-relocation-tax` |
| CZ | IT-IND | `cz-employee-income-tax` |
| CZ | IT-IND | `cz-income-tax` |
| CZ | SC | `cz-employee-contributions` |
| CZ | SC | `cz-social-health` |
| CZ | VAT | `cz-vat-return` |
| CZ | VAT | `czech-republic-vat-return` |
| DE | IT-IND | `de-capital-gains` |
| DE | IT-IND | `de-employee-income-tax` |
| DE | IT-IND | `de-freelance-intake` |
| DE | IT-IND | `de-return-assembly` |
| DE | IT-IND | `germany-income-tax` |
| DE | PR | `de-payroll` |
| DE | PR | `de-payroll-benefits` |
| DE | PR+XB | `de-treaty-withholding-rates` |
| DE | VAT | `de-vat-annual-and-special-schemes` |
| DE | VAT | `germany-vat-return` |
| DE | XB | `de-non-resident-tax` |
| DE | XB | `germany-to-switzerland-cross-border-tax` |
| DK | IT-IND | `dk-capital-gains` |
| DK | IT-IND | `dk-income-tax` |
| DO | IT-IND | `do-capital-gains-tax` |
| DO | IT-IND | `dominican-republic-income-tax` |
| DO | PR | `do-withholding-tax` |
| DO | PR | `dominican-republic-payroll` |
| EG | IT-IND | `eg-freelance-intake` |
| EG | IT-IND | `eg-income-tax` |
| EG | IT-IND | `eg-return-assembly` |
| EG | PR | `eg-payroll` |
| EG | PR | `eg-withholding-tax` |
| ES | IT-CORP | `es-foral-corporate-tax` |
| ES | IT-IND | `es-capital-gains` |
| ES | IT-IND | `es-foral-income-tax` |
| ES | IT-IND | `es-freelance-intake` |
| ES | IT-IND | `es-return-assembly` |
| ES | IT-IND | `es-non-resident-income-tax-irnr-and` |
| ES | PR | `es-foral-payroll` |
| ES | XB | `es-foral-non-resident-tax` |
| FI | IT-CORP+XB | `fi-corporate-cross-border-tax` |
| FI | IT-IND | `fi-individual-cross-border-residence` |
| FR | IT-IND | `fr-capital-gains` |
| FR | IT-IND | `fr-freelance-intake` |
| FR | IT-IND | `fr-income-tax` |
| FR | IT-IND | `fr-personal-income-tax` |
| FR | IT-IND | `fr-return-assembly` |
| FR | XB | `fr-cross-border` |
| GB | IT-IND | `uk-capital-gains-sa108` |
| GB | IT-IND | `uk-freelance-intake` |
| GB | IT-IND | `uk-income-tax-sa100` |
| GB | IT-IND | `uk-return-assembly` |
| GB | IT-IND | `uk-scottish-income-tax` |
| GB | PR | `uk-payroll` |
| GB | PR | `uk-foreign-tax-and-withholding` |
| GB | VAT | `close-the-uk-vat-quarter-from-xero` |
| GB | VAT | `gb-vat-eu-goods-sellers` |
| GB | VAT | `uk-vat-return` |
| GB | VAT | `vat-returns-for-small-businesses-in-the-uk` |
| GB | VAT | `xero-uk-vat-close` |
| GB | XB | `uk-non-resident-sa109` |
| GB | XB | `uk-to-italy-flat-tax-relocation` |
| GB | XB | `uk-to-uae-relocation-tax` |
| GG | PR | `gg-secondary-pensions` |
| GG | PR | `gg-payroll-social-insurance` |
| GR | IT-IND | `gr-capital-gains` |
| GR | IT-IND | `gr-income-tax` |
| GR | VAT | `gr-vat-return` |
| GR | VAT | `greece-vat-return` |
| HT | PR | `ht-payroll-withholding-and-employer-tax` |
| HT | PR | `ht-service-withholding-and-payment-reporting` |
| HU | VAT | `hu-vat-return` |
| HU | VAT | `hungary-vat-return` |
| ID | IT-IND | `id-freelance-intake` |
| ID | IT-IND | `id-income-tax` |
| ID | IT-IND | `id-return-assembly` |
| ID | PR | `id-payroll-pph21` |
| ID | PR | `id-withholding` |
| IE | IT-IND | `ie-freelance-intake` |
| IE | IT-IND | `ie-income-tax-form11` |
| IE | IT-IND | `ie-return-assembly` |
| IE | PR | `ie-foreign-tax-and-withholding` |
| IE | PR | `ie-payroll` |
| IE | PR+XB | `ie-paye-rental-nonresident` |
| IE | XB | `ie-cross-border` |
| IE | XB | `ie-prsi-cross-border` |
| IM | IT-IND | `im-income-tax` |
| IM | IT-IND | `im-non-resident-income-tax` |
| IM | XB | `im-related-party-uk-treaty` |
| IN | IT-IND | `in-freelance-intake` |
| IN | IT-IND | `in-income-tax` |
| IN | IT-IND | `in-income-tax` |
| IN | IT-IND | `in-return-assembly` |
| IN | IT-IND | `in-tds-freelance` |
| IT | SC | `it-employer-contributions` |
| IT | SC | `it-inps-contributions` |
| JP | IT-IND | `jp-freelance-intake` |
| JP | IT-IND | `jp-income-tax` |
| JP | IT-IND | `jp-return-assembly` |
| JP | VAT | `japan-consumption-tax` |
| JP | VAT | `jp-consumption-tax` |
| KE | IT-IND | `ke-income-tax` |
| KE | IT-IND | `ke-income-tax-2` |
| KE | IT-IND | `non-resident-rental-income-tax-on-kenyan-property` |
| KN | SC | `kn-housing-social-development-levy` |
| KN | SC | `kn-social-security-contributions` |
| KR | VAT | `simplified-business-operator-registration-under-vat-act` |
| KR | VAT | `south-korea-vat` |
| KZ | IT-IND | `kz-freelance-intake` |
| KZ | IT-IND | `kz-income-tax` |
| KZ | IT-IND | `kz-return-assembly` |
| KZ | PR | `kz-payroll` |
| KZ | SC | `kz-social-contributions` |
| KZ | SC+PR | `kz-payroll-social` |
| LC | VAT | `lc-imported-services-vat` |
| LC | VAT | `lc-vat` |
| LK | IT-IND | `sri-lanka-capital-gains-tax` |
| LK | IT-IND | `sri-lanka-income-tax` |
| LK | PR | `sri-lanka-payroll` |
| LK | PR | `sri-lanka-withholding-tax` |
| MA | IT-IND | `ma-freelance-intake` |
| MA | IT-IND | `ma-return-assembly` |
| MA | IT-IND | `morocco-income-tax` |
| MA | IT-IND | `morocco-professional-income-tax` |
| MM | IT-IND | `mm-income-tax` |
| MM | IT-IND | `myanmar-personal-income-tax-2` |
| MM | IT-IND | `myanmar-personal-income-tax-4` |
| MM | VAT | `mm-vat-gst` |
| MM | VAT | `myanmar-vat-gst` |
| MM | VAT | `myanmar-vat-gst-2` |
| MT | IT-IND | `how-to-submit-capital-gain-taxes-in-malta` |
| MT | IT-IND | `mt-capital-gains` |
| MT | IT-IND | `mt-freelance-intake` |
| MT | IT-IND | `mt-return-assembly` |
| MT | IT-IND | `mt-vat3-quarterly-return-malta` |
| MT | VAT | `malta-vat-return` |
| MT | VAT | `mt-reverse-charge-vat-services-received-from` |
| MX | IT-IND | `mx-freelance-intake` |
| MX | IT-IND | `mx-income-tax` |
| MX | IT-IND | `mx-return-assembly` |
| NG | IT-IND | `ng-freelance-intake` |
| NG | IT-IND | `ng-income-tax` |
| NG | IT-IND | `ng-personal-income-tax` |
| NG | IT-IND | `ng-return-assembly` |
| NG | VAT | `ng-vat` |
| NG | VAT | `ng-vat-return` |
| NG | VAT | `nigeria-vat` |
| NL | IT-IND | `nl-freelance-intake` |
| NL | IT-IND | `nl-income-tax-special-groups` |
| NL | IT-IND | `nl-return-assembly` |
| NL | PR | `nl-dividend-withholding` |
| NL | PR | `nl-payroll-tax` |
| NL | VAT | `nl-vat-registration` |
| NL | VAT | `nl-vat-return` |
| NO | IT-IND | `no-capital-gains` |
| NO | IT-IND | `no-income-tax` |
| NO | IT-IND | `no-individual-residence` |
| NO | XB | `norway-to-switzerland-wealth-tax-exit` |
| NZ | IT-IND | `nz-capital-gains` |
| NZ | IT-IND | `nz-income-tax-ir3` |
| PK | IT-IND | `pk-freelance-intake` |
| PK | IT-IND | `pk-income-tax` |
| PK | IT-IND | `pk-return-assembly` |
| PK | PR | `pk-payroll` |
| PK | PR | `pk-payroll-eobi` |
| PK | PR | `pk-withholding-tax` |
| PK | VAT | `pakistan-sales-tax` |
| PK | VAT | `pk-sales-tax-federal` |
| PK | VAT | `pk-sales-tax-services` |
| PL | IT-IND | `pl-capital-gains` |
| PL | IT-IND | `pl-income-tax` |
| PL | VAT | `pl-vat-return` |
| PL | VAT | `poland-vat-return` |
| PM | IT-IND | `pm-company-income-tax` |
| PM | IT-IND | `pm-personal-income-tax-2025` |
| PT | IT-IND | `pt-income-tax` |
| PT | IT-IND | `pt-return-assembly` |
| PT | IT-IND | `pt-return-assembly-filing` |
| PT | XB | `pt-cross-border` |
| PT | XB | `pt-foreign-source-treaties` |
| RO | IT-IND | `ro-employee-income-tax` |
| RO | IT-IND | `ro-income-tax` |
| RW | IT-IND | `rw-income-tax` |
| RW | IT-IND | `rwanda-income-tax` |
| SA | IT-IND | `sa-freelance-intake` |
| SA | IT-IND | `sa-return-assembly` |
| SE | IT-IND | `se-capital-gains` |
| SE | IT-IND | `se-employee-income-tax` |
| SE | IT-IND | `se-income-tax` |
| SG | VAT | `sg-gst-return` |
| SG | VAT | `singapore-gst` |
| SH | IT-IND | `sh-company-income-tax` |
| SH | IT-IND | `sh-individual-tax-residence` |
| SH | IT-IND | `sh-personal-income-tax` |
| SK | VAT | `slovakia-vat-registration-4-7-7a` |
| SK | VAT | `slovakia-vat-return` |
| TZ | PR | `tanzania-payroll` |
| TZ | PR | `tanzania-withholding-tax` |
| UA | IT-IND | `ua-freelance-intake` |
| UA | IT-IND | `ua-return-assembly` |
| US | IT-CORP | `us-1120-corporation-return-schedule-ordinary-business` |
| US | IT-CORP | `us-corporate-extension-form-7004-and-the` |
| US | IT-IND | `us-1099-k-and-payment-processors` |
| US | IT-IND | `us-amended-return-form-1040-including-capital` |
| US | IT-IND | `us-capital-gains` |
| US | IT-IND | `us-education-credits-8863` |
| US | IT-IND | `us-estate-gift-706-709` |
| US | IT-IND | `us-fbar-and-fatca-8938` |
| US | IT-IND | `us-federal-income-tax-return-1040` |
| US | IT-IND | `us-federal-return-assembly` |
| US | IT-IND | `us-foreign-earned-income-2555` |
| US | IT-IND | `us-foreign-tax-credit-1116` |
| US | IT-IND | `us-form-1040-individual-return` |
| US | IT-IND | `us-form-1040-individual-return` |
| US | IT-IND | `us-form-1041-trust-and-estate-income` |
| US | IT-IND | `us-form-1065-partnership` |
| US | IT-IND | `us-form-1120-c-corp` |
| US | IT-IND | `us-form-5471-cfc-information` |
| US | IT-IND | `us-form-5472-foreign-owned-us` |
| US | IT-IND | `us-gilti-fdii-beat` |
| US | IT-IND | `us-irs-collections-and-controversy` |
| US | IT-IND | `us-multi-state-residency-and-allocation` |
| US | IT-IND | `us-pl-86-272-income-tax-nexus` |
| US | IT-IND | `us-pl-86-272-income-tax-nexus` |
| US | IT-IND | `us-pte-state-matrix` |
| US | IT-IND | `us-r-and-d-section-174-and-41` |
| US | IT-IND | `us-section-1031-like-kind-exchange` |
| US | IT-IND | `us-section-1202-qsbs` |
| US | IT-IND | `us-secure-2-and-retirement-updates` |
| US | IT-IND | `us-self-employed-health-insurance` |
| US | IT-IND | `us-self-employed-retirement` |
| US | IT-IND | `us-state-bonus-depreciation-conformity-matrix` |
| US | IT-IND | `us-state-estimated-tax-safe-harbors-matrix` |
| US | IT-IND | `us-state-formation-matrix` |
| US | IT-IND | `us-state-new-hire-reporting-matrix` |
| US | IT-IND | `us-tax-return-review-supporting-documents-findings` |
| US | IT-IND+PR | `us-form-941-940-payroll` |
| US | IT-IND+PR | `us-state-payroll-matrix` |
| US | PR | `us-form-941-940-payroll` |
| US | PR | `us-state-payroll-matrix` |
| US | VAT | `no-sales-tax-states` |
| US | VAT | `us-sales-tax` |
| US | VAT | `us-sales-tax-nexus-50-state-matrix` |
| US | VAT | `us-sales-tax-nexus-50-state-matrix` |
| US | XB | `us-expatriation-exit-tax` |
| US | XB | `us-nonresident-cgt` |
| US-AL | IT-IND | `al-income-tax` |
| US-AL | IT-IND | `alabama-income-tax` |
| US-AL | VAT | `al-sales-tax` |
| US-AL | VAT | `alabama-sales-tax` |
| US-AR | VAT | `ar-sales-tax` |
| US-AR | VAT | `arizona-sales-tax` |
| US-AR | VAT | `arkansas-sales-tax` |
| US-CA | IT-IND | `ca-income-tax` |
| US-CA | IT-IND | `us-ca-freelance-intake` |
| US-CA | IT-IND | `us-ca-return-assembly` |
| US-CO | VAT | `co-sales-tax` |
| US-CO | VAT | `colorado-sales-tax` |
| US-CO | VAT | `connecticut-sales-tax` |
| US-GA | IT-CORP | `ga-corporate-and-ptet` |
| US-GA | IT-CORP | `georgia-corporate-income-tax-returns-form-600` |
| US-GA | IT-CORP | `georgia-pass-through-entity-returns-form-700-partnership-and-form-600s-s-corporation` |
| US-GA | IT-IND | `ga-income-tax` |
| US-GA | IT-IND | `georgia-individual-tax-return-form-500` |
| US-ID | VAT | `id-sales-tax` |
| US-ID | VAT | `idaho-sales-tax` |
| US-IL | IT-IND | `il-estimated-tax` |
| US-IL | IT-IND | `il-income-tax` |
| US-IL | VAT | `il-sales-tax` |
| US-IL | VAT | `illinois-sales-tax` |
| US-IN | VAT | `in-sales-tax` |
| US-IN | VAT | `indiana-sales-tax` |
| US-KS | PR | `ks-payroll` |
| US-KS | PR | `ks-social-contributions` |
| US-MA | VAT | `ma-sales-tax` |
| US-MA | VAT | `maine-sales-tax` |
| US-MA | VAT | `maryland-sales-tax` |
| US-MA | VAT | `massachusetts-sales-tax` |
| US-MI | IT-IND | `mi-detroit-individual-return` |
| US-MI | IT-IND | `mi-income-tax` |
| US-MI | IT-IND | `mi-return-assembly` |
| US-MN | VAT | `minnesota-sales-tax` |
| US-MN | VAT | `mn-sales-tax` |
| US-MO | VAT | `missouri-sales-tax` |
| US-MO | VAT | `mo-sales-tax` |
| US-MS | VAT | `mississippi-sales-tax` |
| US-MS | VAT | `ms-sales-tax` |
| US-NC | IT-IND | `nc-income-tax` |
| US-NC | IT-IND | `nc-return-assembly` |
| US-ND | IT-IND | `nd-income-tax` |
| US-ND | IT-IND | `nd-return-assembly` |
| US-NJ | VAT | `new-jersey-sales-tax` |
| US-NJ | VAT | `nj-sales-tax` |
| US-NM | VAT | `new-mexico-sales-tax` |
| US-NM | VAT | `nm-sales-tax` |
| US-NV | VAT | `nevada-sales-tax` |
| US-NV | VAT | `nv-sales-tax` |
| US-NY | IT-IND | `ny-estimated-tax` |
| US-NY | IT-IND | `ny-income-tax` |
| US-NY | IT-IND | `nyc-ubt` |
| US-NY | IT-IND | `us-ny-freelance-intake` |
| US-NY | IT-IND | `us-ny-return-assembly` |
| US-NY | VAT | `ny-sales-tax` |
| US-OH | VAT | `oh-sales-tax` |
| US-OH | VAT | `ohio-sales-tax` |
| US-OK | VAT | `ok-sales-tax` |
| US-OK | VAT | `oklahoma-sales-tax` |
| US-PA | VAT | `pa-sales-tax` |
| US-PA | VAT | `pennsylvania-sales-tax` |
| US-TX | IT-IND | `tx-franchise-tax` |
| US-TX | IT-IND | `us-tx-freelance-intake` |
| US-TX | IT-IND | `us-tx-return-assembly` |
| US-TX | VAT | `tx-sales-tax` |
| US-UT | VAT | `ut-sales-tax` |
| US-UT | VAT | `utah-sales-tax` |
| US-WA | VAT | `wa-sales-tax` |
| US-WA | VAT | `washington-sales-tax` |
| US-WI | VAT | `wi-sales-tax` |
| US-WI | VAT | `wisconsin-sales-tax` |
| US-WY | VAT | `wy-sales-tax` |
| US-WY | VAT | `wyoming-sales-tax` |
| ZA | IT-IND | `capital-gains-tax-rate-tables-2023-to-2027` |
| ZA | IT-IND | `income-tax-rate-tables-by-year-of-assessment-2023-to-2027` |
| ZA | IT-IND | `za-capital-gains` |
| ZA | IT-IND | `za-capital-gains-tables` |
| ZA | IT-IND | `za-income-tax` |
| ZA | IT-IND | `za-income-tax-tables` |
| ZA | VAT | `south-africa-vat` |
| ZA | VAT | `za-vat-return` |
| ZA | VAT+XB | `cancelling-a-vat-registration-and-the-exit-vat-charge` |
| ZA | XB | `leaving-south-africa-tax-emigration` |

## Nearly done

For each country, the 3 tax skills with the fewest rates rows neither linked nor marked unverified. A skill with no rates table or none missing is not listed.

| Country | Skill | Missing | Rows | Linked % | Unverified % |
|---|---|---:|---:|---:|---:|
| AD | `ad-transfer-pricing` | 7 | 7 | 0.0 | 0.0 |
| AD | `ad-income-tax` | 14 | 14 | 0.0 | 0.0 |
| AE | `general-uae-corporate-tax-guide` | 4 | 4 | 0.0 | 0.0 |
| AE | `ae-corporate-tax` | 5 | 5 | 0.0 | 0.0 |
| AE | `uae-vat` | 5 | 5 | 0.0 | 0.0 |
| AL | `albania-payroll` | 8 | 16 | 50.0 | 0.0 |
| AL | `albania-social-contributions` | 8 | 15 | 46.7 | 0.0 |
| AL | `al-cross-border` | 13 | 17 | 23.5 | 0.0 |
| AM | `am-transfer-pricing` | 5 | 5 | 0.0 | 0.0 |
| AM | `am-cross-border` | 7 | 7 | 0.0 | 0.0 |
| AM | `armenia-payroll` | 7 | 7 | 0.0 | 0.0 |
| AR | `ar-vat-return` | 6 | 6 | 0.0 | 0.0 |
| AR | `ar-monotributo` | 12 | 12 | 0.0 | 0.0 |
| AR | `ar-social-contributions` | 16 | 16 | 0.0 | 0.0 |
| AT | `at-svs-contributions` | 5 | 21 | 76.2 | 0.0 |
| AT | `at-transfer-pricing` | 8 | 17 | 52.9 | 0.0 |
| AT | `at-corporate-income-tax` | 13 | 31 | 58.1 | 0.0 |
| AU | `au-gst-bas` | 4 | 8 | 50.0 | 0.0 |
| AU | `au-dssp` | 4 | 4 | 0.0 | 0.0 |
| AU | `au-return-assembly` | 4 | 4 | 0.0 | 0.0 |
| BA | `ba-cross-border` | 3 | 19 | 84.2 | 0.0 |
| BA | `ba-transfer-pricing` | 11 | 19 | 42.1 | 0.0 |
| BA | `bosnia-vat` | 11 | 16 | 31.2 | 0.0 |
| BB | `barbados-vat` | 17 | 18 | 5.6 | 0.0 |
| BB | `bb-income-tax` | 39 | 42 | 7.1 | 0.0 |
| BD | `bd-social-contributions` | 4 | 4 | 0.0 | 0.0 |
| BD | `bd-tax-optimization` | 6 | 6 | 0.0 | 0.0 |
| BD | `bd-crypto-tax` | 7 | 7 | 0.0 | 0.0 |
| BE | `be-capital-gains` | 6 | 14 | 57.1 | 0.0 |
| BE | `belgium-crypto-tax` | 24 | 24 | 0.0 | 0.0 |
| BE | `be-payroll-withholding` | 28 | 36 | 22.2 | 0.0 |
| BF | `bf-tax-optimization` | 17 | 17 | 0.0 | 0.0 |
| BF | `bf-corporate-tax` | 20 | 20 | 0.0 | 0.0 |
| BF | `bf-social-contributions` | 20 | 20 | 0.0 | 0.0 |
| BG | `bulgaria-payroll` | 12 | 17 | 29.4 | 0.0 |
| BG | `bulgaria-social-contributions` | 13 | 17 | 23.5 | 0.0 |
| BG | `bg-cross-border` | 15 | 19 | 21.1 | 0.0 |
| BH | `bahrain-vat` | 19 | 20 | 5.0 | 0.0 |
| BH | `bh-income-tax` | 34 | 37 | 8.1 | 0.0 |
| BM | `bermuda-tax` | 31 | 32 | 3.1 | 0.0 |
| BN | `brunei-tax` | 14 | 14 | 0.0 | 0.0 |
| BO | `bolivia-iva` | 16 | 17 | 5.9 | 0.0 |
| BO | `bolivia-income-tax` | 30 | 40 | 25.0 | 0.0 |
| BO | `bolivia-social-contributions` | 48 | 48 | 0.0 | 0.0 |
| BR | `br-carn-monthly-income-tax-rental-income` | 23 | 28 | 17.9 | 0.0 |
| BR | `br-indirect-tax` | 23 | 23 | 0.0 | 0.0 |
| BS | `bahamas-vat` | 21 | 22 | 4.5 | 0.0 |
| BS | `bs-income-tax` | 43 | 44 | 2.3 | 0.0 |
| BY | `belarus-income-tax` | 5 | 21 | 76.2 | 0.0 |
| CA | `ab-corporate-tax` | 7 | 7 | 0.0 | 0.0 |
| CA | `nt-payroll-tax` | 7 | 7 | 0.0 | 0.0 |
| CA | `leaving-canada-departure-tax` | 9 | 12 | 25.0 | 0.0 |
| CA-AB | `ca-ab-departure-tax-t1244-security-election-defer` | 10 | 13 | 23.1 | 0.0 |
| CA-AB | `ca-ab-deductions-for-self-employed-independent-contractor` | 27 | 40 | 32.5 | 0.0 |
| CH | `switzerland-crypto-tax` | 2 | 9 | 77.8 | 0.0 |
| CH | `ch-taxation-employee-stock-options-and-employee` | 5 | 7 | 28.6 | 0.0 |
| CH | `ch-ahv-iv` | 19 | 38 | 50.0 | 0.0 |
| CI | `ivory-coast-vat` | 13 | 14 | 7.1 | 0.0 |
| CI | `ivory-coast-income-tax` | 30 | 30 | 0.0 | 0.0 |
| CI | `ivory-coast-payroll` | 38 | 40 | 5.0 | 0.0 |
| CL | `cl-social-contributions` | 22 | 22 | 0.0 | 0.0 |
| CL | `cl-income-tax` | 30 | 30 | 0.0 | 0.0 |
| CL | `chile-iva` | 112 | 113 | 0.9 | 0.0 |
| CM | `cameroon-vat` | 15 | 16 | 6.2 | 0.0 |
| CM | `cameroon-income-tax` | 22 | 26 | 15.4 | 0.0 |
| CM | `cameroon-social-contributions` | 42 | 42 | 0.0 | 0.0 |
| CN | `china-pit` | 47 | 48 | 2.1 | 0.0 |
| CO | `colombia-income-tax` | 22 | 22 | 0.0 | 0.0 |
| CO | `co-social-contributions` | 27 | 27 | 0.0 | 0.0 |
| CO | `co-vat-return` | 87 | 88 | 1.1 | 0.0 |
| CR | `costa-rica-social-contributions` | 19 | 19 | 0.0 | 0.0 |
| CR | `costa-rica-payroll` | 48 | 48 | 0.0 | 0.0 |
| CR | `costa-rica-income-tax` | 50 | 50 | 0.0 | 0.0 |
| CW | `cw-payroll-social` | 8 | 10 | 20.0 | 0.0 |
| CY | `cyprus-vat-return` | 1 | 21 | 95.2 | 0.0 |
| CY | `cyprus-payroll` | 6 | 22 | 72.7 | 0.0 |
| CY | `cyprus-social-contributions` | 8 | 27 | 70.4 | 0.0 |
| CZ | `cz-tax-overview` | 5 | 9 | 44.4 | 0.0 |
| CZ | `cz-social-health` | 6 | 20 | 70.0 | 0.0 |
| CZ | `cz-employee-contributions` | 8 | 19 | 57.9 | 0.0 |
| DE | `de-corporate-tax` | 1 | 18 | 94.4 | 0.0 |
| DE | `germany-to-switzerland-cross-border-tax` | 1 | 15 | 93.3 | 0.0 |
| DE | `germany-formation` | 3 | 86 | 96.5 | 0.0 |
| DK | `dk-corporate-tax` | 10 | 21 | 52.4 | 0.0 |
| DO | `dominican-republic-social-contributions` | 12 | 12 | 0.0 | 0.0 |
| DO | `dominican-republic-payroll` | 13 | 13 | 0.0 | 0.0 |
| DO | `dominican-republic-itbis` | 14 | 15 | 6.7 | 0.0 |
| DZ | `algeria-vat` | 23 | 24 | 4.2 | 0.0 |
| DZ | `algeria-social-contributions` | 38 | 38 | 0.0 | 0.0 |
| DZ | `algeria-income-tax` | 47 | 48 | 2.1 | 0.0 |
| EC | `ecuador-payroll` | 17 | 17 | 0.0 | 0.0 |
| EC | `ecuador-iva` | 23 | 24 | 4.2 | 0.0 |
| EC | `ecuador-income-tax` | 38 | 41 | 7.3 | 0.0 |
| EE | `ee-transfer-pricing` | 11 | 18 | 38.9 | 0.0 |
| EE | `ee-corporate-income-tax` | 11 | 16 | 31.2 | 0.0 |
| EE | `estonia-vat-return` | 24 | 31 | 22.6 | 0.0 |
| EG | `eg-bookkeeping` | 4 | 5 | 20.0 | 0.0 |
| EG | `eg-real-estate-tax` | 4 | 4 | 0.0 | 0.0 |
| EG | `eg-withholding-tax` | 7 | 7 | 0.0 | 0.0 |
| ES | `es-return-assembly` | 5 | 5 | 0.0 | 0.0 |
| ES | `es-irpf-deductions` | 8 | 434 | 98.2 | 0.0 |
| ES | `spain-formation` | 14 | 14 | 0.0 | 0.0 |
| ET | `ethiopia-vat` | 14 | 15 | 6.7 | 0.0 |
| ET | `ethiopia-payroll` | 36 | 36 | 0.0 | 0.0 |
| ET | `ethiopia-social-contributions` | 43 | 43 | 0.0 | 0.0 |
| FI | `fi-tax-overview` | 2 | 8 | 75.0 | 0.0 |
| FI | `fi-company-formation` | 3 | 3 | 0.0 | 0.0 |
| FI | `fi-country-by-country-reporting` | 4 | 4 | 0.0 | 0.0 |
| FJ | `fiji-vat` | 17 | 18 | 5.6 | 0.0 |
| FJ | `fj-income-tax` | 19 | 25 | 24.0 | 0.0 |
| FJ | `fj-payroll-social` | 22 | 26 | 15.4 | 0.0 |
| FR | `fr-personal-income-tax` | 1 | 55 | 98.2 | 0.0 |
| FR | `fr-cross-border` | 1 | 34 | 97.1 | 0.0 |
| FR | `leaving-france-exit-tax` | 1 | 19 | 94.7 | 0.0 |
| GB | `gb-tax-relief-under-the-merged-scheme` | 1 | 88 | 98.9 | 0.0 |
| GB | `uk-return-assembly` | 2 | 12 | 83.3 | 0.0 |
| GB | `uk-crypto-tax` | 3 | 17 | 82.4 | 0.0 |
| GD | `gd-annual-stamp-tax` | 3 | 3 | 0.0 | 0.0 |
| GE | `georgia-payroll` | 13 | 15 | 13.3 | 0.0 |
| GE | `georgia-social-contributions` | 13 | 15 | 13.3 | 0.0 |
| GE | `georgia-vat` | 13 | 14 | 7.1 | 0.0 |
| GG | `gg-gst-transition` | 1 | 5 | 80.0 | 0.0 |
| GG | `gg-payroll-social-insurance` | 3 | 3 | 0.0 | 0.0 |
| GG | `gg-property-document-duty` | 7 | 7 | 0.0 | 0.0 |
| GH | `ghana-vat` | 18 | 19 | 5.3 | 0.0 |
| GH | `ghana-pit` | 54 | 55 | 1.8 | 0.0 |
| GI | `gi-payroll-social-insurance` | 3 | 3 | 0.0 | 0.0 |
| GI | `gi-property-stamp-duty` | 3 | 3 | 0.0 | 0.0 |
| GL | `gl-mandatory-pension` | 4 | 4 | 0.0 | 0.0 |
| GP | `gp-producer-octroi-compliance` | 3 | 3 | 0.0 | 0.0 |
| GR | `greece-vat-return` | 11 | 14 | 21.4 | 0.0 |
| GR | `gr-capital-gains` | 11 | 12 | 8.3 | 0.0 |
| GR | `gr-partnerships-single-entry` | 15 | 20 | 25.0 | 0.0 |
| GT | `guatemala-iva` | 17 | 18 | 5.6 | 0.0 |
| GT | `guatemala-social-contributions` | 26 | 26 | 0.0 | 0.0 |
| GT | `guatemala-income-tax` | 31 | 39 | 20.5 | 0.0 |
| HK | `hk-mpf` | 33 | 33 | 0.0 | 0.0 |
| HK | `hong-kong-tax` | 37 | 38 | 2.6 | 0.0 |
| HK | `hk-salaries-tax` | 43 | 43 | 0.0 | 0.0 |
| HN | `honduras-social-contributions` | 32 | 40 | 20.0 | 0.0 |
| HN | `honduras-income-tax` | 32 | 32 | 0.0 | 0.0 |
| HN | `honduras-payroll` | 60 | 60 | 0.0 | 0.0 |
| HR | `hr-cross-border` | 8 | 18 | 55.6 | 0.0 |
| HR | `croatia-social-contributions` | 16 | 19 | 15.8 | 0.0 |
| HR | `croatia-payroll` | 18 | 24 | 25.0 | 0.0 |
| HT | `ht-personal-income-tax-new-code` | 5 | 5 | 0.0 | 0.0 |
| HU | `hu-corporate-tax` | 4 | 11 | 63.6 | 0.0 |
| HU | `hu-cross-border` | 6 | 14 | 57.1 | 0.0 |
| HU | `hu-capital-and-rental-income` | 22 | 27 | 18.5 | 0.0 |
| ID | `id-formation` | 15 | 15 | 0.0 | 0.0 |
| ID | `id-return-assembly` | 17 | 18 | 5.6 | 0.0 |
| ID | `id-pph-final-umkm` | 17 | 17 | 0.0 | 0.0 |
| IE | `ie-formation` | 1 | 23 | 95.7 | 0.0 |
| IE | `ie-cat` | 7 | 17 | 58.8 | 0.0 |
| IE | `ie-preliminary-tax` | 7 | 15 | 53.3 | 0.0 |
| IL | `il-new-immigrant` | 11 | 11 | 0.0 | 0.0 |
| IL | `il-freelancer-ops` | 14 | 15 | 6.7 | 0.0 |
| IL | `il-customs-duty` | 19 | 22 | 13.6 | 0.0 |
| IM | `im-non-resident-income-tax` | 5 | 9 | 44.4 | 0.0 |
| IM | `im-related-party-uk-treaty` | 8 | 9 | 11.1 | 0.0 |
| IM | `isle-of-man-vat` | 10 | 18 | 44.4 | 0.0 |
| IN | `in-income-tax` | 4 | 4 | 0.0 | 0.0 |
| IN | `in-tax-residency` | 9 | 9 | 0.0 | 0.0 |
| IN | `in-professional-tax` | 21 | 23 | 8.7 | 0.0 |
| IQ | `iraq-tax` | 19 | 19 | 0.0 | 0.0 |
| IR | `iran-vat` | 11 | 12 | 8.3 | 0.0 |
| IS | `iceland-payroll` | 3 | 18 | 83.3 | 0.0 |
| IS | `is-transfer-pricing` | 6 | 6 | 0.0 | 0.0 |
| IS | `is-cross-border` | 12 | 13 | 7.7 | 0.0 |
| IT | `it-inps-contributions` | 1 | 28 | 96.4 | 0.0 |
| IT | `italy-formation` | 2 | 22 | 90.9 | 0.0 |
| IT | `it-cross-border` | 4 | 19 | 78.9 | 0.0 |
| JM | `jamaica-gct` | 19 | 20 | 5.0 | 0.0 |
| JM | `jm-income-tax` | 59 | 60 | 1.7 | 0.0 |
| JO | `jordan-gst` | 14 | 15 | 6.7 | 0.0 |
| JP | `japan-formation` | 7 | 7 | 0.0 | 0.0 |
| JP | `jp-etax-filing` | 10 | 11 | 9.1 | 0.0 |
| JP | `japan-transfer-pricing` | 11 | 11 | 0.0 | 0.0 |
| KE | `tax-amnesty` | 7 | 7 | 0.0 | 0.0 |
| KE | `set-up-your-company-in-kenya-we-handle-it-from-abroad` | 11 | 11 | 0.0 | 0.0 |
| KE | `ke-income-tax-2` | 15 | 15 | 0.0 | 0.0 |
| KH | `cambodia-vat` | 21 | 22 | 4.5 | 0.0 |
| KH | `kh-income-tax` | 32 | 32 | 0.0 | 0.0 |
| KR | `kr-social-insurance` | 24 | 24 | 0.0 | 0.0 |
| KR | `south-korea-vat` | 26 | 27 | 3.7 | 0.0 |
| KR | `south-korea-crypto-tax` | 29 | 29 | 0.0 | 0.0 |
| KW | `kuwait-tax` | 14 | 15 | 6.7 | 0.0 |
| KY | `cayman-tax` | 24 | 24 | 0.0 | 0.0 |
| KZ | `kz-tax-optimization` | 6 | 6 | 0.0 | 0.0 |
| KZ | `kz-financial-statements` | 8 | 8 | 0.0 | 0.0 |
| KZ | `kz-einvoice` | 9 | 9 | 0.0 | 0.0 |
| LA | `laos-vat` | 16 | 16 | 0.0 | 0.0 |
| LB | `lebanon-vat` | 14 | 15 | 6.7 | 0.0 |
| LI | `li-transfer-pricing` | 3 | 3 | 0.0 | 0.0 |
| LI | `li-payroll-social` | 6 | 6 | 0.0 | 0.0 |
| LI | `li-corporate-income-tax` | 9 | 9 | 0.0 | 0.0 |
| LK | `sri-lanka-sscl` | 10 | 10 | 0.0 | 0.0 |
| LK | `sri-lanka-withholding-tax` | 13 | 13 | 0.0 | 0.0 |
| LK | `sri-lanka-corporate-tax` | 14 | 14 | 0.0 | 0.0 |
| LT | `lt-payroll-social` | 2 | 29 | 93.1 | 0.0 |
| LT | `lt-cross-border` | 17 | 22 | 22.7 | 0.0 |
| LU | `lu-corporate-tax` | 2 | 22 | 90.9 | 0.0 |
| LU | `lu-transfer-pricing` | 3 | 13 | 76.9 | 0.0 |
| LU | `luxembourg-payroll` | 7 | 27 | 74.1 | 0.0 |
| LV | `lv-transfer-pricing` | 13 | 17 | 23.5 | 0.0 |
| LV | `lv-cross-border` | 19 | 22 | 13.6 | 0.0 |
| MA | `ma-cpu` | 7 | 7 | 0.0 | 0.0 |
| MA | `ma-crypto-tax` | 12 | 12 | 0.0 | 0.0 |
| MA | `ma-einvoice` | 14 | 14 | 0.0 | 0.0 |
| MC | `mc-payroll-social` | 10 | 10 | 0.0 | 0.0 |
| MD | `moldova-vat` | 9 | 13 | 30.8 | 0.0 |
| MD | `md-cross-border` | 9 | 9 | 0.0 | 0.0 |
| MD | `moldova-payroll` | 10 | 17 | 41.2 | 0.0 |
| ME | `montenegro-social-contributions` | 2 | 24 | 91.7 | 0.0 |
| ME | `me-company-formation` | 12 | 12 | 0.0 | 0.0 |
| ME | `montenegro-vat` | 17 | 18 | 5.6 | 0.0 |
| MK | `north-macedonia-payroll` | 8 | 8 | 0.0 | 0.0 |
| MK | `north-macedonia-cross-border` | 10 | 10 | 0.0 | 0.0 |
| MK | `north-macedonia-transfer-pricing` | 10 | 10 | 0.0 | 0.0 |
| MM | `myanmar-personal-income-tax-4` | 6 | 6 | 0.0 | 0.0 |
| MM | `myanmar-ct` | 16 | 16 | 0.0 | 0.0 |
| MN | `mongolia-vat` | 15 | 16 | 6.2 | 0.0 |
| MT | `mt-return-assembly` | 2 | 2 | 0.0 | 0.0 |
| MT | `mt-crypto-tax` | 4 | 11 | 63.6 | 0.0 |
| MT | `mt-reverse-charge-vat-services-received-from` | 5 | 5 | 0.0 | 0.0 |
| MU | `mauritius-vat` | 13 | 14 | 7.1 | 0.0 |
| MV | `maldives-gst` | 16 | 17 | 5.9 | 0.0 |
| MV | `mv-income-tax` | 23 | 23 | 0.0 | 0.0 |
| MX | `mexico-transfer-pricing` | 9 | 9 | 0.0 | 0.0 |
| MX | `mx-cfdi` | 17 | 17 | 0.0 | 0.0 |
| MX | `mx-estimated-tax` | 18 | 18 | 0.0 | 0.0 |
| MY | `my-epf-socso` | 3 | 3 | 0.0 | 0.0 |
| MY | `my-pcb` | 9 | 10 | 10.0 | 0.0 |
| MY | `malaysia-sst` | 20 | 22 | 9.1 | 0.0 |
| MZ | `mozambique-vat` | 14 | 15 | 6.7 | 0.0 |
| MZ | `mozambique-income-tax` | 21 | 21 | 0.0 | 0.0 |
| MZ | `mozambique-social-contributions` | 37 | 37 | 0.0 | 0.0 |
| NG | `ng-income-tax` | 15 | 15 | 0.0 | 0.0 |
| NG | `ng-payroll` | 18 | 18 | 0.0 | 0.0 |
| NG | `ng-vat-return` | 18 | 18 | 0.0 | 0.0 |
| NI | `nicaragua-iva` | 11 | 12 | 8.3 | 0.0 |
| NI | `nicaragua-income-tax` | 18 | 18 | 0.0 | 0.0 |
| NI | `nicaragua-social-contributions` | 28 | 28 | 0.0 | 0.0 |
| NL | `nl-income-tax-special-groups` | 1 | 19 | 94.7 | 0.0 |
| NL | `nl-cross-border` | 1 | 18 | 94.4 | 0.0 |
| NL | `nl-box2-substantial-interest` | 2 | 12 | 83.3 | 0.0 |
| NO | `no-employer-payroll` | 6 | 17 | 64.7 | 0.0 |
| NO | `no-vat-return` | 10 | 17 | 41.2 | 0.0 |
| NO | `no-transfer-pricing` | 12 | 16 | 25.0 | 0.0 |
| NP | `nepal-corporate-tax` | 9 | 9 | 0.0 | 0.0 |
| NP | `nepal-tds` | 10 | 10 | 0.0 | 0.0 |
| NP | `nepal-vat` | 16 | 17 | 5.9 | 0.0 |
| NZ | `nz-timing-deductions-when-expense-incurred` | 2 | 8 | 75.0 | 0.0 |
| NZ | `nz-acc-levies` | 3 | 6 | 50.0 | 0.0 |
| NZ | `nz-capital-gains` | 10 | 15 | 33.3 | 0.0 |
| OM | `oman-vat` | 15 | 16 | 6.2 | 0.0 |
| PA | `panama-itbms` | 32 | 33 | 3.0 | 0.0 |
| PA | `panama-social-contributions` | 36 | 36 | 0.0 | 0.0 |
| PA | `panama-payroll` | 47 | 47 | 0.0 | 0.0 |
| PE | `peru-social-contributions` | 16 | 41 | 61.0 | 0.0 |
| PE | `peru-income-tax` | 29 | 30 | 3.3 | 0.0 |
| PE | `peru-payroll` | 29 | 29 | 0.0 | 0.0 |
| PG | `png-gst` | 16 | 16 | 0.0 | 0.0 |
| PG | `pg-income-tax` | 34 | 34 | 0.0 | 0.0 |
| PH | `ph-income-tax` | 11 | 12 | 8.3 | 0.0 |
| PH | `ph-sss-philhealth` | 29 | 29 | 0.0 | 0.0 |
| PH | `ph-withholding` | 36 | 36 | 0.0 | 0.0 |
| PK | `pk-sales-tax-services` | 5 | 5 | 0.0 | 0.0 |
| PK | `pk-tax-optimization` | 6 | 6 | 0.0 | 0.0 |
| PK | `pk-crypto-tax` | 7 | 7 | 0.0 | 0.0 |
| PL | `poland-vat-return` | 7 | 16 | 56.2 | 0.0 |
| PL | `pl-income-tax` | 7 | 15 | 53.3 | 0.0 |
| PL | `pl-zus-contributions` | 9 | 22 | 59.1 | 0.0 |
| PM | `pm-personal-income-tax-2025` | 12 | 12 | 0.0 | 0.0 |
| PT | `pt-foreign-source-treaties` | 5 | 13 | 61.5 | 0.0 |
| PT | `portugal-crypto-tax` | 6 | 12 | 50.0 | 0.0 |
| PT | `pt-transfer-pricing` | 7 | 15 | 53.3 | 0.0 |
| PY | `paraguay-iva` | 22 | 22 | 0.0 | 0.0 |
| PY | `paraguay-social-contributions` | 25 | 25 | 0.0 | 0.0 |
| PY | `paraguay-income-tax` | 34 | 34 | 0.0 | 0.0 |
| RO | `ro-cas-cass` | 10 | 13 | 23.1 | 0.0 |
| RO | `ro-cross-border` | 12 | 14 | 14.3 | 0.0 |
| RO | `ro-income-tax` | 14 | 18 | 22.2 | 0.0 |
| RS | `rs-cross-border` | 4 | 19 | 78.9 | 0.0 |
| RS | `serbia-vat` | 4 | 16 | 75.0 | 0.0 |
| RS | `rs-transfer-pricing` | 8 | 19 | 57.9 | 0.0 |
| RW | `rwanda-vat` | 13 | 14 | 7.1 | 0.0 |
| RW | `rwanda-social-contributions` | 29 | 29 | 0.0 | 0.0 |
| RW | `rw-income-tax` | 32 | 32 | 0.0 | 0.0 |
| SA | `sa-gosi-saudization` | 3 | 3 | 0.0 | 0.0 |
| SA | `sa-zakat` | 20 | 20 | 0.0 | 0.0 |
| SA | `sa-rett` | 23 | 23 | 0.0 | 0.0 |
| SD | `sd-income-tax` | 12 | 12 | 0.0 | 0.0 |
| SD | `sd-corporate-income-tax` | 14 | 14 | 0.0 | 0.0 |
| SD | `sd-company-formation` | 16 | 16 | 0.0 | 0.0 |
| SE | `se-capital-gains` | 6 | 6 | 0.0 | 0.0 |
| SE | `sweden-payroll` | 8 | 22 | 63.6 | 0.0 |
| SE | `se-closely-held-company-312` | 9 | 15 | 40.0 | 0.0 |
| SG | `sg-zero-cgt` | 6 | 6 | 0.0 | 0.0 |
| SG | `singapore-transfer-pricing` | 10 | 10 | 0.0 | 0.0 |
| SG | `sg-gst-return` | 12 | 12 | 0.0 | 0.0 |
| SH | `sh-company-income-tax` | 2 | 2 | 0.0 | 0.0 |
| SI | `slovenia-income-tax` | 11 | 33 | 66.7 | 0.0 |
| SI | `slovenia-payroll` | 11 | 19 | 42.1 | 0.0 |
| SI | `si-cross-border` | 11 | 17 | 35.3 | 0.0 |
| SJ | `sj-svalbard-company-income-tax` | 4 | 4 | 0.0 | 0.0 |
| SK | `sk-payroll-social` | 19 | 25 | 24.0 | 0.0 |
| SM | `sm-transfer-pricing` | 9 | 9 | 0.0 | 0.0 |
| SM | `sm-cross-border` | 14 | 14 | 0.0 | 0.0 |
| SM | `sm-vat-gst` | 19 | 19 | 0.0 | 0.0 |
| SN | `senegal-vat` | 13 | 14 | 7.1 | 0.0 |
| SN | `senegal-social-contributions` | 24 | 24 | 0.0 | 0.0 |
| SN | `senegal-income-tax` | 27 | 27 | 0.0 | 0.0 |
| SS | `ss-income-tax` | 5 | 5 | 0.0 | 0.0 |
| SV | `el-salvador-social-contributions` | 9 | 9 | 0.0 | 0.0 |
| SV | `el-salvador-iva` | 16 | 17 | 5.9 | 0.0 |
| SV | `el-salvador-payroll` | 21 | 21 | 0.0 | 0.0 |
| TH | `thailand-pit` | 40 | 41 | 2.4 | 0.0 |
| TH | `thailand-vat` | 63 | 64 | 1.6 | 0.0 |
| TN | `tunisia-vat` | 15 | 16 | 6.2 | 0.0 |
| TR | `tr-transfer-pricing` | 5 | 14 | 64.3 | 0.0 |
| TR | `tr-tax-overview` | 5 | 5 | 0.0 | 0.0 |
| TR | `turkey-vat` | 9 | 16 | 43.8 | 0.0 |
| TT | `trinidad-vat` | 14 | 15 | 6.7 | 0.0 |
| TW | `tw-nhi` | 48 | 48 | 0.0 | 0.0 |
| TW | `taiwan-vat` | 60 | 61 | 1.6 | 0.0 |
| TW | `tw-income-tax` | 60 | 60 | 0.0 | 0.0 |
| TZ | `tanzania-tax-optimization` | 12 | 12 | 0.0 | 0.0 |
| TZ | `tanzania-withholding-tax` | 12 | 12 | 0.0 | 0.0 |
| TZ | `tanzania-vat` | 14 | 15 | 6.7 | 0.0 |
| UA | `ua-payroll` | 8 | 15 | 46.7 | 0.0 |
| UA | `ua-bookkeeping` | 10 | 10 | 0.0 | 0.0 |
| UA | `ua-financial-statements` | 10 | 10 | 0.0 | 0.0 |
| UG | `uganda-vat` | 13 | 14 | 7.1 | 0.0 |
| US | `us-capital-gains` | 3 | 3 | 0.0 | 0.0 |
| US | `us-form-5472-foreign-owned-us` | 5 | 5 | 0.0 | 0.0 |
| US | `us-state-bonus-depreciation-conformity-matrix` | 6 | 6 | 0.0 | 0.0 |
| US-AK | `ak-sales-tax` | 11 | 13 | 15.4 | 0.0 |
| US-AL | `al-sales-tax` | 25 | 26 | 3.8 | 0.0 |
| US-AL | `alabama-sales-tax` | 25 | 26 | 3.8 | 0.0 |
| US-AL | `al-income-tax` | 27 | 28 | 3.6 | 0.0 |
| US-AR | `ar-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-AR | `arkansas-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-AR | `ar-income-tax` | 13 | 14 | 7.1 | 0.0 |
| US-AZ | `az-payroll` | 10 | 10 | 0.0 | 0.0 |
| US-AZ | `az-income-tax` | 20 | 21 | 4.8 | 0.0 |
| US-AZ | `az-sales-tax` | 24 | 25 | 4.0 | 0.0 |
| US-CA | `ca-smllc-form-568` | 3 | 3 | 0.0 | 0.0 |
| US-CA | `ca-540-individual-return` | 8 | 13 | 38.5 | 0.0 |
| US-CA | `ca-540-es-estimated-tax` | 9 | 9 | 0.0 | 0.0 |
| US-CO | `co-retail-delivery-and-suts` | 7 | 7 | 0.0 | 0.0 |
| US-CO | `co-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-CO | `colorado-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-CT | `ct-income-tax` | 7 | 7 | 0.0 | 0.0 |
| US-CT | `ct-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-CT | `ct-payroll` | 30 | 30 | 0.0 | 0.0 |
| US-DC | `dc-income-tax` | 3 | 3 | 0.0 | 0.0 |
| US-DC | `dc-sales-tax` | 11 | 12 | 8.3 | 0.0 |
| US-DE | `de-income-tax` | 11 | 11 | 0.0 | 0.0 |
| US-DE | `de-franchise-tax-and-llc` | 16 | 16 | 0.0 | 0.0 |
| US-DE | `de-gross-receipts-tax` | 23 | 24 | 4.2 | 0.0 |
| US-FL | `fl-moving-to-florida-domicile` | 6 | 8 | 25.0 | 0.0 |
| US-FL | `fl-corporate-income-tax` | 8 | 8 | 0.0 | 0.0 |
| US-FL | `fl-sales-tax` | 14 | 14 | 0.0 | 0.0 |
| US-GA | `ga-corporate-and-ptet` | 3 | 3 | 0.0 | 0.0 |
| US-GA | `ga-sales-tax` | 3 | 3 | 0.0 | 0.0 |
| US-GA | `ga-income-tax` | 6 | 6 | 0.0 | 0.0 |
| US-HI | `hi-sales-tax` | 13 | 14 | 7.1 | 0.0 |
| US-HI | `hi-income-tax` | 31 | 31 | 0.0 | 0.0 |
| US-IA | `ia-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-IA | `ia-income-tax` | 15 | 16 | 6.2 | 0.0 |
| US-ID | `id-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-ID | `idaho-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-IL | `il-estimated-tax` | 6 | 6 | 0.0 | 0.0 |
| US-IL | `il-income-tax` | 7 | 7 | 0.0 | 0.0 |
| US-IL | `il-sales-tax` | 11 | 11 | 0.0 | 0.0 |
| US-IN | `in-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-IN | `indiana-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-IN | `in-payroll` | 18 | 18 | 0.0 | 0.0 |
| US-KS | `ks-sales-tax` | 1 | 5 | 80.0 | 0.0 |
| US-KS | `ks-payroll` | 4 | 8 | 50.0 | 0.0 |
| US-KS | `ks-income-tax` | 9 | 12 | 25.0 | 0.0 |
| US-KY | `ky-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-KY | `ky-payroll` | 27 | 27 | 0.0 | 0.0 |
| US-LA | `la-sales-tax` | 10 | 12 | 16.7 | 0.0 |
| US-LA | `la-income-tax` | 14 | 16 | 12.5 | 0.0 |
| US-MA | `maine-sales-tax` | 8 | 9 | 11.1 | 0.0 |
| US-MA | `maryland-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MA | `ma-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-MD | `md-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MD | `md-payroll` | 41 | 41 | 0.0 | 0.0 |
| US-ME | `me-sales-tax` | 8 | 9 | 11.1 | 0.0 |
| US-ME | `me-income-tax` | 27 | 27 | 0.0 | 0.0 |
| US-MI | `mi-corporate-income-tax` | 5 | 5 | 0.0 | 0.0 |
| US-MI | `mi-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MI | `mi-homestead-credit` | 13 | 13 | 0.0 | 0.0 |
| US-MN | `mn-payroll` | 4 | 4 | 0.0 | 0.0 |
| US-MN | `minnesota-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-MN | `mn-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-MO | `missouri-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MO | `mo-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MO | `mo-income-tax` | 19 | 19 | 0.0 | 0.0 |
| US-MS | `mississippi-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MS | `ms-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-MS | `ms-income-tax` | 22 | 22 | 0.0 | 0.0 |
| US-NC | `nc-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-NC | `nc-payroll` | 13 | 13 | 0.0 | 0.0 |
| US-NC | `nc-return-assembly` | 13 | 13 | 0.0 | 0.0 |
| US-ND | `nd-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-ND | `nd-income-tax` | 23 | 24 | 4.2 | 0.0 |
| US-ND | `nd-estimated-tax` | 35 | 35 | 0.0 | 0.0 |
| US-NE | `ne-sales-tax` | 9 | 10 | 10.0 | 0.0 |
| US-NE | `ne-income-tax` | 29 | 30 | 3.3 | 0.0 |
| US-NH | `nh-interest-dividends-note` | 4 | 4 | 0.0 | 0.0 |
| US-NJ | `nj-cbt-and-bait` | 3 | 3 | 0.0 | 0.0 |
| US-NJ | `nj-payroll` | 5 | 5 | 0.0 | 0.0 |
| US-NJ | `nj-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-NM | `new-mexico-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-NM | `nm-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-NM | `nm-income-tax` | 29 | 30 | 3.3 | 0.0 |
| US-NV | `nv-formation` | 6 | 6 | 0.0 | 0.0 |
| US-NV | `nevada-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-NV | `nv-sales-tax` | 10 | 11 | 9.1 | 0.0 |
| US-NY | `ny-residency-leaving-new-york` | 1 | 2 | 50.0 | 0.0 |
| US-NY | `new-york-sales-tax` | 4 | 4 | 0.0 | 0.0 |
| US-NY | `ny-payroll` | 4 | 4 | 0.0 | 0.0 |
| US-NY-NYC | `nyc-unincorporated-business-tax` | 9 | 9 | 0.0 | 0.0 |
| US-OH | `oh-payroll` | 3 | 3 | 0.0 | 0.0 |
| US-OH | `ohio-sales-tax` | 5 | 5 | 0.0 | 0.0 |
| US-OH | `oh-income-tax` | 13 | 13 | 0.0 | 0.0 |
| US-OK | `ok-sales-tax` | 16 | 17 | 5.9 | 0.0 |
| US-OK | `oklahoma-sales-tax` | 16 | 17 | 5.9 | 0.0 |
| US-OK | `ok-income-tax` | 21 | 22 | 4.5 | 0.0 |
| US-OR | `or-income-tax` | 10 | 11 | 9.1 | 0.0 |
| US-OR | `or-payroll` | 28 | 28 | 0.0 | 0.0 |
| US-PA | `pa-income-tax` | 7 | 8 | 12.5 | 0.0 |
| US-PA | `pennsylvania-sales-tax` | 17 | 18 | 5.6 | 0.0 |
| US-PA | `pa-local-eit` | 43 | 43 | 0.0 | 0.0 |
| US-RI | `ri-income-tax` | 14 | 15 | 6.7 | 0.0 |
| US-RI | `ri-sales-tax` | 14 | 15 | 6.7 | 0.0 |
| US-SC | `sc-income-tax` | 21 | 22 | 4.5 | 0.0 |
| US-SC | `sc-sales-tax` | 41 | 42 | 2.4 | 0.0 |
| US-SD | `sd-sales-tax` | 17 | 18 | 5.6 | 0.0 |
| US-TN | `tn-sales-tax` | 44 | 45 | 2.2 | 0.0 |
| US-TX | `tx-margin-tax` | 3 | 3 | 0.0 | 0.0 |
| US-TX | `texas-sales-tax` | 6 | 7 | 14.3 | 0.0 |
| US-TX | `tx-franchise-tax` | 9 | 9 | 0.0 | 0.0 |
| US-UT | `ut-sales-tax` | 18 | 19 | 5.3 | 0.0 |
| US-UT | `utah-sales-tax` | 18 | 19 | 5.3 | 0.0 |
| US-UT | `ut-income-tax` | 24 | 25 | 4.0 | 0.0 |
| US-VA | `va-income-tax` | 4 | 4 | 0.0 | 0.0 |
| US-VA | `va-payroll` | 7 | 7 | 0.0 | 0.0 |
| US-VA | `va-corporate-tax-and-bpol` | 43 | 43 | 0.0 | 0.0 |
| US-VT | `vt-sales-tax` | 15 | 16 | 6.2 | 0.0 |
| US-VT | `vt-income-tax` | 34 | 35 | 2.9 | 0.0 |
| US-WA | `wa-bo-tax` | 3 | 8 | 62.5 | 0.0 |
| US-WA | `wa-business-occupation-tax` | 3 | 8 | 62.5 | 0.0 |
| US-WA | `wa-sales-tax` | 6 | 9 | 33.3 | 0.0 |
| US-WI | `wi-payroll` | 19 | 19 | 0.0 | 0.0 |
| US-WI | `wi-income-tax` | 25 | 25 | 0.0 | 0.0 |
| US-WI | `wi-sales-tax` | 39 | 40 | 2.5 | 0.0 |
| US-WV | `wv-sales-tax` | 15 | 16 | 6.2 | 0.0 |
| US-WV | `wv-income-tax` | 34 | 35 | 2.9 | 0.0 |
| US-WY | `wy-sales-tax` | 16 | 17 | 5.9 | 0.0 |
| US-WY | `wyoming-sales-tax` | 16 | 17 | 5.9 | 0.0 |
| UY | `uruguay-iva` | 23 | 24 | 4.2 | 0.0 |
| UY | `uruguay-income-tax` | 58 | 58 | 0.0 | 0.0 |
| UY | `uruguay-social-contributions` | 100 | 100 | 0.0 | 0.0 |
| UZ | `uzbekistan-vat` | 19 | 21 | 9.5 | 0.0 |
| UZ | `uzbekistan-income-tax` | 31 | 31 | 0.0 | 0.0 |
| UZ | `uzbekistan-social-contributions` | 46 | 46 | 0.0 | 0.0 |
| VE | `venezuela-iva` | 26 | 27 | 3.7 | 0.0 |
| VE | `venezuela-social-contributions` | 34 | 34 | 0.0 | 0.0 |
| VE | `venezuela-income-tax` | 41 | 41 | 0.0 | 0.0 |
| VG | `bvi-tax` | 15 | 16 | 6.2 | 0.0 |
| VN | `vietnam-pit` | 43 | 43 | 0.0 | 0.0 |
| VN | `vietnam-vat` | 58 | 64 | 9.4 | 0.0 |
| XK | `xk-cross-border` | 10 | 10 | 0.0 | 0.0 |
| XK | `xk-corporate-income-tax` | 13 | 13 | 0.0 | 0.0 |
| ZA | `za-tax-residency` | 4 | 4 | 0.0 | 0.0 |
| ZA | `capital-gains-tax-rate-tables-2023-to-2027` | 5 | 5 | 0.0 | 0.0 |
| ZA | `ring-fencing-of-assessed-losses-under-section-20a` | 5 | 5 | 0.0 | 0.0 |
| ZM | `zambia-vat` | 13 | 14 | 7.1 | 0.0 |
| ZM | `zm-income-tax` | 31 | 31 | 0.0 | 0.0 |
| ZW | `zimbabwe-vat` | 13 | 14 | 7.1 | 0.0 |
| ZW | `zw-income-tax` | 46 | 48 | 4.2 | 0.0 |
| ZW | `zw-payroll-social` | 57 | 58 | 1.7 | 0.0 |
