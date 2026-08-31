import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
dups = []

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            lines = content.splitlines()
            title = None
            for line in lines:
                if line.startswith("title:"):
                    title = line.split("title:", 1)[1].strip().strip('"').strip("'")
                    break
            for line in lines:
                if line.startswith("# "):
                    h1 = line[2:].strip().strip('"').strip("'")
                    dups.append((path, title, h1))
                    break

print(f"Found {len(dups)} files with H1 (# ) headings:")
for path, title, h1 in dups[:20]:
    print(f"  {os.path.basename(path)} -> Title: '{title}' | H1: '{h1}'")