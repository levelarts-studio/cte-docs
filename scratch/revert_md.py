import os, re

standards_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

for fname in os.listdir(standards_dir):
    if fname.endswith(".md"):
        path = os.path.join(standards_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Remove {{< std code="15.1" >}}\nText\n{{< /std >}}
        # Replace with - **15.1** — Text
        def replace_std(m):
            code = m.group(1)
            body = m.group(2).strip()
            return f"- **{code}** &mdash; {body}"
        
        pattern = r'\{\{< std code="([^"]+)" >\}\}\s*\n(.*?)\n\s*\{\{< /std >\}\}'
        new_text = re.sub(pattern, replace_std, text, flags=re.DOTALL)
        
        if new_text != text:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"Reverted {fname} to clean standard Markdown bullet lists!")

print("Revert script completed!")