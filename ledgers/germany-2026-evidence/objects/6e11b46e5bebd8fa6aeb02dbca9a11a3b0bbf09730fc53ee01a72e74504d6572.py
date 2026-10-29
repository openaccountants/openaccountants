from pathlib import Path
import json,hashlib,re,subprocess
from fractions import Fraction
P=Path(__file__).resolve().parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');REF='62b7639a5a68324a83a96bb0190fff8b7c76f8c5';slug='leaving-germany-exit-tax';rel='skills/international/germany/'+slug+'.md';raw=subprocess.check_output(['git','show',REF+':'+rel],cwd=R);text=raw.decode();sha=lambda b:hashlib.sha256(b).hexdigest();S=P/'support'/slug;S.mkdir(parents=True,exist_ok=True);(P/'ledgers').mkdir(exist_ok=True)
I={f.stem.replace('.identity',''):json.loads(f.read_text())for f in (P/'sources').glob('*.identity.json')};sources={k:Path(v['reader_path']).read_text().split('\n') for k,v in I.items()};A={}
def anchor(k,s,para,article,start=None,end=None):
 q=sources[s][para-1].split(': ',1)[1]
 if start:q=q[q.index(start):]
 if end:q=q[:q.index(end if end in q else end.lstrip())]
 assert q and q in sources[s][para-1];A[k]={'id':k,'source':s,'article':article,'url':I[s]['url'],'paragraph':para,'exact_quote':q,'actual_read_on':'2026-10-28','reader_sha256':I[s]['reader_sha256'],'raw_sha256':I[s]['raw_sha256']}
anchor('entry','A21',1,'AStG §21(1)');anchor('old','A21',4,'AStG §21(3)',end=' Abweichend');anchor('report-year','A21',8,'AStG §21(7)',end=' § 18')
anchor('trigger','A6',1,'AStG §6(1)');anchor('person','A6',2,'AStG §6(2)');anchor('return','A6',3,'AStG §6(3)');anchor('instalments','A6',4,'AStG §6(4)',end=' Die noch');anchor('accelerate','A6',4,'AStG §6(4)',start='Die noch',end='Abweichend');anchor('death','A6',4,'AStG §6(4)',start='Abweichend',end=' In den Fällen');anchor('return-defer','A6',4,'AStG §6(4)',start='In den Fällen');anchor('reports','A6',5,'AStG §6(5)')
anchor('shares','E17',1,'EStG §17(1)');anchor('gain','E17',2,'EStG §17(2)',end=' 3Weist');anchor('cost','E17',3,'EStG §17(2a)',end=' 4Eine');anchor('allowance','E17',4,'EStG §17(3)');anchor('reorg','E17',7,'EStG §17(6)');anchor('companymove','E17',6,'EStG §17(5)');anchor('cooperative','E17',8,'EStG §17(7)');anchor('cost60','E3c',2,'EStG §3c(2)',end=' 2Satz')
anchor('forty','E3',1,'EStG §3 no.40 opening',start='40. 40 Prozent',end=' a)');anchor('forty-c','E3',1,'EStG §3 no.40(c)',start='c) des Veräußerungspreises oder des gemeinen Werts',end=' d)')
for n,k in [(1,'extended-person'),(2,'low'),(3,'interests'),(4,'indirect'),(5,'rate'),(6,'cap')]:anchor(k,'A2',n,'AStG §2('+str(n)+')')
M={16:['entry','old'],22:['trigger','shares'],23:['person'],24:['trigger'],25:['trigger','gain','forty','forty-c','cost60','allowance'],26:['instalments'],27:['return'],28:['reports'],29:['extended-person','low','interests'],36:['person'],37:['instalments'],38:['return'],39:['return'],40:['return','accelerate'],42:['person'],44:['trigger','shares','cooperative'],49:['shares'],50:['allowance'],51:['allowance'],53:['trigger'],55:['trigger'],56:['trigger'],57:['trigger'],59:['trigger'],63:['trigger','shares','gain','cost','cost60'],68:['forty','forty-c'],73:['cost60'],75:['allowance'],79:['instalments'],80:['instalments'],81:['instalments'],82:['instalments'],84:['accelerate'],86:['accelerate'],87:['accelerate'],88:['accelerate'],89:['accelerate','death'],90:['accelerate'],92:['accelerate'],96:['return'],98:['return'],99:['return'],100:['return'],102:['return'],104:['return-defer'],108:['reports'],109:['reports'],110:['reports'],111:['report-year','accelerate'],119:['extended-person'],120:['low'],121:['interests'],122:['interests'],123:['interests'],124:['interests'],125:['interests'],127:['extended-person'],129:['extended-person'],130:['extended-person'],132:['extended-person'],136:['low'],137:['low'],139:['low'],143:['interests'],144:['interests'],145:['interests'],147:['indirect'],149:['extended-person'],151:['extended-person'],153:['rate','cap'],161:['trigger','shares'],162:['person'],163:['trigger'],164:['gain','forty','forty-c','cost60','allowance'],165:['instalments','accelerate'],166:['reports'],167:['return'],168:['extended-person','interests','low'],181:['old'],182:['reorg','companymove','trigger'],189:['trigger','forty','forty-c','cost60','allowance']}
# Exact native-LF bindings after reading the full current extended-liability/example section.
M={k:v for k,v in M.items()if k<118}
M.update({118:['extended-person'],119:['low'],120:['interests'],121:['interests'],122:['interests'],123:['interests'],124:['interests'],126:['extended-person'],128:['extended-person'],129:['extended-person'],131:['extended-person'],133:['low'],135:['low'],136:['low'],138:['low'],140:['interests'],142:['interests'],143:['interests'],144:['interests'],146:['indirect'],148:['extended-person'],150:['extended-person'],152:['rate','cap'],158:['trigger','shares'],159:['person'],160:['trigger'],161:['gain','forty','forty-c','cost60','allowance'],162:['instalments','accelerate'],163:['reports'],164:['return'],165:['extended-person','interests','low'],178:['old'],179:['reorg','companymove','trigger'],180:['trigger'],185:['trigger','forty','forty-c','cost60','allowance']})
# All substantive current lines, not only selected figures. Presentation and routing remain explicit.
rows=[];sec='Frontmatter';inmeta=True
for lf,l in enumerate(text.split('\n'),1):
 if lf==1:continue
 if inmeta:
  if l=='---':inmeta=False
  continue
 if l.startswith('#'):sec=l.lstrip('# ');continue
 if not l.strip() or re.fullmatch(r'\|[-:| ]+\|',l):continue
 if '<!-- openaccountants-cta-block -->'in l:break
 if l.startswith('| Item |') or l.startswith('| Source |'):kind='presentation/source routing'
 elif sec=='Sources':kind='source routing'
 elif sec=='Ask the client first':kind='intake questions; not legal assertions'
 elif lf in [18,156,181,182,183,184]:kind='scope/referral or hypothetical inputs; no newly asserted entitlement'
 elif lf in M:kind='computed from sourced inputs and stated fictional facts'if 158<=lf<=165 else'legal rule / operative chain'
 else:kind='UNRESOLVED ROW CLASSIFICATION'
 rows.append(dict(id=f'{slug}:{lf}',lf=lf,section=sec,wording=l,kind=kind,anchors=M.get(lf,[])))
# Explicit scope lines with source-bearing statements retain legal anchors; no fake authority for editorial limits.
for z in rows:
 if z['kind']=='UNRESOLVED ROW CLASSIFICATION':print('UNMAPPED',z['lf'],z['wording'][:150])
# Actual first introduction: path did not exist at its parent. No separately verified platform predecessor.
intro='fde7735315a35fb907cfe5e5a125ce1daecd058b';parent=subprocess.check_output(['git','rev-parse',intro+'^'],cwd=R,text=True).strip();new=subprocess.run(['git','cat-file','-e',parent+':'+rel],cwd=R,stderr=subprocess.DEVNULL).returncode!=0;assert new
old=[dict(ref=REF,old_lf=z['lf'],wording=z['wording'],destination=f"Exact current main wording retained in {z['section']}, LF{z['lf']}")for z in rows]
for n,z in [('claim-rows.json',rows),('actual-read-quotes.json',list(A.values())),('old-topics.json',old),('source-identities.json',[I[k]for k in ['A2','A6','A21','E17','E3','E3c']])]: (S/n).write_text(json.dumps(z,ensure_ascii=False,indent=2)+'\n')
controls={'hypothetical_gain':2000000-25000,'taxable_before_allowance':Fraction(3,5)*(2000000-25000),'quarter_value':Fraction(2000000,4),'return_extension_max_years':7+5};assert controls['hypothetical_gain']==1975000 and controls['taxable_before_allowance']==1185000
(S/'controls.json').write_text(json.dumps({k:str(v)for k,v in controls.items()},indent=2)+'\n')
def esc(s):return s.replace('|','\\|').replace('\n','<br>')
out=[f'# Figure and rule ledger: {slug}', '',f'Frozen Guide SHA256 `{sha(raw)}` at public main `{REF}`. Writer draft, not independent review. No Guide edits. Read date 2026-10-28 applies only to the selected source clauses quoted below. Cached source editions are separately pinned; acquisition is not full reading.','','Pre-refresh lineage: first Git introduction `'+intro+'`; the path is absent at parent `'+parent+'`. Therefore there is no older Git body for this slug to map. No separately verified prior platform body is invented. The complete current-main topic map follows.','','| # / LF | Section | Figure / rule as written | Source act/article and official URL | Exact selected original-language quote / classification | Read on |','|---|---|---|---|---|---|']
for z in rows:
 aa=[A[k]for k in z['anchors']];cite='<br>'.join(f"{a['article']} {a['url']}"for a in aa)or'—';quote='<br>'.join(a['exact_quote']for a in aa)or z['kind'];out.append('| '+ ' | '.join(esc(str(x))for x in [z['lf'],z['section'],z['wording'],cite,quote,'2026-10-28'if aa else'—'])+' |')
out+=['','## Old topics carried','','| Comparator / LF | Original substantive or operational unit | Current destination |','|---|---|---|']
for z in old:out.append('| '+ ' | '.join(esc(str(x))for x in [z['ref'][:12]+':'+str(z['old_lf']),z['wording'],z['destination']])+' |')
out+=['','## Evidence and limits','','All quoted strings are literal substrings of the pinned derived paragraph readers. Their normalization convention is explicit; original raw bodies were never normalized. Selected reads: AStG6(1)–(5); AStG2(1)–(6); AStG21(1),(3),(7); EStG17(1),(2),(2a),(3),(5),(6),(7); EStG3 no.40 opening and(c); EStG3c(2) first sentence. Other paragraphs acquired or emitted are not thereby declared read.','','The Guide itself preserves the partial-income chain qualification and absence of valuation/arrival-country methods. This ledger records that bounded derivation; it is not a ruling combining all provisions. Historical source versions beyond the dated cached bodies and a pre-Git platform predecessor remain unverified. Computed hypothetical amounts are not source quotations. The Guide has no oa-check blocks and none was introduced.','']
f=P/'ledgers'/f'{slug}.md';f.write_text('\n'.join(out))
checks={'guide_sha256':sha(raw),'ledger_sha256':sha(f.read_bytes()),'claim_rows':len(rows),'quote_anchors':len(A),'old_units':len(old),'unclassified':[z['lf']for z in rows if z['kind']=='UNRESOLVED ROW CLASSIFICATION'],'source_quote_substrings':all(a['exact_quote']in'\n'.join(sources[a['source']])for a in A.values()),'guide_unchanged':(R/rel).read_bytes()==raw,'old_map_full_exact':len(old)==len(rows),'fictional_controls':{k:str(v)for k,v in controls.items()},'new_legal_review':False};(S/'writer-checks.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
