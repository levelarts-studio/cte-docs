import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            
            # Replace {{< details title="TITLE" closed="true" >}} ... {{< /details >}}
            # with <details ...><summary>TITLE</summary><div class="hx:pt-3"> ... </div></details>
            def details_to_html(m):
                full = m.group(0)
                t_match = re.search(r'title="([^"]+)"', full)
                u_title = t_match.group(1) if t_match else "Unit Details"
                
                # Extract inner content between opening and closing shortcode
                inner = re.sub(r'^\{\{<\s*details[^>]+>\}\}', '', full)
                inner = re.sub(r'\{\{<\s*/details\s*>\}\}$', '', inner).strip()
                
                return f'<details class="hx:my-3 hx:rounded-lg hx:border hx:border-neutral-200 hx:dark:border-neutral-700 hx:bg-neutral-50 hx:dark:bg-neutral-800 hx:p-4">\n  <summary class="hx:cursor-pointer hx:font-semibold hx:text-lg hx:text-neutral-900 hx:dark:text-neutral-100">\n    {u_title}\n  </summary>\n  <div class="hx:pt-3">\n\n{inner}\n\n  </div>\n</details>'

            text = re.sub(r'\{\{<\s*details[^>]+>\}\}[\s\S]+?\{\{<\s*/details\s*>\}\}', details_to_html, text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Converted details shortcodes to native HTML details in {file}")

print("Native HTML details conversion complete!")