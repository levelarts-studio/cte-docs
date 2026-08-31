import os, re

standards_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

# Regex matching standard item lines like "16.1 Identify and differentiate..." or "MP.A.1.1 Apply modeling..."
std_item_regex = re.compile(r'^((?:[A-Z]{2,4}\.)?(?:[A-Z]\.)?\d+\.\d+)\s+(.+)$')

def convert_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    lines = text.splitlines()
    new_lines = []
    converted = 0
    
    for line in lines:
        match = std_item_regex.match(line.strip())
        if match and not line.startswith("{{<"):
            code = match.group(1)
            content = match.group(2)
            new_lines.append(f'{{{{< std code="{code}" >}}}}\n{content}\n{{{{< /std >}}}}')
            converted += 1
        else:
            new_lines.append(line)
            
    if converted > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines) + "\n")
        print(f"Formatted {converted} standard cards in {os.path.basename(path)}")

for f in os.listdir(standards_dir):
    if f.endswith(".md") and f != "_index.md":
        convert_file(os.path.join(standards_dir, f))

print("Visual formatting script finished!")