import os, hashlib

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\static\images\card-art"
os.makedirs(base_dir, exist_ok=True)

palettes = {
    "blender": [("#431407", "#9a3412", "#fdba74"), ("#2e1065", "#7c2d12", "#ff8c00"), ("#3b0764", "#c2410c", "#fb923c")],
    "unreal": [("#0f172a", "#1e3a8a", "#38bdf8"), ("#0284c7", "#0f172a", "#7dd3fc"), ("#1e1b4b", "#1d4ed8", "#60a5fa")],
    "gamedesign": [("#052e16", "#15803d", "#4ade80"), ("#064e3b", "#047857", "#34d399"), ("#14532d", "#166534", "#86efac")],
    "design": [("#3b0764", "#7e22ce", "#c084fc"), ("#4c1d95", "#6b21a8", "#e879f9"), ("#2e1065", "#a21caf", "#f0abfc")],
    "media": [("#4c0519", "#be123c", "#fb7185"), ("#881337", "#9f1239", "#fda4af"), ("#450a0a", "#b91c1c", "#fca5a5")],
    "production": [("#0f172a", "#0284c7", "#38bdf8"), ("#172554", "#1d4ed8", "#93c5fd"), ("#0c4a6e", "#0369a1", "#7dd3fc")],
    "computing": [("#1e1b4b", "#4338ca", "#818cf8"), ("#311b92", "#3730a3", "#a5b4fc"), ("#0f172a", "#3b82f6", "#93c5fd")],
    "career": [("#064e3b", "#0f766e", "#2dd4bf"), ("#047857", "#115e59", "#5eead4"), ("#134e4a", "#0d9488", "#99f6e4")],
    "law": [("#451a03", "#b45309", "#fcd34d"), ("#78350f", "#d97706", "#fde047"), ("#542c09", "#92400e", "#fbbf24")],
    "assignment": [("#1e1b4b", "#4338ca", "#a5b4fc"), ("#312e81", "#3730a3", "#818cf8"), ("#2e1065", "#6b21a8", "#d8b4fe")],
}

def make_art(filename, subj, idx):
    cols = palettes.get(subj, palettes["computing"])[idx % 3]
    c1, c2, c3 = cols
    
    # Generate geometric variation based on filename
    h = int(hashlib.md5(filename.encode()).hexdigest(), 16)
    r1 = 100 + (h % 150)
    r2 = 50 + ((h >> 4) % 100)
    x1 = 600 + ((h >> 8) % 150)
    y1 = 80 + ((h >> 12) % 150)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_{subj}_{idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" />
      <stop offset="100%" stop-color="{c2}" />
    </linearGradient>
    <radialGradient id="glow_{subj}_{idx}" cx="{x1}px" cy="{y1}px" r="450px" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{c3}" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>
    <pattern id="pat_{subj}_{idx}" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{c3}" stroke-opacity="0.08" stroke-width="1.5" />
      <circle cx="20" cy="20" r="1.5" fill="{c3}" fill-opacity="0.15" />
    </pattern>
  </defs>

  <rect width="800" height="450" fill="url(#bg_{subj}_{idx})" />
  <rect width="800" height="450" fill="url(#pat_{subj}_{idx})" />
  <rect width="800" height="450" fill="url(#glow_{subj}_{idx})" />

  <!-- Abstract Tech Shapes -->
  <circle cx="{x1}" cy="{y1}" r="{r1}" fill="none" stroke="{c3}" stroke-opacity="0.2" stroke-width="2" stroke-dasharray="10 15" />
  <circle cx="{x1}" cy="{y1}" r="{r2}" fill="none" stroke="{c3}" stroke-opacity="0.3" stroke-width="1" />
  <path d="M 0 380 Q 400 {250 + (h%100)} 800 350" fill="none" stroke="{c3}" stroke-opacity="0.15" stroke-width="3" />
</svg>'''

    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(svg)

total = 0
for subj in palettes:
    for i in range(1, 4):
        fname = f"{subj}-{i}.svg"
        make_art(fname, subj, i-1)
        total += 1

print(f"Generated {total} card art backgrounds in static/images/card-art/")