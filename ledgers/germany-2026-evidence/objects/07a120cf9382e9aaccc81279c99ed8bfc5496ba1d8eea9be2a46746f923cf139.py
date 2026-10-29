from pathlib import Path
import json,re,hashlib,shutil,datetime,subprocess
root=Path('/Users/michaelcutajar/Documents/ChatGPT/OA');b=root/'output/europe-closeout-2026-10-27/germany-root-estimated-ledger-2026-10-29';p=root/'.claude/worktrees/europe-germany/skills/international/germany/de-estimated-tax.md';body=p.read_text();sha=lambda x:hashlib.sha256(x).hexdigest();assert sha(p.read_bytes())=='5d5f9d8e80b08e2299130e2fe59328714838a89f40a54800eac2e46368e4c382'
I={x['id']:x for x in json.loads((b/'source-identities.json').read_text())};L={k:(b/x['reader']).read_text().split('\n')for k,x in I.items()};A={}
def q(k,sid,n,fragment=None):
 z=I[sid];text=L[sid][n-1];text=re.sub(r'^P\d+: ','',text) if fragment is None else fragment;assert text in L[sid][n-1],(k,text)
 A[k]={'id':k,'source':sid,'act_article':sid,'url':z['url'],'reader':z['reader'],'reader_sha256':z['reader_sha256'],'raw_sha256':z['raw_sha256'],'native_LF':[n,n],'exact_quote':text,'read_on':'2026-10-29'}
q('DATES','estg-37',1,'Der Steuerpflichtige hat am 10. März, 10. Juni, 10. September und 10. Dezember Vorauszahlungen auf die Einkommensteuer zu entrichten, die er für den laufenden Veranlagungszeitraum voraussichtlich schulden wird.')
q('ARISE','estg-37',1,'Die Einkommensteuer-Vorauszahlung entsteht jeweils mit Beginn des Kalendervierteljahres, in dem die Vorauszahlungen zu entrichten sind, oder, wenn die Steuerpflicht erst im Laufe des Kalendervierteljahres begründet wird, mit Begründung der Steuerpflicht.')
q('NOTICE','estg-37',3,'Das Finanzamt setzt die Vorauszahlungen durch Vorauszahlungsbescheid fest.')
q('BASE','estg-37',3,'Die Vorauszahlungen bemessen sich grundsätzlich nach der Einkommensteuer, die sich nach Anrechnung der Steuerabzugsbeträge (§ 36 Absatz 2 Nummer 2) bei der letzten Veranlagung ergeben hat.')
q('ADJUST','estg-37',3,'Das Finanzamt kann bis zum Ablauf des auf den Veranlagungszeitraum folgenden 15. Kalendermonats die Vorauszahlungen an die Einkommensteuer anpassen, die sich für den Veranlagungszeitraum voraussichtlich ergeben wird; dieser Zeitraum verlängert sich auf 23 Monate, wenn die Einkünfte aus Land- und Forstwirtschaft bei der erstmaligen Steuerfestsetzung die anderen Einkünfte voraussichtlich überwiegen werden.')
q('SMALL','estg-37',3,'Bei der Anwendung der Sätze 2 und 3 bleiben Aufwendungen im Sinne des § 10 Absatz 1 Nummer 4, 5, 7 und 9 sowie Absatz 1a, der §§ 10b und 33 sowie die abziehbaren Beträge nach § 33a, wenn die Aufwendungen und abziehbaren Beträge insgesamt 600 Euro nicht übersteigen, außer Ansatz.')
q('IGNORE','estg-37',3,'Die Steuerermäßigung nach § 34a bleibt außer Ansatz. 6Bei der Anwendung der Sätze 2 und 3 bleibt der Sonderausgabenabzug nach § 10a Absatz 1 außer Ansatz.')
q('CHILD','estg-37',3,'In den Fällen des § 31, in denen die gebotene steuerliche Freistellung eines Einkommensbetrags in Höhe des Existenzminimums eines Kindes durch das Kindergeld nicht in vollem Umfang bewirkt wird, bleiben bei der Anwendung der Sätze 2 und 3 Freibeträge nach § 32 Absatz 6 und zu verrechnendes Kindergeld außer Ansatz.')
q('RENT','estg-37',3,'Negative Einkünfte aus der Vermietung oder Verpachtung eines Gebäudes im Sinne des § 21 Absatz 1 Satz 1 Nummer 1 werden bei der Festsetzung der Vorauszahlungen nur für Kalenderjahre berücksichtigt, die nach der Anschaffung oder Fertigstellung dieses Gebäudes beginnen. 9Wird ein Gebäude vor dem Kalenderjahr seiner Fertigstellung angeschafft, tritt an die Stelle der Anschaffung die Fertigstellung. 10Satz 8 gilt nicht für negative Einkünfte aus der Vermietung oder Verpachtung eines Gebäudes, für das Sonderabschreibungen nach § 7b dieses Gesetzes oder erhöhte Absetzungen nach den §§ 14a, 14c oder 14d des Berlinförderungsgesetzes in Anspruch genommen werden. 11Satz 8 gilt für negative Einkünfte aus der Vermietung oder Verpachtung eines anderen Vermögensgegenstands im Sinne des § 21 Absatz 1 Satz 1 Nummer 1 bis 3 entsprechend mit der Maßgabe, dass an die Stelle der Anschaffung oder Fertigstellung die Aufnahme der Nutzung durch den Steuerpflichtigen tritt.')
q('LATER','estg-37',4);q('MIN','estg-37',5)
q('SOLI_BASE','solzg-3',1,'soweit Vorauszahlungen zur Einkommensteuer oder Körperschaftsteuer zu leisten sind: nach den Vorauszahlungen auf die Steuer für Veranlagungszeiträume ab 2002;')
q('SOLI_LIMIT','solzg-3',4);q('SOLI_RATE','solzg-4',1);q('SOLI_YEAR','solzg-6',27)
q('CHURCH_PRE','estg-51a',9);q('CHURCH_STATE','estg-51a',11)
q('CHURCH_RATE','bmf-steuern-a-z',2967,'             je nach Bundesland 8 oder 9 Prozent.')
q('CHURCH_SPECIAL','estg-10',1,'4. gezahlte Kirchensteuer; dies gilt nicht, soweit die Kirchensteuer als Zuschlag zur Kapitalertragsteuer oder als Zuschlag auf die nach dem gesonderten Tarif des § 32d Absatz 1 ermittelte Einkommensteuer gezahlt wurde;')
q('CREDIT','estg-36',2,'Auf die Einkommensteuer werden angerechnet: 1. die für den Veranlagungszeitraum entrichteten Einkommensteuer-Vorauszahlungen (§ 37); 2. die durch Steuerabzug erhobene Einkommensteuer')
q('BALANCE','estg-36',4)
q('NOT_EXPENSE','estg-12',1,'3. die Steuern vom Einkommen und sonstige Personensteuern sowie die Umsatzsteuer für Umsätze, die Entnahmen sind, und die Vorsteuerbeträge auf Aufwendungen, für die das Abzugsverbot der Nummer 1 oder des § 4 Absatz 5 Satz 1 Nummer 1 bis 5, 7 oder Absatz 7 gilt; das gilt auch für die auf diese Steuern entfallenden Nebenleistungen;')
q('ANCILLARY','ao-3',4,'4. Zinsen nach den §§ 233 bis 237 sowie Zinsen nach den Steuergesetzen, auf die die §§ 238 und 239 anzuwenden sind, sowie Zinsen, die über die §§ 233 bis 237 und die Steuergesetze hinaus nach dem Recht der Europäischen Union auf zu erstattende Steuern zu leisten sind, 5. Säumniszuschläge nach § 240,')
q('WEEKENDS','ao-108',3);q('PAYMENT','ao-224',2);q('CHANGE','ao-164',1);q('APPLY','ao-164',2);q('VALID','ao-124',2)
q('REGISTER','ao-138',3);q('REGISTER_MONTH','ao-138',7)
q('LATE','ao-240',1);q('LATE_ANCILLARY','ao-240',2);q('GRACE','ao-240',3)
q('INTEREST_SCOPE','ao-233a',1);q('INTEREST_PERIOD','ao-233a',2);q('INTEREST_BASE','ao-233a',4);q('VOLUNTARY','ao-233a',9)
q('INTEREST_RATE','ao-238',2);q('FULL_MONTH','ao-238',1);q('ROUND','ao-238',5)
q('HIST_2019','egao-97-36',2);q('HIST_2020_2024','egao-97-36',3);q('OLD_ADJUST','estg-52',64)
q('FALSE','ao-370',1);q('ATTEMPT','ao-370',2);q('DEFERRAL','ao-222',1);q('DEF_INTEREST','ao-234',1);q('DEF_CREDIT','ao-234',3)
q('PERSON','estg-1',1,'Natürliche Personen, die im Inland einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, sind unbeschränkt einkommensteuerpflichtig.')
q('PARTNERS','estg-15',1,'die Gewinnanteile der Gesellschafter einer Offenen Handelsgesellschaft, einer Kommanditgesellschaft und einer anderen Gesellschaft, bei der der Gesellschafter als Unternehmer (Mitunternehmer) des Betriebs anzusehen ist,')
# One form-name observation is intentionally narrower than a live filing/2026 form-method claim.
A['ELSTER']={'id':'ELSTER','source':'live official webpage','act_article':'ELSTER published form name','url':'https://www.elster.de/eportal/formulare-leistungen/alleformulare/eingvorauszlg','exact_quote':'Antrag auf Anpassung von Vorauszahlungen','read_on':'2026-10-29','scope':'Actually opened rendered page title/heading. No authenticated form completion, version selection or source-body download asserted.'}
A['MUNICIPAL']={'id':'MUNICIPAL','source':'live official webpage','act_article':'GewStG §1','url':'https://www.gesetze-im-internet.de/gewstg/__1.html','exact_quote':'Die Gemeinden erheben eine Gewerbesteuer als Gemeindesteuer.','read_on':'2026-10-29','scope':'Actually opened official provision, exact displayed sentence; no new raw HTML acquisition claim.'}
# Finite map; every substantive current paragraph/table row receives its own line and explicit classification.
M={21:['NOTICE','BASE','INTEREST_SCOPE','LATE'],25:['DATES','PERSON'],26:['NOTICE'],27:['ARISE'],28:['PERSON','PARTNERS','MUNICIPAL'],34:['DATES'],35:['MIN'],36:['MIN'],37:['MIN'],38:['MIN','LATER'],39:['SMALL'],40:['ADJUST'],41:['SOLI_LIMIT'],42:['SOLI_LIMIT'],43:['SOLI_RATE'],44:['SOLI_RATE'],45:['CHURCH_RATE','CHURCH_STATE'],46:['LATE'],47:['GRACE','PAYMENT'],48:['INTEREST_RATE','FULL_MONTH','ROUND'],49:['INTEREST_PERIOD','HIST_2019','HIST_2020_2024'],50:['REGISTER_MONTH'],52:['SOLI_YEAR'],56:['BASE','ADJUST'],58:['SMALL','CHURCH_SPECIAL'],60:['IGNORE','CHILD'],62:['RENT'],64:['SOLI_BASE','SOLI_LIMIT','SOLI_RATE','CHURCH_PRE'],66:['NOTICE'],68:['CREDIT','BALANCE'],70:['NOT_EXPENSE','ANCILLARY','CHURCH_SPECIAL'],74:['DATES','WEEKENDS'],75:['PAYMENT'],76:['LATER'],77:['CHANGE','APPLY','ADJUST','VALID','ELSTER'],78:['ADJUST','OLD_ADJUST'],79:['REGISTER','REGISTER_MONTH','ADJUST'],83:['LATE','GRACE','LATE_ANCILLARY','CHURCH_PRE'],84:['INTEREST_SCOPE','INTEREST_PERIOD','HIST_2019','HIST_2020_2024','INTEREST_BASE','VOLUNTARY','INTEREST_RATE','ROUND'],85:['LATE','FULL_MONTH'],86:['NOTICE','INTEREST_SCOPE','INTEREST_PERIOD'],87:['FALSE','ATTEMPT','CHANGE'],88:['DEFERRAL','DEF_INTEREST','FULL_MONTH','INTEREST_RATE','DEF_CREDIT'],92:['DATES'],93:['ADJUST'],94:['PAYMENT'],98:['BASE','MIN','SOLI_LIMIT','SOLI_RATE','CHURCH_RATE','CHURCH_PRE']}
rows=[];sec='metadata';inside=False;case=0
for n,l in enumerate(body.split('\n'),1):
 if n==1:continue
 if n<17:
  if l.startswith('description:'):rows.append({'LF':n,'section':'description','wording':l,'anchors':['DATES','MIN','SMALL','ADJUST','SOLI_LIMIT','SOLI_RATE','LATE','INTEREST_RATE'],'kind':'Scope/figure summary; each distinct rule is mapped again at its operative body row'})
  continue
 if '<!-- openaccountants-cta-block -->'in l:break
 if l.startswith('#'):sec=l.lstrip('# ');continue
 if l.startswith('```oa-check'):inside=True;case+=1;continue
 if l.startswith('```'):inside=False;continue
 if not l.strip():continue
 z={'LF':n,'section':sec,'wording':l,'anchors':M.get(n,[]),'kind':''}
 if inside:z['kind']='Declared fictional executable case '+str(case)+' input/formula/output; verified in writer-arithmetic.json'
 elif sec=='Sources':z['kind']='Source provenance or precise Not-yet-confirmed boundary, not a supplied additional entitlement'
 elif sec=='Ask the client first':z['kind']='Decision-changing intake; no additional tax rule'
 elif l.startswith('>')or l.startswith('The 30-day month'):z['kind']='Reference/assumption boundary; the calendar-month caveat prevents applying the executable shortcut generally'
 elif l.startswith('|---')or l.startswith('| Item |')or l.startswith('| Case |'):z['kind']='Presentation/table header'
 elif l.startswith('**Five further'):z['kind']='Preserved earlier qualitative-case presentation; legal anchors are in each actual row below'
 elif l.startswith('| Notice-based'):z['anchors']=['DATES','NOTICE'];z['kind']='Preserved qualitative case'
 elif l.startswith('| Below the minimum'):z['anchors']=['MIN'];z['kind']='Preserved qualitative case'
 elif l.startswith('| Late Q2'):z['anchors']=['LATE','GRACE'];z['kind']='Preserved qualitative calendar-date case; June10→July15 has two started months'
 elif l.startswith('| Solidarity exemption'):z['anchors']=['SOLI_LIMIT'];z['kind']='Preserved qualitative case; assessed flat-rate-tax exclusion explicit'
 elif l.startswith('| Bank line'):z['anchors']=['NOT_EXPENSE','CHURCH_SPECIAL','NOTICE'];z['kind']='Stipulated notice-confirmed qualitative case, not evidence of a universal bank-reference convention'
 elif l.startswith('**Example 2:'):z['anchors']=['SOLI_LIMIT','SOLI_RATE','LATE'];z['kind']='Original fictional worked case2; independently recomputed by writer arithmetic, not statutory client inputs'
 elif z['anchors']:z['kind']='Source-bound rule/figure; exact selected quotations below'
 else:z['kind']='UNCLASSIFIED'
 rows.append(z)
assert not [z for z in rows if z['kind']=='UNCLASSIFIED'],[(z['LF'],z['wording'][:100])for z in rows if z['kind']=='UNCLASSIFIED']
# Track every earlier nonblank body unit, including the legacy source/workflow topics.
current_lines=body.split('\n')
def find(text):
 x=[i for i,l in enumerate(current_lines,1)if text in l];assert x,text;return x[0]
def dst(label,text):return label+'; current LF'+str(find(text))
D={'scope':dst('Scope and notice authority','"Estimated tax" is a US phrase.'),'dates':dst('Rates/date method','| Due dates |'),'inputs':dst('Ask the client first','1. Do you have a current Vorauszahlungsbescheid?'),'notice':dst('Notice/legal payment authority','- **Only once a notice sets them.'),'base':dst('Taxable base','**The starting figure.'),'min':dst('Minimums and below-threshold case','| Minimum yearly total'),'rental':dst('Rental-loss timing','**Rental losses on a new building.'),'surcharges':dst('Surcharge base/mitigation/church route','**Surcharges.'),'late':dst('Penalties and payment day','- **Late payment surcharge**'),'interest':dst('Interest method and dated exceptions','- **Interest after assessment**'),'adjust':dst('Changing the amount','- **Changing the amount.'),'settle':dst('Year-end credit/balance/refund','**Year-end settlement.'),'expense':dst('Income taxes and ancillary charges not deductible','**Prepayments are not a business expense.'),'new':dst('New-business registration','- **New business.'),'cross':dst('Cross-border/referral scope','- Non-residents with German income'),'deferral':dst('Deferral conditions and own interest','- **A client who cannot pay.'),'bank':'Not yet confirmed: current Sources reservation explicitly retains bank-pattern/timing-library uncertainty; no probabilistic pattern or window is promoted to law. The one stipulated notice-confirmed old case is restored at current LF'+str(find('| Bank line')),'cases':dst('Five earlier qualitative scenarios restored, plus two existing executable cases','**Five further qualitative cases.'),'sources':dst('Sources table and complete retained predecessor source list','## Sources'),'false':dst('False-fact reduction application risk','- **False facts in a reduction application.'),'notconfirmed':dst('Precise retained source/specialist boundaries','Not yet confirmed:')}
old=[]
for name,ref in [('pre-refresh-original.md','aec314e7^ before PR873'),('reviewed-restoration.md','427f3162 local review branch before merged PR883')]:
 text=(b/name).read_text();sect='';meta=True
 for n,l in enumerate(text.split('\n'),1):
  if n==1:continue
  if meta:
   if l=='---':meta=False
   continue
  if '<!-- openaccountants-cta-block -->'in l:break
  if l.startswith('#'):sect=l.lstrip('# ')
  if not l.strip():continue
  exact=next((i for i,v in enumerate(current_lines,1)if v==l),None)
  if exact:dest='Exact current wording retained, LF'+str(exact);kind='carried'
  else:
   s=sect.lower();t=l.lower();k='scope'
   if 'source' in s:k='sources'
   elif 'pattern' in s or 'timing-based' in s or 'prepayment references' in s or s.startswith('3.'):k='bank'
   elif 'worked example' in s or s.startswith('example')or s.startswith('test')or 'test suite'in s:k='cases'
   elif 'required input'in s or 'self-check'in s:k='inputs'
   elif 'refusal'in s or 'refuse'in s:k='cross'
   elif 'minimum'in s:k='min'
   elif 'weekend'in s:k='dates'
   elif 'adjustment window'in s:k='adjust'
   elif 'year-end'in s:k='settle'
   elif 'solidarity'in s or 'church tax on' in s:k='surcharges'
   elif '5.1' in s:k='base'
   elif '6.1' in s or '6.2' in s:k='late'
   elif '6.3' in s:k='interest'
   elif '7.3' in s:k='false'
   elif '7.1' in s or '7.2' in s or 'requesting adjustments'in s:k='adjust'
   elif '8: edge' in s:
    k='new' if any(v in t for v in ['first year','questionnaire','founder'])else 'surcharges' if any(v in t for v in ['church','married','splitting'])else 'base' if any(v in t for v in ['§ 35','wages','investment'])else 'adjust' if 'one-off'in t else 'notice'
   elif 'prohibition'in s:
    k='false' if ('facts' in t or 'untrue' in t) else 'late' if ('grace' in t or 'surcharge' in t) else 'surcharges' if ('church' in t or 'solidarity' in t) else 'min' if 'minimum' in t else 'adjust' if ('reducing' in t or 'pay less' in t) else 'cross' if ('vat' in t or 'gewerbe' in t) else 'notice'
   elif 'method, step'in s:
    k='new'if'new business'in t else 'dates'if'diary'in t else 'surcharges'if'church tax'in t else 'adjust'if'change'in t else 'late'if'late'in t else 'settle'if'after the year'in t else 'notice'
   elif 'deadline'in s:k='dates'
   elif 'taxable base'in s:
    k='expense'if'not a business expense'in t else 'settle'if'year-end'in t else 'surcharges'if'surcharge'in t else 'rental'if'rental'in t else 'base'
   elif 'penalties'in s:
    k='deferral'if'defer'in t or'deferral'in t else 'false'if'false facts'in t else 'interest'if'interest'in t else 'late'
   elif 'cross-border'in s:k='cross'
   elif 'ask the client'in s:k='inputs'
   elif 'quick reference'in s:k='dates' if ('date' in t or '10 mar' in t or 'payment schedule' in t) else 'base' if ('computation basis' in t) else 'late' if 'grace' in t else 'notice' if 'amount' in t else 'scope'
   elif 'conservative defaults'in s:k='notice'
   dest=D[k];kind='Not yet confirmed'if k=='bank'else'carried / regrouped'
   if '16 for 2024'in l:dest=D['interest']+'; DE-L08 corrects17months under number7(d), preserves mistaken old16 wording in this comparator';kind='source-corrected'
   if 'no upper end' in t:dest=D['surcharges']+'; upper ends are explicitly derived from the source formula, not printed statutory thresholds';kind='source-derived successor'
  old.append({'comparator':ref,'file':name,'old_LF':n,'old_section':sect,'exact_old_topic':l,'destination':dest,'status':kind})
# Do not accidentally label a recovered historical file an object in the current public repository.
scopes={'estg-37':[[1,7]],'solzg-3':[[1,8]],'solzg-4':[[1,2]],'solzg-6':[[27,27]],'estg-51a':[[1,12]],'estg-36':[[1,2],[4,4]],'estg-12':[[1,2]],'estg-10':[[1,1]],'ao-3':[[4,4]],'ao-108':[[1,1],[3,3]],'ao-124':[[1,2]],'ao-138':[[3,3],[7,7]],'ao-164':[[1,2]],'ao-222':[[1,1]],'ao-224':[[2,2]],'ao-234':[[1,1],[3,3]],'ao-238':[[1,6]],'ao-240':[[1,3]],'ao-370':[[1,2]],'ao-233a':[[1,10]],'egao-97-36':[[1,3]],'estg-52':[[64,64]],'bmf-steuern-a-z':[[2,2],[2944,2967],[5205,5205],[5238,5238]],'estg-1':[[1,1]],'estg-15':[[1,1]]}
for key,z in I.items():assert sha((b/z['raw']).read_bytes())==z['raw_sha256'];assert sha((b/z['reader']).read_bytes())==z['reader_sha256']
# Exact arithmetic, conditional boundaries, dates and original cases; no new tests of application code.
from fractions import Fraction as F
from datetime import date
controls=[{'case':'original1','base':9600-1200,'per_date':(9600-1200)//4,'soli':0,'church':str(F(8400)*F(9,100))},{'case':'original2','full':str(F(22000)*F(55,1000)),'mitigation':str(F(22000-20350)*F(119,1000)),'rounded_overdue':5549//50*50,'surcharge':5549//50*50*2//100},{'case':'mitigation crossing single','exact_base':str(F(119,1000)*20350/(F(119,1000)-F(55,1000))),'display':'37838.28, rounded display of algebraic crossing; not statutory breakpoint'},{'case':'mitigation crossing joint','exact_base':str(F(119,1000)*40700/(F(119,1000)-F(55,1000))),'display':'75676.56, rounded display of algebraic crossing; not statutory breakpoint'},{'case':'2026 due weekdays','dates':[{ 'date':date(2026,m,10).isoformat(),'weekday':date(2026,m,10).strftime('%A')}for m in [3,6,9,12]]},{'case':'legacy June10 to July15','days':(date(2026,7,15)-date(2026,6,10)).days,'started_calendar_months':2,'exceeds_grace':True},{'case':'minimums','400_per100':'both inclusive tests pass','399_annual':'fails annual','99_per_due':'fails per-date'},{'case':'DE-L08 transition','2024_months':17,'2024_interest_start':'2026-06-01','2026_months':15,'2026_interest_start':'2028-04-01'},{'case':'five old scenarios','count':5,'derived_or_qualitative':True,'bank_case':'notice-confirmed stipulated transaction only; old date windows remain unconfirmed'}]
for n,x in [('current-rule-rows.json',rows),('source-quotes.json',list(A.values())),('actual-read-scopes.json',scopes),('old-topics.json',old),('writer-arithmetic.json',controls)]: (b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
# Preserve both completed reviews unchanged; the precise transition erratum is adjacent.
for f in ['DE-est-rev.md','restore-rev.md']:
 shutil.copyfile(root/'output/europe-closeout-2026-10-27/germany-existing-evidence-reconciliation-2026-10-28/preserved-review-reports'/f,b/f)
shutil.copyfile(p,b/'current-guide-final.md')
def esc(v):return str(v).replace('|','\\|').replace('\n','<br>')
out=['# Figure/rule ledger: de-estimated-tax','',f'Writer ledger only, read29October2026. Current Guide SHA256 `{sha(p.read_bytes())}`, main baseline62b7639a. No independent country verdict. Historical completed reviews are preserved unchanged, with the precise DE-L08 transition-period erratum. Existing two executable cases are byte exact, and all five pre-refresh qualitative scenarios are restored. Derived case amounts and algebraic crossings are explicitly distinguished from statutory figures.','','| Current native LF | Section | Exact current wording | Act/article and official URL | Exact selected original-language quote / explicit classification | Read date |','|---|---|---|---|---|---|']
for z in rows:
 anchors=[A[k]for k in z['anchors']];out.append('| '+' | '.join(esc(v)for v in [z['LF'],z['section'],z['wording'],'<br>'.join(x['act_article']+' '+x['url']for x in anchors)or'—','<br>'.join(x['exact_quote']for x in anchors)or z['kind'],'2026-10-29'if anchors else'—'])+' |')
out+=['','## Complete old-topic destinations','','Actual pre-refresh aec314e7 parent and the recovered local427f3162 review-branch body are retained once. The latter object lives in Downloads/oa-f1-wt/wt-rev-903; absence in the public checkout was recorded honestly, then exact a8d6d3b9 SHA256 was verified in its proper repository. Every nonblank pre-CTA body unit, including source and workflow topics, is mapped below. Bank patterns and timing windows remain explicitly unconfirmed rather than being promoted to law.','','| Comparator / LF | Exact old topic | Destination | Status |','|---|---|---|---|']
for z in old:out.append('| '+' | '.join(esc(v)for v in [z['comparator']+':'+str(z['old_LF']),z['exact_old_topic'],z['destination'],z['status']])+' |')
out+=['','## Read scopes and limits','','All50 retained-body quotation strings are exact members of pinned derived readers; raw bodies are unchanged. The two live official-page observations (form name and municipal taxing authority) are expressly labelled as rendered observations, without a raw-body or reader-hash claim. Native LF uses literal newline splitting. Full-source acquisition is not reading: actual selected ranges are in actual-read-scopes.json. The BMF booklet is explicitly2025, so the Guide’s precise2026 state-rate reservation remains. The ELSTER page was opened only to confirm the published form name; no authenticated filing or2026 form-method claim. A mid-year notice’s Soli-limit application remains unconfirmed. No bank pattern library, founders-portal advice, taxpayer notice, authority enquiry or live filing has been verified.','']
(b/'de-estimated-tax.md').write_text('\n'.join(out))
checks={'guide_sha256':sha(p.read_bytes()),'ledger_sha256':sha((b/'de-estimated-tax.md').read_bytes()),'current_units':len(rows),'quote_anchors':len(A),'source_artifacts':len(I),'old_topic_units':len(old),'unclassified':[],'retained_reader_quote_anchors':50,'official_web_observations':2,'quotes_exact':'50 retained-reader strings checked;2 official rendered observations explicitly distinguished','raw_reader_hashes_pass':True,'Guide_body_changed':'DE-L08 one dated interest correction plus DE-L10 five original qualitative scenarios restored; evidence retained','independent_review':'pending, not writer PASS'}
(b/'writer-checks.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks))
