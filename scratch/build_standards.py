import os, re

res_path = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\resources\ame23draftstandards.md"
out_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\standards"

with open(res_path, "r", encoding="utf-8") as f:
    text = f.read()

# Clean up raw markdown image placeholders like ![California Department of Education Logo.][image1]
cleaned_text = re.sub(r'!\[.*?\]\[.*?\]', '', text)
# Clean up raw anchor hashes in headers like {#draft:-2023...}
cleaned_text = re.sub(r'\{#.*?\}', '', cleaned_text)

# 1. Full document
full_doc = f"""---
title: 2023 AME Model Curriculum Standards (Complete)
type: docs
description: Complete California Department of Education Arts, Media, and Entertainment Model Curriculum Standards reference document.
weight: 1
---

{cleaned_text}
"""

with open(os.path.join(out_dir, "cte-arts-entertainment-design-standards.md"), "w", encoding="utf-8") as f:
    f.write(full_doc)

print("Created content/standards/cte-arts-entertainment-design-standards.md!")