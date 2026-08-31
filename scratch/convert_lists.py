import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            
            # Helper to convert cards block inside details to clean bullet list
            def cards_to_list(m):
                cards_block = m.group(0)
                list_items = []
                
                # Find all {{< card ... >}}
                card_matches = re.findall(r'\{\{<\s*card([\s\S]+?)>\}\}', cards_block)
                for card_str in card_matches:
                    link_m = re.search(r'link="([^"]+)"', card_str)
                    title_m = re.search(r'title="([^"]+)"', card_str)
                    sub_m = re.search(r'subtitle="([^"]+)"', card_str)
                    tag_m = re.search(r'tag="([^"]+)"', card_str)
                    
                    c_link = link_m.group(1) if link_m else "#"
                    c_title = title_m.group(1) if title_m else "Module"
                    c_sub = sub_m.group(1) if sub_m else ""
                    c_tag = tag_m.group(1) if tag_m else "MODULE"
                    
                    # Clean title prefix if any remains
                    c_title = re.sub(r'^[A-Z]{2,4}\-\d+:\s*', '', c_title)
                    c_title = re.sub(r'^Assignment:\s*', '', c_title)
                    
                    list_items.append(f'- **[{c_title}]({c_link})** — *{c_sub}* `{c_tag}`')
                
                return "\n".join(list_items)

            # Replace {{< cards >}} ... {{< /cards >}} with compact list items
            text = re.sub(r'\{\{<\s*cards\s*>\}\}[\s\S]+?\{\{<\s*/cards\s*>\}\}', cards_to_list, text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Converted cards to compact button lists in {file}")

print("Course units converted to compact list items!")