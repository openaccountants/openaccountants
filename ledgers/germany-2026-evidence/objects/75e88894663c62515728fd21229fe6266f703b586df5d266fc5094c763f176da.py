from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent;O=P.parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29'
h=lambda b:hashlib.sha256(b).hexdigest()
def dump(p,o):p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
quotes={}
def aq(id,source,lo,hi,article,qualification='Legislative text, own selected reading on 2026-10-29'):
 x=json.loads((A/'sources'/f'{source}.identity.json').read_text());lines=Path(x['reader_path']).read_text().split('\n');q={**x,'id':id,'article':article,'native_LF':[lo,hi],'exact_quote':'\n'.join(lines[lo-1:hi]),'read_on':'2026-10-29','qualification':qualification};assert h(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert h(Path(x['reader_path']).read_bytes())==x['reader_sha256'];quotes[id]=q
# Each selected full clause was actually read before this script's execution.
aq('R01.business-car','U7059a8b10a1f492b',26,27,'EStG § 4(5) sentence 1 no. 6')
aq('R01.allowance','U5d05d24ddb446c3d',13,14,'EStG § 9(1) sentence 3 no. 4')
aq('R02.meal-incorporation','U7059a8b10a1f492b',24,25,'EStG § 4(5) sentence 1 no. 5')
aq('R02.meals','U5d05d24ddb446c3d',38,48,'EStG § 9(4a) sentences 1–11')
aq('R03.soli-children','Uc748242e6e54c746',27,27,'SolzG § 3(2)')
aq('R03.employee-expense','U5d05d24ddb446c3d',7,7,'EStG § 9(1) opening')
aq('R03.special-JAEG','Ubbd69a1741987610',7,8,'SVBezGrV 2026 § 2(1)–(2)','Own exact regulation amounts; special JAEG alone is NOT the contribution-ceiling incorporation. BMG actual 2026 application separately quoted.')
aq('R03.current223-boundary','Uc9fb465ba767d198',7,10,'SGB V § 223(1)–(4), current replacement','Own current text, whose paragraph 4 expressly addresses 2027. Not quoted as the old operative 2026 incorporation or silently assigned a deferred commencement.')
aq('R04.crossborder-mandatory','Ucb9a939517193e9c',32,36,'EStG § 46(2) no. 7')
for name,lo,hi in [('BMG-health-2026',379,380),('BMG-care-2026',435,436)]:
 x=json.loads((P/'sources'/f'{name}.identity.json').read_text());q={**x,'id':'R03.'+name,'article':'BMG: published 2026 health/care contribution-ceiling guidance','native_LF':[lo,hi],'exact_quote':'\n'.join(Path(x['reader_path']).read_text().split('\n')[lo-1:hi]),'read_on':'2026-10-29','qualification':'Explicit official administrative 2026 application, not a statutory quotation. Supports the existing €69,750 annual / €5,812.50 monthly contribution ceiling independently of a bare special-JAEG reference.'};quotes[q['id']]=q
p=P/'sources/BStabG2026.txt';receipt=json.loads((P/'sources/BStabG2026.receipt.json').read_text())
for id,lo,hi,art in [('R03.amend223',1782,1789,'BGBl. I 2026 no. 228, Article 1 no. 61'),('R03.commencement',2703,2714,'Same, Article 8(1)–(4)')]:
 quotes[id]={'id':id,'article':art,'url':receipt['url'],'raw_path':str(P/'sources/BStabG2026.pdf'),'raw_sha256':receipt['sha256'],'reader_path':str(p),'reader_sha256':h(p.read_bytes()),'native_LF':[lo,hi],'exact_quote':'\n'.join(p.read_text().split('\n')[lo-1:hi]),'read_on':'2026-10-29','qualification':'Actual enacted text. No. 61 is not among Article 8 deferred items: general commencement applies. New paragraph 4 expressly sets 2027; it is not promoted into an express 2026 incorporation.'}
dump(P/'own-actual-read-quotes.json',quotes)
(P/'options-and-selection.md').write_text('''# DE-R01–04: sourced options before editing, 29 October 2026

Root has selected Option A for all four findings. These are writer corrections, pending different independent review. Exact own selected source wording, original URLs, raw/reader hashes and native LF are in own-actual-read-quotes.json. The original country freeze and A/B writer seals remain untouched.

- **DE-R01 Option A (selected):** add the ordinary combustion business-car home-to-premises positive-difference formula and actual/logbook alternative to all three PIT routes, plus a €40,000 / 20 km / 12 month / 200 day separating worksheet and the required intake facts. Own EStG § 4(5) no. 6 (native 26–27) and § 9(1) no. 4 (13–14) establish it. Keep separate private-use adjustment, private-car rule and EV referral. **Option B:** explicitly reserve business-car commuting until a genuinely supplied sibling formula exists; the old bookkeeping referral alone supplies none.
- **DE-R02 Option A (selected):** condition the €14 arrival/departure branch on an overnight away from home on that, preceding or following day, keeping independent non-overnight >8h and €28 full-24h branches. Own § 9(4a), 38–48; own business incorporation § 4(5) no. 5, 24–25. Align the fuller freelancer's short 'nothing for eight hours or less' sentence to its already-correct overnight table, so it does not contradict that table. **Option B:** remove the unqualified short arrival/departure phrase and route to the fuller supplied overnight rule.
- **DE-R03 Option A (selected):** evidence successor only for the unchanged child/Soli and employment-cost claims: full own SolzG § 3(2) and EStG § 9(1) opening. Replace special-JAEG-alone support for the health/care ceiling with explicit current BMG 2026 contribution-ceiling application, retaining regulation amount and honestly separating the enacted July replacement and its 2027 text. No numerical Guide change. **Option B:** reserve precisely the unbridged application limb rather than call a special JAEG quotation itself a contribution-ceiling rule. BMG directly confirms both actual 2026 ceilings, so B is unnecessary.
- **DE-R04 Option A (selected):** voluntary filing only when no statutory mandatory assessment applies; replace stale no-method statements with the actual part-year and Swiss-commuter sibling routes, preserving their source limitations. Own § 46(2) no. 7 and actual named sibling scopes. **Option B:** remove obsolete availability claims and state the common mandatory table is not exhaustive, retaining direct scoped referrals.

BMG health actual native 379–380 and care 435–436 expressly state the 2026 ceiling. The enacted § 223 change is Article 1 no. 61, not a deferred Article 8(2) item. This evidence does not fabricate a delayed commencement or a verbatim current-law 2026 cross-reference. The worksheet amount is supported by the ministry's express current 2026 administrative application. No amount conflict found.
''')
# Exact intended operations are prepared before applying any Guide edit.
ops={}
car='''**Business-car commuting adjustment, ordinary combustion car.** In addition to the separate private-use add-back, § 4(5) no. 6 EStG disallows `max(0, D − A)` for travel between home and the business premises. Under the list-price method, `D = 0.0003 × domestic list price at first registration × full one-way kilometres × calendar months`. `A` is the statutory commuting allowance: for this ordinary car case, `EUR 0.38 × full one-way kilometres × actual commuting days`, applying the § 9(1) no. 4 distance and benefit-reduction conditions. When private use is valued under § 6(1) no. 4 sentence 1 or 3, including the logbook method, use the actual documented costs of these commuting trips as `D` instead. Electric/hybrid reductions and family-home trips need their separate rules.

For a stipulated ordinary car with a EUR 40,000 list price, 20 full km, 12 months and 200 commuting days, `D = 2,880`, `A = 1,520`, and the extra nondeductible amount is EUR 1,360. With actual/logbook commuting costs of EUR 1,000 the extra amount is zero; with EUR 2,000 it is EUR 480. These amounts are separate from the private-use add-back.'''
for slug in ['de-income-tax','de-self-employed-income-tax','de-einkommensteuer-freelancer','de-employee-income-tax']:
 text=(P/'before'/f'{slug}.md').read_text();o=[]
 def add(old,new,why):
  assert text.count(old)==1,(slug,why,text.count(old));o.append({'old':old,'new':new,'reason':why})
 ver=re.search(r'^version: (.+)$',text,re.M).group(1);versions={'de-income-tax':'2.6','de-self-employed-income-tax':'2.5','de-einkommensteuer-freelancer':'1.5','de-employee-income-tax':'0.3'};add('version: '+ver,'version: '+versions[slug],'Monotonic content version; date remains 2026-10-29')
 if slug!='de-employee-income-tax':
  if slug!='de-einkommensteuer-freelancer':
   old=next(l for l in text.split('\n') if l.startswith('**Cars.**'))
   new=old.replace('Trips from home to the own office count only at EUR 0.38 per km one way.','Home-to-premises travel uses the commuting allowance and, for a business car, the additional adjustment below.')+'\n\n'+car
   add(old,new,'DE-R01 positive ordinary business-car method and separating cases')
   add('EUR 28 for a full day away; EUR 14 for arrival, departure, or more than 8 hours away','EUR 28 for a full 24-hour day away; EUR 14 for arrival/departure if an overnight away from home occurs on that, preceding or following day, or for a non-overnight day more than 8 hours away','DE-R02 overnight gate, independent >8h branch, preserved EUR28')
   add('4. Car: business asset or private, business-use share, and logbook or 1% method.','4. Car: business asset or private, business-use share, logbook or 1% method, domestic list price at first registration, months used, full one-way distance, actual commuting days and attributable actual costs if using actual/logbook valuation.','DE-R01 calculation inputs')
  else:
   old=next(l for l in text.split('\n') if l.startswith('- **Commuting**'))
   new='- **Commuting** to one\'s own premises uses the employee allowance rules of § 9 EStG through § 4(5) no. 6: EUR 0.38 from the first full kilometre, one way, not for flights. Apply the business-car adjustment below; the private-use amount is separate. The existing `germany-bookkeeping` record-keeping route does not replace this computation.\n\n'+car
   add(old,new,'DE-R01 complete calculation replaces unsupported method referral; old bookkeeping destination retained')
   add('flat amounts only; nothing for eight hours or less;','flat amounts only; for a day without an overnight, nothing for eight hours or less. The EUR 14 arrival/departure branch instead requires an overnight away from home on that, preceding or following day;','DE-R02 align prose with existing qualifying overnight table')
   add('- Prepayments set? A loss carried from earlier years?','- Car method, business-use share, domestic list price at first registration, calendar months, full one-way distance and commuting days? For actual/logbook valuation, the costs attributable to those trips?\n- Prepayments set? A loss carried from earlier years?','DE-R01 calculation inputs')
  marker='| Source | URL | Read on |';pos=text.index(marker);# append to the real Sources table at its first blank boundary
  end=text.index('\n\n',pos)
  addition='\n| EStG § 4(5) nos. 5–6 (business-car commuting adjustment and meal incorporation), selected operative clauses read | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-29 |\n| EStG § 9(1) no. 4 and (4a) (distance allowance and qualifying meal branches), selected clauses read | https://www.gesetze-im-internet.de/estg/__9.html | 2026-10-29 |'
  add(text[pos:end],text[pos:end]+addition,'DE-R01/02 scoped source read dates; original table rows/URLs retained')
 else:
  add('In every other case filing is voluntary:','If no statutory mandatory-assessment case applies under § 46(2) EStG, filing is voluntary:','DE-R04 full statutory mandatory boundary, not only common-case table')
  add('Months of limited liability and German-exempt foreign income are handled under § 2(7) and § 32b EStG; the pack has no method yet.','Use `de-partners-and-part-year` for the residence-period base, German-source income of the other period and progression computation under § 2(7) and § 32b EStG, within that Guide\'s stated conditions and source limits.','DE-R04 actual part-year sibling method route')
  add('Swiss cross-border commuters: refuse here. The commuter case belongs in germany-to-switzerland-cross-border-tax, which does not yet have its commuter part.','For Swiss cross-border commuters, use `germany-to-switzerland-cross-border-tax`: its commuter-status tests and German assessment method are supplied, with the stated home-office, working-day denominator, implementing-text and currency-conversion reservations.','DE-R04 actual Swiss method and precise retained reservations')
 ops[slug]=o

dump(P/'exact-operations.json',ops)
print('Prepared own source quotations, two options per finding, selected A record and operations. No Guide edited by preparation.')
