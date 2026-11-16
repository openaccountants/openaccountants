"""Protected inherited credit bytes are not a reason to rewrite a person's credit."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import skill_checks as checks


ARTIN = '*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) — MIT License.*'
CONTACT = '*OpenAccountants — open-source accounting skills for AI — info@openaaccountants.com*'
DATED_CONTACT = '*Data reflects 2025–2026 rules. OpenAccountants — open-source accounting skills for AI — info@openaccountants.com*'


class ProtectedCreditStyle(unittest.TestCase):
    def check(self, text):
        return checks.check_no_em_dash('example.md', text, {})

    def test_actual_incorporation_two_original_lines_keep_all_three_dashes(self):
        path = ROOT / 'skills/global/cross-border/international-incorporation.md'
        lines = path.read_text().splitlines()
        self.assertEqual(lines[-2:], [ARTIN, CONTACT])
        self.assertEqual((ARTIN + CONTACT).count('—'), 3)
        self.assertEqual(self.check('\n'.join(lines[-2:])), [])
        self.assertEqual(self.check('\r\n'.join(lines[-2:]) + '\r\n'), [])

    def test_actual_invoice_footer_is_exempt_but_authored_description_is_not(self):
        path = ROOT / 'skills/global/cross-border/cross-border-invoicing-compliance.md'
        self.assertEqual(path.read_text().splitlines()[-1], DATED_CONTACT)
        self.assertEqual(self.check(DATED_CONTACT), [])
        text = '---\ndescription: New authored wording — still checked\n---\n' + DATED_CONTACT
        self.assertEqual(self.check(text), ['1 em dash(es)'])

    def test_other_exact_inherited_platform_form(self):
        line = '*OpenAccountants — open-source tax computation skills — info@openaccountants.com*'
        self.assertEqual(self.check(line), [])

    def test_credit_prefix_cannot_hide_appended_claims_or_changed_fields(self):
        for line in [
            ARTIN + ' VAT is 20%', CONTACT + ' Tax is 0%',
            ARTIN[:-1] + ' Tax rate 0%*', CONTACT[:-1] + ' Tax rate 0%*',
            DATED_CONTACT.replace('2025–2026', '2026–2027'),
            CONTACT.replace('open-source accounting skills for AI', 'tax-free companies'),
            ARTIN.replace('MIT License.', 'MIT License. VAT 20%'),
            ARTIN.replace('MIT', 'Another'), ARTIN.replace('Artin', 'Someone'),
            CONTACT.replace('info@openaaccountants.com', 'info@example.com'),
            CONTACT + '\u2028VAT is 20%', CONTACT + '\rVAT is 20%',
            ' ' + CONTACT, CONTACT + ' ',
        ]:
            with self.subTest(line=line):
                self.assertEqual(self.check(line), [f"{line.count('—')} em dash(es)"])

    def test_ordinary_prose_and_markdown_wrappers_stay_checked(self):
        for text in [
            'Tax — 20%', '# Heading — example', '| Rate | — |',
            '> ' + ARTIN, '# ' + CONTACT, '| ' + CONTACT + ' |',
            'New prose: ' + CONTACT, '```markdown\n' + ARTIN + '\n```',
            '---\ndescription: |\n  ' + CONTACT + '\n---\nBody.',
        ]:
            with self.subTest(text=text):
                self.assertEqual(self.check(text), [f"{text.count('—')} em dash(es)"])

    def test_footer_heading_or_credit_does_not_exempt_following_prose(self):
        text = '## Footer\n' + CONTACT + '\nNew tax claim — 20%\n'
        self.assertEqual(self.check(text), ['1 em dash(es)'])
        self.assertEqual(self.check(ARTIN + '\nNew authored prose — example'), ['1 em dash(es)'])

    def test_existing_platform_cta_behavior_is_unchanged(self):
        self.assertEqual(self.check('Writer — text\n' + checks.CTA_MARKER + '\nCTA — text'),
                         ['1 em dash(es)'])
        self.assertEqual(self.check(CONTACT + '\n' + checks.CTA_MARKER + '\nCTA — text'), [])


if __name__ == '__main__':
    unittest.main()
