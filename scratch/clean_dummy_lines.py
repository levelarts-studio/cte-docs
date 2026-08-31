import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Remove any line that matches "- **[Module](#)**"
            lines = [l for l in text.split("\n") if "- **[Module](#)**" not in l]
            text = "\n".join(lines)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Cleaned dummy list lines in {file}")

print("Cleaned dummy lines!")