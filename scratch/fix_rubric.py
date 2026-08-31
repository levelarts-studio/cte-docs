import os, re

assign_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\assignments"

rubric_table = """### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **Technical Execution** | Artifact meets all technical specifications and industry practices. | Artifact meets most specifications with minor errors. | Incomplete artifact or major technical issues. |
| **Documentation & Process** | Thorough process notes, references, and breakdown. | Partial documentation or missing key references. | Incomplete documentation. |
| **Portfolio Presentation** | Well-organized on Google Sites with clear title and summary. | Embedded on Google Sites but missing description. | Not submitted to Google Sites portfolio. |
"""

for file in os.listdir(assign_dir):
    if file.endswith(".md"):
        path = os.path.join(assign_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        if "{{< rubric" in text or "{{% rubric" in text:
            # Replace {{< rubric ... >}}...{{< /rubric >}} or single tag
            text = re.sub(r'\{\{[<>] rubric.*?(?:\}\}|\{\{/rubric\}\})', rubric_table, text, flags=re.DOTALL)
            text = re.sub(r'\{\{< rubric >\}\}', rubric_table, text)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Replaced rubric shortcode in {file}")

print("Cleaned rubric shortcodes!")