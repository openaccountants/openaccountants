"""Import the same publication policy the distributable MCP executes."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mcp"))
from openaccountants_mcp.eligibility import needs_sources, publication_holds  # noqa: E402,F401
