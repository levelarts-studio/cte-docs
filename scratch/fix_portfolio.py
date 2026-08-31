import os

assign_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\assignments"

for file in os.listdir(assign_dir):
    if file.endswith(".md"):
        path = os.path.join(assign_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        if "{{< portfolio >}}" in text or "{{< portfolio" in text:
            text = text.replace("{{< portfolio >}}", "{{< callout type=\"warning\" >}}\n**Portfolio Deliverable**: Upload your final project artifact to your **Google Sites Portfolio** under the section specified in Classroom.\n{{< /callout >}}")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Replaced portfolio shortcode in {file}")

print("Cleaned portfolio shortcodes!")