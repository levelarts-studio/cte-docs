import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

# 1. Overview page
overview_path = os.path.join(base_dir, "01-overview.md")
if os.path.exists(overview_path):
    with open(overview_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Add callout banner
    if "{{< callout" not in text:
        text = text.replace("## **Description**", "{{< callout type=\"info\" >}}\n**Sector Overview**: The Arts, Media, and Entertainment (AME) CTE sector prepares students for technical, creative, and project-based careers in media, game design, visual arts, and performance.\n{{< /callout >}}\n\n## **Description**", 1)
    
    # Convert numbered steps in implementation to % steps %
    if "{{% steps %}}" not in text and "### **Anchor Standards**" in text:
        text = text.replace("### **Anchor Standards**", "{{% steps %}}\n\n### **1. Anchor Standards**", 1)
        text = text.replace("### **Interdisciplinary Standards**", "### **2. Interdisciplinary Standards**", 1)
        text = text.replace("### **Pathway Standards**", "### **3. Pathway Standards**\n\n{{% /steps %}}", 1)
        
    with open(overview_path, "w", encoding="utf-8") as f:
        f.write(text)

# 2. Anchor Standards page
anchor_path = os.path.join(base_dir, "02-anchor-standards.md")
if os.path.exists(anchor_path):
    with open(anchor_path, "r", encoding="utf-8") as f:
        text = f.read()
    if "{{< callout" not in text:
        text = text.replace("## **1.0-12.0 AME Anchor Standards**", "{{< callout type=\"info\" >}}\n**Core Workplace Skills**: Twelve Anchor Standards (1.0–12.0) cover essential 21st-century workplace skills, technical literacy, problem solving, safety, and leadership.\n{{< /callout >}}\n\n## **1.0-12.0 AME Anchor Standards**", 1)
    with open(anchor_path, "w", encoding="utf-8") as f:
        f.write(text)

# 3. Media Production Pathway page
media_path = os.path.join(base_dir, "04-media-production-pathway.md")
if os.path.exists(media_path):
    with open(media_path, "r", encoding="utf-8") as f:
        text = f.read()
    if "{{< callout" not in text:
        text = text.replace("### **Animation, Visual Effects, and Games**", "{{< callout type=\"info\" >}}\n**Media Production Pathway**: Focuses on 3D modeling, animation, visual effects, game engine development, film, television, and digital communications.\n{{< /callout >}}\n\n### **Animation, Visual Effects, and Games**", 1)
    with open(media_path, "w", encoding="utf-8") as f:
        f.write(text)

# 4. Performance & Music Pathway page
perf_path = os.path.join(base_dir, "05-performance-music-pathway.md")
if os.path.exists(perf_path):
    with open(perf_path, "r", encoding="utf-8") as f:
        text = f.read()
    if "{{< callout" not in text:
        text = text.replace("### **Stage and Event Technology**", "{{< callout type=\"info\" >}}\n**Performance & Music Pathway**: Focuses on stage technology, event production, dance, theatre, audio engineering, and music recording arts.\n{{< /callout >}}\n\n### **Stage and Event Technology**", 1)
    with open(perf_path, "w", encoding="utf-8") as f:
        f.write(text)

# 5. Design & Visual Arts Pathway page
des_path = os.path.join(base_dir, "06-design-visual-arts-pathway.md")
if os.path.exists(des_path):
    with open(des_path, "r", encoding="utf-8") as f:
        text = f.read()
    if "{{< callout" not in text:
        text = text.replace("### **Design**", "{{< callout type=\"info\" >}}\n**Design & Visual Arts Pathway**: Focuses on foundational design principles, composition, branding, digital art, studio craft, and graphic communication.\n{{< /callout >}}\n\n### **Design**", 1)
    with open(des_path, "w", encoding="utf-8") as f:
        f.write(text)

# 6. Glossary page - add accordion details
gloss_path = os.path.join(base_dir, "07-glossary-references.md")
if os.path.exists(gloss_path):
    with open(gloss_path, "r", encoding="utf-8") as f:
        text = f.read()
    if "{{< details" not in text and "## **Glossary**" in text:
        text = text.replace("## **Glossary**", "## **Glossary**\n\n{{< details summary=\"Click to expand full CDE AME Glossary of Terms...\" >}}", 1)
        text = text + "\n{{< /details >}}\n"
    with open(gloss_path, "w", encoding="utf-8") as f:
        f.write(text)

print("Scrubbed and enhanced all standards pages!")