# OpenAccountants MCP server — container image for local development and
# self-hosting.  Builds the Python MCP package and runs it under FastMCP's
# Streamable-HTTP transport so remote MCP clients (Claude Desktop custom
# connectors, ChatGPT, agents behind a reverse proxy, etc.) can connect over
# HTTP instead of stdio.
#
# Usage (local host only):
#   docker build -t openaccountants-mcp .
#   docker run --rm -p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0 openaccountants-mcp
#   # then point a local MCP client at http://localhost:8000/mcp
#
# The process defaults to 127.0.0.1. Docker port publishing needs an explicit
# container-side MCP_HOST=0.0.0.0; the host-side 127.0.0.1 binding above keeps
# that published port local. See mcp/README.md before exposing it remotely.
#
# Environment knobs (all optional, see mcp/openaccountants_mcp/server.py):
#   MCP_TRANSPORT             stdio | streamable-http | sse   (default here: streamable-http)
#   MCP_HOST                  bind host                       (default here: 127.0.0.1)
#   MCP_PORT                  bind port                       (default here: 8000)
#   MCP_STREAMABLE_HTTP_PATH  mount path                      (default: /mcp;
#                             set to "/" when fronted by a proxy that strips
#                             an upstream path prefix)
#   OPENACCOUNTANTS_ROOT      skill content root              (set to /app in image)

FROM python:3.11-slim

WORKDIR /app

# Install the MCP server package first so the dependency layer caches well.
COPY mcp ./mcp
RUN pip install --no-cache-dir ./mcp

# Skill content the server reads from $OPENACCOUNTANTS_ROOT/packages.
COPY packages ./packages

ENV OPENACCOUNTANTS_ROOT=/app \
    MCP_TRANSPORT=streamable-http \
    MCP_HOST=127.0.0.1 \
    MCP_PORT=8000

EXPOSE 8000

# The server only reads its installed code and skill packages. A numeric
# identity avoids adding account-management packages to the slim base image.
USER 65532:65532

CMD ["openaccountants-mcp"]
