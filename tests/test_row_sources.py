"""Row-by-row figure check (scripts/check-row-sources.py): offline, with fake pages."""
import importlib.util
import json
import os
import unittest

spec = importlib.util.spec_from_file_location(
    "row_sources", os.path.join(os.path.dirname(__file__), "..", "scripts", "check-row-sources.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)

A = "https://tax.example.gov/a"
B = "https://tax.example.gov/b"


def skill(*rows, worked=""):
    table = "\n".join(rows)
    return f"## Rates, bands and thresholds\n\n| Item | Value | Source |\n|---|---|---|\n{table}\n\n## Worked cases\n\n{worked}\n"


def pages(**by_url):
    return lambda u: by_url.get(u)


class RowSources(unittest.TestCase):
    def test_korean_whole_money_compounds(self):
        for source, amount in [
            ('5억원', 500_000_000), ('250만원', 2_500_000),
            ('1억5천만원', 150_000_000), ('1억 6천만원', 160_000_000),
            ('4억 6천만원', 460_000_000), ('1,400만원', 14_000_000),
            ('1억7,406만원', 174_060_000), ('3억8,406만원', 384_060_000),
            ('6억원', 600_000_000), ('1억5만원', 100_050_000),
            ('1조2억3천4백5십6만원', 1_000_234_560_000),
            ('동일 5억원', 500_000_000), ('약5억원', 500_000_000),
            ('250만 원', 2_500_000),
        ]:
            with self.subTest(source=source):
                self.assertEqual(rs.page_values(source), {amount})
        self.assertEqual(rs.page_values('5억원 및 250만원'), {500_000_000, 2_500_000})

    def test_korean_compounds_never_match_wrong_scales_or_suffixes(self):
        for source, wrong in [
            ('15억원', '500,000,000'), ('1억5천만원', '50,000,000'),
            ('250만원', '250,000,000'), ('1억7,406만원', '74,060,000'),
            ('1억5만원', '150,000,000'), ('5억원', '5%'),
        ]:
            with self.subTest(source=source, wrong=wrong):
                self.assertFalse(rs.found(wrong, rs.page_values(source)))
        for source in ['1경5억원', '1억2억원', '5천천만원', '1,40만원',
                       '일억5천만원', '1억만원', '1천20백만원', '억원']:
            with self.subTest(malformed=source):
                self.assertEqual(rs.page_values(source), set())

    def test_korean_literal_fractions_mask_denominators_and_coefficients(self):
        for source, percent in [
            ('100분의20', 20), ('1천분의20', 2), ('1만분의25', 0.25),
            ('100분의2.5', 2.5), ('100분의20.', 20),
            ('법률에 따라 100분의20의 세율', 20), ('100분의20 이상', 20),
        ]:
            with self.subTest(source=source):
                self.assertEqual(rs.page_values(source), {percent})
        for source, wrong in [('100분의20', '100%'), ('1천분의20', '20%'),
                              ('1천분의20', '100%'), ('100분의2.5', '100%')]:
            with self.subTest(source=source, wrong=wrong):
                self.assertFalse(rs.found(wrong, rs.page_values(source)))
        for source in ['0분의20', '100분의20분의5', '1경5분의20', '1,00분의20']:
            with self.subTest(malformed=source):
                self.assertEqual(rs.page_values(source), set())

    def test_korean_malformed_fraction_continuations_do_not_match_a_valid_prefix(self):
        for source in ['100분의20분의', '100분의20분의X', '100분의20분의X20',
                       '100분의20분의 X20', '100분의20분의5X20', '100분의20분의.']:
            with self.subTest(malformed=source):
                self.assertEqual(rs.page_values(source), set())
        for source in ['100분의20의 세율', '100분의20 이상', '100분의20.',
                       '법률에 따라 100분의20의 세율']:
            with self.subTest(valid=source):
                self.assertEqual(rs.page_values(source), {20})

    def test_korean_number_normalization_preserves_other_notations_and_policy(self):
        for source, figure in [('20퍼센트', '20%'), ('35퍼센트', '35%'),
                               ('twenty per cent', '20%'),
                               ('15 million shillings', '15,000,000'),
                               ('1,234.56', '1,234.56')]:
            with self.subTest(source=source):
                self.assertTrue(rs.found(figure, rs.page_values(source)))
        # Separate statutory rates do not establish their combined arithmetic result.
        self.assertFalse(rs.found('22%', rs.page_values('100분의20 및 100분의2')))
        text = skill(f'| Amount | KRW 500,000,000 | [law]({A}) |')
        self.assertEqual(rs.check_text(text, pages(**{A: '금액 5억원'})), (1, [], []))
        text = skill(f'| Amount | KRW 50,000,000 | [law]({A}) |')
        self.assertEqual([m[0] for m in rs.check_text(text, pages(**{A: '금액 1억5천만원'}))[1]],
                         ['50,000,000'])

    def test_figure_on_linked_page_passes(self):
        t = skill(f"| Rate | 5.20% up to $23,000 | [law]({A}) |")
        n, misses, unreadable = rs.check_text(t, pages(**{A: "rate 5.2% of income not over $23000 " * 20}))
        self.assertEqual((n, misses, unreadable), (1, [], []))

    def test_swiss_apostrophe_thousands(self):
        t = skill(f"| Threshold | CHF 80,000 | [law]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "Freibetrag Fr. 80'000 pro Jahr " * 40}))
        self.assertEqual(misses, [])

    def test_rates_written_in_words(self):
        for page, row in [("the rate is twenty per cent of the gain", "20%"),
                          ("aliquota del dieci per cento", "10%"),
                          ("tipo del veintiuno por ciento", "21%"),
                          ("taux de quatre-vingt-dix pour cent", "90%"),
                          ("按百分之二十五的税率", "25%")]:
            with self.subTest(page=page):
                t = skill(f"| Rate | {row} | [law]({A}) |")
                _, misses, _ = rs.check_text(t, pages(**{A: (page + " ") * 40}))
                self.assertEqual(misses, [])

    def test_wrong_rate_in_words_still_misses(self):
        t = skill(f"| Rate | 25% | [law]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "the rate is twenty per cent " * 40}))
        self.assertEqual([m[0] for m in misses], ["25%"])

    def test_fractional_word_rates_and_wrong_rate_controls(self):
        for page, figure in [
            ('one and a half percentum', '1.5%'),
            ('ONE AND A\nHALF PERCENTUM', '1.5%'),
            ('one and one-half per cent', '1.5%'),
            ('one and one-\nhalf percentum', '1.5%'),
            ('one-hundred and a half percentum', '100.5%'),
            ('The levy and one and a half percent apply.', '1.5%'),
            ('Apply a one and a half percent levy.', '1.5%'),
            ('twenty percent and one and a half percent', '1.5%'),
            ('one percent and a half percent', '0.5%'),
            ('two and a half percent', '2.5%'),
            ('twenty-one and a half percentum', '21.5%'),
            ('twenty one and a half percentum', '21.5%'),
            ('twenty\none and a half percentum', '21.5%'),
            ('twenty-\none and a half percentum', '21.5%'),
            ('half per cent', '0.5%'),
            ('one half percentum', '0.5%'),
        ]:
            with self.subTest(page=page):
                text = skill(f'| Charge | {figure} | [law]({A}) |')
                _, misses, _ = rs.check_text(text, pages(**{A: page}))
                self.assertEqual(misses, [])
        for page, figure in [
            ('one and a half percentum', '15%'),
            ('one and a half percentum', '2.5%'),
            ('one half percentum', '1.5%'),
            ('one and a half months; contribution is two percentum', '1.5%'),
            ('one and a half per thousand', '1.5%'),
            ('one and a half percentage points', '1.5%'),
            ('one and a half percentumage', '1.5%'),
            ('section one and a half; chapter percentum', '1.5%'),
            ('twenty\none and a half percentum', '1.5%'),
            ('twenty-\none and a half percentum', '1.5%'),
            ('one and one-\nhalf percentum', '0.5%'),
            ('three hundred and a half percentum', '0.5%'),
            ('two hundred and one and a half percentum', '1.5%'),
            ('one-hundred and a half percentum', '0.5%'),
            ('and three hundred and a half percentum', '0.5%'),
            ('a two hundred and one and a half percentum', '1.5%'),
        ]:
            with self.subTest(page=page, wrong=figure):
                text = skill(f'| Charge | {figure} | [law]({A}) |')
                _, misses, _ = rs.check_text(text, pages(**{A: page}))
                self.assertEqual([m[0] for m in misses], [figure])

    def test_explicit_million_and_billion_amounts(self):
        for page, figure in [
            ('annual turnover exceeding 1.8 million baht', '1,800,000'),
            ('turnover 1.8 billion baht', '1,800,000,000'),
            ('turnover 2 MILLION baht', '2,000,000'),
            ('turnover 1,234 million baht', '1,234,000,000'),
        ]:
            with self.subTest(page=page):
                text = skill(f'| Threshold | THB {figure} | [law]({A}) |')
                _, misses, _ = rs.check_text(text, pages(**{A: page}))
                self.assertEqual(misses, [])
        for page in ['1.8 months', '18 million baht', 'bare 1.8', '1.8 millionth', '1,8 million baht']:
            with self.subTest(wrong_scale=page):
                text = skill(f'| Threshold | THB 1,800,000 | [law]({A}) |')
                _, misses, _ = rs.check_text(text, pages(**{A: page}))
                self.assertEqual([m[0] for m in misses], ['1,800,000'])

    def test_whole_english_monetary_scales(self):
        for page, figure in [
            ('fifteen million shillings', '15,000,000'),
            ('ten million shillings', '10,000,000'),
            ('twenty-one million dollars', '21,000,000'),
            ('twenty one million dollars', '21,000,000'),
            ('one hundred and fifteen million shillings', '115,000,000'),
            ('nine hundred ninety nine billion rupees', '999,000,000,000'),
            ('FIFTEEN\nMILLION\nSHILLINGS', '15,000,000'),
            ('twenty-\none million pounds', '21,000,000'),
            ('twenty\u2011one million pounds', '21,000,000'),
            ('one-hundred million euros', '100,000,000'),
            ('thirty million baht', '30,000,000'),
            ('two billion rand', '2,000,000,000'),
            ('the allowance and fifteen million shillings', '15,000,000'),
            ('apply a fifteen million shilling limit', '15,000,000'),
        ]:
            with self.subTest(page=page):
                self.assertTrue(rs.found(figure, rs.word_money_values(page)))
                text = skill(f'| Threshold | {figure} | [law]({A}) |')
                self.assertEqual(rs.check_text(text, pages(**{A: page})), (1, [], []))

    def test_word_money_never_falls_back_to_smaller_suffixes(self):
        for page in [
            'one thousand fifteen million shillings',
            'one thousand, fifteen million shillings',
            'one million fifteen million shillings',
            'one trillion fifteen million shillings',
            'one sextillion fifteen million shillings',
            'two hundred and one and a half million shillings',
            'one point five million shillings',
            'minus fifteen million shillings',
            'zero fifteen million shillings',
            'one two million shillings',
            'a one thousand fifteen million shillings',
            'and one thousand fifteen million shillings',
            'a and fifteen million shillings',
            'and and fifteen million shillings',
        ]:
            with self.subTest(page=page):
                self.assertEqual(rs.word_money_values(page), set())
                text = skill(f'| Threshold | 15,000,000 | [law]({A}) |')
                _, misses, unreadable = rs.check_text(text, pages(**{A: page}))
                self.assertEqual(([m[0] for m in misses], unreadable), (['15,000,000'], []))

    def test_word_money_requires_amount_context_and_correct_value(self):
        for page in [
            'fifteen billion shillings', 'sixteen million shillings', 'ten million shillings',
            'fifteen million visitors', 'fifteen million months', 'bare fifteen million',
            'fifteen millionth shillings', 'million shillings', 'fifteenmillion shillings',
            'Section fifteen million shillings', 'Form: fifteen million dollars',
            'Form_fifteen million shillings', 'ref-fifteen million shillings',
            '1 fifteen million shillings', 'fifteen million shillings_identifier',
            '1, fifteen million shillings', 'ref.fifteen million shillings',
            'fifteen million shillings-id', 'fifteen million . OAG shillings',
            'ref\u2011fifteen million shillings', 'fifteen million shillings\u2011id',
            'fifteen million USD', 'USD fifteen million',
        ]:
            with self.subTest(page=page):
                text = skill(f'| Threshold | 15,000,000 | [law]({A}) |')
                _, misses, unreadable = rs.check_text(text, pages(**{A: page}))
                self.assertEqual(([m[0] for m in misses], unreadable), (['15,000,000'], []))

    def test_actual_tanzania_definition_clauses_keep_their_own_amounts(self):
        # ITA s.3, OSG A.S.2025; PDF SHA256 53599ac147250ed28cf5507aa13731beca
        # c8eea7365946884cb4544bcc9e4c4a. Full exclusion limbs, not guessed thresholds.
        residence = '''a private residence of an individual that has
            been owned continuously for three years or
            more and lived in by the individual
            continuously or intermittently for a total of
            three years or more, other than a private
            residence that is realised for a gain in excess of
            fifteen million shillings;'''
        land = '''an interest in land held by an individual that has
            a market value of less than ten million shillings
            at the time it is realised and that has been used
            for agricultural purposes for at least two of the
            three years prior to realisation;'''
        for clause, right, wrong in [(residence, '15,000,000', '10,000,000'),
                                     (land, '10,000,000', '15,000,000')]:
            with self.subTest(clause=clause):
                text = skill(f'| Threshold | {right} | [law]({A}) |')
                self.assertEqual(rs.check_text(text, pages(**{A: clause})), (1, [], []))
                text = skill(f'| Wrong threshold | {wrong} | [law]({A}) |')
                _, misses, unreadable = rs.check_text(text, pages(**{A: clause}))
                self.assertEqual(([m[0] for m in misses], unreadable), ([wrong], []))

    def test_url_with_brackets_is_kept_whole(self):
        u = "https://law.example.gov/act_(01-07-24).pdf"
        t = skill(f"| Rate | 7% | [act]({u}) |")
        _, misses, unreadable = rs.check_text(t, pages(**{u: "rate 7% " * 80}))
        self.assertEqual((misses, unreadable), ([], []))

    def test_zip_of_pdfs_is_read(self):
        import io, zipfile
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            z.writestr("doc.xml", "<a>rate 9%</a>")
        self.assertIn("9%", rs.read_bytes(buf.getvalue()))

    def test_table_in_attribute_is_read(self):
        page = '<div data-table="{&quot;column_1&quot;:{&quot;text&quot;:&quot;Kauniainen 4,70&quot;}}"></div>' + "x" * 500
        self.assertIn("Kauniainen 4,70", rs.read_bytes(page.encode()))

    def test_next_js_page_text_is_read(self):
        page = ('<html><body><nav>menu</nav><script>self.__next_f.push([1,"Veroprosentti on '
                'v\\u00e4hint\\u00e4\\u00e4n 1,30 ja enint\\u00e4\\u00e4n 2,00 \\u003cb\\u003eprosenttia\\u003c/b\\u003e"])'
                '</script></body></html>')
        text = rs.read_bytes(page.encode())
        self.assertIn("vähintään 1,30 ja enintään 2,00", text)
        self.assertNotIn("<b>", text)

    def test_next_data_article_is_read_without_metadata_numbers(self):
        data = {'props': {'pageProps': {
            'response': {'news_detial': {'detail': '<p>Government pays <b>2.75%</b> &amp; employers pay 5%.</p>',
                                        'articleId': 918273}},
            'analytics': {'rate': '9.75%', 'body': 'not article text 8.25%'},
        }}}
        page = '<script type="application/json" id="__NEXT_DATA__">' + json.dumps(data) + '</script>'
        text = rs.read_bytes(page.encode())
        self.assertIn('2.75%', text)
        self.assertIn('& employers pay 5%', text)
        self.assertNotIn('<b>', text)
        self.assertNotIn('918273', text)
        values = rs.page_values(text)
        self.assertTrue(rs.found('2.75%', values))
        self.assertFalse(rs.found('9.75%', values))
        self.assertFalse(rs.found('8.25%', values))

    def test_next_data_without_article_does_not_supply_metadata(self):
        for data in [
            {'props': {'pageProps': {'analytics': {'rate': '2.75%'}}}},
            {'props': {'pageProps': {'response': {'news_detial': {'id': '2.75'}}}}},
            {'props': {'pageProps': []}},
            {'props': None},
            [],
        ]:
            with self.subTest(data=data):
                page = '<script id="__NEXT_DATA__">' + json.dumps(data) + '</script>'
                self.assertFalse(rs.found('2.75%', rs.page_values(rs.read_bytes(page.encode()))))

    def test_invalid_next_data_and_other_scripts_remain_ignored(self):
        for page in [
            '<script id="__NEXT_DATA__">{not valid JSON 2.75%}</script>',
            '<script data-id="__NEXT_DATA__">{"props":{"pageProps":{"body":"2.75%"}}}</script>',
            '<script id="analytics">{"props":{"pageProps":{"body":"2.75%"}}}</script>',
            '''<script data-title=' id="__NEXT_DATA__"'>{"props":{"pageProps":{"body":"2.75%"}}}</script>''',
            '''<script id="analytics" data-title=' id="__NEXT_DATA__"'>{"props":{"pageProps":{"body":"2.75%"}}}</script>''',
            '''<script id="analytics" id="__NEXT_DATA__">{"props":{"pageProps":{"body":"2.75%"}}}</script>''',
        ]:
            with self.subTest(page=page):
                self.assertFalse(rs.found('2.75%', rs.page_values(rs.read_bytes(page.encode()))))

    def test_next_data_uses_real_single_double_or_unquoted_id(self):
        body = json.dumps({'props': {'pageProps': {'article': {'body': 'Actual article 2.75%'}}}})
        for attrs in ['id="__NEXT_DATA__"', "id='__NEXT_DATA__'", 'ID=__NEXT_DATA__',
                      '''data-title=' id="analytics"' id="__NEXT_DATA__"''']:
            with self.subTest(attrs=attrs):
                text = rs.read_bytes(('<script ' + attrs + '>' + body + '</script>').encode())
                self.assertTrue(rs.found('2.75%', rs.page_values(text)))

    def test_next_data_article_script_and_style_are_not_source_text(self):
        data = {'props': {'pageProps': {'article': {'body': '<p>5%</p><script>9.75%</script><style>8.25%</style>'}}}}
        page = '<script id="__NEXT_DATA__">' + json.dumps(data).replace('<', '\\u003c') + '</script>'
        values = rs.page_values(rs.read_bytes(page.encode()))
        self.assertTrue(rs.found('5%', values))
        self.assertFalse(rs.found('9.75%', values))
        self.assertFalse(rs.found('8.25%', values))

    def test_decimal_comma_pages_pass(self):
        t = skill(f"| Rate | 2.25% on EUR 4,050 | [law]({A}) |", f"| Cap | EUR 1,234.56 | [b]({B}) |")
        n, misses, _ = rs.check_text(t, pages(**{A: "taxa 2,25 % peste 4.050 lei " * 30,
                                                  B: "plafond 1\u202f234,56 euros " * 30}))
        self.assertEqual((n, misses), (2, []))

    def test_wrong_figure_still_misses_on_decimal_comma_page(self):
        t = skill(f"| Rate | 2.5% | [law]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "taxa 2,25 % in 2026 100 lei " * 30}))
        self.assertEqual([m[0] for m in misses], ["2.5%"])

    def test_figure_missing_from_its_own_page_is_a_miss(self):
        t = skill(f"| Rate | 6.5% | [law]({A}) |", f"| Base | $184,500 | [ssa]({B}) |")
        n, misses, _ = rs.check_text(t, pages(**{A: "the rate is 6.5 percent " * 30, B: "base 176,100 " * 40}))
        self.assertEqual(n, 2)
        self.assertEqual([m[0] for m in misses], ["$184,500"])

    def test_figure_on_another_rows_page_does_not_count(self):
        t = skill(f"| Rate | 7% | [a]({A}) |", f"| Other | 3% | [b]({B}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "seven 3% " * 50, B: "three 3% " * 50}))
        self.assertEqual([m[0] for m in misses], ["7%"])

    def test_same_inherits_the_link_above(self):
        t = skill(f"| Rate | 4% | [a]({A}) |", "| Reduced | 1.5% | same |")
        n, misses, _ = rs.check_text(t, pages(**{A: "4% and 1.5% apply " * 30}))
        self.assertEqual((n, misses), (2, []))

    def test_unreadable_page_is_not_a_miss(self):
        t = skill(f"| Rate | 9% | [a]({A}) |")
        n, misses, unreadable = rs.check_text(t, pages())
        self.assertEqual((n, misses, len(unreadable)), (1, [], 1))

    def test_rate_sheet_decimal_counts_for_percent(self):
        t = skill(f"| Homer | 4.85% | [sheet]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "Homer City 4.8500000000000001E-2 0.0485 " * 20}))
        self.assertEqual(misses, [])

    def test_statute_and_form_numbers_are_not_figures(self):
        self.assertEqual(rs.figures(f"| Rate | section 79-32,110 Form 1,040 | [a]({A}) |"), [])

    def test_derived_rows_and_zero_are_not_misses(self):
        t = skill(f"| MFS | $125,000 (derived: half of $250,000) | [a]({A}) |", f"| Band | $0 to $10,000 | [a]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "10,000 joint 250,000 " * 30}))
        self.assertEqual(misses, [])

    def test_in_words_marker_and_dot_leaders(self):
        t = skill(f"| Rate | 6% (in words on the page) | [a]({A}) |", f"| Tax | $3,916.09 | [b]({B}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "six percent " * 40, B: "over 250,400.....3,916.09 plus " * 20}))
        self.assertEqual(misses, [])

    def test_worked_cases_are_skipped(self):
        t = skill(f"| Rate | 2% | [a]({A}) |", worked=f"| Tax | $9,999 | [a]({A}) |")
        _, misses, _ = rs.check_text(t, pages(**{A: "2% " * 200}))
        self.assertEqual(misses, [])


if __name__ == "__main__":
    unittest.main()
