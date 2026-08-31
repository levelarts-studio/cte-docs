import os

assign_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\assignments"
scrubbed_count = 0

for file in os.listdir(assign_dir):
    if file.endswith(".md") and not file.startswith("_"):
        path = os.path.join(assign_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Ensure portfolio callout is shortcode
        if "{{< portfolio >}}" not in text and "{{< callout" not in text:
            text = text.replace("## Submit", "{{< callout type=\"warning\" >}}\n**Portfolio Deliverable**: Upload your final project artifact to your **Google Sites Portfolio** under the section specified in Classroom.\n{{< /callout >}}\n\n## Submit")
        
        # Convert numbered steps under ## Steps to % steps %
        if "## Steps" in text and "{{% steps %}}" not in text:
            parts = text.split("## Steps", 1)
            header = parts[0] + "## Steps\n\n{{% steps %}}\n"
            rest = parts[1]
            if "## Submit" in rest:
                step_parts = rest.split("## Submit", 1)
                body = step_parts[0] + "\n{{% /steps %}}\n\n## Submit" + step_parts[1]
            else:
                body = rest + "\n{{% /steps %}}\n"
            text = header + body
            
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        scrubbed_count += 1

print(f"Scrubbed {scrubbed_count} assignment pages!")