import os, shutil, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

# 1. Remove legacy files and folders
legacy_items = [
    os.path.join(base_dir, "about.md"),
    os.path.join(base_dir, "roadmap"),
    os.path.join(base_dir, "resources")
]

for item in legacy_items:
    if os.path.isfile(item):
        os.remove(item)
        print(f"Deleted legacy file {item}")
    elif os.path.isdir(item):
        shutil.rmtree(item)
        print(f"Deleted legacy directory {item}")

# 2. Clean Tier 100 / 200 / 300 / 400 prefixes from _index.md files
learn_dir = os.path.join(base_dir, "learn")

for root, _, files in os.walk(learn_dir):
    for file in files:
        if file == "_index.md":
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Replace "## Tier 100 — " with "## "
            text = re.sub(r'##\s*Tier\s*\d+\s*[\u2014\-–]\s*', '## ', text)
            # Replace "## Tier 100" with "## Foundations"
            text = re.sub(r'##\s*Tier\s*100\b', '## Foundations', text)
            text = re.sub(r'##\s*Tier\s*200\b', '## Intermediate Skills', text)
            text = re.sub(r'##\s*Tier\s*300\b', '## Advanced Techniques', text)
            text = re.sub(r'##\s*Tier\s*400\b', '## Specialization & Pipeline', text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Cleaned tier headers in {fpath}")

print("Legacy cleanup and tier header removal completed!")