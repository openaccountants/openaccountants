from pathlib import Path
import json,hashlib,re,difflib,copy
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27');W=O/'germany-DE-R62-R70-payroll-writer-successor-2026-10-29';C=O/'germany-ledger-independent-review-2026-10-29';A=O/'germany-ledger-writer-2026-10-28';B=O/'germany-ledger-writer-B-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');W.mkdir(exist_ok=True);[(W/x).mkdir(exist_ok=True)for x in ['before','after','ledgers','support']];H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');x=json.loads((C/'DE-R62-R70-payroll-selected-source-read-ledger.json').read_text());qs={}
for r in x['records']:
 if 'quote'not in r:continue
 q=copy.deepcopy(r['quote']);i={k:r[k]for k in ['raw_path','raw_sha256','reader_path','reader_sha256']};assert H(Path(i['raw_path']))==i['raw_sha256']and H(Path(i['reader_path']))==i['reader_sha256'];a,b=q['LF_start'],q['LF_end'];assert q['exact_quote']in'\n'.join(Path(i['reader_path']).read_text().split('\n')[a-1:b]);id='R62-70.'+q['id'];qs[id]={**i,**q,'id':id,'native_LF':[a,b],'read_on':'2026-10-29','actual_read_scope':'Own complete selected operative quote actually read; no whole raw-body reading or acquisition-as-reading claim.'}
q=next(q for q in json.loads((A/'support/germany-payroll/actual-read-quotes.json').read_text())if q['id']=='ANNUAL');i=json.loads((A/'sources'/(q['source']+'.identity.json')).read_text());assert q['exact_quote']==Path(i['reader_path']).read_text().split('\n')[6];qs['R69.ANNUAL']={**i,**q,'id':'R69.ANNUAL','native_LF':[7,7],'read_on':'2026-10-29','actual_read_scope':'Own actual full DEUV10(1) paragraph read from nativeLF7.'}
i=x['records'][-1]['source'];ls=Path(i['reader_path']).read_text().split('\n');assert H(Path(i['raw_path']))==i['raw_sha256']and H(Path(i['reader_path']))==i['reader_sha256']
for id,a,b,article in [('R67.BMG-rate',390,402,'BMG explicit2026averageadditionalrate, administrativeguidance'),('R67.BMG-ceiling',379,380,'BMG explicit2026healthcontributionceiling, administrativeguidance')]:qs[id]={**i,'id':id,'article':article,'native_LF':[a,b],'exact_quote':'\n'.join(ls[a-1:b]),'read_on':'2026-10-29','actual_read_scope':'Own entire native375–427 actually read, following previously ceiling-only scoped reading. Administrative guidance; not Bundesanzeiger acquisition or statutory quotation.'}
obs=C/'new-primary-checks/payroll-SGBX26-web-observation.json';o=json.loads(obs.read_text());quote=re.search(r'L13: (.*?)\nL14:',o['result']).group(1);qs['R69.SGBX26']={'id':'R69.SGBX26','article':'SGBX26(3), retained official web-tool observation','url':o['url'],'raw_path':str(obs),'raw_sha256':H(obs),'reader_path':str(obs),'reader_sha256':H(obs),'native_LF':None,'exact_quote':quote,'read_on':'2026-10-29','actual_read_scope':'Own complete retained web-tool response read; operativeparagraphs1–7 at WebL10–19, selected exactWebL13. JSON observation, NOT originalHTML or whole Regulation text. No portal execution.','kind':'retained official web-tool response JSON'}
dump(W/'own-actual-read-quotes.json',qs)
(W/'options-and-selection.md').write_text('''# DE-R62–70: two sourced options and selection

Own exact German operative quotes, official URLs, raw/reader identities and actual29October2026 read scopes are in own-actual-read-quotes.json. Selected-source conditions are read from retained bodies; no acquisition is treated as reading. Current target germany-payroll matches the independent report's native coordinates. Identical already concrete conditions are mirrored only where absent from de-payroll; its correct agricultural15/90, actual F and2027 boundary remain.

| Finding | A selected under standing authority | B viable narrower alternative | Own source |
|---|---|---|---|
| R62 | Qualify deduction-only/three-next-payment defaults by employer nonfault and all three statutory final-sentence exceptions | Limit default explicitly to ordinary cash-pay/no-exception case and refer exact alternatives | SGBIV28g, RECOVER |
| R63 | State U1 bonus and specified≤4week-job exclusions; short-time actual-pay base; no transplant to U2/insolvency | Label shared base only starting point and add same selectors as separate step | AAG7(2), AAGBASE |
| R64 | Split premium up to25hour base/excess; add00–04 Sunday/holiday continuation if begunbeforemidnight | Give up-to25 worksheet plus precise partial-excess route | SvEV1(1)no1/EStG3b, NIGHTSV/NIGHT |
| R65 | Add same-trainer prior internship gate for≤3month accompanying internship; preserve distinct compulsory/orientation branches | Restrict claim to stipulated no-prior-internship facts | MiLoG22, MINEXCEPT |
| R66 | Add agricultural15weeks/90days only to agricultural branch; actual no-fault aggregation decision-date rule | Explicitly exclude these precise branches with actual statutory selectors | SGBIV8(1)/(2), MINI |
| R67 | Use explicit BMG2026 administrative2.9 and ceiling; derive42.3/F fourdecimal rounding, fund-specific rule separate | Preserve prior estimate as history and separately give actual BMG published worksheet | BMG native375–427, not Gazette acquisition; PAP values |
| R68 | Add insolvency/closure/end-all-jobs next-payroll≤6weeks alternative, narrow agricultural exception | State ordinary continuing-employer deadline and same alternative separately | SGBIV28a(2a), UVREPORT |
| R69 | Give16February2026 for ordinary2025annual-report deadline, distinguishing nominal15February and actual authority exceptions | Label15February nominal only and provide next-working-day rule | DEUV10(1)/SGBX26(3), ANNUAL/retained actualwebobservation |
| R70 | Add nonfault illness, contingent-unincurred-expense exclusion and achievable performance-pay average | Limit fixed-pay worksheet to stipulated matching facts and refer actual average branch | EntgFG3/4, SICK/SICKPAY |

Original worked sections/examples, URLs/order, CTA, trust/bylines and protected metadata remain exact. No whole payroll audit, Gazette acquisition, universal U2 exclusion, agricultural flat-tax extension, automatic retroactive insurance or new actual filing claim.
''')
allops={};proofs={}
for s in ['germany-payroll','de-payroll']:
 p=next((R/'skills').rglob(s+'.md'));original=p.read_text();b=original;ops=[]
 def op(old,new,why):
  global b
  assert b.count(old)==1,(s,why,b.count(old));ops.append({'finding':why,'before':old,'after':new});b=b.replace(old,new,1)
 def line(prefix):return next(l for l in b.split('\n')if l.startswith(prefix))
 version='1.0'if s=='germany-payroll'else'1.4';op('version: '+version,'version: '+('1.1'if s=='germany-payroll'else'1.5'),'version')
 recovery='Under § 28g SGB IV the ordinary claim is recovered by deduction from pay. A missed deduction can ordinarily be recovered at the next three payments, and later if the employer was not at fault. The deduction-only and three-payment restrictions do not apply where the employee intentionally or grossly negligently breaches § 28o(1), bears the entire total social contribution, or receives only benefits in kind.'
 if s=='germany-payroll':
  old=line('The employee owes the wage tax;');op(old,old.replace('and recovers the employee\'s share only by deduction from pay','and ordinarily recovers the employee\'s share by deduction from pay, subject to the § 28g exceptions stated below'),'R62')
  old=line('8. **Contributions.**');op(old,old.split(' A missed deduction')[0]+' '+recovery+' ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).','R62')
  old=line('What breaks when the order is wrong:');op(old,old.replace('a missed employee share is lost after three payments','a missed employee deduction cannot ordinarily be recovered after the next three payments unless the employer-nonfault or other § 28g exception above applies'),'R62')
 else:
  old=line('- **Social insurance.**');op(old,old.replace('only by deducting it from pay','ordinarily by deducting it from pay, subject to the § 28g exceptions below'),'R62 mirror')
  old=line('- A missed employee deduction');op(old,'- '+recovery+' ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).','R62 mirror')
  old=line('- **Lost employee share:**');op(old,'- **Missed employee deduction:** recovery after the next three payments requires the employer-nonfault exception or another actual § 28g exception stated above; the employer still owes the whole contribution ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).','R62 mirror')
 prefix='U1, U2 and the insolvency levy'if s=='germany-payroll'else'- U1 applies to employers';old=line(prefix);new=old+' For U1, exclude one-time pay under § 23a SGB IV and pay for employment lasting no longer than four weeks where the nature of the job prevents sickness-pay entitlement under § 3(3) EntgFG. Do not transfer that U1 exclusion to U2 or the insolvency levy. During short-time allowance, AAG levies use actual earned pay up to the pension ceiling (§ 7(2) AAG).';op(old,new,'R63')
 if s=='germany-payroll':
  old=line('| Contribution-free only where');op(old,'| Contribution exemption for an otherwise qualifying tax-free surcharge: applies to the part based on hourly basic pay up to this amount; the excess part remains contributory | EUR 25 | [§ 1(1) no. 1 SvEV](https://www.gesetze-im-internet.de/svev/__1.html) |','R64')
 else:
  old=line('**Tax-free night, Sunday');new=old.replace('They are free of contributions only where the hourly pay they are based on is not above EUR 25','For an otherwise qualifying tax-free surcharge, the part based on hourly basic pay up to EUR 25 is free of contributions; the part based on excess hourly basic pay remains contributory');op(old,new,'R64 mirror')
 # Extend each current premium explanation/table without altering original examples.
 if s=='germany-payroll':
  old=line('| Contribution exemption for an otherwise qualifying');
 else:old=line('**Tax-free night, Sunday')
 addition=' Sunday and holiday work also includes 00:00–04:00 on the following day if the night work began before midnight (§ 3b(3) no. 2 EStG). With EUR 30 hourly basic pay and an otherwise qualifying 25% night premium, EUR 7.50 is tax-free within the EUR 50 tax ceiling; EUR 6.25 is contribution-free and EUR 1.25 remains contributory. Actual work, additional payment and applicable statutory percentage gates still apply.'
 # insert standalone paragraph after table's existing explanation, or append same paragraph in B
 if s=='germany-payroll':
  anchor=line('The two caps differ:');op(anchor,anchor+addition,'R64')
 else:op(old,old+addition,'R64 mirror')
 prefix='Not covered by the minimum wage'if s=='germany-payroll'else'**Minimum wage.**';old=line(prefix);new=old.replace('orientation or study-accompanying internships of up to three months','orientation internships of up to three months and training- or study-accompanying internships of up to three months only if no such prior internship with the same trainer/employer existed');op(old,new,'R65')
 if s=='germany-payroll':
  old=line('- **Short-term jobs.**');op(old,old.replace('three months or 70 working days in a calendar year','three months or 70 working days in a calendar year, or 15 weeks or 90 working days for employment in an agricultural business'),'R66')
 prefix='- **Several jobs.** Several Minijobs'if s=='germany-payroll'else'**Minijob rules.**';old=line(prefix);op(old,old+' If aggregation shows that the minor-employment conditions fail, insurance begins on the day the competent insurance decision is notified under § 8(2) SGB IV, unless the employer intentionally or grossly negligently failed to investigate the facts needed to assess insurance status. This is the specific aggregation rule, not a universal bar on retroactive insurance.','R66')
 if s=='germany-payroll':
  old=line('| Average additional rate for 2026');op(old,'| Average additional rate for 2026, where legally required for the § 242(3) SGB V groups; ordinary payroll uses the employee fund\'s actual rate | 2.9% | [BMG published 2026 contributions guidance](https://www.bundesgesundheitsministerium.de/beitraege/seite); earlier [Finance ministry monthly report](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2026/02/Inhalte/Kapitel-2-Analysen/2-3-sollbericht-2026.html) is an estimate source |','R67')
  old=line('The official notice of the average');op(old,'The retained BMG administrative guidance expressly publishes 2.9% for 2026. Use it where the average rate is legally required; ordinary employees use their fund-specific additional rate. This is an actual current official administrative publication, not a separately retained Federal Gazette announcement. The earlier finance ministry estimate is preserved as history, not the sole current-rate evidence.','R67')
  old=line('| Total contribution rate 2026:');op(old,old.replace('42.3% (check)','42.3%'),'R67');old=line('| Factor F 2026:');op(old,old.replace('0.6619 (check)','0.6619').replace('Derived; the labour ministry publishes it in the Federal Gazette','Derived from 28 / 42.3 = 0.6619385…, rounded to four decimals; § 20(2a) SGB IV requires four-decimal rounding. No separate Gazette acquisition is claimed'),'R67')
  old=line('- [ ] Figures marked "check"');op(old,'- [ ] Apply the employee fund\'s actual additional rate, or the published 2.9% average where legally required; use the sourced four-decimal F and confirm the actual church-tax state selector.','R67')
 old=line('| Health and care ceiling');op(old,old[:-2]+'; [BMG actual 2026 contribution-ceiling guidance](https://www.bundesgesundheitsministerium.de/beitraege/seite) expressly states these amounts; the special-JAEG reference alone is not treated as the whole 2026 contribution-ceiling proof |','R67')
 if s=='germany-payroll':old=line('| Special annual report to accident insurance')
 else:
  # B omitted this whole special-report row: adding the actual own duty is finite sibling route, not changing existing ordinary annual DEUV row.
  old=line('| Annual report for 2026 |')
  op(old,old+'\n| Special annual report to accident insurance for employees insured in 2026 | Ordinarily 16 February 2027; on insolvency, definitive business closure or end of all employment, next payroll and at latest six weeks. The statutory agricultural-BG exception applies only where the work value is not used for contribution calculation | [§ 28a(2a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html) |','R68 mirror');old=None
 if old:op(old,'| Special annual report to accident insurance for everyone employed and insured in 2026 | Ordinarily 16 February 2027 ("zum 16. Februar des Folgejahres"). On insolvency, definitive business closure or end of all employment: next payroll, at latest six weeks. The statutory agricultural-BG exception applies only where the work value is not used for contribution calculation | [§ 28a(2a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html) |','R68')
 if s=='germany-payroll':
  old=line('The 2025 annual report was due');op(old,old.replace('due by 15 February 2026','due by Monday 16 February 2026: nominal 15 February was a Sunday, so § 26(3) SGB X moves the ordinary deadline to the next working day. This does not override an authority notice expressly fixing the day under that provision or an authority-set appointment under § 26(5). The [actual social-procedure rule](https://www.gesetze-im-internet.de/sgb_10/__26.html) supplies this adjustment; AO § 108 is not its authority. '), 'R69')
  # exact connective needs grammar below
  b=b.replace('The 2025 annual report and the 2025 wage tax certificates','The 2025 wage tax certificates') if False else b
 old=line('- **Continued pay in sickness.**')if s=='germany-payroll'else line('**Sick pay and the maternity top-up.**');new=old.replace('Up to six weeks per incapacity','For incapacity due to sickness without employee fault, up to six weeks per incapacity').replace('Continued pay for up to six weeks per incapacity','Continued pay for up to six weeks per incapacity due to sickness without employee fault');new+=' Under § 4(1a) EntgFG, additional overtime pay is excluded, as are expense reimbursements contingent on actual expenses that do not arise during incapacity. For performance-related remuneration, use the average earnings achievable during the employee\'s applicable regular working time.';op(old,new,'R70')
 # Append precise current reading source; retains all old source URLs/date rows.
 old=next(l for l in b.split('\n')if l.startswith('| MiLoG §§'))if s=='de-payroll'else next(l for l in b.split('\n')if 'Read on' in l and l.startswith('| Source')) if False else None
 # Source row follows actual last table row, kept simple at EOF before CTA if present handled by exact insertion at existing BMG row.
 bmglines=[l for l in b.split('\n')if l.startswith('|')and('Federal Health Ministry' in l or'Federal health ministry' in l)]
 if bmglines:
  old=bmglines[-1];op(old,old+'\n| Selected operative recovery, U1, surcharge, internship, aggregation, sickness and report exceptions; actual BMG 2026 rate and ceiling (administrative guidance), read 29 October 2026 | https://www.gesetze-im-internet.de/sgb_4/__28g.html ; https://www.gesetze-im-internet.de/aufag/__7.html ; https://www.bundesgesundheitsministerium.de/beitraege/seite | 2026-10-29 |','actual selected sources')
 (W/'before'/p.name).write_text(original);(W/'after'/p.name).write_text(b);allops[s]=ops
 # Before applying, exact body protection guard.
 origblocks=re.findall(r'```oa-check.*?```',original,re.S);assert origblocks==re.findall(r'```oa-check.*?```',b,re.S)and len(origblocks)==(0 if s=='germany-payroll'else 2)
 heading='## Worked cases'if s=='germany-payroll'else'## Worked examples';a=original.index(heading);z=original.find('\n## ',a+3);aa=b.index(heading);zz=b.find('\n## ',aa+3);assert original[a:z]==b[aa:zz]
 u=lambda t:re.findall(r'https?://[^\s<>|)]+',t);it=iter(u(b));assert all(any(y==x for y in it)for x in u(original)),s
 x=b
 for q in reversed(ops):assert x.count(q['after'])==1;x=x.replace(q['after'],q['before'],1)
 assert x==original
 p.write_text(b);proofs[s]={'path':str(p),'before_sha256':hashlib.sha256(original.encode()).hexdigest(),'after_sha256':H(p),'bytes':p.stat().st_size,'ops':len(ops),'full_inverse':True,'original_2_examples_and_complete_worked_section_exact':True,'old_URL_order_exact':True}
 dump(W/'exact-operations.json',allops);dump(W/'preservation-proof.json',proofs)
print(json.dumps(proofs,indent=2))
