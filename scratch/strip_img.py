import os

courses = [
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\imc.md",
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\gad1.md",
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\gad2.md"
]

for p in courses:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    new_lines = [l for l in lines if not l.strip().startswith("image=")]
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

print("Stripped image params from course maps!")