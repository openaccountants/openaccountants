---
name: yt-employer-payroll-relief
description: "Mayotte employer payroll relief reference for 2026. Distinguishes the January RGDU commencement from the July LODEOM commencement, the local minimum-wage reference and the prohibition on combining the two reliefs. Explains the Mayotte coefficient parameters, local contribution limits and period changes without substituting mainland figures. Includes an algebraic illustration with explicit assumptions and an evidence checklist. Complete contribution bases, sector-specific LODEOM eligibility, DSN coding, emergency measures and independent accountant verification remain outside this initial source-cited draft."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/yt-employer-payroll-relief"
  jurisdiction: "YT"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Mayotte: RGDU and LODEOM employer relief

## Commencement and choice of relief

Mayotte's social security authority confirms **RGDU from the January 2026 employment period** and **LODEOM from 1 July 2026**, with the latter first declared at the August due date. Both reduce employer contributions. They **cannot be combined**. Eligibility for LODEOM depends, among other things, on workforce size and activity sector. [CSSM guidance](https://www.cssm.fr/actualite/reduction-generale-degressive-unique-rgdu-et-exoneration-lodeom).

Article 3 of Decree 2026-82 expressly distinguishes the January commencement of its RGDU/rate provisions from the July commencement of its LODEOM provisions, by employment period. Do not apply July relief to January employment solely because the contribution is paid later. [Decree 2026-82, article 3](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000053465499).

## RGDU parameters specific to Mayotte

The 2026 RGDU decreases to zero at **1.6 times the Mayotte minimum wage**. The superseded local relief ended at 1.4 times minimum wage. CSSM describes LODEOM schedules ending at 2.2, 2.7 or 3.5 times the local minimum wage, depending on the applicable schedule; those endpoints alone do not establish eligibility or the intervening calculation. [CSSM guidance](https://www.cssm.fr/actualite/reduction-generale-degressive-unique-rgdu-et-exoneration-lodeom).

The June 2026 version of Social Security Code article D.241-7-1 supplies the Mayotte formula:

`coefficient = Tmin + Tdelta × [(1 / (A − 1)) × (A × S / R − 1)]^P`

Here `S` is the applicable annual Mayotte minimum-wage amount and `R` is the annual remuneration defined by the governing provisions. For 2026, `Tmin = 0`, `P = 1` and `A = 1.6`. The maximum coefficient depends on the eligible local contribution rates; reduce Tdelta where the employer's actual eligible rate total is lower. [Article D.241-7-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/); [Urssaf's Mayotte calculation section](https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html).

When a parameter affecting the annual minimum wage changes during the year, article D.241-7-1 requires the annual value to combine the amounts for the periods before and after the change. It does not prescribe freezing Mayotte's minimum wage at its January amount for every 2026 calculation. Use the applicable local wage, working-time adjustments and payroll period evidence. [Article D.241-7-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/).

## Illustrative coefficient check

Assume an eligible worker with `R = 1.2 × S`, no other adjustments, and an independently established eligible `Tdelta = 0.24`. The expression is:

`0.24 × [(1 / 0.6) × (1.6 / 1.2 − 1)] = 0.133333…`

At `R = 1.6 × S`, the expression is zero. At `R = S`, it is 0.24. The assumed 0.24 is **not a published universal rate**; this example tests the algebra and does not calculate a payslip or override statutory rounding, annual regularisation or contribution caps. [Formula: article D.241-7-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/).

## Implementation evidence

Before claiming relief, record the employment period, establishment, employee eligibility, working time, remuneration, applicable local minimum wage, eligible contribution total and chosen relief. For LODEOM, establish the business's sector, workforce and exact schedule rather than selecting the largest endpoint. These are practical controls for the conditions above.

CSSM points employers to the updated Urssaf declaration guide and payroll-software changes. The linked guide did not download successfully in this research, so no DSN code or operational filing instruction is supplied here. The complete LODEOM eligibility law, individual contribution bases, other payroll charges and emergency cyclone measures remain to be researched. Independent source review and accountant attestation are pending. [CSSM](https://www.cssm.fr/actualite/reduction-generale-degressive-unique-rgdu-et-exoneration-lodeom).

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `yt-employer-payroll-relief` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/yt-employer-payroll-relief. If neither is available, confirm every figure against the official source pages cited above before relying on it.
