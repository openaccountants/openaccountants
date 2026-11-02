import json,datetime
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
from pathlib import Path
out=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def money(v):
 v=F(v);return (Decimal(v.numerator)/Decimal(v.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
def dc(v):return F(str(v))
def parts(base,rates):return [money(F(base)*dc(r)) for r in rates]
base=F('5101.20');r=F(6000);s1=F('510.12');s2=F('388.68')
er=parts(base,['.236','.055','.002','.006','.0075','.015']);ee=parts(base,['.047','.0155','.001','.0015'])
for i,(a,e) in enumerate(zip(er,['1203.88','280.57','10.20','30.61','38.26','76.52'])):c('employercomponent'+str(i),a,Decimal(e))
for i,(a,e) in enumerate(zip(ee,['239.76','79.07','5.10','7.65'])):c('employeecomponent'+str(i),a,Decimal(e))
ers=money(s1*F('.0096'))+money(s2*F('.0104'));ees=money(s1*F('.0019'))+money(s2*F('.0021'))
c('employersolidarity',ers,Decimal('8.94'));c('employeesolidarity',ees,Decimal('1.79'));c('employertotal',sum(er)+ers,Decimal('1648.98'));c('employeetotal',sum(ee)+ees,Decimal('333.37'));c('employercost',6000+sum(er)+ers,Decimal('7648.98'));c('preIRPFcash',6000-sum(ee)-ees,Decimal('5666.63'))
c('parttimeCC',max(900,80*F('11.98')),F('958.4'));c('parttimeAT',max(900,80*F('8.58')),900)
her=parts(970,[F('.236')*F('.8'),'.015',F('.055')*F('.2'),F('.002')*F('.2'),'.0075']);hee=parts(970,['.047','.0155','.0015'])
for i,(a,e) in enumerate(zip(her,['183.14','14.55','10.67','.39','7.28'])):c('houseemployer'+str(i),a,Decimal(e))
for i,(a,e) in enumerate(zip(hee,['45.59','15.04','1.46'])):c('houseemployee'+str(i),a,Decimal(e))
c('houseemployertotal',sum(her),Decimal('216.03'));c('houseemployeetotal',sum(hee),Decimal('62.09'));c('houseremitted',sum(her)+sum(hee),Decimal('278.12'));c('houseprecash',900-sum(hee),Decimal('837.91'))
c('SMIannual',1221*14,17094);c('SMImonthlywithsixth',1221*F(7,6),F('1424.50'));c('CCgroup7table',F('1424.40'),F('1424.4'));c('ATformulaexceedsCCtable',1221*F(7,6)-F('1424.4'),F('.1'))
comp=(10000+1200)*F('.93');c('RETAcomputable',comp,10416);c('RETA180days',comp/180*30,1736);c('not6assumedmonths',comp/6!=comp/180*30,False);c('full365different12',comp/365*30!=comp/12,True)
for n,rate,e in [('CC','.283','339.60'),('AT','.013','15.60'),('cessation','.009','10.80'),('training','.001','1.20'),('MEI','.009','10.80')]:c('RETA'+n,money(1200*F(rate)),Decimal(e))
c('RETAtotal',1200*F('.315'),378);c('components315',F('28.3')+F('1.3')+F('.9')+F('.1')+F('.9'),F('31.5'));c('TGSS314not315',F('31.5')-F('31.4'),F('.1'))
c('published3months',F('88.64')*3,F('265.92'));c('diagnosticMEI',money(F('950.98')*F('.009')),Decimal('8.56'));c('diagnostictotal',80+money(F('950.98')*F('.009')),Decimal('88.56'));c('diagnostic3months',3*Decimal('88.56'),Decimal('265.68'));c('publishednotdoubleMEI',F('88.64'),F('88.64'))
c('3percent90days',90>=90,True);c('89doesnot90',89>=90,False);c('company3percent',10000*F('.97'),9700);c('ordinary7percent',10000*F('.93'),9300)
c('averagewithinnotpermonth',F(1000+1300,60)*30,F(1150));c('averagebelow',F(1000+1200,60)*30,1100);c('signedmonthone',F('1143.79')-1000,F('143.79'));c('signedmonthtwo',F('1143.79')-1200,F('-56.21'));c('signednet',F('143.79')-F('56.21'),F('87.58'));c('signedquota',money(F('87.58')*F('.315')),Decimal('27.59'))
c('plurianonzero',min((20000-F('17323.68'))/2,4000/2),F('1338.16'));c('pluriRETAcap',min((30000-F('17323.68'))/2,1000/2),500);c('plurinoexcess',max(F('17323.68')-F('17323.68'),0),0)
c('ITnotcoveredreduction',1200*F('.283')*F('.055'),F('18.678'));c('familyfirstbonus',money(F('950.98')*F('.283')/2),Decimal('134.56'));c('familylaterbonus',money(F('950.98')*F('.283')/4),Decimal('67.28'));c('ceuta75CConly',1200*F('.283')*F('.25'),F('84.9'))
def ar(b,k):
 r21=F('7.36')*(1+(b-k)/b*F('2.52')*F('6.15')/F('7.36'));r26=(r21+F('8.10'))/2;return b*(F('21.20')-r26)/100
c('agro2026rawfloorfixture',ar(F('1424.4'),F('986.7')),F('157.949307'));c('agro2026floor',max(F('179.44'),min(279,ar(F('1424.4'),F('986.7')))),F('179.44'));c('agro2026middle',money(ar(F(3000),F('986.7'))),Decimal('248.09'));c('agro2026cap',min(279,ar(F('5101.2'),F('986.7'))),279);c('agrodailyraw',ar(F(100),F('42.90')),F('9.045321'));c('agrodailyfloor',max(F('8.16'),ar(F('61.93'),F('42.90'))),F('8.16'))
c('agrogroup1cap',min(279,2000*F('.155')),279);c('inactiveD',30-20*F('1.3636'),F('2.728'));c('inactivebase',F('2.728')*F('47.48'),F('129.52544'));c('inactiveCCreduced',money(F('129.52544')*F('.115')*F('.8089')),Decimal('12.05'));c('inactiveMEIunreduced',money(F('129.52544')*F('.009')),Decimal('1.17'))
c('cessationindicator',600*F(7,6),700)
for n,p,e in [('nofloor','.8',560),('childfloor','1.07',749),('nocap','1.75',1225),('onecap','2',1400),('twocap','2.25',1575)]:c(n,700*F(p),e)
c('cessationordinaryfloor',max(560,min(1225,700*F('.7'))),560);c('lowbaseexception',min(1225,700*F('.7')),490);c('partialnoordinaryfloor',700*F('.5'),350);c('pluriSMIequalityfails',F(500)+F(721)<1221,False);c('pluriSMIbelow',F(500)+F('720.99')<1221,True)
c('regularrefundexpense',max(800-1100,0),0);c('regularrefundincome',max(1100-800,0),300)
c('interestannual',10000*F('.0325')*F('1.25'),F('406.25'));c('interest73days',10000*F('.040625')*F(73,365),F('81.25'));c('nominal31May2026Sunday',datetime.date(2026,5,31).weekday(),6);c('29May2026Friday',datetime.date(2026,5,29).weekday(),4)
(out/'tranche12-controls.json').write_text(json.dumps({'count':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'PASS')
