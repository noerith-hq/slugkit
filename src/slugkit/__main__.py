"""Command-line interface: ``slugkit "Hello World"`` or ``python -m slugkit``."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from slugkit.core import slugify


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="slugkit", description="Turn text into a URL-friendly slug."
    )
    parser.add_argument("text", nargs="+", help="text to convert")
    parser.add_argument("-s", "--separator", default="-", help="word separator (default: -)")
    parser.add_argument("-m", "--max-length", type=int, help="maximum length of the slug")
    args = parser.parse_args(argv)

    try:
        print(slugify(" ".join(args.text), separator=args.separator, max_length=args.max_length))
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
