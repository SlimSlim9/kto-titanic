FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock .python-version ./
COPY ./src/titanic/mcp_server ./src/titanic/mcp_server

RUN uv sync -n --group mcp-server

EXPOSE 8000

ENTRYPOINT ["uv", "-n", "run", "--no-sync", "--group", "mcp-server", "python", "-m", "titanic.mcp_server.server"]
