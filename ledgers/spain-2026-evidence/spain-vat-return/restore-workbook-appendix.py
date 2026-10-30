from pathlib import Path
p=Path('ledgers/spain-vat-return.md')
s=p.read_text()
if '## Old workbook' not in s:
 p.write_text(s.rstrip()+'\n\n'+Path(__file__).with_name('old-workbook-topic-appendix.md').read_text())
