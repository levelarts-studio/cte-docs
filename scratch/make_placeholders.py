import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\static\images\placeholders"
os.makedirs(base_dir, exist_ok=True)

def make_svg(filename, title, subtitle, color1, color2):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color1}" />
      <stop offset="100%" stop-color="{color2}" />
    </linearGradient>
    <radialGradient id="glow" cx="80%" cy="20%" r="60%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-opacity="0.05" stroke-width="1" />
    </pattern>
  </defs>

  <rect width="800" height="450" fill="url(#bg)" />
  <rect width="800" height="450" fill="url(#grid)" />
  <rect width="800" height="450" fill="url(#glow)" />

  <!-- Accent Circle -->
  <circle cx="700" cy="100" r="180" fill="#ffffff" fill-opacity="0.03" />

  <g transform="translate(60, 220)">
    <text font-family="system-ui, -apple-system, sans-serif" font-weight="800" font-size="44" fill="#ffffff" letter-spacing="-1">{title}</text>
    <text y="45" font-family="system-ui, -apple-system, sans-serif" font-weight="500" font-size="22" fill="#ffffff" fill-opacity="0.75">{subtitle}</text>
  </g>
  
  <rect x="60" y="320" width="80" height="4" rx="2" fill="#ffffff" fill-opacity="0.4" />
</svg>'''
    path = os.path.join(base_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

items = [
    ("computing.svg", "Computing & Hardware", "PC Literacy & OS Systems", "#1e1b4b", "#311b92"),
    ("design.svg", "Design & Visual Craft", "Color, Composition & Line", "#3b0764", "#4c1d95"),
    ("media.svg", "Media & Storytelling", "Narrative, Shots & Editing", "#4c0519", "#881337"),
    ("career.svg", "Career & Portfolio", "Resumes, O*NET & Industry", "#064e3b", "#047857"),
    ("law.svg", "Law, Ethics & AI", "Copyright, IP & Attribution", "#451a03", "#78350f"),
    ("production.svg", "Production & Pipelines", "GDD, Agile & Teamwork", "#172554", "#1e40af"),
    ("blender.svg", "Blender 3D", "Modeling, UVs & Texturing", "#431407", "#9a3412"),
    ("unreal.svg", "Unreal Engine 5", "Blueprints, Lumen & Scenes", "#0f172a", "#1e293b"),
    ("gamedesign.svg", "Game Design", "Mechanics, Pacing & Feel", "#14532d", "#15803d"),
    ("assignment.svg", "Assignment Spec", "Required Deliverable & Rubric", "#312e81", "#4338ca"),
    ("course-imc.svg", "Intro to Media Careers", "IMC Course Map & Pathways", "#1e1b4b", "#4338ca"),
    ("course-gad1.svg", "Game Art & Design 1", "3D Modeling, Textures & Engine", "#064e3b", "#047857"),
    ("course-gad2.svg", "Game Art & Design 2", "Tech Art, Blueprints & Capstone", "#431407", "#7c2d12"),
]

for name, title, sub, c1, c2 in items:
    make_svg(name, title, sub, c1, c2)

print(f"Generated {len(items)} SVG placeholder banners!")