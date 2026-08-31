import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

# 1. Update content/courses/_index.md: Cards get image and tag
courses_idx = os.path.join(base_dir, "courses", "_index.md")
if os.path.exists(courses_idx):
    with open(courses_idx, "r", encoding="utf-8") as f:
        text = f.read()
    
    def add_course_img(m):
        c = m.group(0)
        if 'image=' not in c:
            c = c.replace('{{< card', '{{< card\n    image="/images/card-placeholder.webp"')
        return c
    
    text = re.sub(r'\{\{<\s*card[\s\S]+?>\}\}', add_course_img, text)
    with open(courses_idx, "w", encoding="utf-8") as f:
        f.write(text)
    print("Added images to Course Maps index cards!")

# 2. Update content/learn/_index.md: Cards get image and tag
learn_idx = os.path.join(base_dir, "learn", "_index.md")
if os.path.exists(learn_idx):
    with open(learn_idx, "r", encoding="utf-8") as f:
        text = f.read()
        
    def add_learn_img(m):
        c = m.group(0)
        if 'image=' not in c:
            c = c.replace('{{< card', '{{< card\n    image="/images/card-placeholder.webp"')
        return c
        
    text = re.sub(r'\{\{<\s*card[\s\S]+?>\}\}', add_learn_img, text)
    with open(learn_idx, "w", encoding="utf-8") as f:
        f.write(text)
    print("Added images to Module Library index cards!")

# 3. Update content/learn/blender/_index.md: Cards get image, tag, but NO subtitle
blender_idx = os.path.join(base_dir, "learn", "blender", "_index.md")
if os.path.exists(blender_idx):
    with open(blender_idx, "r", encoding="utf-8") as f:
        text = f.read()
        
    def format_blender_card(m):
        c = m.group(0)
        if 'image=' not in c:
            c = c.replace('{{< card', '{{< card\n    image="/images/card-placeholder.webp"')
        # Remove subtitle parameter
        c = re.sub(r'subtitle="[^"]+"\s*', '', c)
        return c
        
    text = re.sub(r'\{\{<\s*card[\s\S]+?>\}\}', format_blender_card, text)
    with open(blender_idx, "w", encoding="utf-8") as f:
        f.write(text)
    print("Formatted Blender index cards (images + tags, no description)!")

print("Card rules applied successfully!")