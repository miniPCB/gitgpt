import re
import os
import subprocess
from datetime import datetime
from pathlib import Path

INIT_PATH = Path("gitgpt/__init__.py")
CHANGELOG_PATH = Path("CHANGELOG.md")

def get_current_version():
    content = INIT_PATH.read_text()
    match = re.search(r'__version__\s*=\s*\"(.+?)\"', content)
    return match.group(1) if match else "0.0.0"

def update_version(new_version):
    content = INIT_PATH.read_text()
    content = re.sub(r'__version__\s*=\s*\".+?\"', f'__version__ = "{new_version}"', content)
    INIT_PATH.write_text(content)
    print(f"✅ Version updated to {new_version} in {INIT_PATH}")

def update_changelog(new_version, added, changed, fixed):
    today = datetime.today().strftime("%Y-%m-%d")
    header = f"## [{new_version}] - {today}\n"
    lines = [header]

    if added:
        lines.append("### Added")
        for item in added:
            lines.append(f"- {item}")
    if changed:
        lines.append("### Changed")
        for item in changed:
            lines.append(f"- {item}")
    if fixed:
        lines.append("### Fixed")
        for item in fixed:
            lines.append(f"- {item}")
    lines.append("\n")

    original = CHANGELOG_PATH.read_text() if CHANGELOG_PATH.exists() else "# 📜 Changelog\n\n"
    updated = original.strip().split("\n", 2)
    new_changelog = updated[0] + "\n\n" + "\n".join(lines) + "\n".join(updated[1:]) + "\n"
    CHANGELOG_PATH.write_text(new_changelog)
    print("📝 CHANGELOG.md updated.")

def prompt_list(label):
    print(f"\n🧠 Enter items to include under '{label}' (press Enter twice to finish):")
    items = []
    while True:
        line = input("- ").strip()
        if not line:
            break
        items.append(line)
    return items

def git_commit_and_tag(version):
    try:
        subprocess.run(["git", "add", str(INIT_PATH), str(CHANGELOG_PATH)], check=True)
        subprocess.run(["git", "commit", "-m", f"v{version} release"], check=True)
        subprocess.run(["git", "tag", f"v{version}"], check=True)
        subprocess.run(["git", "push"], check=True)
        subprocess.run(["git", "push", "--tags"], check=True)
        print("🚀 Git commit, tag, and push completed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")

def main():
    current_version = get_current_version()
    print(f"🔢 Current version: {current_version}")
    new_version = input("📌 Enter new version: ").strip()

    if not new_version or new_version == current_version:
        print("❌ Invalid or unchanged version. Aborting.")
        return

    added = prompt_list("Added")
    changed = prompt_list("Changed")
    fixed = prompt_list("Fixed")

    update_version(new_version)
    update_changelog(new_version, added, changed, fixed)
    git_commit_and_tag(new_version)

    print(f"🎉 Bumped to version {new_version} and tagged release!")

if __name__ == "__main__":
    main()
