#!/usr/bin/env python3
"""Build MkDocs and check the shipped HTML contains the live site title."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict"],
        cwd=ROOT,
        check=True,
    )
    index = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    if "<title>Web3 Outpost Documentation</title>" not in index:
        raise SystemExit("built index.html is missing the docs title")
    if "Web3 Outpost" not in index:
        raise SystemExit("built index.html is missing Outpost copy")
    healthz_template = (ROOT / "nginx.conf.template").read_text(encoding="utf-8")
    if "location = /healthz" not in healthz_template:
        raise SystemExit("nginx template is missing /healthz")
    if "LISTEN_PORT" not in healthz_template:
        raise SystemExit("nginx template does not bind PORT")
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
