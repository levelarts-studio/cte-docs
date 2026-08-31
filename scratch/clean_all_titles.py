import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Remove any CODE-123: prefix from markdown link text: [CODE-123: Title] -> [Title]
            text = re.sub(r'\[[A-Z]{2,4}\-\d+:\s*', '[', text)
            # Remove Assignment: prefix from link text: [Assignment: Title] -> [Title]
            text = re.sub(r'\[Assignment:\s*', '[', text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Cleaned remaining title prefixes in {file}")

print("Cleaned all remaining course link titles!")