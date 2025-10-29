#!/usr/bin/env python3
"""Download external imagery assets for the Silvia Protopapa site."""

from __future__ import annotations

import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets" / "images"
HEADSHOT_URL = (
    "https://diversity.utexas.edu/ige/wp-content/uploads/sites/50/2020/11/Silvia-Protopapa.jpg"
)
HEADSHOT_PATH = ASSETS_DIR / "silvia-protopapa-headshot.jpg"


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    destination.write_bytes(data)
    print(f"Downloaded {destination.relative_to(ROOT)} ({len(data)} bytes)")


def main() -> int:
    print("Fetching remote imagery...")
    try:
        download(HEADSHOT_URL, HEADSHOT_PATH)
    except urllib.error.URLError as error:
        print(
            "Failed to download headshot. Please verify network access and rerun the script.",
            file=sys.stderr,
        )
        print(f"Reason: {error}", file=sys.stderr)
        return 1

    print("All assets downloaded successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
