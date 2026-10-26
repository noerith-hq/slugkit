# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- Open the `stable` version of the documentation by default once a release exists.

## [0.1.0] - 2026-10-26

### Added

- Initial project foundation from `noerith-starter`.
- `slugkit` Python library (`slugify`, `is_slug`) and the `slugkit` command-line tool, with tests.
- Versioned documentation site (MkDocs Material and mike) published to GitHub Pages.
- Python test matrix and strict documentation build workflow.
- Python lint and test checks in `ci/verify.sh`, and `pip` updates in Dependabot.

### Changed

- Split release validation from publication so write access is granted only to the publish job.
- Check both YAML workflow extensions and local composite actions for immutable action references.
- Present a polished starter README while preserving project-specific initialization.

### Security

- Allow `contents: write` in `docs.yml` in addition to `release.yml`, so the documentation workflow can push the built site to the `gh-pages` branch. See `docs/decisions/0001-docs-stack-and-pages-deployment.md`.
- Reject broad or unexpected GitHub Actions write permissions.
- Use the hardened, immutable revision of the NOERITH reusable CI workflow.

[Unreleased]: https://github.com/noerith-hq/slugkit/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/noerith-hq/slugkit/releases/tag/v0.1.0
