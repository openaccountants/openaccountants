"""Public Guide attribution and legacy display-metadata filtering."""
import re
import yaml

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


def sanitize_markdown(text, metadata=None):
    """Remove Guide endorsement metadata, preserving legal review instructions."""
    metadata = metadata or {}
    # The stored source remains unchanged. Generated copies omit legacy scalar
    # metadata, including indented continuations of a removed YAML field.
    if text.startswith("---\n"):
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if match:
            try:
                parsed = yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                parsed = None
            if isinstance(parsed, dict):
                metadata = parsed
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
    standalone_values = {"pending", "pending_review", "research-verified", "accountant-verified", "accountant-reviewed", "1", "2"}
    for key in ("reviewed_by", "verified_by", "reviewer"):
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            standalone_values.add(value.strip().casefold())

    def remove_standalone_metadata(match):
        value = match.group("value").strip().strip("*").strip().casefold()
        return "" if value in standalone_values else match.group(0)

    text = re.sub(
        r"(?im)^[ \t]*(?:[-*>][ \t]*)?(?:\*{1,2})?(?:Reviewed by|Verified by|Checked by|Attested by|Lead verifier|Jurisdiction reviewer|Review status|Quality tier|Verification status)(?:\*{1,2})?[ \t]*:[ \t]*(?P<value>[^\n]*)(?:\n|$)",
        remove_standalone_metadata, text,
    )
    # Remove the dated endorsement, retaining any following limitations or instructions.
    person = r"(?:\*\*)?(?:a licensed accountant|[A-Z][\w'’-]*(?:[ \t]+[A-Z][\w'’-]*){1,5})(?:\*\*)?"
    text = re.sub(
        r"(?m)^[ \t]*(?:>[ \t]*)?Reviewed against (?:the cited tax authorities|the cited sources|official sources) by "
        + person + r" on \d{4}-\d{2}-\d{2}\.[ \t]*(?:\n|$)?", "", text,
    )
    text = re.sub(
        r",?[ \t]*method attested by " + person
        + r"(?: on \d{4}-\d{2}-\d{2})?(?: \((?:https?://)?openaccountants\.com/network/[^)\n]+\))?",
        "", text,
    )
    text = re.sub(r"(?i)[ \t]*\((?:Tier [12][ \t]*[—:-][ \t]*)?(?:accountant[- ](?:reviewed|verified)|research[- ]verified|attested by another accountant)(?:,[ \t]*(?:reviewer sign-off pending|pending accountant sign-off))?\)", "", text)
    text = re.sub(r"(?im)^(#{1,6}\s+)Verified (rates[^\n]*)", r"\1\2", text)
    text = re.sub(r"(?i)\baccountant[- ](?:reviewed|verified)\s+(?=(?:(?:UK VAT|uk-vat-return)\s+|\[[^\]\n]+\]\([^\n)]+\)\s+)?Guide\b)", "", text)
    return re.sub(r"(?i)Michael Cutajar and (?:the )?OpenAccountants team", PUBLISHER, text)
