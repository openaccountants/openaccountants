from pathlib import Path
import ast,json,re,hashlib
T=Path(__file__).resolve().parent;O=T.parent;B=O/'germany-ledger-writer-B-2026-10-29';P=O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29'
def enrich(topics):
 tree=ast.parse((B/'freelancer-ledger.py').read_text());mp=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mp' for t in n.targets));D=next(x for x in json.loads((B/'current-and-pre-refresh-identities.json').read_text()) if x['slug']=='de-einkommensteuer-freelancer');oldlines=D['pre_refresh_body'].split('\n');cur=(T/'after/de-einkommensteuer-freelancer.md').read_text().split('\n');pmap=json.loads((P/'support/de-einkommensteuer-freelancer.line-map.json').read_text());tmap=json.loads((T/'support/de-einkommensteuer-freelancer.line-map.json').read_text());audit=[]
 def coords(s):
  def f(m):
   a=int(m[1]);b=int(m[2]) if m[2] else a;pa=pmap[str(a)]['start'];pb=pmap[str(b)]['end'];a=tmap[str(pa)]['start'];b=tmap[str(pb)]['end'];return str(a) if a==b else f'{a}–{b}'
  return re.sub(r'(\d+)(?:[–-](\d+))?',f,s)
 for i,row in enumerate(topics['pre_refresh_rows'],1):
  lo,hi=row['old_native_LF'];keys=[k for k in mp if lo<=k<=hi]
  if len(keys)<=1:continue
  assert hashlib.sha256('\n'.join(oldlines[lo-1:hi]).encode()).hexdigest()==row['old_unit_sha256'];components=[]
  for k in keys:
   dest,why=mp[k];now=coords(dest);openings=[]
   for m in re.finditer(r'(\d+)(?:[–-](\d+))?',now):
    a=int(m[1]);b=int(m[2]) if m[2] else a;assert 1<=a<=b<=len(cur);openings.append({'native_LF':[a,b],'first_line':cur[a-1],'last_line':cur[b-1]})
   note='Historical topic preserved at the actual current destination, with current source qualifications; no claim that old prose is byte-identical.'
   if k in [99,258]:note+=' DE-B04 expressly corrects old gross-price eligibility: test800 net of containedVAT; irrecoverableVAT remains in deductible cost, not the eligibility limit.'
   if k==159:note+=' DE-R01 now supplies the positive business-car commuting formula; old bare bookkeeping routing did not itself supply it.'
   if k==160:note+=' DE-R02 preserves the qualifying-overnight alternative; short non-overnight≤8h is separate.'
   if k==278:note+=' DE-R16 limits the eligible410 deduction and applies statutory reduction inputs.'
   components.append({'old_component_LF':k,'exact_old_line':oldlines[k-1],'original_per_line_destination':dest,'original_per_line_disposition':why,'current_destination':now,'actual_current_scope_note':note,'actual_current_destination_openings':openings})
  row['pre_R17_destination']=row['current_destination'];row['R17_component_destinations']=components;row['current_destination']='; '.join(dict.fromkeys(x['current_destination'] for x in components));row['R17_disposition']='Every original grouped topic now has its own actual current destination; prior first-key-only map retained as history. Current source corrections govern old erroneous claims.'+(' DE-B04 corrects gross GWG eligibility; contained VAT determines eligibility, irrecoverable VAT remains in cost.' if any(k in [99,258] for k in keys) else '');audit.append({'pre_refresh_row':i,'old_native_LF':[lo,hi],'old_unit_sha256':row['old_unit_sha256'],'components':components})
 (T/'R17-grouped-unit-assessment.json').write_text(json.dumps({'role':'Writer evidence precision, not new legal review','original_pre_refresh_revision':D['pre_refresh_revision'],'original_pre_refresh_sha256':D['pre_refresh_sha256'],'all_grouped_units_with_multiple_per_line_definitions':len(audit),'assessments':audit},ensure_ascii=False,indent=2)+'\n')
 text='# DE-R17 grouped component reading\n\nActual old component line and current destination openings read for the finite first-key-only map correction; original full bodies/controls remain retained. No broad source-law rereading is claimed.\n'
 for x in audit:
  text+=f'\n## Pre-refresh row{x["pre_refresh_row"]}, oldLF{x["old_native_LF"]}\n'
  for c in x['components']:
   text+=f'\nOld LF{c["old_component_LF"]}: {c["exact_old_line"]}\n\nCurrent {c["current_destination"]}: '+ ' / '.join(z['first_line']+' … '+z['last_line'] for z in c['actual_current_destination_openings'])+'\n'
 (T/'R17-component-reading.md').write_text(text)
 return topics
