import re
import os
import subprocess
import logging
from datetime import datetime
from pathlib import Path

# --- File Paths ---
INIT_PATH = Path("gitgpt/__init__.py")
CHANGELOG_PATH = Path("CHANGELOG.md")
LOG_PATH = Path("version_bump.log")
PYPROJECT_PATH = Path("pyproject.toml")

# --- Setup Logging ---
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_current_version():
    content = INIT_PATH.read_text(encoding="utf-8")
    match = re.search(r'__version__\s*=\s*"(.+?)"', content)
    version = match.group(1) if match else "0.0.0"
    logging.info(f"Current version detected: {version}")
    return version

def is_valid_version(version):
    return re.match(r"^\d+\.\d+\.\d+$", version) is not None

def suggest_next_version(version):
    major, minor, patch = map(int, version.split("."))
    return f"{major}.{minor}.{patch + 1}"

def update_version(new_version):
    content = INIT_PATH.read_text(encoding="utf-8")
    updated_content = re.sub(r'__version__\s*=\s*".+?"', f'__version__ = "{new_version}"', content)
    INIT_PATH.write_text(updated_content, encoding="utf-8")
    logging.info(f"Updated version in {INIT_PATH}")
    print(f"✅ Version updated to {new_version} in {INIT_PATH}")

def prompt_list(label):
    print(f"\n🧠 Enter items to include under '{label}' (press Enter twice to finish):")
    items = []
    while True:
        line = input("- ").strip()
        if not line:
            break
        items.append(line)
    logging.info(f"{label} entries: {items}")
    return items

def update_changelog(new_version, added, changed, fixed):
    today = datetime.today().strftime("%Y-%m-%d")
    lines = [f"## [{new_version}] - {today}"]

    if added:
        lines.append("### Added")
        lines.extend(f"- {item}" for item in added)
    if changed:
        lines.append("### Changed")
        lines.extend(f"- {item}" for item in changed)
    if fixed:
        lines.append("### Fixed")
        lines.extend(f"- {item}" for item in fixed)
    lines.append("")  # for newline

    if CHANGELOG_PATH.exists():
        old_changelog = CHANGELOG_PATH.read_text(encoding="utf-8")
    else:
        old_changelog = "# 📜 Changelog\n"
    updated_changelog = old_changelog.strip() + "\n\n" + "\n".join(lines)
    CHANGELOG_PATH.write_text(updated_changelog, encoding="utf-8")
    logging.info(f"CHANGELOG.md updated for version {new_version}")
    print("📝 CHANGELOG.md updated.")

def check_git_clean():
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    clean = result.stdout.strip() == ""
    if not clean:
        logging.warning("Git working directory is not clean.")
    return clean

def git_commit_and_tag(version):
    try:
        subprocess.run(["git", "add", str(INIT_PATH), str(CHANGELOG_PATH)], check=True)
        subprocess.run(["git", "commit", "-m", f"v{version} release"], check=True)
        subprocess.run(["git", "tag", f"v{version}"], check=True)
        subprocess.run(["git", "push"], check=True)
        subprocess.run(["git", "push", "--tags"], check=True)
        logging.info(f"Git commit and tag created for v{version}")
        print("🚀 Git commit, tag, and push completed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git operation failed: {e}")
        print(f"❌ Git operation failed: {e}")

def log_bump(version):
    message = f"Bumped to {version}"
    logging.info(message)

def update_pyproject_version(new_version):
    if not PYPROJECT_PATH.exists():
        logging.warning("pyproject.toml not found. Skipping.")
        return

    lines = PYPROJECT_PATH.read_text(encoding="utf-8").splitlines()
    in_project_section = False
    new_lines = []

    for line in lines:
        stripped = line.strip()

        # Detect section
        if stripped.startswith("["):
            in_project_section = stripped == "[project]"

        # Replace version line inside [project]
        if in_project_section and stripped.startswith("version"):
            new_lines.append(f'version = "{new_version}"')
            logging.info("Updated version line in [project] section.")
        else:
            new_lines.append(line)

    PYPROJECT_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print("🛠️ pyproject.toml version updated.")
    logging.info(f"pyproject.toml version set to {new_version}")

def main():
    print("🛠️  Version Bump Utility")
    current_version = get_current_version()
    print(f"🔢 Current version: {current_version}")

    suggested = suggest_next_version(current_version)
    new_version = input(f"📌 Enter new version [{suggested}]: ").strip() or suggested

    if not is_valid_version(new_version) or new_version == current_version:
        print("❌ Invalid or unchanged version. Aborting.")
        logging.warning(f"Aborted: Invalid or unchanged version '{new_version}'")
        return

    if not check_git_clean():
        print("⚠️ Warning: Git working directory not clean. Continue? (y/N)")
        if input().strip().lower() != "y":
            logging.info("User aborted due to dirty Git status.")
            return

    added = prompt_list("Added")
    changed = prompt_list("Changed")
    fixed = prompt_list("Fixed")

    update_version(new_version)
    update_pyproject_version(new_version)
    update_changelog(new_version, added, changed, fixed)
    git_commit_and_tag(new_version)
    log_bump(new_version)

    print(f"🎉 Bumped to version {new_version} and tagged release!")

if __name__ == "__main__":
    main()
