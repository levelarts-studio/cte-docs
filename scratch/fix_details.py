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
            
            # Replace {{< details summary="Title Text" >}} with {{< details title="Title Text" closed="true" >}}
            def fix_details(m):
                full = m.group(0)
                # match summary="..." or title="..."
                t_val = ""
                s_match = re.search(r'summary="([^"]+)"', full)
                if s_match:
                    t_val = s_match.group(1)
                else:
                    t_match = re.search(r'title="([^"]+)"', full)
                    if t_match:
                        t_val = t_match.group(1)
                
                if t_val:
                    return f'{{{{< details title="{t_val}" closed="true" >}}}}'
                return full

            text = re.sub(r'\{\{< details[^>]+>\}\}', fix_details, text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                fixed_count += 1

print(f"Updated details shortcodes with title= and closed=true in {fixed_count} files!")