# slugkit architecture

## Context

Tiny, dependency-free helpers for turning text into URL-friendly slugs.

The project addresses: Generating clean, predictable URL slugs from text, including accented and Vietnamese text, usually means pulling in a heavy dependency or maintaining ad-hoc regular expressions.

## System context

slugkit is a pure-Python library with no runtime dependencies and no network access.

- **Users:** Python developers who import `slugkit` or run the `slugkit` command.
- **Upstream systems:** none. The library uses only the Python standard library.
- **Downstream consumers:** applications that need slugs for URLs, file names or identifiers.
- **Trust boundaries:** input text is untrusted. `slugify` only transforms strings and never evaluates them, and its output contains only lowercase ASCII letters, digits and the chosen separator.
- **Operating environment:** Python 3.10 or newer on any platform.

## Code structure

- `src/slugkit/`: the library. `core.py` holds `slugify` and `is_slug`, `__main__.py` the command-line interface.
- `tests/`: automated tests (pytest).
- `docs/`: the documentation site (MkDocs Material), architecture overview and decision records. The API reference is generated from the docstrings in `src/slugkit`.
- `ci/`: repository checks. `ci/verify.sh` also runs the linter and the tests.
- `.github/workflows/`: `ci.yml` (organization secure CI), `python.yml` (Python version matrix and strict documentation build), `docs.yml` (publishes the documentation) and `release.yml` (controlled release).

## Data and AI considerations

slugkit processes no personal data, stores nothing and uses no AI components.

## Security and operations

- No authentication, secrets or persistent state.
- CI follows the organization baseline: read-only permissions by default and every action pinned to a commit SHA. The only write permission outside `release.yml` is `contents: write` in `docs.yml`, which pushes the built site to the `gh-pages` branch. See [ADR 0001](decisions/0001-docs-stack-and-pages-deployment.md).
- The documentation is served by GitHub Pages from the `gh-pages` branch: the `dev` version on every push to `main`, and `X.Y.x` plus `stable` on each release.

## Decisions

Use `docs/decisions/` for decisions that affect architecture, risk, data handling, or long-term maintenance. See the [decision index](decisions/README.md).
