# 📜 Changelog

All notable changes to **GitGPT** will be documented in this file.

---

## [0.1.0] - 2025-04-18

### Added
- ✅ Initial release with core functionality:
  - AI-powered commit message generation using OpenAI's GPT based on `git diff`
  - Support for ten repository types (`eagle`, `generic`, `firmware`, `docs`, `website`, `cli`, `data`, `api`, `desktop`, `testing`)
  - Interactive repo browser with `favorites` system saved in `config.json`

- ✅ CLI command structure:
  - `gitgpt`  
    → Launches the interactive commit assistant for selected repo
  - `gitgpt model`  
    → Interactive menu to select OpenAI model (`gpt-4o`, `gpt-4`, `gpt-3.5-turbo`)
  - `gitgpt favorites` / `gitgpt fav`  
    → View and delete saved Git repo favorites
  - `gitgpt config` / `gitgpt cfg`  
    → View full current configuration (`favorites` and `openai_model`)
  - `gitgpt clear-cache` / `gitgpt reset`  
    → Clear all saved favorites and model preference
  - `gitgpt version` / `--version` / `ver`  
    → Display current GitGPT version from `__init__.py`
  - `gitgpt upgrade` / `up`  
    → Smart upgrade command:
      - Uses `git pull && pip install .` if in a Git repo
      - Falls back to `pip install --upgrade gitgpt` if not
      - Logs output to `~/gitgpt_upgrade_log.txt`
  - `gitgpt --help` / `-h` / `help`  
    → Displays a full emoji-enhanced command reference banner

- ✅ Auto-commit and push:
  - Adds modified files
  - Commits with GPT-generated message
  - Pushes to remote
  - Offers to pull if branch is behind

- ✅ Git + PyPI support:
  - Smart install detection
  - Upgrade paths for both GitHub and PyPI installs

- ✅ Version + changelog tooling:
  - Includes `bump_version.py` for version bumping, changelog updates, tagging, and pushing releases

### Improved
- 🔄 Enhanced help banner with emojis and alias listings
- 🧠 Alias support for all key CLI commands
- 📦 Packaged as a pip-installable module with `pyproject.toml`

### Notes
- 🔐 API key must be saved in `secrets.json`
- 📄 `config.json` stores model + favorites
- 🧠 Version defined in `gitgpt/__init__.py`
- 📝 `CHANGELOG.md` updated automatically with `bump_version.py`
- 📤 Upgrade logs saved to `~/gitgpt_upgrade_log.txt`

## [0.1.3] - 2025-04-19
