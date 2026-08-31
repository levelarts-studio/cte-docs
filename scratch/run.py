import os

b = r"C:\Users\tilgh\Documents\GitHub\cte-docs"
m_tsv = os.path.join(b, "scratch", "modules.tsv")
a_tsv = os.path.join(b, "scratch", "assignments.tsv")

mc, ac = 0, 0
if os.path.exists(m_tsv):
    for l in open(m_tsv, "r", encoding="utf-8"):
        l = l.strip()
        if not l: continue
        p = l.split("\t")
        if len(p) < 7: continue
        m_id, subj, tier, slug, title, stds, kws = p
        st = ", ".join([f'"{s.strip()}"' for s in stds.split(",") if s.strip()])
        kw = ", ".join([f'"{k.strip()}"' for k in kws.split(",") if k.strip()])
        fp = os.path.join(b, "content", "learn", subj, f"{slug}.md")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        if not os.path.exists(fp):
            body = f'---\nid: {m_id}\ntitle: "{title}"\nentity: module\nsubject: {subj}\ntier: {tier}\nstatus: stub\ntools: []\nprereqs: []\nstandards: [{st}]\nkeywords: [{kw}]\nduration: 20\nvideo: ""\naliases: ["/m/{m_id}"]\n---\n\n## What you\'ll be able to do\n\n- Understand {title}.\n\n## Video\n\n## Read\n\n## Try it\n\n## Terms\n\n## Next\n{{{{< nextup >}}}}\n'
            open(fp, "w", encoding="utf-8").write(body)
            mc += 1

if os.path.exists(a_tsv):
    for l in open(a_tsv, "r", encoding="utf-8"):
        l = l.strip()
        if not l: continue
        p = l.split("\t")
        if len(p) < 7: continue
        a_id, title, tier, reqs, stds, port, sec = p
        rq = ", ".join([f'"{r.strip()}"' for r in reqs.split(",") if r.strip()])
        st = ", ".join([f'"{s.strip()}"' for s in stds.split(",") if s.strip()])
        ev = stds.split(",")[0].strip() if stds else ""
        fp = os.path.join(b, "content", "assignments", f"{a_id}.md")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        if not os.path.exists(fp):
            body = f'---\nid: {a_id}\ntitle: "{title}"\nentity: assignment\ntier: {tier}\nstatus: stub\nrequires: [{rq}]\nstandards: [{st}]\nevidence_for: "{ev}"\nportfolio: {port}\nportfolio_section: "{sec}"\nest_time: 90\nsetting: lab\naliases: ["/a/{a_id}"]\n---\n\n## The task\n\nTask for {title}.\n\n## Before you start\n\n## Steps\n\n## Submit\n\n{{{{< portfolio >}}}}\n\n## Rubric\n\n{{{{< rubric >}}}}\n'
            open(fp, "w", encoding="utf-8").write(body)
            ac += 1

print(f"Generated {mc} modules and {ac} assignments")