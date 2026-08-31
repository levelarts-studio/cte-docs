import os, re

learn_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"

for subdir in ["character", "animation"]:
    target_dir = os.path.join(learn_dir, subdir)
    if not os.path.exists(target_dir):
        continue
        
    for fname in os.listdir(target_dir):
        if fname.endswith(".md") and fname != "_index.md":
            fpath = os.path.join(target_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
                
            # Normalize estimated_time -> duration
            text = re.sub(r'(?m)^estimated_time:\s*"(\d+)\s*mins?"', r'duration: \1', text)
            text = re.sub(r'(?m)^type:\s*docs\r?\n', '', text)
            text = re.sub(r'(?m)^subject:\s*"3D Character Design"', 'subject: character', text)
            text = re.sub(r'(?m)^subject:\s*"Game Animation"', 'subject: animation', text)
            
            # Remove hardcoded badge and callout
            text = re.sub(r'(?s)\{\{<\s*badge.*?>\}\}\s*', '', text)
            text = re.sub(r'(?s)\{\{<\s*callout type="warning"\s*>\}\}.*?\{\{<\s*/callout\s*>\}\}\s*', '', text)
            
            # Add aliases if missing
            if 'aliases:' not in text:
                id_match = re.search(r'(?m)^id:\s*"?([A-Z]+-\d+)"?', text)
                if id_match:
                    mod_id = id_match.group(1)
                    text = re.sub(r'(?m)^(id:.*)$', f'\\1\naliases: ["/m/{mod_id}"]', text, count=1)
            
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Normalized {subdir}/{fname}")

print("Outlier normalization completed!")