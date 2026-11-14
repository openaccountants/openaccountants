---
name: france-references
jurisdiction: FR
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
type: router
description: Where to find the official French tax texts behind the France skills, and the related open-source projects that model French tax law, with what each is good for.
tier: 2
---

# France: official sources and related open-source projects

> **General reference only.** This file points to where French tax rules are published and to open-source projects that model them. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in France.

OpenAccountants is AGPL-3.0. The projects below have licences compatible with it.

## The method, step by step

1. Start from the France skill for the job (see the pack README). Each skill names the official page behind each figure.
2. To check a figure, open the official source in this order: the code article on Legifrance (the law), then the BOFiP commentary on bofip.impots.gouv.fr (the administration's binding reading), then the impots.gouv.fr or Service Public page (the plain-language summary, which also shows when it was last checked).
3. For social contributions, use the Urssaf rate pages (urssaf.fr, taux et barèmes); they print each year's rates and ceilings.
4. Use the open-source projects below only to cross-check an arithmetic result or to see how a rule has been coded. They are not a source of law: where they differ from Legifrance or BOFiP, the official text wins.

### Official sources

| Source | What it is for |
|---|---|
| Legifrance (legifrance.gouv.fr) | The Code général des impôts, the Livre des procédures fiscales, the Code de la sécurité sociale, the Code de commerce, and each finance law as published in the Journal officiel |
| BOFiP (bofip.impots.gouv.fr) | The tax administration's commentary, by series (IR, IS, TVA, BIC, BNC, RFPI, CF), and the yearly scales (BAREME) |
| impots.gouv.fr | Forms, notices, the yearly income tax brochure, and plain-language answers for individuals and businesses |
| Service Public (service-public.gouv.fr and entreprendre.service-public.gouv.fr) | Checked summaries of the rules, each with a "Vérifié le" date |
| Urssaf (urssaf.fr) | Employer and self-employed contribution rates, the social security ceiling, the Smic and the payroll reliefs |

### Related open-source projects

**OpenFisca France**

- Repository: [openfisca/openfisca-france](https://github.com/openfisca/openfisca-france)
- Licence: AGPL-3.0 (LICENSE.AGPL.txt in the repository)
- Language: French
- Stars: 317 on 14 November 2026
- Scope: a model of the French tax and benefit system: income tax, social contributions, housing and family benefits and more, written as executable Python with a web API.
- Why it matters: the main rules-as-code project for France, maintained by a dedicated organisation and used by French public services. It covers far more than income tax.
- Integration: same licence (AGPL-3.0). Formulas, parameter values and test cases can be referenced or adapted with attribution.

**Calculette Impôts (DGFiP source code)**

- Repository: [GouvernementFR/calculette-impots-m-source-code](https://github.com/GouvernementFR/calculette-impots-m-source-code)
- Licence: the README states CeCILL 2.1; GitHub detects the LICENSE file as AGPL-3.0. Both are compatible with AGPL-3.0.
- Language: French (M, the DGFiP's internal language)
- Stars: 86 on 14 November 2026; last updated January 2017
- Scope: the source code the DGFiP published for its income tax calculator.
- Why it matters: it is the administration's own engine, but the published version is old. Use it to see how the computation was structured, not for current figures.
- Integration: logic can be adapted with attribution.

**Calculette Impôts Python**

- Repository: [openfisca/calculette-impots-python](https://github.com/openfisca/calculette-impots-python)
- Licence: AGPL-3.0
- Language: French and Python
- Stars: 9 on 14 November 2026; last updated April 2016
- Scope: a Python translation of the DGFiP M-language calculator.
- Why it matters: easier to read than the M source; a bridge between the official logic and the OpenAccountants format. As old as the code it translates.
- Integration: AGPL-3.0, directly compatible.

## When to refuse or refer

- Never quote a figure from an open-source project as the law: confirm it on Legifrance or BOFiP first.
- Never use the DGFiP M source for a current year's figures: the published code dates from 2017.
- Where a client's position depends on a text that cannot be opened (for example a Legifrance article that refuses the read), say so and refer to a French expert-comptable or avocat fiscaliste.

## Sources

| Source and what was read | Official URL | Read on |
|---|---|---|
| Service Public F1419, income tax scale: read for the 2026 scale and its "Vérifié le" date, as an example of a checked summary | https://www.service-public.gouv.fr/particuliers/vosdroits/F1419 | 2026-11-14 |
| BOFiP BOI-IR-LIQ-20-20-30, the décote: read as an example of BOFiP commentary giving the 2026 figures | https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant=BOI-IR-LIQ-20-20-30-20260407 | 2026-11-14 |
| Urssaf, taux de cotisations secteur privé: read for the 2026 employer and employee rates page | https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html | 2026-11-14 |
| GitHub repository openfisca/openfisca-france: read for the licence file, star count and last update | https://github.com/openfisca/openfisca-france | 2026-11-14 |
| GitHub repository GouvernementFR/calculette-impots-m-source-code: read for the README licence statement, star count and last update | https://github.com/GouvernementFR/calculette-impots-m-source-code | 2026-11-14 |
| GitHub repository openfisca/calculette-impots-python: read for the licence, star count and last update | https://github.com/openfisca/calculette-impots-python | 2026-11-14 |

Not yet confirmed: none.
