from writer import *
import difflib
out=[]
def article(sid,a):
 ls=lf(ARCH/f'sources/{sid}.txt');starts=[i for i,x in enumerate(ls) if x=='§ '+a];st=starts[-1];en=next((i for i in range(st+1,len(ls)) if re.fullmatch(r'§ \d+[a-z]*',ls[i])),len(ls));return ws('\n'.join(ls[st:en])),[st+1,en]
for before,after,arts in [(13,14,['2','11','12','13','15','16','17','17f','17g','17k','19','21','21a','22','25','26','27','30','30c','42','43','44','45','46b','49']), (12,13,['2','11','13','15','16','17f','17g','43','44','45','46b']), (19,20,['16','27','69','79','154','155','156','161'])]:
 for a in arts:
  b,br=article(before,a);c,cr=article(after,a);d={'article':a,'before_source':before,'after_source':after,'before_nativeLF':br,'after_nativeLF':cr,'before_raw_sha256':receipts[str(before)]['sha256'],'after_raw_sha256':receipts[str(after)]['sha256'],'before_selected_sha256':hashlib.sha256(b.encode()).hexdigest(),'after_selected_sha256':hashlib.sha256(c.encode()).hexdigest(),'whitespace_joined_equal':b==c}
  if b!=c:d['word_diff']=' '.join(difflib.unified_diff(b.split(),c.split(),n=8))
  out.append(d)
(EVID/'dated-operative-comparisons.json').write_text(json.dumps({'method':'Last exact statutory article header, to next exact article header; whitespace joined only. Mechanical comparison, not a claim that whole future bodies were read. Actual present quotation reads are separately catalogued.','comparisons':out},ensure_ascii=False,indent=2)+'\n')
for d in out:
 if not d['whitespace_joined_equal']:print(d['before_source'],d['after_source'],d['article'],d['word_diff'][:1800])
