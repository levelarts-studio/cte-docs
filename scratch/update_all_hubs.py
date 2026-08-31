import os, re

learn_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"
updated_hubs = 0

for subj in os.listdir(learn_dir):
    subj_path = os.path.join(learn_dir, subj)
    idx_path = os.path.join(subj_path, "_index.md")
    
    if os.path.isdir(subj_path) and os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        
        # Format every card in the subject index:
        # Add image="/images/card-placeholder.webp"
        # Remove subtitle parameter
        def format_hub_card(m):
            c = m.group(0)
            if 'image=' not in c:
                c = c.replace('{{< card', '{{< card\n    image="/images/card-placeholder.webp"')
            # Remove subtitle attribute
            c = re.sub(r'subtitle="[^"]+"\s*', '', c)
            return c
            
        text = re.sub(r'\{\{<\s*card[\s\S]+?>\}\}', format_hub_card, text)
        
        if text != orig:
            with open(idx_path, "w", encoding="utf-8") as f:
                f.write(text)
            updated_hubs += 1

print(f"Updated all {updated_hubs} top-level subject library index pages with images and tags (no description)!")