# Contributor checks and releases

All runtime repositories run their existing Rust/build tests plus workflow lint
and changed-line whitespace checks. **Required CI** combines those results into
one merge requirement. Main requires an up-to-date PR, a maintainer approval and
resolved conversations; force pushes and branch deletion are blocked. Admins
retain an override for maintenance.

Actions tokens default to read-only. Outside contributors need approval before
fork workflows run. Tests run on GitHub-hosted machines without physical devices
or repository secrets. Actions are pinned to commits. Dependabot opens grouped
weekly Actions and Rust update PRs; it never merges them automatically.

**Draft source release** is manual. Select an existing `v…` tag whose commit is
on main and has a successful main-branch CI run. The workflow generates a draft
release for maintainer review. It creates no tag, uploads no binaries and deploys
nothing to a device. Publishing the draft is a separate maintainer action.

Shared workflows and community templates live in this repository. Consumer
workflows pin a reviewed commit. The product repositories keep their own builds
and tests. Existing failure/recovery alerts remain enabled.
