import os, re

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            # Replace {{< callout type="warning" >} with {{< callout type="warning" >}}
            text = text.replace('{{< callout type="warning" >}', '{{< callout type="warning" >}}')
            # Replace {{{< /callout >}} with {{< /callout >}}
            text = text.replace('{{{< /callout >}}', '{{< /callout >}}')
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Fixed callout typo in {file}")

print("Exact callout typo fix completed!")