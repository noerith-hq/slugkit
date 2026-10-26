# 0001: Documentation stack and GitHub Pages deployment

- **Status:** Accepted
- **Date:** 2026-10-26
- **Owner:** Repository maintainers

## Context

slugkit needs public documentation that is versioned (a `dev` version for `main`, a `stable` version and one version per minor release), has a generated API reference, and is hosted at no cost.

## Decision

Build the documentation with Material for MkDocs, mkdocstrings and mike, and publish it with GitHub Pages from the `gh-pages` branch.

- `docs.yml` deploys the `dev` version (alias `latest`) on every push to `main`.
- `release.yml` calls `docs.yml` after it publishes a release, which deploys `X.Y.x` with the aliases `stable` and `X.Y.Z`. Pre-releases are published under their own version and do not move `stable`.
- `docs.yml` is called from `release.yml` because tags and releases created with `GITHUB_TOKEN` do not trigger `on: push: tags` workflows.
- `python.yml` builds the site with `mkdocs build --strict` on every pull request, so broken links and bad cross-references fail review.

### Alternatives considered

- **GitHub Pages "GitHub Actions" source (`actions/deploy-pages`).** No extra branch, but it publishes a single version and needs `pages: write` and `id-token: write`, which `ci/verify.sh` also rejects.
- **Deploy key or personal access token.** Avoids `contents: write` in the workflow but adds a long-lived secret that must be stored and rotated.
- **Deploy only from `release.yml`.** Satisfies the original write-permission rule, but there would be no `dev` documentation between releases.

## Consequences

- **Security:** the `deploy` job in `docs.yml` has `contents: write`, the only write permission outside `release.yml`. `ci/verify.sh` now allows `contents: write` in those two files only and still rejects every other write permission. `docs.yml` runs only on pushes to `main` and from `release.yml`, never on pull requests, and every action is pinned to a commit SHA.
- **Operations:** GitHub Pages must be enabled once (Settings, Pages, deploy from the `gh-pages` branch, root folder). The `gh-pages` branch is generated output; do not edit it by hand.
- **Cost:** none for a public repository.
- **Maintenance:** Material for MkDocs reaches end of life on 5 May 2027; Zensical is its maintained successor. Evaluate the migration before then.
