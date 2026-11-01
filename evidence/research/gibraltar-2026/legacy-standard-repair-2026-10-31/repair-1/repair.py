from pathlib import Path
R=Path(__file__).resolve().parents[5]
E=Path(__file__).resolve().parent
p=R/'skills/gibraltar/gi-property-stamp-duty.md'
old=(E/'gi-property-stamp-duty.reviewed.md').read_text()
bad='This Guide does not compute a separate penalty or interest amount for the stated job. Keep the domestic return/payment and dispute requirements in the linked taxpayer Guides separate from the allocation, formation or relief test. The unresolved procedural limits remain listed in Sources. This is a scope boundary, not a finding that no penalty applies.'
good="See [Stamping, responsibility and late instruments](#stamping-responsibility-and-late-instruments) in Deadlines and filing for this Guide's section 16 penalty and interest method, and “Base-penalty examples only” in Two worked examples that recompute for its controls. Those examples exclude interest, further penalties, court fines and other charges; they are not total settlement amounts. The limitations on later interest notices, day counting and actual settlement remain explicit in that method and Sources."
assert old.count(bad)==1
new=old.replace(bad,good).replace('version: "0.5"','version: "0.6"').replace('# Gibraltar property conveyance and mortgage stamp duty\n','# Gibraltar property conveyance and mortgage stamp duty v0.6\n')
p.write_text(new)
