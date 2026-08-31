import os, re

res_path = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\resources\ame23draftstandards.md"
out_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

with open(res_path, "r", encoding="utf-8") as f:
    text = f.read()

# Clean up image placeholders and anchor tags {#...}
text = re.sub(r'!\[.*?\]\[.*?\]', '', text)
text = re.sub(r'\{#.*?\}', '', text)

# Split sections based on key headings
sections = [
    ("01-overview.md", "Overview & Description", "Overview, Description, and Core Framework of AME MCS", 10, r"## \*\*Overview\*\*", r"## \*\*Arts, Media, and Entertainment: Anchor Standards\*\*"),
    ("02-anchor-standards.md", "Anchor Standards (1.0 - 12.0)", "1.0 to 12.0 Anchor Standards for Career Ready Practice", 20, r"## \*\*Arts, Media, and Entertainment: Anchor Standards\*\*", r"## \*\*Arts, Media, and Entertainment: Interdisciplinary Standards\*\*"),
    ("03-interdisciplinary-standards.md", "Interdisciplinary Standards (13.0 - 16.0)", "13.0 to 16.0 Interdisciplinary Standards", 30, r"## \*\*Arts, Media, and Entertainment: Interdisciplinary Standards\*\*", r"## \*\*Arts, Media, and Entertainment: Pathway Standards\*\*"),
    ("04-media-production-pathway.md", "Media Production Pathway", "Animation, VFX, Games, Film, TV, and Digital Communications Standards", 40, r"\*\*Media Production Pathway\*\*", r"\*\*Performance, Music, and Live Events Pathway\*\*"),
    ("05-performance-music-pathway.md", "Performance, Music & Live Events", "Stage, Event Technology, Dance, Theatre, and Music & Recording Arts", 50, r"\*\*Performance, Music, and Live Events Pathway\*\*", r"\*\*Design, Visual, and Graphic Arts Pathway\*\*"),
    ("06-design-visual-arts-pathway.md", "Design, Visual & Graphic Arts", "Design and Studio Arts Pathway Standards", 60, r"\*\*Design, Visual, and Graphic Arts Pathway\*\*", r"\*\*Registered Pre-Apprenticeship Program Alignment\*\*"),
    ("07-glossary-references.md", "Glossary & References", "AME CTE Definitions, Contributors, and References", 70, r"\*\*Registered Pre-Apprenticeship Program Alignment\*\*", None)
]

# Clear existing section files except _index.md
for existing in os.listdir(out_dir):
    if existing != "_index.md":
        os.remove(os.path.join(out_dir, existing))

for fname, title, desc, weight, start_pat, end_pat in sections:
    start_match = re.search(start_pat, text)
    if not start_match:
        print(f"Warning: Start pattern not found for {fname}")
        continue
    start_idx = start_match.start()
    
    if end_pat:
        end_match = re.search(end_pat, text[start_idx:])
        if end_match:
            section_content = text[start_idx : start_idx + end_match.start()]
        else:
            section_content = text[start_idx:]
    else:
        section_content = text[start_idx:]
        
    front_matter = f"""---
title: "{title}"
type: docs
description: "{desc}"
weight: {weight}
---

"""
    file_path = os.path.join(out_dir, fname)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(front_matter + section_content.strip() + "\n")
    print(f"Created {fname} ({len(section_content)} chars)")

print("Standards document split completed!")