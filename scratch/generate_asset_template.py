"""
Generates the Asset_List_and_Pipeline_Template.docx for GAD2 Module 2.4.
Matches styling and visual structure of Art_Style_Guide_Template.docx:
- Clean typography (Calibri, slate-900 / indigo / slate-500 palette)
- Shaded header rows (0F172A navy header, white bold text)
- Alternating data rows (F8FAFC and FFFFFF)
- Metadata block at top
- Explicit industry-standard tables, descriptions, and student worksheet sections
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

COLOR_PRIMARY = RGBColor(0x3B, 0x49, 0xDF)   # Royal Indigo
COLOR_DARK = RGBColor(0x0F, 0x17, 0x2A)      # Slate 900
COLOR_MUTED = RGBColor(0x64, 0x74, 0x8B)     # Slate 500
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)     # Pure White

HEX_HEADER_BG = "0F172A"                     # Deep Slate Navy
HEX_ROW_ALT = "F8FAFC"                       # Ultra Light Slate
HEX_ROW_WHITE = "FFFFFF"
HEX_META_BG = "F1F5F9"                       # Light Slate Gray
HEX_BORDER = "CBD5E1"                        # Subtle Slate Border

def set_cell_shading(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    mar_xml = (
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    cell._tc.get_or_add_tcPr().append(parse_xml(mar_xml))

def set_table_borders(table, color="E2E8F0"):
    tblPr = table._tbl.tblPr
    borders_xml = (
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(parse_xml(borders_xml))

def add_header_paragraph(doc, eyebrow_text, title_text, subtitle_text):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    p_title.paragraph_format.line_spacing = 1.15
    
    r_eye = p_title.add_run(eyebrow_text + "\n")
    r_eye.font.name = "Calibri"
    r_eye.font.size = Pt(9.5)
    r_eye.font.bold = True
    r_eye.font.color.rgb = COLOR_PRIMARY
    
    r_main = p_title.add_run(title_text)
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(22.0)
    r_main.font.bold = True
    r_main.font.color.rgb = COLOR_DARK
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run(subtitle_text)
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.0)
    r_sub.font.color.rgb = COLOR_MUTED

def add_section_header(doc, section_num_str, section_title, section_desc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    
    r_num = p.add_run(section_num_str + " ")
    r_num.font.name = "Calibri"
    r_num.font.size = Pt(12.5)
    r_num.font.bold = True
    r_num.font.color.rgb = COLOR_PRIMARY
    
    r_title = p.add_run(section_title)
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(12.5)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_DARK
    
    if section_desc:
        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_before = Pt(0)
        p_desc.paragraph_format.space_after = Pt(6)
        p_desc.paragraph_format.keep_with_next = True
        r_desc = p_desc.add_run(section_desc)
        r_desc.font.name = "Calibri"
        r_desc.font.size = Pt(9.5)
        r_desc.font.color.rgb = COLOR_MUTED

def format_styled_table(table, col_widths, headers, data_rows):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = ""
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h_text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = COLOR_WHITE
        set_cell_shading(hdr_cells[i], HEX_HEADER_BG)
        set_cell_margins(hdr_cells[i], top=80, bottom=80, left=100, right=100)
        hdr_cells[i].width = col_widths[i]
        
    # Data Rows
    for row_idx, row_data in enumerate(data_rows):
        row_cells = table.add_row().cells
        bg_hex = HEX_ROW_ALT if row_idx % 2 == 0 else HEX_ROW_WHITE
        for col_idx, text_val in enumerate(row_data):
            row_cells[col_idx].text = ""
            p = row_cells[col_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(text_val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            # Subtle bold for first column
            if col_idx == 0 and not text_val.startswith("["):
                r.font.bold = True
                r.font.color.rgb = COLOR_DARK
            elif text_val.startswith("["):
                r.font.color.rgb = COLOR_MUTED
            else:
                r.font.color.rgb = COLOR_DARK
            set_cell_shading(row_cells[col_idx], bg_hex)
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=90, right=90)
            row_cells[col_idx].width = col_widths[col_idx]

def create_document():
    doc = docx.Document()
    
    # 0.75 in margins for compact table display
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
    # Header & Subtitle
    add_header_paragraph(
        doc,
        eyebrow_text="GAME ART & DESIGN 2 · VERTICAL SLICE PRE-PRODUCTION",
        title_text="Master Asset List & Production Pipeline Document",
        subtitle_text="Official studio tracking registry, naming taxonomy, polygon budgets, LOD standards, and technical ingestion pipeline for the Vertical Slice project."
    )
    
    # Metadata Box (Table 0)
    meta_table = doc.add_table(rows=2, cols=3)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    set_table_borders(meta_table)
    
    meta_fields = [
        [
            ("PROJECT TITLE\n", "[Game / Vertical Slice Title]"),
            ("STUDIO / TEAM\n", "[Team / Studio Name]"),
            ("VERSION / DATE\n", "v1.0 · [Current Date]")
        ],
        [
            ("LEAD TECH ARTIST / ASSET LEAD\n", "[Student Name]"),
            ("TARGET ENGINE\n", "Unreal Engine 5.x"),
            ("COURSE / UNIT\n", "GAD2 · Unit 2 (Module 2.4)")
        ]
    ]
    
    col_w = [Inches(2.3), Inches(2.3), Inches(2.4)]
    for r_idx, row in enumerate(meta_table.rows):
        for c_idx, cell in enumerate(row.cells):
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            lbl, val = meta_fields[r_idx][c_idx]
            
            r_lbl = p.add_run(lbl)
            r_lbl.font.name = "Calibri"
            r_lbl.font.size = Pt(8.0)
            r_lbl.font.bold = True
            r_lbl.font.color.rgb = COLOR_MUTED
            
            r_val = p.add_run(val)
            r_val.font.name = "Calibri"
            r_val.font.size = Pt(9.5)
            r_val.font.bold = True
            r_val.font.color.rgb = COLOR_DARK
            
            set_cell_shading(cell, HEX_META_BG)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            cell.width = col_w[c_idx]
            
    # SECTION 1: Naming Conventions & Taxonomy
    add_section_header(
        doc,
        "SECTION 1:",
        "Studio Naming Conventions & UE5 Taxonomy",
        "Enforce strict, machine-readable asset syntax to prevent broken references, broken redirectors, and missing textures."
    )
    
    p_rule = doc.add_paragraph()
    p_rule.paragraph_format.space_after = Pt(6)
    r_rule_lbl = p_rule.add_run("Canonical Asset Syntax: ")
    r_rule_lbl.bold = True
    r_rule_lbl.font.size = Pt(9.5)
    r_rule_lbl.font.color.rgb = COLOR_PRIMARY
    
    r_rule_code = p_rule.add_run("[Prefix]_[Category]_[AssetName]_[Variant]_[Suffix]\n")
    r_rule_code.bold = True
    r_rule_code.font.size = Pt(9.5)
    r_rule_code.font.color.rgb = COLOR_DARK
    
    r_rule_ex = p_rule.add_run("Example: SM_Prop_Generator_01 (Static Mesh) | T_Prop_Generator_01_ORM (Packed Texture) | MI_Prop_Generator_01 (Material Instance)")
    r_rule_ex.font.size = Pt(8.5)
    r_rule_ex.font.color.rgb = COLOR_MUTED

    # Table 1.1: Prefixes
    t_prefix = doc.add_table(rows=1, cols=3)
    p_w = [Inches(1.2), Inches(1.8), Inches(4.0)]
    p_headers = ["PREFIX", "ASSET CATEGORY", "DESCRIPTION & INDUSTRY USAGE EXAMPLE"]
    p_rows = [
        ["SM_", "Static Mesh", "Rigid environment props, modular walls, floors, furniture (e.g. SM_Prop_Terminal_01)"],
        ["SK_", "Skeletal Mesh", "Rigged meshes with joints & skin weights: characters, weapons, doors (e.g. SK_Hero_Pilot)"],
        ["M_", "Master Material", "Base shader network containing parameter nodes; never applied directly (e.g. M_Prop_Master)"],
        ["MI_", "Material Instance", "Instanced shader with custom textures/parameters; applied to models (e.g. MI_Prop_Terminal_01)"],
        ["T_", "Texture Map", "2D image file paired with semantic suffix for channel role (e.g. T_Prop_Terminal_01_BC)"],
        ["BP_", "Blueprint Actor", "Interactive gameplay logic actor containing components and code (e.g. BP_Door_Airlock)"],
        ["WBP_", "Widget Blueprint", "UMG user interface widget for HUD, pause menus, reticles (e.g. WBP_HUD_HealthBar)"],
        ["NS_ / NE_", "Niagara VFX", "Niagara particle system or emitter for fire, smoke, sparks (e.g. NS_VFX_SteamVent_01)"],
        ["A_ / SFX_", "Audio Sound Wave", "Imported WAV audio file or sound cue (e.g. A_SFX_Door_Pneumatic_Open)"],
        ["UCX_", "Custom Convex Collision", "Convex collision hull exported from DCC inside mesh FBX (e.g. UCX_SM_Prop_Crate_01)"]
    ]
    format_styled_table(t_prefix, p_w, p_headers, p_rows)
    
    # Table 1.2: Texture Suffixes & Channel Packing
    p_tx_intro = doc.add_paragraph()
    p_tx_intro.paragraph_format.space_before = Pt(8)
    p_tx_intro.paragraph_format.space_after = Pt(4)
    r_tx_t = p_tx_intro.add_run("Texture Map Suffixes & Channel Packing Standards:")
    r_tx_t.bold = True
    r_tx_t.font.size = Pt(9.5)
    r_tx_t.font.color.rgb = COLOR_DARK
    
    t_suffix = doc.add_table(rows=1, cols=4)
    s_w = [Inches(1.1), Inches(1.8), Inches(1.6), Inches(2.5)]
    s_headers = ["SUFFIX", "MAP TYPE", "COLOR SPACE", "TECHNICAL RULE & PACKING"]
    s_rows = [
        ["_BC / _D", "Base Color / Albedo", "sRGB (Enabled)", "Pure surface color only. Absolutely zero pre-baked lighting or cavity AO."],
        ["_N", "Normal Map", "Linear (sRGB Off)", "Tangent space normal map (DirectX format: +X right, -Y down/green, +Z up)."],
        ["_ORM", "Packed AO / Rough / Metal", "Linear (sRGB Off)", "Red = Ambient Occlusion | Green = Roughness | Blue = Metallic."],
        ["_E", "Emissive", "sRGB (Enabled)", "Self-illumination mask multiplied by emissive color parameter for HDR glow."],
        ["_Mask", "Utility / Opacity Mask", "Linear (sRGB Off)", "Grayscale mask for alpha clipping, dirt splats, or team color shifts."]
    ]
    format_styled_table(t_suffix, s_w, s_headers, s_rows)

    # SECTION 2: Directory Architecture
    add_section_header(
        doc,
        "SECTION 2:",
        "Content Browser Directory Structure & Git Hygiene",
        "Strict project folder architecture to prevent missing assets, circular dependencies, and broken redirectors."
    )
    
    t_dirs = doc.add_table(rows=1, cols=3)
    d_w = [Inches(2.2), Inches(2.8), Inches(2.0)]
    d_headers = ["FOLDER PATH", "PERMITTED CONTENT & ASSET TYPES", "GOVERNANCE & GIT RULES"]
    d_rows = [
        ["/Game/Art/Environment/", "Modular architectural kits (walls, floors), terrain, foliage", "Sub-divided by zone (e.g. Lab, Exterior, Reactor)."],
        ["/Game/Art/Props/", "Dressing and interactable 3D props and containers", "Organized by theme (Tech, Furniture, Industrial)."],
        ["/Game/Art/Characters/", "Hero and enemy skeletal meshes, rigs, animations", "Each character gets dedicated sub-folder."],
        ["/Game/Art/Materials/", "Master shaders (M_), Material Functions (MF_), shared textures", "Instances remain in asset folders; masters live here."],
        ["/Game/Art/VFX/", "Niagara emitters, particle textures, and materials", "Fully self-contained particle assets."],
        ["/Game/Audio/", "SFX, Foley, VO, Music tracks, Sound Cues, Attenuations", "Organized into SFX, Music, and VO subdirectories."],
        ["/Game/Blueprints/", "Gameplay actors, player character, interactables, GameModes", "Only tested, working logic committed to shared main."],
        ["/Game/UI/", "Widget Blueprints (WBP_), UI textures, icons, fonts", "Standardized canvas scale (1080p baseline)."],
        ["/Game/Maps/", "Master persistent level (Slice_P) and lighting sublevels", "Level Instances used to prevent Git merge conflicts."],
        ["/Game/Developers/[Name]/", "Personal testing sandbox for individual artists & designers", "STRICT QUARANTINE: Never referenced in /Maps/."]
    ]
    format_styled_table(t_dirs, d_w, d_headers, d_rows)

    # SECTION 3: Technical Metrics, LODs & Poly Budgets
    add_section_header(
        doc,
        "SECTION 3:",
        "Technical Metrics, LODs & Poly Budgets",
        "Define polygon targets, LOD reduction chains, collision hulls, and modern Unreal Engine 5 Nanite integration rules."
    )
    
    t_budgets = doc.add_table(rows=1, cols=4)
    b_w = [Inches(1.8), Inches(1.3), Inches(2.4), Inches(1.5)]
    b_headers = ["ASSET CLASS", "LOD0 BUDGET (TRIS)", "LOD CHAIN TARGETS", "NANITE POLICY"]
    b_rows = [
        ["Hero Character", "25,000 – 45,000", "LOD1: 50% | LOD2: 25% | LOD3: 12%", "NO (Skeletal Mesh, non-Nanite)"],
        ["Hero Prop / Vehicle", "15,000 – 30,000", "LOD1: 50% | LOD2: 25% | LOD3: 10%", "YES (Nanite enabled if rigid)"],
        ["Medium Environment Prop", "3,000 – 8,000", "LOD1: 50% | LOD2: 25% | LOD3: 10%", "YES (Nanite enabled)"],
        ["Small Prop / Clutter", "300 – 1,500", "LOD1: 50% | LOD2: 20% | LOD3: Cull", "YES (Nanite or single LOD)"],
        ["Modular Architectural Piece", "200 – 1,200", "LOD1: 50% | LOD2: 25%", "YES (Nanite enabled)"]
    ]
    format_styled_table(t_budgets, b_w, b_headers, b_rows)
    
    p_tech_notes = doc.add_paragraph()
    p_tech_notes.paragraph_format.space_before = Pt(6)
    p_tech_notes.paragraph_format.space_after = Pt(6)
    runs_tech = [
        ("• Pivot & Origin Standard: ", True, COLOR_DARK),
        ("Floor-standing props MUST have pivot origin centered at Z=0 (base). Wall props pivot on rear mounting plane. Doors pivot at the hinge line. Units: 1 Unreal Unit (UU) = 1 centimeter (cm).\n", False, COLOR_MUTED),
        ("• Collision Physics Rule: ", True, COLOR_DARK),
        ("Every physical asset must have Simple Collision (UCX_ custom convex or engine box/capsule). Never leave interactive props set to 'Complex Collision as Simple' (severe CPU performance cost).\n", False, COLOR_MUTED),
        ("• Texture Budget: ", True, COLOR_DARK),
        ("Max 2048x2048 for props. 4096x4096 reserved only for hero characters or master landscape. All texture dimensions must be power-of-two (512, 1024, 2048) for mipmap streaming.", False, COLOR_MUTED)
    ]
    for txt, bld, col in runs_tech:
        r = p_tech_notes.add_run(txt)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = bld
        r.font.color.rgb = col

    # SECTION 4: Master Asset Tracking Manifest
    add_section_header(
        doc,
        "SECTION 4:",
        "Master Asset Tracking Manifest (Asset List)",
        "The single source of truth across Art, Audio, and Design. Itemize every asset required for the 5-minute slice."
    )
    
    p_man_info = doc.add_paragraph()
    p_man_info.paragraph_format.space_after = Pt(6)
    r_man_info = p_man_info.add_run(
        "Priority Key: P0 = Critical Path / Core Slice Blocker | P1 = Essential Gameplay Asset | P2 = Polish / Dressing\n"
        "Status Key: Blockout → HighPoly → LowPoly/UV → Texturing → In-Engine → Approved"
    )
    r_man_info.font.size = Pt(8.5)
    r_man_info.font.bold = True
    r_man_info.font.color.rgb = COLOR_PRIMARY
    
    t_manifest = doc.add_table(rows=1, cols=8)
    m_w = [Inches(0.8), Inches(1.6), Inches(1.1), Inches(0.9), Inches(0.5), Inches(0.8), Inches(0.7), Inches(0.6)]
    m_headers = ["ID", "ASSET NAME (CANONICAL)", "CATEGORY / ZONE", "OWNER", "PRIO", "POLY BUDGET", "COLLISION", "STATUS"]
    m_rows = [
        ["AST-001", "SM_Prop_Terminal_Console_01", "Environment Prop", "[Artist A]", "P0", "4,500 tris", "UCX Convex", "Approved"],
        ["AST-002", "SM_Mod_Wall_Panel_400x300", "Modular Kit (Lab)", "[Artist B]", "P0", "650 tris", "Simple Box", "Approved"],
        ["AST-003", "SK_Hero_Pilot_01", "Hero Character", "[Lead Artist]", "P0", "38,000 tris", "PhysicsAsset", "LowPoly/UV"],
        ["AST-004", "SM_Prop_Crate_SciFi_01", "Props (Container)", "[Artist A]", "P1", "1,200 tris", "Simple Box", "Texturing"],
        ["AST-005", "A_SFX_Door_Airlock_Cycle", "Audio SFX", "[Sound Lead]", "P0", "N/A (48kHz)", "N/A", "In-Engine"],
        ["AST-006", "WBP_HUD_ReactorStatus", "UI / UMG Widget", "[UI Artist]", "P1", "N/A (Vector)", "N/A", "Blockout"],
        ["AST-007", "NS_VFX_SteamVent_01", "Niagara VFX", "[Tech Artist]", "P2", "N/A (Emitter)", "N/A", "HighPoly"],
        ["AST-008", "[SM_Prop_Name_01]", "[Environment / Prop]", "[Assignee]", "P0", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-009", "[SM_Prop_Name_02]", "[Environment / Prop]", "[Assignee]", "P0", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-010", "[SM_Prop_Name_03]", "[Environment / Prop]", "[Assignee]", "P1", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-011", "[SM_Mod_Name_01]", "[Modular Architecture]", "[Assignee]", "P1", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-012", "[SM_Mod_Name_02]", "[Modular Architecture]", "[Assignee]", "P1", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-013", "[SK_Character_Name]", "[Character / Creature]", "[Assignee]", "P0", "[0,000 tris]", "[Collision]", "[Status]"],
        ["AST-014", "[A_SFX_Sound_Name]", "[Audio / Foley / Ambience]", "[Assignee]", "P1", "[N/A]", "[N/A]", "[Status]"],
        ["AST-015", "[WBP_UI_Widget_Name]", "[UI / HUD Element]", "[Assignee]", "P1", "[N/A]", "[N/A]", "[Status]"],
        ["AST-016", "[NS_VFX_Effect_Name]", "[Visual Effects / Niagara]", "[Assignee]", "P2", "[N/A]", "[N/A]", "[Status]"]
    ]
    format_styled_table(t_manifest, m_w, m_headers, m_rows)

    # SECTION 5: Audio & UI Asset Specifications
    add_section_header(
        doc,
        "SECTION 5:",
        "Audio & UI Asset Technical Standards",
        "Specifications for non-mesh assets to ensure balanced soundscapes and responsive interface presentation."
    )
    
    t_audioui = doc.add_table(rows=1, cols=4)
    au_w = [Inches(1.8), Inches(1.5), Inches(2.2), Inches(1.5)]
    au_headers = ["ASSET TYPE", "TECHNICAL FORMAT", "SPATIALIZATION & BEHAVIOR", "MEMORY / RESOLUTION"]
    au_rows = [
        ["3D Spatialized SFX", "48kHz / 16-bit Mono WAV", "Linear/Logarithmic Attenuation (200cm - 1800cm)", "< 400 KB per one-shot"],
        ["Ambient Environmental Loop", "48kHz / 16-bit Stereo WAV", "Seamless loop points, concurrency limit 2", "< 4 MB per sound bed"],
        ["2D UI Feedback Audio", "48kHz / 16-bit Stereo WAV", "Non-spatialized (Plays direct to 2D master)", "< 150 KB, crisp attack"],
        ["UI HUD Widget / Icons", "PNG with Alpha / 9-Slice", "Anchored to canvas; responsive 1080p/4K", "512x512 max power-of-2"],
        ["Font Typography", "OTF / TTF Format", "High readability at small sizes; licensable", "< 500 KB per weight"]
    ]
    format_styled_table(t_audioui, au_w, au_headers, au_rows)

    # SECTION 6: Ingestion & Quality Gate Protocol
    add_section_header(
        doc,
        "SECTION 6:",
        "Asset Ingestion & Quality Gate Protocol",
        "Mandatory pre-commit technical verification checklist. Every asset must satisfy all criteria before being merged into the master branch."
    )
    
    t_gate = doc.add_table(rows=1, cols=3)
    g_w = [Inches(0.6), Inches(2.4), Inches(4.0)]
    g_headers = ["GATE", "VERIFICATION STAGE", "TECHNICAL ACCEPTANCE CRITERIA"]
    g_rows = [
        ["QG-1", "Transforms & Scale", "In Blender: Scale is applied (1.0, 1.0, 1.0) and rotation is zeroed. Units match 1:1 in Unreal."],
        ["QG-2", "Origin & Pivot Alignment", "Floor props pivot at absolute bottom (Z=0). Doors pivot at hinge. Socket locations added."],
        ["QG-3", "Naming & File Cleanliness", "Prefix, category, name, variant, and suffix follow Section 1. Zero spaces. Zero special characters."],
        ["QG-4", "Geometry & Topology", "Zero non-manifold edges, zero internal faces, zero un-welded boundary seams. Clean quad/tri flow."],
        ["QG-5", "UV Unwrapping & Density", "UV Channel 0 has zero overlapping islands. Texel density matches project target (10.24 px/cm)."],
        ["QG-6", "Texture Channel Packing", "ORM texture packed correctly (Red = AO, Green = Roughness, Blue = Metallic). sRGB unchecked."],
        ["QG-7", "Material Instancing", "Mesh uses Material Instance (MI_) derived from approved Master Material (M_). Zero loose raw shaders."],
        ["QG-8", "Collision Geometry", "Simple UCX_ convex hull or primitive collision verified in UE5 viewport (Alt + C). Player cannot clip."],
        ["QG-9", "LODs / Nanite Verification", "Nanite enabled for rigid geometry, or LOD0-LOD3 reduction chain validated without popping."],
        ["QG-10", "Source File Repository", "Raw .blend or .spp source saved in project art_source directory; clean layer naming preserved."]
    ]
    format_styled_table(t_gate, g_w, g_headers, g_rows)

    # SECTION 7: Team Sign-Off & Deliverable Checklist
    add_section_header(
        doc,
        "SECTION 7:",
        "Team Sign-Off & Deliverable Checklist",
        "Complete all checklist items before submitting your master asset registry to Google Sites."
    )
    
    t_signoff = doc.add_table(rows=1, cols=4)
    so_w = [Inches(0.6), Inches(2.6), Inches(1.8), Inches(2.0)]
    so_headers = ["DONE", "DELIVERABLE REQUIREMENT", "TEAM ROLE RESPONSIBLE", "SIGN-OFF STATUS"]
    so_rows = [
        ["[  ]", "Audit of greybox slice completed (all required meshes listed)", "Level Designer & Tech Artist", "[Pending / Complete]"],
        ["[  ]", "Naming convention table reviewed and adopted by all artists", "Lead Technical Artist", "[Pending / Complete]"],
        ["[  ]", "Folder structure verified inside /Game/ content root", "Lead Technical Artist", "[Pending / Complete]"],
        ["[  ]", "Master Asset Tracking Manifest populated (min 15 unique assets)", "Entire Studio Team", "[Pending / Complete]"],
        ["[  ]", "All P0 critical-path assets assigned with explicit owners & budgets", "Production Lead", "[Pending / Complete]"],
        ["[  ]", "Audio SFX and UI asset specifications documented", "Audio & UI Leads", "[Pending / Complete]"],
        ["[  ]", "Ingestion quality gate test passed for first batch of blockouts", "Lead Technical Artist", "[Pending / Complete]"],
        ["[  ]", "Document exported as PDF and embedded in Google Sites portfolio", "All Team Members", "[Pending / Complete]"]
    ]
    format_styled_table(t_signoff, so_w, so_headers, so_rows)
    
    return doc

if __name__ == "__main__":
    doc = create_document()
    
    res_path = os.path.join("static", "resources", "Asset_List_and_Pipeline_Template.docx")
    down_path = os.path.join("static", "downloads", "Asset_List_and_Pipeline_Template.docx")
    
    os.makedirs(os.path.dirname(res_path), exist_ok=True)
    os.makedirs(os.path.dirname(down_path), exist_ok=True)
    
    doc.save(res_path)
    doc.save(down_path)
    print(f"Successfully generated: {res_path} ({os.path.getsize(res_path)} bytes)")
    print(f"Successfully generated: {down_path} ({os.path.getsize(down_path)} bytes)")

