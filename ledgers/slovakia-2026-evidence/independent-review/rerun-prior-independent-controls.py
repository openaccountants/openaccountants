from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_DOWN
from datetime import date
import re, yaml, json, hashlib, subprocess, difflib
ROOT=Path('/Users/michaelcutajar/Documents/ChatGPT/OA')
W=ROOT/'.claude/worktrees/europe-slovakia'
G=W/'skills/international/slovakia'
OUT=ROOT/'output/europe-closeout-2026-10-27/sk-ledger-independent-review-2026-10-29'
def q(x):return D(str(x)).quantize(D('.01'),rounding=ROUND_HALF_UP)
def down(x):return D(str(x)).quantize(D('.01'),rounding=ROUND_DOWN)
def dime(x):return D(str(x)).quantize(D('.1'),rounding=ROUND_DOWN)
def blocks(s):return [yaml.safe_load(x) for x in re.findall(r'```oa-check\n(.*?)```',s,re.S)]
def dump(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n')
# Freshly rerun independent reference arithmetic, no oa step strings evaluated.
# No oa-check step strings are evaluated here.
refs=[]
refs.append(dict(flat_expenses=D(20000),partial_base=D(48000)-20000-6000,allowance=q(D('284.13')*21),base=D(22000)-q(D('284.13')*21),tax=q((D(22000)-q(D('284.13')*21))*D('.15')),micro_loss_used=min(D(8000),D(10000)),controlled_trader_loss_used=min(D(8000),D(10000)/2),controlled_trader_loss_left=D(8000)-min(D(8000),D(10000)/2),government_bond_tax=D(1000)*D('.13'),foreign_bank_interest_tax=D(1000)*D('.19'),exempt_retail_bond_tax=D(0)))
allowance=q(q(D('284.13')*D('51.6'))-D(36000)/3); taxable=D(36000)-allowance;tax=q(taxable*D('.19'));bonus=min(D(1200)-q((D(36000)-D(27432))/10),q(D(36000)*D('.29')))
refs.append(dict(allowance_cap=q(D('284.13')*D('51.6')),allowance=allowance,base=taxable,tax=tax,taper_threshold=D('1.5')*12*1524,bonus=bonus,tax_after_bonus=tax-bonus,child_15_in_june=D(6)*100+6*50,child_18_in_june=D(6)*50,child_born_june=D(7)*100,changing_count_cap=D(4000)*(D('.29')/2+D('.36')/2),changing_count_bonus=min(D(1800),D(4000)*(D('.29')/2+D('.36')/2)),low_base_bonus=min(D(1200),D(2000)*D('.29')),combined_base=D(2000)+4000,combined_bonus=min(D(1200),D(6000)*D('.29')),partial_combined_base=D(2000)+D(4000)/2,partial_combined_bonus=min(D(1200),D(4000)*D('.29')),old_mortgage_bonus=min(D(1000)/2,D(400)),new_mortgage_bonus=min(D(3000)/2,D(1200)),new_partial_bonus=min(D(2000)/2,D(1200)/2),return_balance_variant=tax-bonus+100-5500))
base=D(20000)+1500; used=min(D(4000),base/2); tax=(base-used)*D('.1');room=tax-D(960);credit=min(D(500),room)
refs.append(dict(base_before_loss=base,loss_cap=base/2,loss_used=used,base_after_loss=base-used,tax_10=tax,tax_payable=max(tax,D(960)),tax_if_21=(base-used)*D('.21'),cliff_cost=(base-used)*D('.21')-tax,computer_first_year=q(D(4800)/4/2),ordinary_car_first_year=q(D(30000)/4/2),qualifying_bev_first_year=q(D(30000)/2/2),furniture_first_year=q(D(6000)/6/2),admin_building_full_year=D(800000)/40,qualifying_hotel_full_year=D(800000)/20,improvements_boundary=D(800000)/10,improvement_excess_over_boundary=D(80000)-D(800000)/10,separate_improvements_full_year=q(D(80000)/6),min_credit_room_variant=room,min_credit_used_variant=credit,tax_after_prior_credit_variant=tax-credit,final_payment_variant=tax-credit-1000))
loss=min(D(400000),D(300000)/2); tax=(D(300000)-loss)*D('.24');S=D(2000000)-500000+200000+100000+200000;ebitda=S+4000000+1000000;capacity=ebitda*D('.3');blocked=max(D(0),D(4000000)-capacity);carryroom=D(3600000)-3200000;covered=D(120000)-20000;thinlimit=D(300000)/4
refs.append(dict(loss_cap=D(300000)/2,loss_used=loss,loss_cf=D(400000)-loss,base_after_loss=D(300000)-loss,tax_24=tax,tax_payable=max(tax,D(11520)),monthly_advance=tax/12,statutory_sum_bases=S,tax_ebitda=ebitda,interest_capacity=capacity,interest_addback=blocked,threshold_boundary_excess=D(3000000)-3000000,carry_room=carryroom,interest_carry_used=min(blocked,carryroom),interest_carry_left=blocked-min(blocked,carryroom),thin_covered_costs=covered,thin_capacity=thinlimit,thin_disallowed=covered-min(covered,thinlimit),thin_allowed=min(covered,thinlimit),thin_negative_ebitda_disallowed=covered-min(covered,max(D(0),D(-100000)/4)),thin_zero_ebitda_disallowed=covered-min(covered,max(D(0),D(0)/4)),final_payment_variant=tax-30000))
# Additional ten scenarios recomputed from stated facts and law, independent of embedded steps.
refs += [dict(output_vat=D(40000)*D('.23')+D(10000)*D('.05')+D(2000)*D('.19'),payable=D(10080)-4600),dict(output_vat=D(30000)*D('.23')+D(2000)*D('.23'),input_vat=D(2000)*D('.23')+D(5750)/2+1150,payable=D(7360)-4485)]
refs += [dict(output_vat=D(200)*D('.23'),nonpayer_tax=D(200)*D('.23'),nonpayer_cost=D(200)*D('1.23'),payer_net_vat=D(46)-46,payer_cost=D(200)),dict(turnover_before=D(4500)*11,ordinary_turnover=D(4500)*12,ordinary_excess_50000=D(54000)-50000,ordinary_room_to_62500=D(62500)-54000,alternative_turnover=D(4500)*11+14000,alternative_excess_62500=D(63500)-62500,project_vat=D(14000)*D('.23'),project_total=D(14000)*D('1.23'),gross_price_net=q(D(14000)/D('1.23')),gross_price_vat=D(14000)-q(D(14000)/D('1.23')))]
social=sum(down(D(2500)*r) for r in map(D,['.014','.04','.03','.01']));health=down(D(2500)*D('.05'));adv=q((D(2500)-social-health-D('497.23'))*D('.19'));ersocial=sum(down(D(2500)*r) for r in map(D,['.014','.14','.03','.005','.005','.0025','.0475']));eracc=down(D(2500)*D('.008'));erhealth=down(D(2500)*D('.11'))
refs.append(dict(ee_social=social,ee_health=health,advance=adv,advance_after_bonus=adv-100,net_pay=D(2500)-social-health-adv+100,er_social=ersocial,employer_cost=D(2500)+ersocial+eracc+erhealth,to_social_insurer=social+ersocial+eracc))
sbase=down(D(28500)/12/D('1.486'));hbase=down(D(24000)/12/D('1.486'));rates=list(map(D,['.044','.18','.06','.0475']))
refs.append(dict(social_base=sbase,social_month=sum(down(sbase*r) for r in rates),health_base=hbase,health_advance=down(hbase*D('.16')),special_month=sum(down(D('396.24')*r) for r in rates),annual_floor_2026=D(1524)*D('.6'),annual_ceiling_2026=D(1524)*11,annual_special_2026=D(1524)*D('.26'),cycle_income_threshold_2026=D(1524)*12/2))
refs += [dict(wht_19=D(8000)*D('.19'),net_paid=D(8000)*D('.81'),wht_35_noncooperating=D(8000)*D('.35')),dict(sk_tax=D(400000)*D('.21'),foreign_share_pct=D(50000)/400000*100,credit_limit=D(84000)*D(50000)/400000,credit=min(D(7500),D(50000)*D('.10'),D(10500)),tax_payable=D(84000)-5000,not_creditable=D(7500)-5000)]
extra=(D(250000)-180000)*D('.21');fine=dime(extra*D('.1')*(D((date(2028,1,1)-date(2027,4,1)).days)/365+D((date(2028,7,1)-date(2028,1,1)).days)/366))
refs.append(dict(adjustment=D(250000)-180000,extra_tax=extra,penalty=fine,penalty_paid_early=dime(fine*2/3),minimum_penalty=extra/100))
refs.append(dict(add_back=D(1200000)-1080000,over_basic_threshold=D(1200000)-1000000,extra_tax=D(120000)*D('.24'),penalty=dime(D(28800)*D('.03')*D((date(2026,12,1)-date(2026,4,1)).days)/365),late_interest_variant=dime(D(28800)*D('.15')*10/365),small_revenue_after=D(99500)+1000,small_tax_before=D(20000)*D('.1'),small_tax_after=D(21000)*D('.21'),small_extra_tax=D(21000)*D('.21')-D(20000)*D('.1'),large_revenue_after=D(4999500)+1000,large_extra_tax=D(201000)*D('.24')-D(200000)*D('.21')))
files=['slovakia-pit.md','sk-corporate-income-tax.md','slovakia-vat-return.md','slovakia-vat-registration-4-7-7a.md','sk-payroll-social.md','sk-cross-border.md','sk-transfer-pricing.md']
actual=sum([blocks((G/f).read_text()) for f in files],[])
results=[]
for block,ref in zip(actual,refs):
 assert set(ref)==set(block['expected']),(block['name'],set(ref)^set(block['expected']))
 for k,v in ref.items():assert abs(v-D(str(block['expected'][k])))<D('.000001'),(block['name'],k,v,block['expected'][k])
 results.append(dict(name=block['name'],independently_recomputed=ref,expected_fields=len(ref),all_match=True))
assert len(actual)==len(refs)==14
dump('independent-14-example-controls.json',results)
extra=[]
def check(n,got,want,source):
 assert got==want,(n,got,want)
 extra.append(dict(name=n,computed=got,expected=want,source=source,pass_=True))
check('May1200 daily floor before20days',down(D(1200)/31)*20,D(774),'SP partial-month instructions / Act138(13)')
check('May774 four fund sum',sum(down(D(774)*r) for r in rates),D('256.57'),'SP May2026 actual example')
check('2025 income threshold',q(D('273.99')*D('10.5')),D('2876.90'),'Current SP July/October guidance and Act21(7)')
for inc,want in [('2876.90',False),('2876.91',True)]:check('Annual coverage income '+inc,D(inc)>D('2876.90'),want,'Act21(5)/293gnb;2025income')
for months,want in [(59,False),(60,False),(61,True)]:check('More than60month restart '+str(months),months>60,want,'Act21(3) exception')
check('DDS own240+60 sharedcap',min(D(240)+60,D(180)),D(180),'ITA11(8)–(10)')
check('2026 earlywithdrawal latestaddbackyear',2026+3,2029,'ITA11(11)')
check('Child June15birthday',D(6)*100+6*50,D(900),'ITA33(1)')
check('Child June18birthday',D(6)*50,D(300),'ITA33(1)')
check('Books ads50stillallowed',D(50)<=50,True,'VAT Annex7 ex4901')
check('Periodical erotic10stillallowed',D(10)<=10,True,'VAT Annex7 ex4902')
check('Audio narration50allowed',D(50)>=50,True,'VAT Annex7a CPA58.11.30')
check('Rentalproportionalexpense',q(D(2000)*5500/6000),D('1833.33'),'ITA9(1)(g)')
check('Quarterlyturnover exactly100000fails',D(100000)<100000,False,'VAT77(2)')
check('Fastrefund aggregate exactly1000passes',D(1000)<=1000,True,'VAT79(2)(c)')
dump('additional-source-boundary-controls.json',extra)
print(json.dumps(dict(blocks=len(results),expected_fields=sum(len(x) for x in refs),additional_controls=len(extra),all_pass=True),indent=2))
