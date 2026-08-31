import os

files = {
    "anchor-standards.md": 10,
    "interdisciplinary-standards.md": 20,
    "animation-vfx-games.md": 30,
    "design-visual-arts.md": 40,
    "cte-arts-entertainment-design-standards.md": 50
}

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

for name, w in files.items():
    path = os.path.join(base_dir, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        lines = text.splitlines()
        new_lines = []
        has_weight = False
        for l in lines:
            if l.startswith("weight:"):
                new_lines.append(f"weight: {w}")
                has_weight = True
            else:
                new_lines.append(l)
        if not has_weight:
            new_lines.insert(3, f"weight: {w}")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines) + "\n")

print("Updated standards weights!")