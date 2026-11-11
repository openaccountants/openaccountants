---
name: kr-income-tax-reference
description: Reference sections for kr-income-tax (Deadlines and filing, Penalties and interest), moved from the parent skill word for word so each file stays under the size limit. MUST load alongside kr-income-tax.
version: 2.2
jurisdiction: KR
tax_year: 2025
tax_year_notes: "Coverage starts with the 2025 year (2025년 귀속, filed in 2026) and includes the 2026 year (2026년 귀속, filed in 2027). The law was read at 5 November 2026. Expense rates are those of 국세청고시 제2026-14호, which applies to 2025 only; no rate notice for 2026 was read, so a 2026 computation on 단순경비율 or 기준경비율 is Needs Input. The 2026 revision bills before the National Assembly are not treated as law. The local credit rule in 지방세특례제한법 art. 167의2 has a stated end date of 31 December 2026, and its effect on a 2026 return filed in 2027 is held."
last_updated: 2026-11-05
depends_on:
  - kr-income-tax
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# kr-income-tax: reference sections

Moved word for word from `kr-income-tax`. Load that skill first.

## Deadlines and filing

Where a date falls on a Saturday, Sunday, public holiday, substitute holiday or Labour Day (노동절), it moves to the next day (국세기본법 art. 5(1), as amended on 11 November 2025). A system failure also moves the date (art. 5(3)). Dates for 2026 are computed from the statute: no NTS page for that year was read.

| Item | 2025 year | 2026 year | Basis |
| --- | --- | --- | --- |
| 사업장현황신고 (VAT-exempt business) | 10 February 2026 | 10 February 2027 | 소득세법 art. 78; NTS https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2283&cntntsId=7699 |
| Final return and payment (종합소득세) | 1 June 2026, because 31 May 2026 is a Sunday | 31 May 2027 | Arts 70, 76 |
| 성실신고확인 filers | 30 June 2026 | 30 June 2027 | Art. 70의2 |
| Local income tax | Same dates, to the local government | Same dates | 지방세법 art. 95(1); 지방세기본법 art. 24(1) |
| Instalment of national tax | Within 2 months after the due date. Computed, not read on a page: 3 August 2026, as 1 August is a Saturday; 성실신고 filers 31 August 2026, as 30 August is a Sunday | Computed, not read on a page: 2 August 2027, as 31 July is a Saturday; 성실신고 filers 30 August 2027 | 소득세법 art. 77 |
| Estimated tax (중간예납), paid in the year itself | 1 December 2025, as 30 November was a Sunday | 30 November 2026 | 소득세법 art. 65 |
| VAT | Route to `south-korea-vat`. The prior version's '25 January and 25 July' is the final return date for a general operator's 2 periods (부가가치세법 art. 49), beside the interim step in art. 48. A 간이과세자 has one period, the year (art. 67) | Same | 부가가치세법 |

**Payment in instalments.** The prior version said 'with NTS approval'. The article needs no approval. Tax payable over KRW 10,000,000 may be split: up to KRW 20,000,000, the excess over KRW 10,000,000; above KRW 20,000,000, up to 50% (소득세법 art. 77; 시행령 art. 140). Local income tax over KRW 1,000,000 may be split within 2 months: up to KRW 2,000,000, the excess over KRW 1,000,000; above that, up to 50% (지방세법 art. 95(4); 시행령 art. 92(3)).

**The 2025 year extension (date-limited).** NTS 7664 records an administrative extension of the payment date from 1 June 2026 to 31 August 2026, with instalments to 2 November 2026. It covered (1) businesses within the January 2026 VAT payment extension: general operators with 2024 revenue of KRW 1,000,000,000 or less and first half 2025 sales down 30% or more on the prior year, in manufacturing, construction, wholesale, retail, food, accommodation, transport or services; and all 간이과세자; excluding real estate rental and professional services; (2) businesses in the oil-sensitive VAT extension; and (3) operators hurt by unpaid platform settlements (티몬, 위메프). It needed a return by 1 June 2026, and excluded people with financial income over KRW 20,000,000 and 성실신고 filers. Others could apply on Hometax: 로그인 > 증명·등록·신청·사업자현황 > 세금관련 신청·신고 공통분야 > 신고·납부 기한연장 신청/내역조회 > 신고분 납부기한 연장신청. This is administrative practice, not statute. It extended payment, not filing, and those dates have passed. Whether local tax had the same extension was not read: held. No such measure is assumed for 2026.

**Estimated tax (중간예납).** It is half (the prior version's 'approximately 50%') of the prior year's 중간예납기준액, with notices issued 1 to 15 November and payment by 30 November (art. 65). It is not collected where the instalment is under KRW 500,000 (art. 86(4)). The rest of the list comes from 시행령 art. 123 and NTS 7673 for 2026. Outside it: a person who started in 2026 and was not in business at 31 December 2025; a person who suspended or closed by 30 June 2026, or closed later with 수시 payment or assessment; a 납세조합 member whose union withheld monthly from January to June; a real estate seller whose preliminary payment exceeds 50% of the base; and a person with only these: interest, dividend, employment, pension or other income; 사무지원 서비스 income; income assessed under art. 82; self-employed artists (저술가, 화가, 배우, 가수, 영화감독, 연출가, 촬영사, as the page lists them); athletes, coaches and referees; independent insurance and securities solicitors; door-to-door sales commissions where the 2025 year-end settlement was made; separately taxed small housing rental income; and joint business income of 전환정비사업조합 members. A person whose half-year tax is under 30% of the base may file an estimate (art. 65(3)): half of the computed tax, less reliefs, interim payments, 수시부과 and withholding. A 복식부기의무자 with no base must file (art. 65(5)). Local income tax has no such instalment in the articles read.

**Filing forms.** Hometax, or paper, 별지 제40호서식(1); 제40호서식(4) for 단순경비율. NTS 7665 attachments: the return and payment statement; deduction and credit statements with proofs; for 복식부기의무자 the balance sheet, income statement, trial balance and adjustment statement (art. 70(4); failure to attach is treated as no return); 간편장부 소득금액계산서; 추계소득금액계산서; 성실신고확인서; 영수증수취명세서 (별지 제40호의5); 결손금소급공제세액환급신청서.

**성실신고확인.** Certifier: 세무사, 공인회계사, 세무법인 or 회계법인; a 세무사 cannot certify their own return (시행령 art. 133).

**Local return.** After the Hometax return, follow 개인지방소득세 신고 이동 to Wetax, or 신고내역조회 > 지방소득세 신고이동 (NTS 7664). Wetax itself was not read. Filing with the wrong authority remains valid (지방세법 art. 95(1)). Paying a provisional 납부서 by the deadline counts as filing, where NTS sent one (art. 95(5), (6); 시행령 art. 92(4)). Amendments and refund claims go to the local government (art. 96; 지방세기본법 arts 49, 50).

**No return needed (소득세법 art. 73; NTS 7664).** Employment income alone, settled at year end, unless the person has pay, public pension, retirement or settled business income from 2 or more payers not combined at year end, has pay or retirement income with no withholding duty, or was not settled. Prior year revenue under KRW 75,000,000 and no other income, as an insurance agent, door-to-door seller or contract delivery seller settled by the company. Retirement income and settled business income only. Non-taxed or separately taxed income only. Other income of KRW 3,000,000 or less where separate taxation is chosen. The NTS list ends with 등 (and so on), so a case outside these limbs is Needs Input. 사업소득 of any other kind needs a return, including a nil or loss result (art. 70(1)).

**Amended and late returns.** 수정신고 (국세기본법 art. 45), 경정청구 within 5 years, or 3 months after a decision that increases tax (art. 45의2), and 기한 후 신고 (art. 45의3).

## Penalties and interest

| Offence | Penalty | Basis |
| --- | --- | --- |
| No return (무신고) | 20% of tax; fraud 40%, offshore fraud 60%. 복식부기의무자: larger of that and revenue × 7/10,000 (fraud 14/10,000). A 복식부기의무자 who files an estimate without the art. 70(4) statements is treated as filing no return (NTS 7665, NTS 7669) | 국세기본법 art. 47의2; 소득세법 art. 70(4) |
| Under-reporting (과소신고) | 10% of the additional tax; fraud 40% (offshore 60%) + 10% on the rest. 복식부기의무자 fraud: larger of the 40% (60%) amount and under-reported revenue × 14/10,000, plus the 10% on the rest | Art. 47의3 |
| Late payment (납부지연), text to 30 June 2026 | Tax × days × 22/100,000 (the prior version's 0.022%, about 8.03% a year), to the date of payment, leaving out the days from the notice date to the notice due date; 3% of tax unpaid at a notice due date. Days after the notice due date count for 5 years at most. The days limb does not apply where the tax on a notice is under KRW 1,500,000 | Art. 47의4(1), (7), (8); 시행령 art. 27의4(1) |
| Late payment, text from 1 July 2026 | Daily 22/100,000 from the day after the legal due date to the day before the notice date or the payment date. After the notice due date: 3%, then 67/10,000 per month to the day before payment, 5 years at most, plus the collection notice cost by registered post. Where the tax on a notice is under KRW 1,500,000, the monthly limb and that cost do not apply, and the 3% still does | Art. 47의4(1), (7), (8); 시행령 art. 27의4(2). 법률 제21212호 부칙 art. 3: a notice due date passed by 30 June 2026 stays on the old text |
| Records not kept (무기장) | Computed tax × (unrecorded income ÷ 종합소득금액, taken as 1 if above 1 and 0 if below 0) × 20%. Not for 소규모사업자. The prior version's 'KRW 200,000 to 2,000,000' has no primary support and was replaced | 소득세법 art. 81의5; 시행령 arts 132(4), 147(1) |
| Art. 81의5 with no-return penalty | Only the larger (equal: 국세기본법) | 국세기본법 art. 47의2(6) |
| No 성실신고확인서 | Larger of computed tax × (business income ÷ 종합소득금액, taken as 1 if above 1 and 0 if below 0) × 5%, and business revenue × 2/10,000. Applies with no computed tax | 소득세법 art. 81의2 |
| 영수증수취명세서 | 1% of the amount not filed or not clear. Not 소규모사업자 or 단순경비율 filers; a 기준경비율 filer is exempt only on costs other than 매입비용, 임차료 and pay | Art. 81; 시행령 art. 147(1), (2) |
| 증명서류 (evidence) | 2% of amounts without proper evidence. Same carve-outs as the row above | Art. 81의6; 시행령 art. 147(1), (2) |
| 사업장현황 report | 0.5%, for medical, veterinary and pharmacy only | Art. 81의3; 시행령 art. 147의2 |
| 사업용계좌, card and cash receipts | Art. 81의8 0.2%; art. 81의9 5%, and cash receipts 1%, 5% or 20% as listed | Arts 81의8, 81의9 |
| 계산서 | 1% and the listed summary penalties | Art. 81의10 |
| 지급명세서 | 1% (0.5% if filed within 3 months); daily workers 0.25% (0.125% if filed within 1 month); 간이지급명세서 0.25% (0.125% if filed within 1 month, or within 3 months for 근로소득 of workers other than daily workers paid before 1 January 2027) | Art. 81의11(1)(1); 법률 제19196호 부칙 art. 6(4), which keeps the earlier art. 81의11(1)(1)나 for that income |

These penalties sit in different Acts and each reaches only its own duty. The art. 47의2 to 47의4 rules apply to national tax. Local tax has its own rules (지방세기본법 arts 53 to 55) and is not penalised by the national Act. Art. 81의5 penalty is charged within 소득세법 on the duties in arts 160 and 161. 지방세법 art. 99(1) sets the local share of those 소득세법 penalties at 10%, with the larger-only rule where 지방세기본법 arts 53 or 54 also apply.

**Reductions (국세기본법 art. 48).** Reasonable cause and the extension grounds remove a penalty (art. 48(1)). Amended return, of the art. 47의3 penalty: 90% within 1 month, 75% within 3, 50% within 6, 30% within 12, 20% within 18 and 10% within 24. Late return, of the art. 47의2 penalty: 50% within 1 month, 30% within 3, 20% within 6. Not available where the person knew a correction was coming. These do not reduce the late payment penalty.

**Local tax.** 지방세기본법 art. 53: 20%, fraud 40%. Art. 54: 10%, fraud 40% + 10%. Art. 55: 22/100,000 per day to payment or notice (시행령 art. 34(1)), capped at 75% of the tax (art. 55(1)); 3% at a notice due date; monthly 66/10,000 (art. 34(2)), for 60 months at most (art. 55(1)), not under KRW 450,000 (art. 55(4)). Art. 57(2): the same reductions. Where 소득세법 art. 70(4) treats a person as filing no return, the local return is treated as not filed too (지방세법 art. 99(2)).

## Sources

Read on 5 November 2026. law.go.kr text was fetched at the version dates shown. Tables in the statutes are images: arts 55(1) and 35(3) were checked by viewing the image, others from the image's alternative text. Translations of statutory terms are the author's, not official.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| 소득세법, in force 31 December 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared with the 2026 text on the rate, deduction, credit, withholding and penalty articles listed in the next row |
| 소득세법, in force 5 November 2026 (법률 제21221호 with 제21548호) | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 1의2, 3, 4, 5, 6, 14, 19, 24, 26, 27, 33, 33의2, 35, 39, 43, 45, 47, 50 to 54, 55, 56의2, 59 to 59의4, 60, 61, 65, 70, 70의2, 73, 74, 76, 77, 78, 80, 81 to 81의14 (headings and operative sentences), 85, 85의2, 86, 127, 129, 144의2, 149, 150, 152, 160, 160의2, 160의5 and the 법률 제21548호 부칙, with 법률 제20615호 부칙 art. 14 |
| 소득세법, version in force 1 July 2022 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=237497&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20220701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 81의11, 164의3, for the earlier rule kept by 법률 제19196호 부칙 art. 6(4) |
| 소득세법, version dated 1 January 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260101&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 59의2 |
| 소득세법, version dated 21 April 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=285523&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260421&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 59의2 |
| 소득세법, version dated 1 January 2027 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20270101&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared on rates and selected articles, no full comparison |
| 소득세법 시행령, in force 28 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279961&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared on arts 67, 83, 118의8, 132, 133, 143, 147, 208, 208의2(1) |
| 소득세법 시행령, in force 1 October 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290841&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 55, 61, 67, 78, 78의3, 83, 97, 118의8, 119의3, 123, 132, 133, 140, 143, 145, 147, 147의2, 184, 208, 208의2(1) |
| 소득세법 시행규칙 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=286379&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 67, 67의2, 95의2 at 1 July 2025 and 1 July 2026, which differ only in the ministry name; the forms list at 1 July 2026 |
| 국세기본법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=289999&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 5, 45, 45의2, 45의3, 47의2 to 47의5, 48 and 법률 제21212호 부칙 at 2 October 2026. The 11 November 2025 text was machine compared on those articles; arts 47의4, 47의5 and 48 differ, and those spans were read |
| 국세기본법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=283623&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 27의4 at 15 September 2025 and 1 July 2026 |
| 지방세법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 91, 92, 94 to 97, 99, 103의13; no difference between the 2025 and 2026 versions on them; art. 103의17 at the 2026 version |
| 지방세법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290815&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 92 |
| 지방세기본법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290139&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 24, 49, 50, 53 to 55, 57, with no difference from the 11 November 2025 text on them |
| 지방세기본법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290497&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 34 |
| 지방세특례제한법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=286607&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260602&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 167의2, 167의3 and 법률 제12955호 부칙 art. 2 |
| 지방세특례제한법, version dated 9 September 2027 (법률 제21901호, 8 September 2026) | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=289389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20270909&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 167의2, 167의3 and 법률 제12955호 부칙 art. 2 match the row above, with the end date unchanged |
| 조세특례제한법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=284389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 7 (industry list), 86의3, 104의8, 122의3, 126의6, 132의2 (limit only) |
| 조세특례제한법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=288915&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 104의5, 121의6 and the 104의5 부칙 |
| 조세특례제한법, dated 11 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279739&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251111&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared with the current text on arts 7, 86의3, 104의8, 122의3, 126의6, 132의2 |
| 조세특례제한법 시행령, in force 28 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279959&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 104의5; compared on art. 121의6 |
| 부가가치세법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276117&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260102&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 8, 26, 48, 49, 67 |
| 국고금 관리법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276079&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260102&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 47 |
| 국세청고시 제2026-14호, 2025년 귀속 경비율 고시 | https://nts.go.kr/nts/na/ntt/selectNttInfo.do?nttSn=1350024 | 2026-11-05 | Read in part: arts 2 and 4 and the rate rows in the table above; 1,542 rows parsed, others not individually checked |
| NTS 종합소득세 개요 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2224&cntntsId=7664 | 2026-11-05 | Read in full: dates, extension, no return cases, Wetax link |
| NTS 신고납부기한 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2225&cntntsId=7665 | 2026-11-05 | Read in full: dates and attachments |
| NTS 세액계산 흐름도 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2226&cntntsId=7666 | 2026-11-05 | Read in full |
| NTS 세율 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667 | 2026-11-05 | Read in full: table labelled 2023 to 2025 |
| NTS 가산세 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2228&cntntsId=7668 | 2026-11-05 | Read in full |
| NTS 기장의무 판단 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2230&cntntsId=7669 | 2026-11-05 | Read in full |
| NTS 간편장부 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2231&cntntsId=7670 | 2026-11-05 | Read in full |
| NTS 성실신고확인제도 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2234&cntntsId=7672 | 2026-11-05 | Read in full |
| NTS 중간예납 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2236&cntntsId=7673 | 2026-11-05 | Read in full |
| NTS 사업장현황신고 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2283&cntntsId=7699 | 2026-11-05 | Read in full |
| NTS 사업소득 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6464&cntntsId=7900 | 2026-11-05 | Read in full: withholding lists |
| NABO 2026년 세법개정안 분석 | https://www.nabo.go.kr/board/file/down.do?fid=33319646 | 2026-11-05 | Digest of bills, read in part: pp. 1 to 6 and 54 to 58, and term searches over the 294 pages |

### Source conflicts

- **Health premiums.** The prior version treated them as a 소득공제. 시행령 art. 55(1) makes the owner's own premium 필요경비. Corrected.
- **NTS 7672 and 조세특례제한법 art. 122의3(5).** The page states a clawback test on revenue and expenses of 20% and a monthly rent date of 31 December 2025. The Act read says 사업소득금액, 10% (성실사업자 20%), and 31 December 2026. The Act is used here; the page may be dated.
- **NTS 7664 on holidays.** The page lists 공휴일 and 토요일. 국세기본법 art. 5(1) as amended adds 일요일, 대체공휴일 and 노동절. The Act is used.
- **NTS 7668 caption year.** The penalty table's year label differs from its heading. Only rates matching the statute are used.
- **`south-korea-vat`.** That sibling guide states the simplified VAT figures its own way, and this file's prior version used KRW 48,000,000 as a registration test. This file defers to that guide on VAT, which was not changed.

### Other legacy topics

- **Contributor.** The prior version's table named the Open Accountants Community as contributor and its skill version as 2.1.
- **Key legislation.** The prior table's references were corrected: business income is art. 19 (art. 27 is necessary expenses); income deductions are arts 50 to 54; tax credits are arts 56 to 59의4 and art. 65 is estimated tax; local income tax is 지방세법 arts 91 to 103의13.
- **Known gaps.** Non-resident Korean-source income; financial income above the test (금융소득 종합과세); real estate capital gains (양도소득세); corporate income tax (법인세); international income and treaties.
- **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional, such as a 세무사 or 공인회계사, before filing or acting on them.

Not yet confirmed: the 2026 expense rate notice; whether 지방세특례제한법 art. 167의2 reaches a 2026 return filed in 2027; the local e-filing credit amount under art. 167의3; local government rate variations under 지방세법 art. 92(2); the text and passage of the 2026 revision bills, including the withholding rate, dependant income test, monthly rent, birth and marriage credits; the result for children born in 2017 under 법률 제21548호 부칙 art. 2(3); the 2026 NTS pages for dates, including any extension for that year; whether local tax had the 2025 payment extension; the pension deduction on an estimate route (시행령 art. 143(2)); the absence of a separate health premium deduction on an estimate route; the split of tax to employment income for art. 59(1); the amount of 납세조합공제 on a return under 소득세법 art. 76(3)(5); whether 납세조합 징수세액 in art. 76(3)(5) is the net amount collected; the mapping of 납세조합공제 to the return forms; the inference that 납세조합공제 stays outside the credits in step 7; whether 지방세특례제한법 art. 167의2(1) gives a local credit for 납세조합공제; the basis for a home office share; the second car rule in 시행령 art. 78의3; transitional limits on older carried losses; depreciation rates; the art. 132의2 list; the marriage credit; 조세특례제한법 art. 7 relief, 최저한세 and 농어촌특별세 computations; currency conversion of receipts; the 시행령 별표 3의3 service list; and the art. 144의2 year-end settlement list.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template with Tier 2 metadata; rates and thresholds tested against primary text; local income tax, expense rates, bookkeeping tests, health premiums, child credit, instalments and penalties corrected; refusal messages and question threshold added; onboarding fallback changed to intake only |
| 2.1 | November 2026 | Estimated tax: KRW 500,000 instalment floor replaces the KRW 300,000 prior year test |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Korean bank formats; local platform patterns (KakaoTalk Pay, Naver Pay, Toss); worked examples |
| 1.0 | 2025 | Initial version |
