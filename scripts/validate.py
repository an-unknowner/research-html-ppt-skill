from pathlib import Path
import re, json
root = Path(__file__).resolve().parents[1]
skill = root / "skills/research-html-ppt"
for name in ("SKILL.md", "agents/openai.yaml", "assets/blank-template.html"):
    assert (skill / name).is_file(), name
entry = (skill / "SKILL.md").read_text(encoding="utf-8")
assert entry.startswith("---\nname: research-html-ppt\ndescription:")
for path in skill.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if not re.match(r"[a-z]+://", link):
            assert (path.parent / link.split("#")[0]).exists(), (path, link)
html = (skill / "assets/blank-template.html").read_text(encoding="utf-8")
data = json.loads(re.search(r'<script type="application/json" id="deck-data">(.*?)</script>', html, re.S)[1])
assert len(data["slides"]) == 10
assert len({s["id"] for s in data["slides"]}) == 10
assert all(not v for v in data["meta"].values())
assert all(not v for obj in data["entities"].values() for v in obj.values())
assert all(not v for obj in data["claims"].values() for v in obj.values())
for slide in data["slides"]:
    assert slide["subject"] in data["entities"]
    assert slide["claim"] in data["claims"]
    for item in slide["items"]:
        assert item["entity"] in data["entities"]
        assert item["claim"] in data["claims"]
        assert not item["src"] and not item["alt"]
print("PASS: skill structure, links, 10 blank layouts, shared references")
