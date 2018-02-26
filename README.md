# Dotbot ```atom``` plugin

Plugin for [Dotbot](https://github.com/anishathalye/dotbot), that adds a ```atom``` directive.
It allows installation of extensions and themes for [Atom](https://atom.io).

## Requirements

Besides `dotbot`, Atom shell commands (namely the package manager `apm`) need to be accessible from within your shell.

See https://flight-manual.atom.io/getting-started/sections/installing-atom/ for more information.

## Installation

Add this repository to you dotfiles repository:

```
git submodule add https://github.com/mikedevnull/dotbot-atom.git
```

Modify your `install` script to include the plugin:

```bash
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASEDIR}" --plugin-dir dotbot-atom -c "${CONFIG}" "${@}"
```

## Usage

Simply add a list of packages or themes to install to the `atom` directive:

```yaml
- atom:
  - seti-ui
  - linter
  - clang-format
```

Please note: older package version will **not** be updated.
Installed packages not listed here will **not** be removed.
Both actions are better to be handled while interacting with atom directly.
