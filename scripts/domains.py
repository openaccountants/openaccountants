#!/usr/bin/env python3
"""Read docs/domains.yml: the one list of domains a skill can carry in ``domain:``.

The rules live in the data file; this module only reads it. Three callers:
scripts/skill_checks.py (the date rule, check a, and the source-host rule, check m),
scripts/validate-guides.py (through skill_checks) and scripts/build-library.py (the
official-host allow-list for library figures).

``resolve(value)`` says what a ``domain:`` value means:

    none      no value: checked as before (tax rules)
    website   a value the website writes (website_values): checked as before
    active    an active domain: its rules apply. Two ids are also website values
              (payroll, bookkeeping): scripts/skill_checks.py applies their rules only
              to a file that carries the domain's date field, so files the website
              labelled are checked as before
    proposed  a proposed domain: checked as before, with a warning
    unknown   not in the file: checked as before, with a warning
    unreadable  the file could not be read: checked as before, with a warning
"""

import os
import re

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
DOMAINS_FILE = os.path.join(REPO_ROOT, "docs", "domains.yml")
TAX = "tax"

#: Government second-level domains: anything.gov, x.gov.ie, x.gob.mx, x.gouv.fr,
#: x.govt.nz, x.gv.at, x.go.jp. A domain with ``government: true`` accepts these.
GOVERNMENT_HOST_RE = re.compile(r"(?:^|\.)(?:gov|(?:gov|gob|gouv|govt|gv|go)\.[a-z]{2})$")

_cache = {}


class DomainsError(Exception):
    """docs/domains.yml is missing or not the shape this module reads."""


def load(path=None):
    """The parsed file, ``{"website_values": set, "domains": {id: dict}}``, cached per path."""
    path = path or DOMAINS_FILE
    if path not in _cache:
        try:
            import yaml
            with open(path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except Exception as exc:  # missing file, no PyYAML, bad YAML
            raise DomainsError(f"{os.path.relpath(path, REPO_ROOT)} could not be read: {exc}") from exc
        if not isinstance(data, dict) or not isinstance(data.get("domains"), list):
            raise DomainsError(f"{os.path.relpath(path, REPO_ROOT)} has no `domains:` list")
        domains = {}
        for entry in data["domains"]:
            if not isinstance(entry, dict) or not entry.get("id"):
                raise DomainsError(f"a domain without an id: {entry!r}")
            if entry["id"] in domains:
                raise DomainsError(f"domain {entry['id']!r} is listed twice")
            domains[entry["id"]] = entry
        if TAX not in domains:
            raise DomainsError("the tax domain is missing")
        _cache[path] = {
            "website_values": {str(v) for v in data.get("website_values") or []},
            "domains": domains,
        }
    return _cache[path]


def resolve(value, path=None):
    """``(status, domain dict or None)`` for a ``domain:`` value (see the module docstring)."""
    value = str(value or "").strip()
    if not value:
        return "none", None
    try:
        data = load(path)
    except DomainsError:
        return "unreadable", None
    if value in data["domains"]:
        domain = data["domains"][value]
        return ("active" if domain.get("status") == "active" else "proposed"), domain
    if value in data["website_values"]:
        return "website", None
    return "unknown", None


def is_website_value(value, path=None):
    """True for a value the website writes in ``domain:`` (website_values)."""
    try:
        return str(value or "").strip() in load(path)["website_values"]
    except DomainsError:
        return False


def get(domain_id, path=None):
    """The domain dict for an id (raises DomainsError or KeyError)."""
    return load(path)["domains"][domain_id]


def date_fields(domain):
    """The frontmatter keys a skill in ``domain`` must carry to say it is current."""
    fields = domain.get("date_field") or []
    return [fields] if isinstance(fields, str) else list(fields)


def is_date_key(key):
    """A key ending in _date or _on holds a YYYY-MM-DD date (docs/domains.yml)."""
    return key.endswith("_date") or key.endswith("_on")


def _hosts(domain, path=None, seen=None):
    """``{host: whose}`` for a domain, with the hosts of every domain it names in ``also``."""
    seen = set() if seen is None else seen
    if domain["id"] in seen:
        return {}
    seen.add(domain["id"])
    sources = domain.get("official_sources") or {}
    out = {}
    for other in sources.get("also") or []:
        out.update(_hosts(get(other, path), path, seen))
    out.update({str(h).lower(): str(w) for h, w in (sources.get("hosts") or {}).items()})
    return out


def official_hosts(domain_id=TAX, path=None):
    """``{host: whose}``: the named official hosts of a domain (government domains aside)."""
    return _hosts(get(domain_id, path), path)


def host_is_official(host, domain_id=TAX, path=None):
    """True when ``host`` is a government domain (if the domain accepts them) or one of its hosts."""
    host = host.lower().strip(".")
    domain = get(domain_id, path)
    if (domain.get("official_sources") or {}).get("government") and GOVERNMENT_HOST_RE.search(host):
        return True
    return any(host == h or host.endswith("." + h) for h in official_hosts(domain_id, path))


def url_host(url):
    return re.sub(r"^https?://", "", url.strip().lower()).split("/", 1)[0].split(":", 1)[0]
