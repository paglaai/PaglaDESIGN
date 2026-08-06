@echo off
rem PaglaDESIGN MCP server launcher (Windows).
rem Uses the PaglaAI shared venv if present, else python from PATH.
rem Requires: python -m pip install mcp (see requirements.txt)

setlocal
set "MCP_DIR=%~dp0"
set "VENV_PY=D:\PaglaAI\.venv\Scripts\python.exe"

if exist "%VENV_PY%" (
  "%VENV_PY%" "%MCP_DIR%server.py" %*
) else (
  python "%MCP_DIR%server.py" %*
)
endlocal
