import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"
cleaned_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            
            # Remove ## Video and ## Read sections
            new_text = text.replace("## Video\n\n", "").replace("## Read\n\n", "").replace("## Video\r\n\r\n", "").replace("## Read\r\n\r\n", "")
            
            if new_text != text:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_text)
                cleaned_count += 1

print(f"Cleaned {cleaned_count} module pages!")