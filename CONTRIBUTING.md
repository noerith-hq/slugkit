# Contributing

Thanks for helping improve slugkit! Bug reports, fixes and documentation improvements are all welcome.

This project follows the [NOERITH contribution guide](https://github.com/noerith-hq/.github/blob/main/CONTRIBUTING.md): short-lived `feat/`, `fix/` or `docs/` branches, Conventional Commits, and pull requests into `main`. This page covers what is specific to slugkit.

## Development setup

```bash
git clone https://github.com/noerith-hq/slugkit.git
cd slugkit
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]" -r requirements-docs.txt
```

## Before you open a pull request

```bash
./ci/verify.sh        # the full repository contract, including lint and tests
mkdocs build --strict # docs must build without warnings
```

## Working on the documentation

```bash
mkdocs serve          # live preview at http://127.0.0.1:8000
```

Every page has an **Edit** button that opens the Markdown source on GitHub. The API reference is generated from the docstrings in `src/slugkit`, so change the docstring rather than the page.

## Pull requests

- Keep each pull request focused on one change.
- Add or update tests for behaviour changes.
- Use Google-style docstrings for public functions.

## Releases

Maintainers publish a release by pushing a tag such as `v0.2.0`. The docs workflow then deploys the `0.2.x` version of the site and points `stable` at it. Every push to `main` updates the `dev` version.
