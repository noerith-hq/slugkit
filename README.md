# slugkit

[![CI](https://github.com/noerith-hq/slugkit/actions/workflows/ci.yml/badge.svg)](https://github.com/noerith-hq/slugkit/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-latest-teal)](https://noerith-hq.github.io/slugkit/)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

> Tiny, dependency-free helpers for turning text into URL-friendly slugs.

## Status

Sample project

## Problem

Generating clean, predictable URL slugs from text, including accented and Vietnamese text, usually means pulling in a heavy dependency or maintaining ad-hoc regular expressions.

## Getting started

slugkit is not published to PyPI yet. Install it straight from GitHub (Python 3.10 or newer):

```bash
pip install "git+https://github.com/noerith-hq/slugkit.git"
```

```python
from slugkit import slugify

slugify("Xin chào, Việt Nam!")               # 'xin-chao-viet-nam'
slugify("Hello World", separator="_")        # 'hello_world'
slugify("A very long article title", max_length=12)  # 'a-very-long'
```

Or from the command line:

```console
$ slugkit "Hello, World!"
hello-world
```

Full documentation lives at **<https://noerith-hq.github.io/slugkit/>**. Do not add credentials, API keys, customer data, or production configuration to this repository.

## Local development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]" -r requirements-docs.txt
mkdocs serve   # live preview of the documentation at http://127.0.0.1:8000
```

## Testing

Run the repository contract locally. It also runs the linter and the test suite:

```bash
./ci/verify.sh
```

During development you can run the pieces directly:

```bash
ruff check .
pytest
mkdocs build --strict
```

## Architecture

Read and maintain [the architecture overview](docs/architecture.md). Record significant technical choices in [architecture decisions](docs/decisions/README.md).

## Security

Report vulnerabilities through the organization [security policy](https://github.com/noerith-hq/.github/blob/main/SECURITY.md). Never commit secrets; use a secure secret-management service when a deployment is introduced.

## Contributing

Follow the NOERITH [contribution guide](https://github.com/noerith-hq/.github/blob/main/CONTRIBUTING.md), [code of conduct](https://github.com/noerith-hq/.github/blob/main/CODE_OF_CONDUCT.md), and [support policy](https://github.com/noerith-hq/.github/blob/main/SUPPORT.md). Project-specific setup is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Development conventions

- Default branch: `main`.
- Feature branches: `feat/<short-name>`.
- Fix branches: `fix/<short-name>`.
- Security branches: `security/<short-name>`.
- Use Conventional Commits and Semantic Versioning.
- Use pull requests for normal changes; review major dependency updates manually.
- Owner bypass is reserved for an emergency only.

## License

Licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution.
