import os, re

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Replace {{< card image="..."s >}} or {{< card s >}} with {{< cards >}}
            text = re.sub(r'\{\{<\s*card[^>]*s\s*>\}\}', '{{< cards >}}', text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Fixed cards tag typo in {file}")

print("Fixed all cards tag typos!")