#!/usr/bin/env python3
"""Check that a deployed PaglaDESIGN site is reachable and serves the expected document."""

from __future__ import annotations

import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

EXPECTED_MARKERS = ("PaglaDESIGN", "DesignDNA")


def check(url: str) -> None:
    request = Request(
        url, headers={"User-Agent": "PaglaDESIGN-deployment-smoke-test/1"}
    )
    with urlopen(
        request, timeout=20
    ) as response:  # noqa: S310 - URL is workflow input.
        status = response.status
        content_type = response.headers.get("content-type", "")
        body = response.read(250_000).decode("utf-8", errors="replace")

    if status < 200 or status >= 400:
        raise RuntimeError(f"{url}: unexpected HTTP status {status}")
    if "text/html" not in content_type:
        raise RuntimeError(f"{url}: expected HTML, received {content_type!r}")
    missing = [marker for marker in EXPECTED_MARKERS if marker not in body]
    if missing:
        raise RuntimeError(f"{url}: missing expected markers: {', '.join(missing)}")
    print(f"PASS {url} ({status}, {content_type})")


def main() -> int:
    urls = sys.argv[1:]
    if not urls:
        print("usage: smoke_test.py URL [URL ...]", file=sys.stderr)
        return 2

    last_error: Exception | None = None
    for attempt in range(1, 6):
        try:
            for url in urls:
                check(url)
            return 0
        except (HTTPError, URLError, TimeoutError, RuntimeError) as error:
            last_error = error
            if attempt < 5:
                print(f"Attempt {attempt} failed: {error}; retrying", file=sys.stderr)
                time.sleep(attempt * 5)

    print(f"Smoke test failed: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
