import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

for fname in os.listdir(base_dir):
    if fname.endswith(".md"):
        path = os.path.join(base_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        lines = text.splitlines()
        has_desc = any(l.startswith("description:") for l in lines)
        has_sum = any(l.startswith("summary:") for l in lines)
        
        title_val = "Standards Section"
        for l in lines:
            if l.startswith("title:"):
                title_val = l.split("title:", 1)[1].strip().strip('"').strip("'")
                break
                
        new_fm = []
        if not has_desc:
            new_fm.append(f'description: "{title_val}"')
        if not has_sum:
            new_fm.append(f'summary: "{title_val}"')
            
        if new_fm:
            text = text.replace("---\n", "---\n" + "\n".join(new_fm) + "\n", 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Added desc/summary to {fname}")

print("Fixed standards metadata!")