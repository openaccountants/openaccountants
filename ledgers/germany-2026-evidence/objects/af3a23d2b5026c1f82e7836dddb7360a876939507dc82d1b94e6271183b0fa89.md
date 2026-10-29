# DE-R13: payment-method boundary on three-day grace

This is a finite operational exception, not a missing broad tax domain. The trade late-payment row (frozen LF152, current LF156) states no surcharge for a delay up to three days without the statutory payment-method exception. Corporate current LF108 narrows the exception to cheques only. AO240(3), second sentence excludes payments within AO224(2), no.1, which includes delivery/transmission of payment instruments (cash as well as cheques).

Actual retained official sources already independently read:

- https://www.gesetze-im-internet.de/ao_1977/__240.html , B `AO240.grace`, DEB019 literalLF9, reader SHA `2cfa86cfaac164f5f98e3dc6a02b04d67165a70fc4439631021fe7a3ae0bf631`: `Ein Säumniszuschlag wird bei einer Säumnis bis zu drei Tagen nicht erhoben. Dies gilt nicht bei Zahlung nach § 224 Absatz 2 Nummer 1.`
- https://www.gesetze-im-internet.de/ao_1977/__224.html , A corporate quote109/AO224, reader `Ud818a09838515be4.reader.txt` literalLF7–9, SHA `d0b8f9648ceb978be2ed418912b741a3e5840f2512e6d916d605ac4f3b98d62f`: actual no.1 says `bei Übergabe oder Übersendung von Zahlungsmitteln am Tag des Eingangs, bei Hingabe oder Übersendung von Schecks jedoch drei Tage nach dem Tag des Eingangs`.

**Option A (recommended):** qualify the two grace statements by the actual AO224(2), no.1 exception, naming delivery/transmission of payment instruments such as cash or cheques, without changing the existing rate, fifty-euro rounding, ordinary transfer method or original examples. Add/reuse the exact source bindings.

**Option B:** remove the unconditional grace statement from those short rows and refer to AO240(3)'s actual payment-method condition. No new positive rule for a different payment channel is inferred.

Separating condition control: a late payment by a method within224(2), no.1 cannot be excused solely by invoking three-day grace. This does not change the independent due-date/effective-payment-time rules, the three-day deemed cheque timing, or the normal-transfer grace branch. No new source acquisition required.
