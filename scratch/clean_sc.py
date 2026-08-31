import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Remove {{< nextup >}}
            if "{{< nextup >}}" in text or "{{< nextup" in text:
                text = re.sub(r'\{\{[<>] nextup.*?\}\}', '', text)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Removed nextup in {file}")

print("Custom shortcode cleanup finished!")