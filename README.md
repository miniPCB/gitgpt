# 🧠 GitGPT: AI-Powered Git Commit Assistant

GitGPT is a Python CLI tool that uses OpenAI's GPT models to generate meaningful Git commit messages based on diffs. It supports both EAGLE PCB design projects and generic repositories, and now includes a CLI for managing favorites, selecting models, viewing config, and even upgrading itself.

---

## ✨ Features

- 🧠 AI-powered commit messages using actual `git diff`
- 🗂️ Interactive repo selector + favorites system
- 📂 Supports both `eagle` and `generic` repo types
- 🔧 Selectable OpenAI models (e.g. `gpt-4o`, `gpt-4`, `gpt-3.5`)
- ⚠️ Merge conflict detection
- 🔄 Auto push and optional `git pull`
- ⬆️ `gitgpt upgrade` to update via Git or PyPI
- 🧹 `gitgpt clear-cache` to reset config
- 🧠 `gitgpt model`, `gitgpt favorites`, `gitgpt config` and more

---

## 📦 Installation

### 1. Clone and install locally

```bash
git clone https://github.com/miniPCB/gitgpt.git
cd gitgpt
pip install .
```

### 2. Dependencies

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup

Create a `secrets.json` in the project root:

```json
{
  "openai_api_key": "sk-..."
}
```

Optionally define favorites and model in `config.json`:

```json
{
  "openai_model": "gpt-4o",
  "favorites": [
    { "path": "C:\\Repos\\EAGLE", "type": "eagle" },
    { "path": "C:\\Repos\\MyApp", "type": "generic" }
  ]
}
```

---

## 🚀 Usage

Run with no arguments to enter commit mode:

```bash
gitgpt
```

### Supported Commands

| Command            | Alias(es)   | Description                                        |
|--------------------|-------------|----------------------------------------------------|
| `model`            |             | Select GPT model interactively                    |
| `favorites`        | `fav`       | View or delete saved Git repo favorites           |
| `config`           | `cfg`       | Show the current configuration                    |
| `clear-cache`      | `reset`     | Remove all favorites and model selection          |
| `version`          | `--version`, `ver` | Show current version                       |
| `upgrade`          | `up`        | Pull latest from Git or upgrade via PyPI          |
| `--help`           | `help`, `-h`| Show CLI help with command summary                |

---

## 📂 Repo Types

- `eagle` → for EAGLE .brd, .sch, .epf, Gerber projects
- `generic` → any regular software, script, or content repo
- other types like `firmware`, `docs`, `api`, `desktop`, etc. also supported via config

---

## 🧪 Example

```bash
gitgpt favorites
gitgpt model
gitgpt
```

---

## 🆙 Upgrading GitGPT

```bash
gitgpt upgrade
```

- If installed via Git: pulls latest and reinstalls
- If installed via PyPI: runs `pip install --upgrade gitgpt`
- Logs to `~/gitgpt_upgrade_log.txt` and shows current version

---

## 📄 License

MIT License © 2025 Nolan Manteufel

---

Start committing smarter, not harder. 🧠✨
