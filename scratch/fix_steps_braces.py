import os, re

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
fixed_count = 0

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Replace single brace {% steps %} or {% /steps %} with double {{% steps %}} and {{% /steps %}}
            text = re.sub(r'(?<!\{)\{\s*%\s*steps\s*%\s*\}(?!\})', '{{% steps %}}', text)
            text = re.sub(r'(?<!\{)\{\s*%\s*/\s*steps\s*%\s*\}(?!\})', '{{% /steps %}}', text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                fixed_count += 1

print(f"Fixed step shortcode braces in {fixed_count} files!")