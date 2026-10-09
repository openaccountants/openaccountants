"""Public Guide attribution and legacy display-metadata filtering (stdlib only)."""
import re

PUBLISHER = "OpenAccountants"
FOUNDER_CREDIT = "OpenAccountants · Founded by Michael Cutajar"
FOUNDER_PROFILE = "https://www.openaccountants.com/network/ecd6fe97-c3ed-4337-8e12-d1e7456201a9"
RETIRED_FIELDS = {
    "tier", "quality_tier", "review_status", "reviewed_by", "verified_by",
    "verified_at", "reviewed_at", "reviewer", "reviewer_credential", "trust_label",
    "verification_status", "attestations", "attestation_count",
}


def attribution(meta):
    """Only an explicit author field is authorship; reviewers never are."""
    author = meta.get("authored_by")
    if not isinstance(author, str) or not author.strip():
        author = None
    elif author.strip().lower() in {
        "openaccountants", "openaccountants team",
        "michael cutajar and the openaccountants team",
        "michael cutajar and openaccountants team",
    } or meta.get("content_origin") == "automated-draft":
        author = None
    return {
        "publisher": PUBLISHER,
        "founder_credit": FOUNDER_CREDIT,
        "founder_profile": FOUNDER_PROFILE,
        "authored_by": author.strip() if author else None,
        "author_profile": meta.get("author_profile") if author else None,
    }


def sanitize_markdown(text):
    """Remove Guide endorsement metadata, preserving legal review instructions."""
    # The stored source remains unchanged. Generated copies omit legacy scalar
    # metadata, including indented continuations of a removed YAML field.
    if text.startswith("---\n"):
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if match:
            lines, dropping = [], False
            for line in match.group(1).splitlines():
                key = re.match(r"^([\w-]+):", line)
                if key:
                    dropping = key.group(1) in RETIRED_FIELDS
                if not dropping:
                    lines.append(line)
            if not any(line.startswith("publisher:") for line in lines):
                lines.append("publisher: OpenAccountants")
            text = "---\n" + "\n".join(lines) + "\n---\n" + text[match.end():]
    text = re.sub(
        r"(?im)^\s*(?:[-*>]\s*)?(?:\*\*)?(?:Reviewed by|Verified by|Checked by|Attested by|Lead verifier|Jurisdiction reviewer|Review status|Quality tier|Verification status)(?:\*\*)?\s*:[^\n]*(?:\n|$)",
        "", text,
    )
    text = re.sub(r"(?im)^\s*(?:>\s*)?Reviewed against (?:the cited tax authorities|the cited sources|official sources) by [^\n]*(?:\n|$)", "", text)
    text = re.sub(r"(?im)^\s*(?:>\s*)?Verified by [^\n]*(?:\n|$)", "", text)
    text = re.sub(r"(?i)\s*\((?:accountant[- ](?:reviewed|verified)|research[- ]verified|attested by another accountant)\)", "", text)
    text = re.sub(r"(?im)^(#{1,6}\s+)Verified (rates[^\n]*)", r"\1\2", text)
    text = re.sub(r"(?i)\baccountant[- ](?:reviewed|verified)\s+(?=(?:(?:UK VAT|uk-vat-return)\s+|\[[^\]\n]+\]\([^\n)]+\)\s+)?Guide\b)", "", text)
    return re.sub(r"(?i)Michael Cutajar and (?:the )?OpenAccountants team", PUBLISHER, text)
