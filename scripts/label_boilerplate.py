"""Old trust-label text that is not skill content.

The trust label lives in frontmatter only (docs/skill-template.md line 11):
Built from the law, plus Approved by [name]. Older exports also wrote label
claims into the body ("Source-cited draft: not reviewed by an accountant",
"Validated by | Pending", a "Talk to a verified accountant" footer). They
contradict the frontmatter and say nothing about tax.

`strip(body)` removes exactly these. The checks compare bodies after
`strip`, so deleting one of these lines is not a content change: it neither
fails old content on the content checks nor clears an approval. Anything
not listed here is content. Add a pattern only for text that makes a label
claim and carries no tax fact.
"""

import re

# The footer section only: from the CTA marker (or the heading) up to the next
# heading of any level or the end of the file. Content after it (a Sources table, figures)
# is kept.
CTA_TAIL = re.compile(
    r"\n*(?:<!-- openaccountants-cta-block -->\s*\n)?(?:---\s*\n\s*)?## Talk to a verified accountant\n"
    r"(?:(?!#{1,6} ).*\n?)*",
)

# Whole lines only. A line that also carries other text stays.
LINES = [re.compile(p) for p in (
    r"^The most up-to-date(?:, verified)? version of this skill is maintained at .*$",
    r"^>?\s*(?:\*\*)?Source-cited draft(?:: not reviewed by an accountant)?(?:, not for filing)?\.?(?:\*\*)?"
    r"(?: Built by Michael Cutajar and the OpenAccountants team\.)?\s*$",
    r"^Built by Michael Cutajar and the OpenAccountants team\.(?: (?:\*\*)?Source-cited draft: not reviewed by an accountant\.(?:\*\*)?)?\s*$",
    r"^\|\s*Validated [Bb]y\s*\|\s*Pending[^|]*\|\s*$",
    r"^\|\s*Quality tier\s*\|[^|]*\|\s*$",
    # Old reviewer lines in the body. Who approved a skill lives in the frontmatter
    # (reviewed_by); a body line naming a reviewer is a label claim, not tax content.
    r"^>?\s*Reviewed against the cited tax authorities by .*$",
    r"^\|\s*(?:Validated by|Validation date|Verified by)\s*\|[^|]*\|\s*$",
)]

RENAMES = (
    ("## Verified rates & thresholds (accountant-reviewed)", "## Rates and thresholds"),
)


LINK_DEFINITION = re.compile(r"^\[[^\]]+\]:\s*\S", re.M)


def _drop_footer(match):
    # Keep link definitions that happen to sit inside the footer: the text
    # above refers to them.
    kept = [line for line in match.group(0).split("\n") if LINK_DEFINITION.match(line)]
    return "\n\n" + "\n".join(kept) + ("\n" if kept else "")


def strip(body):
    body = CTA_TAIL.sub(_drop_footer, body)
    for old, new in RENAMES:
        body = body.replace(old, new)
    kept = [line for line in body.split("\n") if not any(p.match(line) for p in LINES)]
    body = "\n".join(kept)
    return re.sub(r"\n{3,}", "\n\n", body).rstrip() + "\n"


def body_of(text):
    """Body without the frontmatter block."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def same_content(old_text, new_text):
    """True when two versions differ only in frontmatter or old label text."""
    return strip(body_of(old_text)) == strip(body_of(new_text))
