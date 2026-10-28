---
id: greybox-slice
title: "Greybox the Vertical Slice"
entity: assignment
tier: 200
status: complete
requires: ["UE-206"]
standards: ["GD.18.4", "GD.17.6"]
evidence_for: "GD.18.4"
portfolio: true
portfolio_section: "GAD2 U2"
est_time: 180
setting: studio
aliases: ["/a/greybox-slice"]
---

## The task

Build the full playable layout of your studio's slice in Unreal Engine, in blockout geometry. No final art, no finished materials. By the end of this build, a player should be able to walk from start to finish and understand every space's purpose, scale, and pacing, even though everything is still grey.

This runs two weeks. It's a team build: the level designer leads, but everyone contributes blockout geometry for their designated area of the slice.

**Deliverable**: Completed playable master greybox level + recorded video walkthrough + high-resolution screenshots with a comprehensive design write-up published to your Google Sites portfolio.

---

## Before you start

Read [Level Blockout Workflow](/m/UE-206/) (`UE-206`).

---

## Steps

{{% steps %}}

### Step 1 — Place your scale references

Before placing a single wall, place a player-scale reference in your level: a player capsule or simple character mesh at 180cm tall (the standard human reference) and a door opening at 100cm wide. Leave both in the level the whole time you're building. Every hallway, arena, ceiling, and doorway gets judged directly against these two numbers.

### Step 2 — Block the critical path

Build the route a player has to take to get from the start of the slice to the end. Simple shapes only: cubes for walls and floors, cylinders for pillars, ramps or stairs for elevation changes. Ensure the player can traverse the entire length of the slice without encountering dead ends on the primary route.

### Step 3 — Block out the secondary spaces

Build combat arenas, puzzle chambers, discovery nooks, and optional branching spaces off the critical path, strictly adhering to your team's GDD and scope contract. Keep geometry untextured and unlit so testing remains fast and low-cost.

### Step 4 — Label every space

Drop a 3D Text Actor in every distinct area naming its intended gameplay function in a word or two: `COMBAT`, `PUZZLE`, `SAFE ZONE`, `REWARD`, `HAZARD`. When external playtesters or teammates walk the level, labels ensure everyone instantly understands what the space is designed to ask of the player.

### Step 5 — Walk it, repeatedly

Test the level at actual player speed in first-person or third-person mode — never rely on flying around in the editor viewport. As you walk:
- Note anywhere the scale feels cramped, oversized, or awkward relative to the 180cm reference.
- Check whether the critical path reads clearly or causes unintended confusion.
- Assess whether the pacing feels flat or successfully provides an alternation of tension and rest.

### Step 6 — Fix what you find

Adjust geometry immediately based on what walking it revealed: widen narrow choke points, raise low ceilings, clarify sightlines to guide the player, or reshape an arena to introduce a deliberate lull before a combat beat.

### Step 7 — Playtest with someone outside the build

Have a teammate or classmate who was not involved in building that specific section walk the greybox blind without spoken guidance. Watch where they hesitate, where they look first, and where they get lost. That behavior is neutral diagnostic data, not a personal critique of your layout.

### Step 8 — Finalize and save the level

Complete the level layout and ensure all assets are saved cleanly in the project:
- Organize your Outliner into tidy folders by zone (e.g., `Zone_01_Entry`, `Zone_02_Arena`, `Zone_03_Puzzle`).
- Confirm Player Start, lighting, scale references, and 3D text labels are placed correctly.
- Save the level (`Ctrl + S`) and verify the map reopens and plays cleanly from start to finish without errors.

### Step 9 — Record your video walkthrough

Record a continuous, in-engine video walkthrough of the complete level:
- Use OBS Studio, Windows Game Bar (`Win + G`), or screen recording software.
- Play in First-Person or Third-Person PIE (Play In Editor) mode at normal walking and running speed. **Do not use the flying editor camera.**
- Walk the complete critical path from player spawn to the level exit/slice climax.
- Demonstrate key spatial transitions: hallway choke points, arena scale, elevation changes via ramps/stairs, and puzzle/combat areas.
- Upload the video to YouTube (as Unlisted) or Google Drive (ensure link permissions are set to "Anyone with the link can view").

### Step 10 — Capture screenshots and publish the write-up

Assemble the visual gallery and written documentation for your Google Sites portfolio:
1. **Screenshot Gallery**: Capture at least **4 high-resolution, labeled screenshots** showing:
   - **Spawn & Initial Vista**: The opening view showing the critical path forward.
   - **Primary Gameplay Space**: The main combat arena, puzzle chamber, or encounter room with a 180cm scale reference visible.
   - **Focal Landmark / Navigation Choke Point**: A distinctive structural element or transition that guides player orientation.
   - **Climax / Exit Area**: The finale chamber, extraction zone, or objective threshold.
2. **Written Design Analysis**: Author a clear breakdown explaining:
   - **Layout & Player Guidance**: How your geometry and sightlines communicate where to go without artificial minimaps or arrows.
   - **Metrics & Proportions**: The specific dimensions used for corridors, doors, and ceilings, and how they relate to the 180cm character scale.
   - **Pacing Rhythm**: How the level alternates between high-intensity action zones and moments of breath, discovery, or recovery.
   - **Playtest Iterations**: At least two specific adjustments made to scale, pathing, or sightlines based on walking the level or observing blind playtesters.

{{% /steps %}}

---

## Submit

{{< callout type="info" >}}
**Google Sites Portfolio & Classroom Deliverable**:
Publish your work to your Google Sites portfolio under **Coursework > Unit 2: The Vertical Slice**:
1. **Page Title**: Module 2.3 — Greybox Level Design & Walkthrough
2. **Video Walkthrough**: Embed your recorded gameplay playthrough video showing continuous traversal from spawn to exit.
3. **Screenshot Gallery**: Include at least 4 high-resolution, labeled screenshots showcasing key zones, sightlines, and scale references.
4. **Design Write-Up**: Include your comprehensive written analysis covering layout, player metrics, pacing rhythm, and playtest adjustments.
5. **Classroom Submission**: Submit the published Google Sites page URL to the matching assignment slot in Google Classroom.
{{< /callout >}}

---

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Player-Scale Metrics** | Scale references missing or removed; dimensions feel arbitrarily oversized or cramped compared to player height | 180cm human capsule and 100cm door reference maintained in scene; spaces accurately sized to realistic player metrics | Flawless metric consistency; architectural proportions, door clearances, and combat arenas calibrated precisely to player camera and movement speeds |
| **Critical Path & Navigation** | Navigation is disorienting; critical path is broken, blocked, or indistinguishable from dead ends | Continuous, walkable critical path from slice start to finish with readable sightlines and progression flow | Exemplary level geometry that intuitively guides player line-of-sight and movement without requiring explicit verbal instructions |
| **Functional Labeling & Pacing Rhythm** | Unlabeled rooms; pacing is flat or uniformly intense without shifts in challenge or rest | Every functional space labeled with a 3D text actor (`COMBAT`, `PUZZLE`, `SAFE ZONE`); level includes at least one distinct shift in pacing | Clear spatial taxonomy across all zones; sophisticated rhythm alternating tension build-up, climax, and recovery beats matching the GDD |
| **Blind Playtesting & Iteration** | No recorded outside playtest; issues discovered during editor fly-throughs are left unfixed | Blind walk-through conducted with an outside playtester; player hesitation points documented and addressed with geometric fixes | Rigorous observational playtesting; detailed notes capturing player navigation friction and deliberate geometric revisions that solved core pathing problems |
| **Video Walkthrough Documentation** | Video walkthrough is missing, choppy, or recorded via flying editor camera; path is incomplete or skips major zones | Clear, continuous gameplay video walkthrough recorded in PIE mode at player eye level from spawn to level exit | High-definition, smooth walkthrough video with natural pacing; thoroughly demonstrates scale, navigation flow, and spatial rhythm from the player's perspective |
| **Screenshots & Portfolio Write-Up** | Incomplete portfolio page; fewer than 4 screenshots; write-up is superficial or missing playtest reflection | At least 4 high-resolution labeled screenshots with a thorough design write-up covering layout, metrics, pacing, and playtest adjustments | Professional portfolio presentation featuring beautifully composed, annotated captures and an in-depth spatial analysis reflecting industry-standard level design principles |

---

## Notes

- **Everything here is temporary geometry**: Nothing you build in this assignment is meant to survive into the final slice as-is. That's the point: the blockout exists so the team can test the actual experience before investing finished art time into a layout that might not work.
- **Only one person saves the shared level at a time**: If working on a shared project machine or network drive, coordinate verbally so two teammates do not save over each other's unsaved session.
- **If a space doesn't work, say so now**: Finding out a combat arena is too small while it's still grey boxes costs almost nothing. Finding out after it's been fully art-passed costs real time the team doesn't have.
