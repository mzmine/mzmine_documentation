#!/usr/bin/env bash
# Deploy a versioned copy of the docs to the gh-pages branch.
# Normally GitHub Actions does this (see .github/workflows), use this only to
# fix up a deployment manually.
#
#   ./deploy_githubpages.sh latest                  # rebuild the master docs
#   ./deploy_githubpages.sh 4.8.0                   # (re)publish a release version
#
# Do NOT use "mkdocs gh-deploy" anymore, it would overwrite the versioned site.
set -euo pipefail
mike deploy --push "$@"
