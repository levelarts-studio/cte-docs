import os, re

courses_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses"

for fname in os.listdir(courses_dir):
    if fname.endswith(".md"):
        fpath = os.path.join(courses_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Regex to strip CODE: or CODE - prefixes from titles in unit-item-title divs
        # e.g. <div class="unit-item-title">MEDIA-101: What Makes a Story</div> -> <div class="unit-item-title">What Makes a Story</div>
        text = re.sub(r'(<div class="unit-item-title">)[A-Z]+-\d+:\s*', r'\1', text)
        text = re.sub(r'(<div class="unit-item-title">)[A-Z]+-\d+\s*-\s*', r'\1', text)
        
        # Also clean markdown link text if any remain
        text = re.sub(r'(\*\*\[)[A-Z]+-\d+:\s*', r'\1', text)
        text = re.sub(r'(\*\*\[)[A-Z]+-\d+\s*-\s*', r'\1', text)
        
        if text != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Stripped code prefixes in {fname}")

print("All course maps cleaned of course code prefixes!")