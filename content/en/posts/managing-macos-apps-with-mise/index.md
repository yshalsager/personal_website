+++
title = "Managing macOS apps with mise"
description = "Install and upgrade macOS applications distributed as DMG or ZIP files using mise's GitHub backend and a reusable global task."
tags = ["macOS", "mise"]
date = "2026-08-08"
+++

[mise](https://mise.jdx.dev/) is a fast, flexible tool manager that can install and keep development tools in sync across machines. Its GitHub backend can also download arbitrary release assets, making it useful for managing macOS applications alongside your usual command-line tools.

mise downloads GitHub release assets, but it does not install DMG applications into `/Applications`. Add this custom global task to `~/.config/mise/config.toml`:

```toml
[tasks."macos:install-dmg-app"]
hide = true
run = '''
set -euo pipefail

install_path="${MISE_TOOL_INSTALL_PATH:?MISE_TOOL_INSTALL_PATH is required}"
dmg_pattern="${MACOS_DMG_PATTERN:-*.dmg}"
app_pattern="${MACOS_APP_PATTERN:-*.app}"

dmg="$(find "$install_path" -maxdepth 1 -name "$dmg_pattern" -type f -print -quit)"
app_root="$install_path"

if [ -n "$dmg" ]; then
  mount="$(hdiutil attach "$dmg" -nobrowse -readonly |
    awk '/\/Volumes\// {print substr($0, index($0, "/Volumes/")); exit}')"

  cleanup() {
    hdiutil detach "$mount" -quiet 2>/dev/null || true
  }
  trap cleanup EXIT
  app_root="$mount"
fi

app="$(find "$app_root" -maxdepth 1 -name "$app_pattern" -type d -print -quit)"
[ -n "$app" ] || { echo "No .app found in $app_root"; exit 1; }

app_name="${MACOS_APP_NAME:-$(basename "$app")}"
case "$app_name" in
  *.app) ;;
  *) app_name="$app_name.app" ;;
esac

ditto "$app" "/Applications/$app_name"
'''
```

Then declare apps using mise's GitHub backend:

```toml
[tools."github:user/repo"]
version = "latest"
asset_pattern = "App-darwin-arm64-{{ version }}.dmg"
postinstall = "mise run --skip-tools --raw macos:install-dmg-app"
```

For ZIP releases containing an `.app`:

```toml
asset_pattern = "App-*.zip"
strip_components = 0
postinstall = "mise run --skip-tools --raw macos:install-dmg-app"
```

Install or upgrade the configured apps:

```sh
mise install
mise upgrade
```
