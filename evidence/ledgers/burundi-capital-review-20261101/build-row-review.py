#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
E=Path(__file__).resolve().parent;W=E.parent/'burundi-capital-20261101';S=E.parents[3]/'sources'
rows=json.loads((W/'bi-capital-income-tax.json').read_text())
notes={
'C01':'Complete IR19 with IR18/20/21 neighbours: natural-person annual tax, first employment/business/rental and second capital/gain categories. No company classification imported.',
'C02':'IR20 resident worldwide taxable-income limb read with source arts6–7. Residence is routed to owner Guide rather than guessed.',
'C03':'IR20 nonresident Burundi-source limb read together with additional gain asset limitation IR90; no blanket rate on nonresidents.',
'C04':'Complete IR88 read visually at PDF30, following rental provisions and before89. Cash/in-kind, listed payment types, natural-person limitation and not already taxed business-profit condition all retained.',
'C05':'IR2(u) full definition and both valuation paragraphs visually read PDF6. Financial assets and collectible movables are in asset scope; no unsupported common cost formula supplied.',
'C06':'IR98 PDF33 visually read with95–99. Company taxable base includes capital/gains with already-taxed-dividend exception. Does not establish15% company gain rate.',
'C07':'IR23 visually read PDF13:15% second category and separate sentence applying same rate to IR37(2) asset-sale product. Not source-withholding rate or full professional-gain computation.',
'C08':'Original IR89 table visually read PDF31:0 à5 ans/20%, not OCR26%. Separate cell transcription is disclosed; no boundary operator inferred.',
'C09':'Original table5 à10 ans/15%. Eight-year examples are strictly inside range.',
'C10':'Original table10 à15 ans/10%; precise anniversaries remain held.',
'C11':'Original table15 à30 ans/5%; precise anniversaries remain held.',
'C12':'Original table30 ans et plus/2,5%; precise30-year overlap held.',
'C13':'IR89 opening sentence visually read with2(u): coefficient multiplies disposal price into deemed gain base; then IR23 tax rate applies.',
'C14':'IR89 expressly requires no legal obligation to depreciate; mere absence of claimed depreciation is insufficient. Body uses legal obligation and excludes depreciable business extension.',
'C15':'IR89 sentence is exact. Newly recovered2021order17 expressly points to540/188of13Mar2000 completed by540/577of31Jul2000; recovered2025order1145 revisits those orders and supplies reference-value rules. Replace unrecovered-order narrative with recovered-source/current2026chain hold. No tariff calculation certified.',
'C16':'IR91 full first paragraph visually read: housing-use immovable/fraction and adjoining land. No words principal residence/self-occupation duration in actual clause.',
'C17':'IR91 second paragraph: one disposal of one building/fraction. Repeat rule does not turn one transaction into multiple exempt properties.',
'C18':'IR91 final paragraph: new grant may follow5years measured from last grant. Four years fails; six years alone does not prove grant. Grant execution remains held.',
'C19':'IR93 cap is correctly quoted. Actual2021order18 additionally limits deductible registration duties to those PAID BY SELLER on immovable sale. Add explicit condition to rate/base/inputs and case1; eligible alone does not show decisive payer predicate.',
'C20':'January201 entire clause visually read PDF51: only Treasury bill/bond interest. No first-half secondary-market gain exemption inferred from this sentence.',
'C21':'July217 full first sentence visually read PDF57: Treasury interest exempt for2026/27; commencement2771July checked signed final page.',
'C22':'July217 second sentence visually read: Treasury-securities secondary-market disposal gains also exempt. No private security or retrospective January extension.',
'C23':'January252 signed final physical249/printed246 visually read.1erJanuary2026, promulgated31Dec2025. Superscript transcription normalization only.',
'C24':'July277 signed physical267 visually read.01July2026, signed30June2026. No inference from fiscal title alone.',
'C25':'IR2(o) full definition visually read PDF5:loans/deposits/guarantees/currentaccounts/statefunds/bonds/participatory/debt securities; return of principal not interest.',
'C26':'IR2(j) full definition visually read PDF4, including profit-linked debt-title assimilation. Scope words maintained.',
'C27':'IR2(j) liquidation excess over REVALUED PAID-UP capital visually read. Original issue is not ordinary acquisition cost; mechanics explicitly held.',
'C28':'IR2(v) entire royalty definition visually read PDF6, copyright/media/IP/equipment/industrialcommercialscientificexperience/naturalresources. Body says specified categories, no unsupported valuation.',
'C29':'IR2(u) full professional-immovable difference formula visually read. Business-disposal IR23proceeds interaction remains held, not silently resolved by definition.',
'C30':'January80 actual enacted complete replacement read PDF26with79–88neighbours. Asset-saleproduct in business holding/liq/equipment limb retained. Nothing says this resolves professional netvalue tension.',
'C31':'July79 actual enacted full replacement read PDF25with78–86neighbours. Same asset-sale limb retained; difference in other expense crossrefs not silently rewritten.',
'C32':'January148 complete replacement read PDF44: six payment categories, financialintermediary/state/professionexceptions and gamingcharges. Body routes payer computation and holds gaming, duplicates no withholding figure.',
'C33':'July156 full replacement read PDF47–48with155/157–158neighbours: same payer distinctions/special gaming. Scope kept separate from individual second-category rate.',
'C34':'IR92 full sentence visually read PDF31. Seller declares AND pays corresponding movable/immovable gain tax within15CALENDARdays following disposalMONTH. Not15days after deed/payment.',
'C35':'IR123–124 original full asset/payer/seller/paymentclock visually read PDF41. Buyer may be resident OR nonresident; seller is nonresident.2021order3 corrects IR22 finality references to122point4°,123and125 for Burundi-source nonresident income not attributable to PE. Repair blanket held/neverinferred finality narrative; annual-return/reconciliation remains distinct.',
'C36':'IR24 full annual clause visually read PDF13–14, lastdaythirdmonth afteryearend prescribedform. No current private-capital box inferred.2021order3 does not replace this deadline.',
'C37':'Original IR25quote matches2020page14 but is no longer complete current rule.2021order3 table printed338 corrects25point2°119et120 TO118et119. Body must state corrected references; still no general IR122capital-withholding annualexemption. Read26optional filing.',
'C38':'January146 full replacement of IR28 read PDF43. It expressly re-enacts119/120 and126 crossrefs plus37(2)salecredit. Do NOT overwrite enacted2026replacement with2021correction of earlier28. Calculation/allocation execution held.',
'C39':'July154 full replacement read PDF46–47. Same warning: actual later text controls its own list; annual and monthly clocks read, privategain not automatically equal businesssalecredit.',
'C40':'Actual fourpage official form read, business-income title, line8assetproceeds,28/29businessminprofit,31–36credits,37balance and administrationreceipt. Does not prove private-gain boxes or nonexistence of separate form.',
'C41':'Official portal live reader opened: Moyens/Grands and Petits/Micro separate routing, documentation list. Exact quote verified. No authentication/payment/submission screens claimed.',
'C42':'IR90 entire firstparagraph visually read PDF31. Nonresident asset limitation for resident-companyshares or Burundiimmovableparticipation retained, distinct from source and withholding.',
'C43':'IR90 secondparagraph visually read:50%ATLEAST ofparticipationvalue attributable toBurundiimmovables. No strictgreater-than or costbasis inferred.',
'C44':'Complete IR6–7 read PDF7–8, including localpropertyrights and direct/indirectfinancialdisposals in residentcompany plusforeignresidual; does not erase IR90additionalgainlimitation.',
'C45':'Independent Decimal recomputation:100m×15%=15mgain;×15%=2.25mtax; lowcredit1m balance1.25m; highcredit2.25m balance0;750000outsidecredit. Arithmetic correct. Add express seller-paid eligible-duty facts per2021order18 before predicate acceptance.',
'C46':'Independent Decimal recomputation:15mgain and2.25mtax. Fouryearlastgrant barred by5yearrule; sixyearcase explicitlyassumes freshgrant, giving0and2.25mdifference. No invented principalresidencecondition. Notautomaticrelief.',
'C47':'Independent Decimal recomputation:2m×15%=300000; AugustTreasurycoupon exemptunderJuly217 =>0, otherwise-taxableprivatecoupon=>300000 beforewithholdingreconciliation. Securityidentitydecision; nonbusiness/nootherexemptionfacts stated.'
}
repairs={'C15':'R4','C19':'R3','C35':'R2','C37':'R2','C45':'R3'}
out=[]
for r in rows:
 out.append({'id':r['id'],'claim':r['claim'],'section':r['section'],'original_writer_article':r['article'],'original_writer_quote':r['exact_quote'],'official_url':r['official_url'],'original_source_sha256':r['source_sha256'],'review_read_date':'2026-11-01','original_quote_check':'Matches actual original page; table-cell delimiter/inline superscript normalization disclosed where relevant','verdict':'repair required' if r['id'] in repairs else 'pass within stated partial scope','finding':repairs.get(r['id']),'independent_check':notes[r['id']]})
(E/'row-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
md=['# Independent every-row review, frozen capital candidate','', 'All47writerledgerrows checked against actual original clauses and relevant neighbours. Original wording is retained as historical evidence; exact2020quotation is not proof of2026operative meaning. Newly recovered2021implementation order and2025valuation order are recorded separately.42rows pass within the partial scope;5rows require the narrow repairs below. R1category is outside the rowledger.','', '| Row | Verdict | Decisive original quote | Independent reading and conditions |','|---|---|---|---|']
for r in out:md.append('| '+r['id']+' | '+r['verdict']+(' ('+r['finding']+')' if r['finding'] else '')+' | '+r['original_writer_quote'].replace('|',' / ')+' | '+r['independent_check']+' |')
(E/'row-review.md').write_text('\n'.join(md)+'\n')
print({'rows':len(out),'pass':sum(x['finding'] is None for x in out),'repair_rows':repairs})
