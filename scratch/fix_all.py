import os, re

# 1. Update hugo.yaml with global cascade
hugo_path = r"C:\Users\tilgh\Documents\GitHub\cte-docs\hugo.yaml"
with open(hugo_path, "r", encoding="utf-8") as f:
    hugo_text = f.read()

if "cascade:" not in hugo_text:
    hugo_text += "\ncascade:\n  - type: docs\n"
    with open(hugo_path, "w", encoding="utf-8") as f:
        f.write(hugo_text)
    print("Added global cascade: type: docs to hugo.yaml!")

# 2. Fix broken callouts and steps syntax across all content .md files
content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
fixed_files = 0

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig_text = text
            
            # Fix {< callout -> {{< callout
            text = re.sub(r'\{\s*<\s*callout', '{{< callout', text)
            # Fix {< /callout -> {{< /callout
            text = re.sub(r'\{\s*<\s*/\s*callout\s*>\s*\}', '{{< /callout >}}', text)
            text = re.sub(r'\{\s*<\s*/\s*callout', '{{< /callout', text)
            
            # Fix {< cards -> {{< cards
            text = re.sub(r'\{\s*<\s*cards', '{{< cards', text)
            text = re.sub(r'\{\s*<\s*/\s*cards', '{{< /cards', text)
            
            # Fix {< card -> {{< card
            text = re.sub(r'\{\s*<\s*card', '{{< card', text)
            text = re.sub(r'\{\s*<\s*/\s*card', '{{< /card', text)

            # Fix {% steps -> {{% steps %}}
            text = re.sub(r'\{\s*%\s*steps', '{{% steps %}}', text)
            text = re.sub(r'\{\s*%\s*/\s*steps', '{{% /steps %}}', text)
            
            # Ensure type: docs in front matter if missing
            if file.startswith("_index.md") and "cascade:" not in text:
                text = text.replace("---\n", "---\ntype: docs\ncascade:\n  type: docs\n", 1)
            
            if text != orig_text:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                fixed_files += 1

print(f"Fixed callout/steps syntax and front matter in {fixed_files} files!")