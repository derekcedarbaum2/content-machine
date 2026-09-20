"""Check the distributable plugin without calling a model or external service."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
SKILLS = {"content-machine", "content-setup", "draft", "interview", "lessons", "oracle", "repurpose"}

def validate(root):
    root = Path(root)
    errors = []
    try:
        manifest = json.loads((root / ".claude-plugin/plugin.json").read_text())
        if manifest.get("name") != "content-machine" or not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
            errors.append("Plugin name or version is invalid")
    except (OSError, ValueError) as error:
        errors.append(f"Cannot read plugin manifest: {error}")
    for name in sorted(SKILLS):
        p = root / "skills" / name / "SKILL.md"
        if not p.exists():
            errors.append(f"Missing skill: {name}")
            continue
        text = p.read_text()
        if not text.startswith("---\n") or "description:" not in text.split("---", 2)[1]:
            errors.append(f"Missing skill frontmatter: {name}")
    for name in ("profile.md", "voice-guide.md", "sources.md", "content-lessons.md"):
        if not (root / "templates/personal" / name).is_file():
            errors.append(f"Missing onboarding template: {name}")
    for p in root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        for url in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", p.read_text()):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith(("#", "/", "~")):
                continue
            target = unquote(url.split("#")[0])
            if target and not (p.parent / target).exists():
                errors.append(f"Broken link in {p.relative_to(root)}: {target}")
    return errors

if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Plugin validation: {len(errors)} error(s)")
    raise SystemExit(bool(errors))
