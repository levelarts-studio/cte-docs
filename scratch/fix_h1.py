import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
fixed_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.splitlines()
            new_lines = []
            removed = False
            
            for line in lines:
                if not removed and line.startswith("# "):
                    removed = True
                    continue # Skip top-level H1 heading in markdown body
                new_lines.append(line)
                
            if removed:
                with open(path, "w", encoding="utf-8") as f:
                    f.write("\n".join(new_lines) + "\n")
                fixed_count += 1

print(f"Removed duplicate H1 headings from {fixed_count} markdown files!")