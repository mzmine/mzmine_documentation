#!/usr/bin/env bash
#
# Publishes everything in .github/pages-root/ to the root of the gh-pages
# branch, next to the version directories managed by mike. mike leaves files it
# does not own alone, so this only has to do something when those files change.
#
# The branch is never checked out: gh-pages holds a full copy of the docs for
# every published version, so a checkout would move hundreds of megabytes to
# write a 2 KB file. Instead the files are hashed straight into a temporary
# index built from the remote branch, and the resulting commit is pushed.
#
# Files removed from .github/pages-root/ are NOT removed from the branch, delete
# those by hand.
#
# Needs a git identity (user.name / user.email) for the commit.
#
# Usage: .github/scripts/publish-pages-root.sh [branch]

set -euo pipefail

BRANCH="${1:-gh-pages}"
REMOTE="${REMOTE:-origin}"
SRC="$(cd "$(dirname "$0")/../pages-root" && pwd)"
cd "$(git rev-parse --show-toplevel)"

git fetch --quiet "$REMOTE" "$BRANCH"
BASE="$(git rev-parse FETCH_HEAD)"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
export GIT_INDEX_FILE="$TMP/index"

git read-tree "$BASE"
while IFS= read -r -d '' file; do
  blob="$(git hash-object -w -- "$file")"
  git update-index --add --cacheinfo "100644,$blob,${file#"$SRC"/}"
done < <(find "$SRC" -type f -print0)

TREE="$(git write-tree)"
if [ "$TREE" = "$(git rev-parse "$BASE^{tree}")" ]; then
  echo "gh-pages root files are already up to date"
  exit 0
fi

COMMIT="$(git commit-tree "$TREE" -p "$BASE" -m "Update static gh-pages root files")"
git push --quiet "$REMOTE" "$COMMIT:refs/heads/$BRANCH"
echo "published the gh-pages root files to $BRANCH"
