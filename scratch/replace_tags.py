import os, re

content_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content"

tag_map = {
    "/learn/blender/": ("3D MODELING", "orange"),
    "/learn/unreal/": ("ENGINE", "indigo"),
    "/learn/character/": ("3D CHARACTER", "purple"),
    "/learn/animation/": ("GAME ANIMATION", "blue"),
    "/learn/gamedesign/": ("GAME DESIGN", "green"),
    "/learn/design/": ("VISUAL CRAFT", "purple"),
    "/learn/media/": ("MEDIA STORY", "amber"),
    "/learn/production/": ("PIPELINE", "indigo"),
    "/learn/computing/": ("COMPUTING", "blue"),
    "/learn/career/": ("CAREER", "green"),
    "/learn/law/": ("ETHICS & LAW", "amber"),
    "/assignments/": ("LAB SPEC", "indigo")
}

updated_files = 0

for root, _, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            orig = text
            
            # Replace tag="STUB" based on link pattern inside card shortcode
            def replace_card_stub(m):
                card_str = m.group(0)
                new_tag = "LESSON"
                new_color = "indigo"
                
                for path_key, (tag_val, col_val) in tag_map.items():
                    if path_key in card_str:
                        new_tag = tag_val
                        new_color = col_val
                        break
                        
                card_str = re.sub(r'tag="STUB"', f'tag="{new_tag}"', card_str)
                card_str = re.sub(r'tagColor="[^"]+"', f'tagColor="{new_color}"', card_str)
                if 'tagColor=' not in card_str:
                    card_str = card_str.replace(f'tag="{new_tag}"', f'tag="{new_tag}"\n    tagColor="{new_color}"')
                return card_str

            text = re.sub(r'\{\{< card[^>]+>\}\}', replace_card_stub, text, flags=re.DOTALL)
            # Catch multi-line card shortcodes
            text = re.sub(r'\{\{< card[\s\S]+?>\}\}', replace_card_stub, text)
            
            if text != orig:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(text)
                updated_files += 1

print(f"Updated STUB tags across {updated_files} files!")