# Actual exploratory failures and resolutions

- Initial unprivileged git fetch: fatal unable to access GitHub, could not resolve host. A normal approved network fetch then succeeded; no alternative Git history was fabricated.
- NBR direct page/media endpoint403 and SIO current law/EOSB pages403: exact failures are in sources/acquisition*.json. LLOC original Arabic law/regulations were acquired without disguising requests.
- EDB live source redirects to homepage: exact resolved URLs in acquisition3.json. The dated archive embedded PDF was then recovered and read; homepage and search snippets were not used as authority.
- First optional extraction using bs4 failed with ModuleNotFoundError. Replaced by standard-library HTMLParser and ZIP/XML reader, saved in extract.py.
- Ledger exact-substring checks initially failed for Arabic line-break/contraction and Sijilat unrendered-HTML text. Corrected against actual captured source words. Sijilat was explicitly changed to a labelled visible-browser read receipt because raw translation dictionaries contain retired values. No unmatched quote was accepted.
- An exploratory validate-guides.py --help invocation ran full mode because this script does not implement --help. It reported stale generated index.json and llms-full.txt. Those generated files remain unchanged. The required --changed-only --no-index-check runs pass; their actual output is saved.
