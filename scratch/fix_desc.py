import os

files = {
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\imc.md": "Intro to Media Careers course map outlining units, modules, and assignments.",
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\gad1.md": "Game Art & Design 1 course map outlining 3D modeling, texturing, and Unreal Engine units.",
    r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\courses\gad2.md": "Game Art & Design 2 course map outlining technical art, retopology, and capstone units."
}

for path, desc_text in files.items():
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "description:" not in text:
        text = text.replace("---\n", f"---\ndescription: \"{desc_text}\"\n", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

print("Added explicit description params to course maps!")