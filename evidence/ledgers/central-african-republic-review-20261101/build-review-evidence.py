from pathlib import Path
import json,subprocess,re,hashlib
out=Path(__file__).parent
head='2460f6898fd1eb9bc7ddbf211377c617cc7ce7e9'
rules=json.loads(subprocess.check_output(['git','show',head+':evidence/ledgers/central-african-republic-draft-20261101/rules.json']))
# Manually written independent reading outcomes. Pages are one-based PDF pages, not OCR line positions.
checks={
'I01':('cgi2023', '5-7','Dwelling owner/usufructuary/tenant; principal stay only without that dwelling; vital economic/professional interests; treaty and article 4 caveats checked.'),
'I02':('cgi2023','22-24','Article 66 combines net categories irrespective of domestic/foreign source, subject to treaties; individual scope preserved.'),
'I03':('cgi2023','13-15,29-31','35(17) gives 378,000; visual p30 confirms defective 378.0000, next band 378,001-1,680,000 and 8%; interpretation is expressly held for live filing.'),
'I04':('cgi2023','29-31','All remaining marginal endpoints 1,680,001/3,360,000/3,360,001/5,040,000 and rates 15/28/40 checked against annual employee table.'),
'I05':('cgi2023','14-16,30','Cash/benefits, 30% professional costs, family allowance and employee retirement/CNSS deductions checked; no employee contribution percentage invented.'),
'I06':('cgi2023','28-30','Article 81 business classes 30%, agriculture 20%, and minimum comparison checked; employee scale not extended to businesses.'),
'I07':('cgi2023','29-30','0.3/1.85%, 300,000/1,850,000 floors; HT turnover plus products/profits; down-to-1000 rounding, regulated commission base, mixed separation and art83 exceptions checked.'),
'I08':('cgi2023','22-24','Final-levy exclusion and same-category loss carry to third subsequent year checked; pleasure/vacation property exclusion retained.'),
'I09':('cgi2023','30-32','Signed category return at residence/designated office by 30 April next fiscal year; acknowledgement and foreign movable-property nature/value/income declaration by same date checked.'),
'I10':('cgi2023','29-31','Article84 individual distributed capital-income tax 15% of gross distributions checked; no standalone royalty proposition inferred.'),
'I11':('cgi2023','20-22','Personal movable/immovable rights and land-rich shares; disposal/market minus acquisition price; undeducted non-rental capital improvements and principal-home exemption checked. Other exemptions remain explicitly incomplete.'),
'I12':('cgi2023','35-37,57-58','Art115 imports IS payment mechanism for non-salaried IRPP; art119 excess is carryforward credit against next instalments, not unconditional cash refund.'),
'C01':('cgi2023','37-39','Entity forms/activity/election checked; base-regime corporate annual turnover <=30m exemption is only from IS, not all taxes.'),
'C02':('cgi2023','39-41,51-52','Territorial business/operation scope with treaty reservation, net products less expenses and direct business necessity checked. Foreign-branch qualification is correctly routed.'),
'C03':('cgi2023','52-54','Art133 30% ordinary/20% agriculture; minimum is comparison, not addition.'),
'C04':('cgi2023','52-54','Art133bis 0.3/1.85%, 300,000/1,850,000 floors; tax-exclusive turnover/products/profits including interest/dividends, 1000 rounding, regulated commissions and separated mixed activities checked.'),
'C05':('cgi2023','53-54','Narrow pooled maritime/fluvial transport and fire co-insurance exemption, annual turnover not above3m; not blanket insurance exemption.'),
'C06':('cgi2023','50-52','Loss becomes next-year charge; unabsorbed amounts successively through third year following loss, not indefinite or carryback.'),
'C07':('cgi2023','51-53','Calendar 12-month baseline; start in last6months permits next-year first balance but provisional31December result taxed/credited; no filing holiday.'),
'C08':('cgi2023','54-58','Four copies before1May; DSF/balance by30April following instalment year, crediting payments checked.'),
'C09':('cgi2023','57-58','Normal-real thirds due15Feb/15Jun/15Oct; first provisionally penultimate year and second regularisation checked.'),
'C10':('cgi2023','57-58','Simplified-real halves due15Mar/15Sep; first penultimate year and regularisation by15Jun checked.'),
'C11':('lf2026','4-7','Read old/new boundary; new135bis and bis1 both say real regime and four copies; separate supporting schedules retained, overlapping scope is explicitly unresolved.'),
'C12':('lf2026','5-7','Approved annual statements and plausibility/coherence/comparability/internal concordance; no audit, limited review, statutory certification or assurance; taxpayer responsibility checked visuallyp6.'),
'C13':('lf2026','5-7','National-order expert/comptable agree, manager/legal representative incompatibility, ministerial order; separate fiscal-counsel co-certification and taxpayer statutory-auditor signing prohibition checked; reconciliation hold retained.'),
'C14':('cgi2023','40-42','Actual non-excessive employee/manager remuneration conditions checked; broader deduction computation expressly remains held.'),
'T01':('cgi2023','50-52','Correction R1: foreign/common-control scope, price/thin-capitalisation/other transfers and privileged/non-cooperative dependence waiver correct, but art131(2)(a) also expressly covers majority ownership through an intermediary.'),
'T02':('cgi2023','51-53','No taxation or tax amount more than half lower than CAR ordinary hypothetical comparator. Exactly half is not more than half. Amount comparison, not headline rates, checked.'),
'T03':('cgi2023','51-53','Privileged-recipient actual/normal/non-excessive proof distinct from non-cooperative outright non-deduction; OECD/UN/CEMAC list plus ministerial supplementation checked; no operative list promoted.'),
'T04':('cgi2023','41-43','All listed services, head-office/technical/financial/accounting, commissions/honoraria, debt products and IP; outside-Community location; real/non-abnormal/non-excessive;20% before expense; last profitable non-prescribed loss-year result; distribution treatment checked.'),
'T05':('cgi2023','41-43','Still-valid IP rights and separate distribution treatment for recipient participating in management/capital of outside-Community enterprise checked, without reversing participation direction.'),
'T06':('cgi2023','41-43','Community-enterprise purchases, buying centres/intermediaries,5% of purchases; discounts benefit enterprise and invoice attached to supplier invoice checked.'),
'X01':('cgi2023','25-27','Residence move taxes relevant income only from domicile/residence establishment; not exemption of all other CAR-source income.'),
'X02':('cgi2023','25-27','Income available through departure, profits since last taxed exercise and acquired/not received; provisional30days before, completion first2months next year; abandonment of all CAR residence checked.'),
'X03':('lfr2025','3-5','New393 excludes CAR nationals by origin from departure-clearance class; temporary/permanent and current tax; employer1month or rupture-notification day; managers under audit special permanent certificate guarantee >=10% annual turnover checked.'),
'X04':('lfr2025','4-6','Borrowing/foreign transfer/state contracts prior attestation;3months from signature,1month stayed/moratorium debt; debt not yet due or duly stayed exceptions checked.'),
'X05':('lfr2025','4-6','DGID manual/electronic unique administrative status evidence; approvals, foreign bank transfers, exemption, specified supplier payments and exports; regulatory issue conditions held.'),
'X06':('cgi2023','51-53','Treaty-subject foreign branch/agency results attached to CAR parent at seat; comparison method without precise evidence checked.'),
'X07':('cgi2023','65-68','166bis1 foreign services15% final levy treaty-subject, separate gross distributed capital-income15%; no independent20% royalty or blanket interest exemption.'),
'X08':('cgi2023','66-68','166bis3 remittance by15th following invoicing/retention; invoice separation and credits/conditions read with neighbours.'),
'V01':('lf2024','19-21','Habitual/occasional independent economic supply; <30mHT excluded; liberal-profession compulsory treatment; legal-person irrevocable authorised option, other natural persons barred; employees outside independent class.'),
'V02':('lf2024','26-28','General19%, customs-supported taxable-product exports/international transport0%, enumerated product tariff5%; visualp27 confirms both rates and list anomalies not silently corrected.'),
'V03':('lf2024','20-22,25','Goods/self-supplies, services/platforms/commissions, intra-community acquisitions/imports, public orders; aid direct consideration or price supplement condition checked.'),
'V04':('lf2024','25-27','Ordinary consideration plus accessory costs/non-VAT taxes; import customs/excise; real exact invoice discounts/debours excluded; margin limited used goods/travel/listed wholesalers, not general.'),
'V05':('lf2024','27-29','Necessary business inputs and registered compliant invoice/import payment/self-supply/withholding evidence; end of2ndyear after chargeability exercise limit checked separately from carryforward.'),
'V06':('lf2024','28-30','Blocked-credit classes and professional tourism/catering/show, enumerated petroleum and vehicle exceptions checked. Cash threshold and detailed classification held; no broad all-vehicle/all-oil rule stated.'),
'V07':('lf2024','29-31','Direct attribution before shared prorata; numerator taxable+exports denominator total with exclusions; provisional prior actual/new forecast; definitive+correction DSF30April; below10% no deduction checked.'),
'V08':('lf2024','30-32','NIU registration before status; supplier/address/NIU/date/nature/rate/net/VAT/client identity+number/continuous number;10years after accounting-entry year checked; machine implementation held.'),
'V09':('lf2024+lf2025','lf2024:32-34;lf2025:7-9','Old/new275bis read; monthly return+payment15th after operation month real regime;275bis1 expressly abrogated and275bis2 NEANT monthly retained. No stale quarterly revival.'),
'V10':('lf2024','33-35','Unlimited carryforward distinct from initial claim limit; refund for legal persons in enumerated exports/structural reduced-rate or retention/investment>100m/reciprocal missions/cessation cases; current compliance+3 consecutive credit months checked.'),
'V11':('lf2024','33-35','DGID request following quarter, form and3 credit returns; exporters EX1/repatriation/transport; no next-month reuse, cancellation upon rejection; full execution held.'),
'V12':('lf2024+lf2025','lf2024:22-25;lf2025:7-9','Use/exploitation, material performance and intangible recipient state; non-taxable Community recipient exception250(5), separate travel/transport/platform rules; solvent accredited resident representative or customer payment;2025 nonresident withholding checked.'),
'V13':('lf2025','5-8','New249 condition-specific financial/insurance, non-assujetti property, publichealth, authorised-price education, tariff medicine and diplomatic exemptions; reciprocity/quotas/officialuse/DGIDvisa; competitive nonprofit activity taxable.'),
'V14':('lf2026','6-8','Prior declare/pay then Treasury refund; public-contract/NGO/charter/mining-forest permit classes; diplomatic/UN and State gifts excluded; listed nonrefundable levies and art17 implementation held.'),
'F01':('ohada-companies-2014','76-78,94-96','SARL limited contributions and1/several members; SA contribution liability and single shareholder confirmed visuallyp95 (line omitted by PDF text extraction).'),
'F02':('ohada-companies-2014','76-78','Art311 default1m, equal shares nominal>=5000, national contrary provision reservation carried beside figure; live CAR override not asserted.'),
'F03':('ohada-companies-2014','76-78','Full subscription/in-kind payment; cash half at subscription, remainder2years fromRCCM under statutes checked, not all cash at formation.'),
'F04':('ohada-companies-2014','94-96','SA10m minimum; full subscription before statutes; cash quarter, remainder3years fromRCCM; visualp95 confirms25%.'),
'F05':('ohada-companies-2014','77-79','Immediate deposit approved bank/credit/microfinance or notary, receipt/formingcompany account; statutes record and manager availability onRCCM; national notarial-reservation preserved.'),
'F06':('ohada-companies-2014','28-30','97 participation exception toRCCM;98 personality onRCCM unless Act otherwise;101 statutes formation distinct from third-party opposability checked.'),
'F07':('ohada-companies-2014','35-37','137/138 accounts+management report;140 SA/SAS/where applicable SARL auditor45days before ordinary meeting, meeting within6months; auditor duty scoped.'),
'F08':('GUFE','web lines62-76,113-163','Independently opened primary GUFE route; entity checklist, ID/criminal/seat/statutes/capital evidence, complete counter dossier/payment,48workinghours service statement and RCCM/NIF/affiliation+connected tax/social/sector steps verified. No statutory guarantee.'),
'W01':('cgi2023','34-36','Monthly net salary and annual scale reduced to month in110; bases/bands owned by individualGuide.'),
'W02':('cgi2023','34-36','15th of eachmonth baseline; <=5 salaried workers quarterly by15th following quarter; only remittance exception and period-attribution hold retained.'),
'W03':('cgi2023','35-37','113 two administration slip copies;119 named employer summary before31January; distinguished employee annual return.'),
'W04':('cgi2023','34-36','Correction R2: ten-day cession/cessation clock and111 foreign-paid resident salary obligation correct;112 covers retained amounts OR tax due, latter limb missing.'),
'O01':('lf2025','9-11','NewLPF4 fiscalyear12months1Jan-31Dec/DGID definition; actual budget FCFA label checked, no invented exchange rate.'),
'O02':('lf2025','13-15','New243(1) missed/late registration application/return/annex/registered-publicity act500000; recidivism withinweek1000000; general/special priority not guessed.'),
'O03':('lf2025','13-15','New243(2)25%duties, badfaith/fraud50-100%;243(7)25% declaration/paymentmethods and fraud/resistance escalation50-100% according degree checked.'),
'O04':('lf2025','13-15','New243(10) absent required tax-free exemption invoice visa50000 each detected breach; no combined sanctions assumed.'),
'O05':('lf2025','10-12','New71 written identity/NIU/address/calculation/offence/date/appeal right/conditions/paymentperiod checked.'),
'O06':('lf2025','11-13','New88 written information request max10days from receipt; missing-support minutes/inadmissibility administrative/judicial dispute phases; not old adjustment-response20days.'),
'O07':('lf2025','11-13','New17190days from complaint receipt (old extension dropped); deemed accepted if no notifieddecision; originator barred from signing undernullity; wider admissibility held.'),
'B01':('cgi2023','70-72','Annual masonry-founded buildings, attached enduring industrial plant, exemptions169 checked; distinct tax from rentIRPP/VAT.'),
'B02':('cgi2023','70-73','Rentalvalue less40%, annually with1January property status;12% marketvalue/cost minimum and down-to1000base checked.'),
'B03':('cgi2023','72-74','Individual/non-IS15% versus ISlegalperson30%; nearest10tax rounding and30000minimum checked.'),
'B04':('cgi2023','70-72','169(12) first principal residential property ownerand/orfamily; other publicpurpose/ownership/location/non-income exceptions read, no rental-property blanket exemption.'),
'B05':('cgi2023','71-73','171 prefilledF61bis20day approve/correct;173 owner/debtor plus statutory exemption beneficiaries oneF66 perproperty before1Feb; forms not treated fetched.'),
'B06':('cgi2023','71-73','174 alltenants incldiplomatic/consular/international, landlord/property/prior-year-rentF67 before15Jan; non-declared timely rent non-deductible checked.'),
'B07':('cgi2023','72-74','175 locationassessment,176owner1Jan withusufruct/emphyteusis/building-on-others-land allocations;177bis31Marchpayment checked.'),
'B08':('cgi2023','7-9','14-16rent gross less40%charges; tenant-borne ownerexpense additions, landlord-borne tenantexpense reductions, qualifying subsidies/indemnities; separate from buildingtax/finalIRPP.')
}
assert set(checks)==set(rules)
guides={p:subprocess.check_output(['git','show',head+':'+p],text=True) for p in subprocess.check_output(['git','ls-tree','-r','--name-only',head,'skills/central-african-republic'],text=True).splitlines() if Path(p).name.startswith('cf-')}
rows=[]
for k,(source,pages,note) in checks.items():
 placements=[]
 for path,text in guides.items():
  for n,line in enumerate(text.splitlines(),1):
   if re.search(r'ledger '+k+r'\b',line): placements.append({'path':path,'line':n,'rule_text_exact':rules[k]['text'] in line})
 rows.append({'id':k,'source':source,'pdf_pages_read':pages,'article':rules[k]['act_article'],'primary_url':rules[k]['url'],'outcome':'correction' if k in ['T01','W04'] else 'pass_with_stated_scope','independent_check':note,'placements':placements})
assert all(len(r['placements'])==1 and r['placements'][0]['rule_text_exact'] for r in rows)
(out/'rule-review.json').write_text(json.dumps({'candidate':head,'reviewed_on':'2026-11-01','rules_checked':len(rows),'scope':'Baseline text and specifically identified amendments only; full-current-law and execution holds survive. 81 grouped records contain many limbs; 81 is not asserted as count of individual figures.','rows':rows},indent=2,ensure_ascii=False))
md=['# Independent primary-source rule review','',f'Candidate `{head}`. Read date 2026-11-01. 81 grouped records, each placement and its numerical/conditional limbs checked. Counts are not accountant attestation.','', '| ID | Primary PDF pages / article | Result and independent check |','|---|---|---|']
for r in rows: md.append(f"| {r['id']} | {r['source']} pp.{r['pdf_pages_read']}; {r['article']} | {r['outcome']}: {r['independent_check']} |")
(out/'rule-review.md').write_text('\n'.join(md)+'\n')
print('81 manual rule outcomes;81 exact rule placements;T01/W04 corrections recorded.')
