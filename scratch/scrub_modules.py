import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"
mod_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Format ## Try it with % steps %
            if "## Try it" in text and "{{% steps %}}" not in text:
                parts = text.split("## Try it", 1)
                header = parts[0] + "## Try it\n\n{{% steps %}}\n\n### Step 1 — Key Concepts & Tools\nReview the core principles and tool shortcuts for this lesson.\n\n### Step 2 — Practice Exercise\nFollow along in software (Blender, Unreal Engine, Krita, or PureRef) to build the exercise file.\n\n### Step 3 — Self Check & Review\nVerify your results against the rubric criteria.\n\n{{% /steps %}}\n"
                rest = parts[1]
                if "## Terms" in rest:
                    term_parts = rest.split("## Terms", 1)
                    body = "\n## Terms" + term_parts[1]
                else:
                    body = rest
                text = header + body
                
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            mod_count += 1

print(f"Scrubbed {mod_count} textbook module pages!")