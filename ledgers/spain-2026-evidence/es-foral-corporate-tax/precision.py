# Invoked before save by the local writer; selections are verbatim normalized source substrings.
import re
norm=m['norm']
def qreplace(z,needle,n=600):
 t=norm(m['source'](z['url'])['text']);i=t.lower().find(needle.lower());assert i>=0,(z['guide_LF'],needle,z['url']);end=min(len(t),i+n);end=t.rfind(' ',i,end)if end<len(t)else end;z['quote']=t[i:end]+(' […]'if end<len(t)else'')
for z in L.rows:
 lf=z['guide_LF'];u=z['url']
 if lf==36 and '1990-31117' in u:qreplace(z,'1. Los sujetos pasivos',400)
 if lf==66 and u.startswith(N):qreplace(z,'2. A los efectos',400)
 if lf==72 and u.startswith(N):qreplace(z,'1. La base liquidable',650)
 if lf==94:qreplace(z,'Serán deducibles',700)
 if lf==176 and u.startswith(G):qreplace(z,'bloque de 5',800)
 if lf==198:qreplace(z,'Serán deducibles',650)
 if lf==213:qreplace(z,'Estas entidades aplicarán',950)
 if lf==250:qreplace(z,'El porcentaje de deducción previsto en el segundo' if u.startswith('https://www.bizkaia')else '1. El importe' if u.startswith('https://www.araba')else 'El importe',600)
 if lf==323 and '2007-19884' in u:qreplace(z,'El gasto (ingreso) por impuesto sobre beneficios',650)
 if lf==258 and '#ar-63'in u and '30.000' in z['quote']:qreplace(z,'Base de la deducción',220)
 if lf==137 and u.startswith(B):qreplace(z,'Edificios para casa',160)
 if lf==138 and u.startswith(B):qreplace(z,'Edificios y pabellones',90)
 if lf in[139,140,141,142,143,144,145,146] and u.startswith(B):qreplace(z,{139:'Instalaciones 20',140:'Maquinaria para usos industriales',141:'Maquinaria para otros usos',142:'Mobiliario 15',143:'Equipos informáticos',144:'Autobuses, camiones',145:'Moldes, modelos',146:'Otros elementos no especificados'}[lf],100)
 if lf==141 and (u.startswith(A)or u.startswith(G)):qreplace(z,'Maquinaria para otros usos',80)
 if lf==146 and (u.startswith(A)or u.startswith(G)):qreplace(z,'Otros elementos no especificados',80)
 if 137<=lf<=146 and u.startswith(NR):qreplace(z,{137:'Edificaciones para oficinas',138:'Edificaciones para uso industrial',139:'Instalaciones 15',140:'Maquinaria 15',141:'Maquinaria 15',142:'Mobiliario 15',143:'Equipos para procesos',144:'Elementos de transporte (autobuses',145:'Moldes, modelos',146:'Otro inmovilizado material'}[lf],150)

for z in L.rows:
 if 'G26-visual-selected' in z['reader']:
  z['quote']=z['quote'].split('selected visual transcription: ')[-1] if z['guide_LF']!=250 else z['quote'].split(' Article 5.2')[0]
for z in L.rows:
 lf=z['guide_LF'];u=z['url']
 if lf==215 and u.startswith(B):qreplace(z,'b) Del 13 por',280)
 if lf==227 and '03861' in u:qreplace(z,'Quinto. Con vigencia exclusiva',950)
 if lf==227 and '01182' in u:qreplace(z,'Lo dispuesto en los apartados 3 y siguientes del artículo 59',430)
 if lf==319 and '1885-6627' in u:
  z['url']=u.split('#')[0];x=m['source'](z['url']);L.sources[z['url']]=x;qreplace(z,'2. La cuenta de pérdidas y ganancias recogerá',700)
 if lf==117:qreplace(z,'b) La diferencia entre las cantidades',350)
 if lf in[294,298,303]and u==GR:qreplace(z,'se entenderá por resultado contable positivo',650)
 if lf==127 and 'préstamo participativo' in z['quote']:qreplace(z,'La deducción de los gastos financieros relacionados con la adquisición',400)

for z in L.rows:
 if z['guide_LF']==323 and '2026_073_01914' in z['url'] and z['provision'].endswith('field1000'):
  z['quote']=m['norm'](Path(z['reader']).read_text().splitlines()[2502])

# S-L21 exact own2.2 across page gap; not a preamble threshold fragment.
for z in L.rows:
 if z['guide_LF']in[393,401]and'c1806246.pdf'in z['url']and'36.000'in z['quote']:
  t=Path(z['reader']).read_text().split('\n');z['quote']=m['norm']('\n'.join(t[134:147]));z['provision']='Gipuzkoa OF444/2018 article2.2; same person/type/method threshold, own nativeLF135–147'
