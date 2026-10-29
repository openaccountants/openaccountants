from writer import *
def units(t):
 out=[];buf=[];start=1;fence=False;front=False
 for i,l in enumerate(t.split('\n')+[''],1):
  if i==1 and l=='---':front=True
  elif front and l=='---':front=False
  if l.startswith('```'):fence=not fence
  if not l.strip() and not fence and not front:
   if buf:out.append((start,i-1,'\n'.join(buf)));buf=[]
  else:
   if not buf:start=i
   buf.append(l)
 return out
def mapbody(old,current,overrides):
 out=[]
 for lo,hi,t in units(old):
  n=current.find(t)
  if n>=0:
   a=current[:n].count('\n')+1;dest=f'{a}–{a+t.count(chr(10))}';why='Exact topic block retained, including every table/list member.'
  else:assert lo in overrides,(lo,hi,t[:100]);dest,why=overrides[lo]
  out.append({'old_native_LF':[lo,hi],'old_unit_sha256':hashlib.sha256(t.encode()).hexdigest(),'old_exact_opening':ws(t)[:230],'current_destination':dest,'disposition':why})
 return out
def table(m):
 out=['| Prior native LF | Exact opening | Current destination | Disposition |','|---|---|---|---|']
 for x in m:out.append('| '+str(x['old_native_LF'])+' | '+x['old_exact_opening'].replace('|','\\|')+' | '+x['current_destination']+' | '+x['disposition']+' |')
 return '\n'.join(out)
