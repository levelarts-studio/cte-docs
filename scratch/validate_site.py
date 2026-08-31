import os, re

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs"

# 1. Load Standards keys from data/standards.yaml
standards_file = os.path.join(base_dir, "data", "standards.yaml")
valid_standards = set()
with open(standards_file, "r", encoding="utf-8") as f:
    for line in f:
        line_s = line.strip()
        if line_s and not line_s.startswith("#") and ":" in line_s and not line.startswith(" ") and not line.startswith("\t"):
            key = line_s.split(":", 1)[0].strip().strip('"').strip("'").lower()
            if key:
                valid_standards.add(key)

# 2. Front matter simple parser
def parse_fm(content):
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    res = {}
    for line in parts[1].splitlines():
        line_s = line.strip()
        if not line_s or line_s.startswith("#"):
            continue
        if ":" in line_s:
            k, v = line_s.split(":", 1)
            k, v = k.strip(), v.strip()
            if v.startswith("[") and v.endswith("]"):
                items = [i.strip().strip('"').strip("'") for i in v[1:-1].split(",") if i.strip()]
                res[k] = items
            elif (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                res[k] = v[1:-1]
            else:
                res[k] = v
    return res

module_ids = {}
assignment_ids = {}
all_ids = set()
aliases = set()
errors = []

# Scan content/learn
learn_dir = os.path.join(base_dir, "content", "learn")
for root, _, files in os.walk(learn_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            meta = parse_fm(content)
            m_id = meta.get("id")
            if m_id:
                if m_id in all_ids:
                    errors.append(f"Duplicate ID '{m_id}' in {path}")
                all_ids.add(m_id)
                module_ids[m_id] = (path, meta)
            alias_list = meta.get("aliases", [])
            for a in alias_list:
                if a in aliases:
                    errors.append(f"Duplicate alias '{a}' in {path}")
                aliases.add(a)

# Scan content/assignments
assign_dir = os.path.join(base_dir, "content", "assignments")
for root, _, files in os.walk(assign_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            meta = parse_fm(content)
            a_id = meta.get("id")
            if a_id:
                if a_id in all_ids:
                    errors.append(f"Duplicate ID '{a_id}' in {path}")
                all_ids.add(a_id)
                assignment_ids[a_id] = (path, meta)
            alias_list = meta.get("aliases", [])
            for a in alias_list:
                if a in aliases:
                    errors.append(f"Duplicate alias '{a}' in {path}")
                aliases.add(a)

# Validate prereqs & standards on modules
for m_id, (path, meta) in module_ids.items():
    prereqs = meta.get("prereqs", [])
    for pr in prereqs:
        if pr not in module_ids:
            errors.append(f"Module '{m_id}' ({path}) references unknown prereq '{pr}'")
    stds = meta.get("standards", [])
    for st in stds:
        if str(st).lower() not in valid_standards:
            errors.append(f"Module '{m_id}' ({path}) references unknown standard '{st}'")

# Validate requires & standards on assignments
for a_id, (path, meta) in assignment_ids.items():
    requires = meta.get("requires", [])
    for req in requires:
        if req not in module_ids:
            errors.append(f"Assignment '{a_id}' ({path}) references unknown requirement '{req}'")
    stds = meta.get("standards", [])
    for st in stds:
        if str(st).lower() not in valid_standards:
            errors.append(f"Assignment '{a_id}' ({path}) references unknown standard '{st}'")

# Validate Course Maps
courses_dir = os.path.join(base_dir, "content", "courses")
for root, _, files in os.walk(courses_dir):
    for file in files:
        if file.endswith(".md") and not file.startswith("_"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            for line in content.splitlines():
                if "modules:" in line:
                    m_str = line.split("modules:", 1)[1].strip()
                    if m_str.startswith("[") and m_str.endswith("]"):
                        refs = [r.strip().strip('"').strip("'") for r in m_str[1:-1].split(",") if r.strip()]
                        for r in refs:
                            if r not in module_ids:
                                errors.append(f"Course Map '{file}' references unknown module '{r}'")
                elif "assignments:" in line:
                    a_str = line.split("assignments:", 1)[1].strip()
                    if a_str.startswith("[") and a_str.endswith("]"):
                        refs = [r.strip().strip('"').strip("'") for r in a_str[1:-1].split(",") if r.strip()]
                        for r in refs:
                            if r not in assignment_ids:
                                errors.append(f"Course Map '{file}' references unknown assignment '{r}'")

print("=== VALIDATION RESULTS ===")
if errors:
    print(f"FAILED: Found {len(errors)} validation error(s):")
    for err in errors:
        print(f"  - {err}")
    exit(1)
else:
    print("SUCCESS! All site link integrity & course map validation checks passed.")
    print(f"  - Verified {len(module_ids)} modules")
    print(f"  - Verified {len(assignment_ids)} assignments")
    print(f"  - Verified {len(all_ids)} unique IDs & {len(aliases)} unique aliases")
    print(f"  - Verified all prereqs, requirements, standards, and course maps")