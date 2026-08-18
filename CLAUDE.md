# Arsenal

Personal knowledge base of Red Team tools, infrastructure, and hardware setup notes — not an application codebase. There's no build, lint, or test tooling; entries are Markdown documentation, occasionally with embedded shell/StackScript snippets.

## Structure

* `Cloud/` — cloud provider setup for Red Team use (subfolders per provider: AWS, Azure, Linode)
* `Coding/` — language-specific setup/tooling notes (subfolders per language)
* `Containers/` — Red Team tools containerized
* `Hardware/` — hardware setup (subfolders per device type)
* `Resources/` — misc reference material
* `Tools/` — individual tool install/config notes

## Adding a new entry

Each top-level section has a template — copy the closest one rather than inventing a new structure:
* `Cloud/cloud_template.md`
* `Coding/coding_template.md`
* `Tools/tool_template.md`

Common shape across entries: `# Title`, then bolded `**Description:**` / `**Requirements:**` (and for Cloud entries, `**Provider:**` / `**Service:**`), then numbered setup steps or a fenced command block, ending with a `## References` list of source URLs.

## Shell/StackScript conventions

Several entries (e.g. `Cloud/Linode/stackscript_*.md`) embed provisioning scripts. When writing or editing these:
* StackScripts run entirely as root — don't prefix commands with `sudo`, it's a no-op and inconsistent if only some lines have it.
* When a step should run as a specific non-root user (e.g. a `recon` user), use `su - <user> -c "..."` for one-liners or `su - <user> <<'EOF' ... EOF` for multi-line blocks — don't rely on bare `su <user>` or assume a later command "inherits" a user switch.
* Quote heredoc delimiters (`<<'EOF'`) when the block should NOT have variables expanded by the outer (root) shell before being handed to the sub-shell.
* Prefer `mkdir -p` for idempotency, and guard steps that depend on a prior build/install succeeding (e.g. check a binary exists before `cp`-ing it into a system path) rather than assuming success.
