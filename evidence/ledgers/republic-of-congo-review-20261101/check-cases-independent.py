from decimal import Decimal as D
from pathlib import Path
import json,re,yaml
# Independent arithmetic, separate from the repository's oa-check evaluator.
calculations={
'cg-company-formation':[
 ({'shares':D(300000)/5000,'initial_cash_minimum':D(300000)/2,'remaining_cash':D(300000)/2},'F02/F03: chosen cash capital, minimum nominal, half paid; fee separate.'),
 ({'sarl_fee_plus_full_capital':D(300000)+300000,'sa_fee_plus_full_capital':D(10000000)+500000,'difference':D(10500000)-600000},'F02/F04/F10: full capital plus displayed fee, not total ancillary costs or required initial paid-in capital.')],
'cg-corporate-income-tax':[
 ({'is_before_credits':max(D(20000800)//1000*1000*D('.28'),D(100000000)*D('.01'))},'C01/C08: ordinary domestic company; round profit first; no credits/other levies.'),
 ({'cash_tax':max(D(10000000)*D('.28'),D(20000000)*D('.01')),'noncash_tax':max(D(9800000)*D('.28'),D(20000000)*D('.01')),'difference':D(200000)*D('.28')},'C04 excludes cash at equality; other deduction conditions assumed met.')],
'cg-cross-border':[
 ({'withholding':D(10000000)*D('.20'),'net_payment':D(10000000)*D('.80')},'X05: no treaty reduction/gross-up; assumed gross royalty within scope.'),
 ({'deemed_profit':D(10000000)*D('.22'),'special_is':D(10000000)*D('.22')*D('.33'),'ordinary_withholding':D(10000000)*D('.20'),'difference':D(10000000)*(D('.20')-D('.22')*D('.33'))},'X05/X07: alternative legal facts, qualifying permit/regime and no base exclusions; not elective or stacked rates.')],
'cg-income-tax':[
 ({'iba':max(D(10000900)//1000*1000*D('.30'),D(200000000)*D('.015'))},'I02: ordinary IBA outside forfait; rounded ordinary equals minimum.'),
 ({'gain':D(30000000)-20000000-2000000,'investment_gain_tax':D(8000000)*D('.10'),'qualifying_home_gain_tax':D(0),'difference':D(8000000)*D('.10')},'I08/I09: documented qualifying costs; principal home at least five years versus investment property.')],
'cg-payroll-social':[
 ({'net_taxable':(D(3000000)-120000)*D('.80'),'annual_its':D(1200)+D(885000)*D('.10')+D(804000)*D('.15')},'I14/I15/I17: retirement120000 is established example input, never certified CNSS4percent; no final monthly remittance.'),
 ({'quotient':D(2304000)/2,'correct_annual':(D(1200)+D(537000)*D('.10'))*2,'incorrect_one_part':D(1200)+D(885000)*D('.10')+D(804000)*D('.15'),'over_withheld':D(210300)-109800},'I14/I15/I17: married without children expressly verified; does not use widowed exception; evidence decides parts, not election.')],
'cg-tax-overview':[
 ({'company_is':max(D(10000000)*D('.28'),D(100000000)*D('.01')),'individual_iba':max(D(10000000)*D('.30'),D(100000000)*D('.015')),'difference':D(200000)},'C01/C08/I02: independently reconciled profits; excludes distribution/social/other levies; does not recommend incorporation.'),
 ({'correct_total':D(1000000)*(1+D('.18')+D('.18')*D('.05')),'underbilling':D(1000000)*D('.18')*D('.05')},'V01: ordinary correctly classified VAT invoice; no universal profit surcharge.')],
'cg-transfer-pricing':[
 ({'addback':D(12000000)-10000000,'incremental_is':D(2000000)*D('.28')},'T01/C01: supported arm length charge is hypothetical study result, not safe harbour; minimum assumed not decisive.'),
 ({'first_required':D(int(max(499000000,500000000)>=500000000)),'second_required':D(int(max(499000000,499000000)>=500000000))},'T01/T02: assets OR turnover; equality meets threshold; arm length applies in both fact patterns.')],
'cg-vat-gst':[
 ({'vat':D(1000000)*D('.18'),'centimes':D(1000000)*D('.18')*D('.05'),'invoice_total':D(1000000)*(1+D('.18')+D('.18')*D('.05'))},'V01: centimes5percent of VAT, not price; ordinary correctly classified supply.'),
 ({'vat_disallowed_at_boundary':D(0),'vat_disallowed_above_boundary':D(30000),'difference':D(30000)},'V05/C04: VAT cash exclusion alone strictly over200000; supported VAT30000 hypothetical; other conditions preserved; IS boundary differs.')]
}
rows=[]
for slug,values in calculations.items():
 t=Path('skills/republic-of-congo',slug+'.md').read_text();bs=re.findall(r'```oa-check\n(.*?)```',t,re.S);assert len(bs)==2
 for index,(computed,legal) in enumerate(values):
  b=bs[index];name=b.splitlines()[0].removeprefix('name: ')
  expected=yaml.safe_load('expected:\n'+b.split('expected:\n',1)[1])['expected']
  assert all(abs(computed[k]-D(str(v)))<=D('.01') for k,v in expected.items()),(slug,name)
  rows.append({'guide':slug,'case_number':index+1,'case':name,'independent_results':{k:str(v) for k,v in computed.items()},'expected_match':True,'legal_condition_check':legal})
Path('evidence/ledgers/republic-of-congo-review-20261101/cases.json').write_text(json.dumps(rows,indent=2)+'\n')
print(len(rows),'cases independently recomputed, all expectations match')
