@echo off
rem PaglaDESIGN MCP server launcher (Windows).
rem Uses active virtualenv or workspace .venv if present, else python from PATH.
rem Requires: python -m pip install mcp (see requirements.txt)

setlocal
set "MCP_DIR=%~dp0"

if defined VIRTUAL_ENV (
  "%VIRTUAL_ENV%\Scripts\python.exe" "%MCP_DIR%server.py" %*
) else if exist "%MCP_DIR%..\..\.venv\Scripts\python.exe" (
  "%MCP_DIR%..\..\.venv\Scripts\python.exe" "%MCP_DIR%server.py" %*
) else (
  python "%MCP_DIR%server.py" %*
)
endlocal
