"""Regression tests for behaviour the mcp 2.x migration had to preserve.

The 2.x SDK forwards a ``ToolError``'s message to the client and masks every
other exception as a bare "Error executing tool <name>"; the server's input
errors must stay visible. Transport settings also moved from the constructor
to ``MCPServer.run()``, so ``main()`` has to pass them per transport.
"""

from __future__ import annotations

import unittest
from unittest import mock

from mcp.client import Client
from mcp.server.mcpserver.exceptions import ToolError

from openaccountants_mcp import server


class ToolInputErrorContractTests(unittest.IsolatedAsyncioTestCase):
    def test_is_both_a_tool_error_and_a_value_error(self) -> None:
        self.assertTrue(issubclass(server.ToolInputError, ToolError))
        self.assertTrue(issubclass(server.ToolInputError, ValueError))
        with self.assertRaisesRegex(ValueError, "not found"):
            server.get_skill("does-not-exist-xyz")

    async def test_client_sees_the_input_error_message(self) -> None:
        async with Client(server.mcp) as client:
            result = await client.call_tool("get_skill", {"slug": "does-not-exist-xyz"})
        self.assertTrue(result.is_error)
        text = " ".join(getattr(block, "text", "") for block in result.content)
        self.assertIn("Skill 'does-not-exist-xyz' not found", text)


class TransportWiringTests(unittest.TestCase):
    def _run_main(self, transport: str) -> mock.Mock:
        with mock.patch.object(server.mcp, "run") as run, mock.patch.multiple(
            server,
            _TRANSPORT=transport,
            _HTTP_HOST="0.0.0.0",
            _HTTP_PORT=9001,
            _STREAMABLE_HTTP_PATH="/",
        ):
            server.main()
        return run

    def test_stdio_passes_no_http_settings(self) -> None:
        self._run_main("stdio").assert_called_once_with(transport="stdio")

    def test_streamable_http_passes_host_port_and_path(self) -> None:
        self._run_main("streamable-http").assert_called_once_with(
            transport="streamable-http", host="0.0.0.0", port=9001, streamable_http_path="/"
        )

    def test_sse_passes_host_and_port(self) -> None:
        self._run_main("sse").assert_called_once_with(transport="sse", host="0.0.0.0", port=9001)


if __name__ == "__main__":
    unittest.main()
