# Initial helper parse failure missing space in else36 retained in tool history; fixed before any computation.
from fractions import Fraction as F
from math import floor,ceil

def tariff(x):
 x=floor(x)
 if x<=12348:r=0
 elif x<=17799:y=F(x-12348,10000);r=(F('914.51')*y+1400)*y
 elif x<=69878:z=F(x-17799,10000);r=(F('173.10')*z+2397)*z+F('1034.87')
 elif x<=277825:r=F('.42')*x-F('11135.63')
 else:r=F('.45')*x-F('19470.38')
 return floor(r)
def up56(z):return max(2*(tariff(floor(z*F('1.25')))-tariff(floor(z*F('.75')))),floor(z*F('.14')))
def tax56(x):
 if x>34939:
  v=up56(34939)
  if x>222260:return v+floor((222260-34939)*F('.42'))+floor((x-222260)*F('.45'))
  return v+floor((x-34939)*F('.42'))
 v=up56(x)
 if x>14071:v=min(v,up56(14071)+floor((x-14071)*F('.42')))
 return v

def annual(gross,cls,care=None,kvz=F('2.9'),child=0):
 if care is None:care=F('.018')if cls==2 else F('.024')
 rv=min(gross,101400)*F('.093');hc=min(gross,69750)*(F('.07')+kvz/200+care)
 av=0 if cls==6 else min(gross,101400)*F('.013')
 vsp=ceil(rv+max(hc,min(1900,hc+av)))
 anp=0 if cls==6 else 1230;sap=0 if cls==6 else 36
 efa=4260 if cls==2 else 0
 x=max(0,gross-vsp-anp-sap-efa)
 tax=2*tariff(F(x,2))if cls==3 else tariff(x)if cls in[1,2,4]else tax56(x)
 return {'rv':str(rv),'healthcare':str(hc),'av':str(av),'VSP':vsp,'zve':x,'tax':tax}
for g,values in [(20000,[380,0,0,2234,2766]),(60000,[9389,8091,4822,15364,15895]),(100000,[23248,21634,15012,30157,30689])]:
 for cls,e in zip([1,2,3,5,6],values):
  z=annual(g,cls);assert z['tax']==e,(g,cls,z,e)
print('15officialvectorsPASS')
for g,c,care in[(55000,1,F('.024')),(72000,3,F('.018')),(18000,5,F('.018')),(108000,3,F('.0155'))]:print(g,c,annual(g,c,care, F('2.5')if g==108000 else F('2.9')))
