"""Actual callable startup surfaces use the current method, never a guessed fallback."""

import tempfile
from hashlib import sha256
from pathlib import Path
import unittest
from unittest.mock import patch

from mcp.client import Client
from openaccountants_mcp import server


def document(name, body, status=""):
    return (f"---\nname: {name}\njurisdiction: XX\ncategory: international\ntier: 2\n"
            + (f"status: {status}\n" if status else "")
            + f"---\n\n# {name}\n\n{body}\n")


class StartupMethodTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.packages = Path(self.temp.name)
        self.patch = patch.object(server, "PACKAGES_DIR", self.packages)
        self.patch.start()
        server._index.cache_clear()
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(self.patch.stop)
        self.addCleanup(server._index.cache_clear)
        self.method = self.write("workflow-base", "Keep the unexplained 400 receipt unresolved. A confirmed legal default requires its trigger evidence.")
        self.write("xx-income-tax", "Fictional country rules, no assumed approval.")

    def write(self, name, body, status="", folder="xx"):
        path = self.packages / folder / f"{name}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(document(name, body, status))
        return path

    def prompts(self):
        return [lambda: server.skill_review("xx-income-tax", "unexplained receipt"),
                lambda: server.tax_return("XX", "2026", "fictional"),
                lambda: server.vat_check("XX"), lambda: server.find_deductions("XX"),
                lambda: server.compare_jurisdictions("XX, YY")]

    def current_hash(self):
        _, body = server._parse_frontmatter(self.method.read_text())
        return sha256(body.encode()).hexdigest()

    def test_tools_and_all_start_branches_load_actual_current_method(self):
        outputs = [server.get_skill("xx-income-tax"), server.get_skill_sections("xx-income-tax")]
        outputs += [server.start(), server.start("taxes"), server.start(jurisdiction="XX"),
                    server.start("taxes", "XX"), server.start("gibberish"),
                    server.start("taxes", "YY")]
        for out in outputs:
            with self.subTest(status=out.get("status"), slug=out.get("slug")):
                self.assertEqual(out["workflow"]["status"], "available")
                self.assertEqual(out["workflow"]["body_sha256"], self.current_hash())
                self.assertNotIn("markdown", out["workflow"])
                self.assertTrue(out["workflow"]["load_required"])
                self.assertIn("get_skill('workflow-base')", out["workflow"]["load_instruction"])
                self.assertIn("does not mean", out["workflow"]["load_instruction"])
                self.assertEqual(out["application_status"], "blocked" if out.get("status") == "uncovered" else "available")
                self.assertTrue(any("unresolved" in s for s in out["guardrails"]))
        plan = server.start("taxes", "XX")
        self.assertEqual(plan["skills_to_load"][0]["slug"], "workflow-base")

    def test_method_without_applicable_country_content_is_not_a_ready_plan(self):
        self.method.write_text(document("workflow-base", "General preparation only.").replace(
            "jurisdiction: XX", "jurisdiction: GLOBAL").replace("category: international", "category: foundation"))
        server._index.cache_clear()
        plan = server.start("taxes", "GLOBAL")
        self.assertEqual(plan["status"], "uncovered")
        self.assertEqual(plan["application_status"], "blocked")
        self.assertEqual(plan["workflow"]["status"], "available")
        self.assertEqual(plan["skills_to_load"], [])
        self.assertIn("list_skills", plan["next_action"])
        self.assertIn("General preparation only", server.get_skill("workflow-base")["markdown"])
        self.write("cross-border-tax-router", "Route after real countries are established.", folder="global").write_text(
            document("cross-border-tax-router", "Route after real countries are established.").replace("jurisdiction: XX", "jurisdiction: GLOBAL"))
        server._index.cache_clear()
        self.assertEqual(server.start("taxes", "GLOBAL")["status"], "uncovered")
        self.assertEqual(server.start("taxes", "INTL")["status"], "uncovered")

    def test_preparation_prompts_include_method_and_do_not_claim_assumed_facts_or_approval(self):
        for prompt in self.prompts():
            text = prompt()
            self.assertIn(self.current_hash(), text)
            self.assertIn("get_skill('workflow-base')", text)
            self.assertNotIn("unexplained 400 receipt unresolved", text)
            for unsafe in ("assume MORE tax", "conservative default applied", "verified by [verifier name]",
                           "classify from the transaction description and flag as Assumed", "No LLM computes"):
                self.assertNotIn(unsafe, text)
        self.assertIn("conditions", server.vat_check("XX"))
        self.assertIn("available", server.tax_return("XX"))

    def test_missing_method_blocks_application_but_preserves_inspection(self):
        self.method.unlink()
        server._index.cache_clear()
        for read in (server.get_skill, server.get_skill_sections):
            out = read("xx-income-tax")
            self.assertEqual(out["application_status"], "blocked")
            self.assertEqual(out["workflow"]["status"], "unavailable")
            self.assertIn("Do not apply", out["next_action"])
        plan = server.start("taxes", "XX")
        self.assertEqual(plan["status"], "blocked")
        self.assertEqual(plan["skills_to_load"], [])
        for prompt in self.prompts():
            with self.assertRaisesRegex(server.ToolInputError, "workflow-base.*unavailable"):
                prompt()

    def test_new_hold_or_conflicting_alias_blocks_even_after_catalogue_warmup(self):
        for problem in ("hold", "conflict"):
            with self.subTest(problem=problem):
                self.assertEqual(server.get_skill("xx-income-tax")["application_status"], "available")
                if problem == "hold":
                    self.method.write_text(document("workflow-base", "Do not use", "needs_sources"))
                else:
                    alias = self.write("workflow-base", "Different method", folder="yy")
                    server._index.cache_clear()
                self.assertEqual(server.get_skill("xx-income-tax")["application_status"], "blocked")
                if problem == "conflict":
                    alias.unlink()
                self.method.write_text(document("workflow-base", "Current method."))
                server._index.cache_clear()

    def test_unreadable_method_does_not_fall_back_to_prior_body(self):
        self.assertEqual(server.get_skill("xx-income-tax")["application_status"], "available")
        read = Path.read_text
        def fail(path, *args, **kwargs):
            if path.resolve() == self.method.resolve():
                raise PermissionError("fictional revoked method read")
            return read(path, *args, **kwargs)
        with patch.object(Path, "read_text", fail):
            out = server.get_skill("xx-income-tax")
        self.assertEqual(out["application_status"], "blocked")
        self.assertNotIn("body_sha256", out["workflow"])

    def test_method_rewrite_is_read_fresh_and_full_source_is_preserved(self):
        first = server.get_skill("xx-income-tax")
        self.method.write_text(document("workflow-base", "Second current method; conditional only."))
        second = server.get_skill("xx-income-tax")
        self.assertNotEqual(first["workflow"]["body_sha256"], second["workflow"]["body_sha256"])
        self.assertEqual(second["workflow"]["body_sha256"], self.current_hash())
        _, raw_body = server._parse_frontmatter(self.method.read_text())
        full = server.get_skill("workflow-base")
        self.assertTrue(full["markdown"].startswith(raw_body))
        self.assertFalse(full["workflow"]["load_required"])
        self.assertNotIn("get_skill('workflow-base')", full["next_action"])


class StartupSDKTests(unittest.IsolatedAsyncioTestCase):
    async def test_client_receives_blocked_method_without_an_execution_plan(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(server, "PACKAGES_DIR", Path(temp)):
            server._index.cache_clear()
            path = Path(temp) / "tax.md"
            path.write_text(document("xx-income-tax", "Fictional source."))
            async with Client(server.mcp) as client:
                result = await client.call_tool("start", {"intent": "taxes", "jurisdiction": "XX"})
            self.assertFalse(result.is_error)
            data = result.structured_content
            self.assertEqual(data["status"], "blocked")
            self.assertEqual(data["skills_to_load"], [])
            server._index.cache_clear()


if __name__ == "__main__":
    unittest.main()
