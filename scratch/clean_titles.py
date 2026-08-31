import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"
mod_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            
            # Clean card title="CODE: Title" -> title="Title" in _index.md files
            def clean_card_title(m):
                full_attr = m.group(0)
                # match title="CODE-123: Title" or title="CODE: Title"
                cleaned_attr = re.sub(r'title="[A-Z]{2,4}\-\d+:\s*', 'title="', full_attr)
                return cleaned_attr
            
            text = re.sub(r'title="[A-Z]{2,4}\-\d+:[^"]+"', clean_card_title, text)
            
            # Clean front matter title: "CODE-123: Title" -> title: "Title"
            text = re.sub(r'title:\s*"[A-Z]{2,4}\-\d+:\s*', 'title: "', text)
            
            # If leaf module page, add badge at top if id is present and badge not yet added
            if file != "_index.md" and "id:" in text:
                id_match = re.search(r'id:\s*"([^"]+)"', text)
                if id_match:
                    mod_id = id_match.group(1)
                    badge_str = f'{{{{< badge content="{mod_id}" color="indigo" >}}}}\n\n'
                    if badge_str.strip() not in text:
                        text = text.replace("---\n\n", f"---\n\n{badge_str}", 1)
                        if badge_str.strip() not in text and text.startswith("---"):
                            parts = text.split("---", 2)
                            if len(parts) >= 3:
                                text = f"---{parts[1]}---\n\n{badge_str}" + parts[2].lstrip()

            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                mod_count += 1

print(f"Cleaned card titles and added badges across {mod_count} module files!")