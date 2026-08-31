import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"

for subject in os.listdir(base_dir):
    subj_path = os.path.join(base_dir, subject)
    index_path = os.path.join(subj_path, "_index.md")
    
    if os.path.isdir(subj_path) and os.path.exists(index_path):
        # Read all module files in subject directory
        modules = []
        for file in os.listdir(subj_path):
            if file.endswith(".md") and file != "_index.md":
                fpath = os.path.join(subj_path, file)
                with open(fpath, "r", encoding="utf-8") as f:
                    text = f.read()
                
                # Extract title, description, weight, id, status
                mod_title = file.replace(".md", "").replace("-", " ").title()
                t_match = re.search(r'title:\s*"([^"]+)"', text)
                if t_match:
                    mod_title = t_match.group(1)
                    # Strip any prefix like "BLND-101: "
                    mod_title = re.sub(r'^[A-Z]{2,4}\-\d+:\s*', '', mod_title)
                    
                mod_desc = "Textbook module."
                d_match = re.search(r'description:\s*"([^"]+)"', text)
                if d_match:
                    mod_desc = d_match.group(1)
                    # Strip prefix from desc
                    mod_desc = re.sub(r'^[A-Z]{2,4}\-\d+:\s*', '', mod_desc)
                    mod_desc = re.sub(r' textbook module stub\.', '', mod_desc)
                
                mod_weight = 100
                w_match = re.search(r'weight:\s*(\d+)', text)
                if w_match:
                    mod_weight = int(w_match.group(1))
                    
                mod_status = "STUB"
                s_match = re.search(r'status:\s*"([^"]+)"', text)
                if s_match:
                    mod_status = s_match.group(1).upper()
                    
                rel_link = f"/learn/{subject}/{file.replace('.md', '')}/"
                modules.append({
                    "title": mod_title,
                    "desc": mod_desc,
                    "weight": mod_weight,
                    "status": mod_status,
                    "link": rel_link
                })
        
        # Sort modules by weight
        modules.sort(key=lambda x: x["weight"])
        
        if not modules:
            continue
            
        # Group into 3-4 logical progression sections
        chunk_size = max(1, (len(modules) + 2) // 3)
        sections = [
            ("Foundations & Principles", modules[:chunk_size]),
            ("Core Workflows & Applied Craft", modules[chunk_size:chunk_size*2]),
            ("Advanced Pipeline & Specialization", modules[chunk_size*2:])
        ]
        
        # Read index front matter
        with open(index_path, "r", encoding="utf-8") as f:
            idx_text = f.read()
            
        fm_parts = idx_text.split("---", 2)
        if len(fm_parts) >= 3:
            fm = fm_parts[1].strip()
            # Title header
            subj_name = subject.replace("-", " ").title()
            body_md = f"Textbook modules for **{subj_name}** organized in sequential learning order from basic foundations to advanced production pipelines.\n\n"
            
            for sec_title, sec_mods in sections:
                if not sec_mods:
                    continue
                body_md += f"## {sec_title}\n\n{{{{< cards >}}}}\n"
                for m in sec_mods:
                    body_md += f'  {{{{< card\n    link="{m["link"]}"\n    title="{m["title"]}"\n    subtitle="{m["desc"]}"\n    tag="{m["status"]}"\n    tagColor="amber"\n  >}}}}\n'
                body_md += "{{{{< /cards >}}}}\n\n"
                
            new_index_content = f"---\n{fm}\n---\n\n{body_md}"
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(new_index_content)
            print(f"Populated grid cards for {index_path} ({len(modules)} modules)")

print("All subject index pages populated with clean grid cards!")