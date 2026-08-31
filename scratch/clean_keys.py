import os

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"
cleaned_count = 0

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            if not text.startswith("---"):
                continue
            
            parts = text.split("---", 2)
            if len(parts) < 3:
                continue
            
            fm_text = parts[1]
            body_text = parts[2]
            
            lines = fm_text.strip().splitlines()
            seen_keys = set()
            new_lines = []
            
            in_cascade = False
            
            for line in lines:
                if line.strip().startswith("cascade:"):
                    in_cascade = True
                    new_lines.append(line)
                    continue
                if in_cascade and (line.startswith("  ") or line.startswith("\t")):
                    new_lines.append(line)
                    continue
                else:
                    in_cascade = False
                
                if ":" in line:
                    key = line.split(":", 1)[0].strip()
                    if key in seen_keys:
                        continue
                    seen_keys.add(key)
                new_lines.append(line)
            
            new_fm = "\n".join(new_lines)
            new_text = f"---\n{new_fm}\n---" + body_text
            
            if new_text != text:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_text)
                cleaned_count += 1

print(f"Cleaned YAML front matter duplicate keys in {cleaned_count} files!")