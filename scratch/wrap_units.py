import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            
            # 1. Clean card titles: title="CODE-123: Title" or title="Assignment: Title" -> title="Title"
            text = re.sub(r'title="[A-Z]{2,4}\-\d+:\s*', 'title="', text)
            text = re.sub(r'title="Assignment:\s*', 'title="', text)
            
            # 2. Wrap Unit sections in {{< details title="Unit X: Name" closed="true" >}}
            # Split front matter
            parts = text.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                body = parts[2]
                
                # Split body by "## Unit "
                unit_blocks = re.split(r'\n(?=##\s*Unit\s+)', body)
                
                new_body = unit_blocks[0]
                for block in unit_blocks[1:]:
                    lines = block.strip().split("\n")
                    header_line = lines[0]
                    u_title = header_line.replace("## ", "").strip()
                    inner_content = "\n".join(lines[1:]).strip()
                    
                    # If already wrapped in details, avoid double wrapping
                    if "{{< details" in inner_content:
                        new_body += f"\n\n## {u_title}\n\n{inner_content}"
                    else:
                        new_body += f"\n\n{{{{< details title=\"{u_title}\" closed=\"true\" >}}}}\n\n{inner_content}\n\n{{{{< /details >}}}}"
                        
                text = f"---{fm}---\n{new_body}\n"
                
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Cleaned card titles and wrapped units in {file}")

print("Course maps updated with compact details accordions!")