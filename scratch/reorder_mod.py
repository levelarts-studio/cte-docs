import os

base_dir = r"C:\Users\tilgh\Documents\GitHub\cte-docs\content\learn"

# Ordered list of modules for each subject from Basic to Advanced
ordering = {
    "blender": [
        "interface-and-navigation.md",
        "objects-transforms-and-pivots.md",
        "primitive-modeling.md",
        "edit-mode-basics.md",
        "viewport-shading-and-preview.md",
        "modifiers-introduction.md",
        "hard-surface-modeling.md",
        "topology-and-edge-flow.md",
        "uv-unwrapping.md",
        "texturing-and-pbr-maps.md",
        "baking-normal-maps.md",
        "cameras-and-rendering.md",
        "lighting-in-blender.md",
        "sculpting-introduction.md",
        "retopology.md",
        "modular-kit-building.md",
        "poly-budget-and-lods.md",
        "game-ready-export.md",
        "saving-packing-and-exporting.md",
        "keyframe-animation-basics.md",
        "rigging-basics.md"
    ],
    "unreal": [
        "project-setup-and-folder-structure.md",
        "interface-and-navigation.md",
        "placing-and-transforming-actors.md",
        "importing-assets.md",
        "level-blockout-workflow.md",
        "lighting-basics.md",
        "nanite-and-lumen.md",
        "materials-basics.md",
        "collision-and-triggers.md",
        "blueprint-fundamentals.md",
        "variables-and-flow-control.md",
        "input-and-character-movement.md",
        "ui-widgets-and-hud.md",
        "audio-in-engine.md",
        "landscape-and-environment.md",
        "data-tables-and-save-systems.md",
        "performance-and-profiling.md",
        "packaging-a-build.md"
    ],
    "gamedesign": [
        "what-is-a-game.md",
        "genres-and-player-profiles.md",
        "mechanics-dynamics-aesthetics.md",
        "the-core-loop.md",
        "player-guidance-and-affordance.md",
        "level-design-basics.md",
        "game-feel-and-feedback.md",
        "rapid-prototyping.md",
        "playtesting-methods.md",
        "systems-and-balancing.md",
        "economy-and-progression.md",
        "ux-and-ui-principles.md",
        "narrative-in-games.md",
        "worldbuilding-and-environmental-storytelling.md",
        "accessibility-in-games.md",
        "multiplayer-and-networking-concepts.md",
        "monetization-models.md"
    ],
    "design": [
        "elements-of-art.md",
        "line-shape-and-form.md",
        "value-and-contrast.md",
        "principles-of-design.md",
        "composition-and-focal-point.md",
        "color-theory-basics.md",
        "color-modes-and-spaces.md",
        "perspective-and-depth.md",
        "mood-boards-and-reference.md",
        "thumbnails-and-ideation.md",
        "storyboarding-basics.md",
        "shape-language-in-character-design.md",
        "silhouette-and-readability.md",
        "typography-basics.md",
        "wireframes-and-layout.md",
        "color-scripting-and-mood.md",
        "iteration-and-revision.md",
        "the-critique-process.md"
    ],
    "media": [
        "what-makes-a-story.md",
        "narrative-structure.md",
        "character-and-conflict.md",
        "pre-production-documents.md",
        "point-of-view.md",
        "shot-types-and-framing.md",
        "camera-angles-and-movement.md",
        "sound-in-story.md",
        "continuity-and-coverage.md",
        "editing-cuts-and-transitions.md",
        "exporting-and-delivery.md",
        "reading-a-media-message.md",
        "source-credibility-and-bias.md",
        "platform-and-audience.md"
    ],
    "production": [
        "production-phases.md",
        "roles-on-a-creative-team.md",
        "the-creative-brief.md",
        "the-game-design-document.md",
        "project-planning-and-milestones.md",
        "task-boards-and-sprints.md",
        "meetings-standups-and-notes.md",
        "giving-and-receiving-feedback.md",
        "pitching-a-concept.md",
        "asset-management-and-naming.md",
        "version-control-for-teams.md",
        "budgets-and-resources.md",
        "scope-and-the-vertical-slice.md",
        "handoff-and-documentation.md"
    ],
    "computing": [
        "what-a-computer-is-doing.md",
        "operating-systems-and-why-they-differ.md",
        "files-folders-and-paths.md",
        "file-types-and-extensions.md",
        "naming-conventions.md",
        "keyboard-fluency-and-shortcuts.md",
        "ergonomics-and-the-workstation.md",
        "installing-and-updating-software.md",
        "cloud-vs-local-storage-and-backup.md",
        "reading-a-spec-sheet.md",
        "staying-safe-and-private-online.md",
        "accounts-passwords-phishing.md"
    ],
    "career": [
        "interests-skills-and-aptitude.md",
        "the-arts-entertainment-design-cluster.md",
        "pathways-focus-areas-job-titles.md",
        "game-industry-roles-map.md",
        "reading-an-onet-entry.md",
        "education-and-training-routes.md",
        "staff-freelance-and-work-for-hire.md",
        "entrepreneurship-and-freelancing.md",
        "unions-guilds-and-professional-orgs.md",
        "professional-email-and-communication.md",
        "resumes.md",
        "artist-statement-and-bio.md",
        "documenting-your-work.md",
        "building-a-google-sites-portfolio.md",
        "interviews-and-portfolio-review.md",
        "careers-portfolio-page.md",
        "networking-and-professional-presence.md",
        "cross-sector-careers-for-game-skills.md"
    ],
    "law": [
        "what-intellectual-property-is.md",
        "copyright-basics.md",
        "fair-use-the-four-factors.md",
        "licenses-cc-royalty-free-commercial.md",
        "attribution-and-citing-sources.md",
        "trademark-and-publicity-rights.md",
        "ndas-and-confidentiality.md",
        "contracts-and-terms.md",
        "terms-of-use-and-platform-rules.md",
        "how-generative-ai-works.md",
        "ai-authorship-and-ownership.md",
        "responsible-ai-use-and-verification.md"
    ]
}

total_updated = 0

for subj, files in ordering.items():
    subj_dir = os.path.join(base_dir, subj)
    if not os.path.exists(subj_dir):
        continue
    
    for idx, fname in enumerate(files, start=1):
        weight_val = idx * 10
        fpath = os.path.join(subj_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                text = f.read()
            
            lines = text.splitlines()
            new_lines = []
            has_weight = False
            for l in lines:
                if l.startswith("weight:"):
                    new_lines.append(f"weight: {weight_val}")
                    has_weight = True
                else:
                    new_lines.append(l)
            if not has_weight:
                new_lines.insert(3, f"weight: {weight_val}")
            
            with open(fpath, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines) + "\n")
            total_updated += 1

print(f"Reordered {total_updated} modules from basic to advanced!")