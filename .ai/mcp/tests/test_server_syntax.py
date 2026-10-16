import py_compile
from pathlib import Path


def test_mcp_server_compiles():
    """Verify that server.py and rag.py compile without syntax errors."""
    mcp_dir = Path(__file__).resolve().parent.parent
    py_compile.compile(str(mcp_dir / "server.py"), doraise=True)
    py_compile.compile(str(mcp_dir / "rag.py"), doraise=True)
