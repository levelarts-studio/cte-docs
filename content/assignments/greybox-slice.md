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

Build the full playable layout of your studio's slice in Unreal, in blockout geometry. No final art, no finished materials. By the end of this, a player should be able to walk from start to finish and understand every space's purpose, even though everything is still grey.

This runs two weeks. It's a team build: the level designer leads, but everyone contributes blockout geometry for their area of the slice.

**Deliverable**: Completed master greybox level (committed in Git repository or saved to shared project) + team playthrough documentation and individual portfolio reflection entries.

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

### Step 8 — Save and share it

Save the completed greybox level into the shared project repository. If working in the same project file or Git repo:
- Coordinate verbally who is actively in the Unreal editor and saving at any given time to avoid silent file overwrites.
- Confirm with your team before beginning and after completing your editing session.
- Push or commit your level changes cleanly.

### Step 9 — Write it up and document

Assemble the team and individual documentation:
- **Producer**: Record and post a playthrough video or a set of annotated screenshots tracing the critical path, accompanied by the team's notes and findings from the outside playtest, to your team's shared documentation.
- **Individual Studio Members**: Post to your personal Google Sites portfolio **Coursework** page under the `GAD2 U2` section documenting:
  1. Which specific area or encounter in the level you blocked out.
  2. One concrete change you made to scale, pathing, or pacing after walking it yourself.

{{% /steps %}}

---

## Submit

{{< callout type="info" >}}
**Google Classroom & Portfolio Submission**:
1. **Producer Submission**: The producer submits the master level file location (or Git repository commit hash) and a video playthrough link or annotated screenshots once in Google Classroom on behalf of the studio.
2. **Individual Portfolio Entry**: Each studio member publishes a post on their Google Sites portfolio **Coursework** page under the `GAD2 U2` section with:
   - Screenshot(s) of the section of the greybox level they built.
   - Written statement identifying the section built and detailing one specific design change made after in-game walk-through testing.
{{< /callout >}}

---

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Player-Scale Metrics** | Scale references missing or removed; dimensions feel arbitrarily oversized or cramped compared to player height | 180cm human capsule and 100cm door reference maintained in scene; spaces accurately sized to realistic player metrics | Flawless metric consistency; architectural proportions, door clearances, and combat arenas calibrated precisely to player camera and movement speeds |
| **Critical Path & Navigation** | Navigation is disorienting; critical path is broken, blocked, or indistinguishable from dead ends | Continuous, walkable critical path from slice start to finish with readable sightlines and progression flow | Exemplary level geometry that intuitively guides player line-of-sight and movement without requiring explicit verbal instructions |
| **Functional Labeling & Pacing Rhythm** | Unlabeled rooms; pacing is flat or uniformly intense without shifts in challenge or rest | Every functional space labeled with a 3D text actor (`COMBAT`, `PUZZLE`, `SAFE ZONE`); level includes at least one distinct shift in pacing | Clear spatial taxonomy across all zones; sophisticated rhythm alternating tension build-up, climax, and recovery beats matching the GDD |
| **Blind Playtesting & Iteration** | No recorded outside playtest; issues discovered during editor fly-throughs are left unfixed | Blind walk-through conducted with an outside playtester; player hesitation points documented and addressed with geometric fixes | Rigorous observational playtesting; detailed notes capturing player navigation friction and deliberate geometric revisions that solved core pathing problems |
| **Version Control & Team Coordination** | File save conflicts or uncoordinated overwrites; missing level asset in shared project | Coordinated check-ins and saves; completed master greybox level cleanly committed to Git or saved in the team project | Professional asset and level pipeline management; zero merge/save collisions, clear commit messaging, and seamless team integration |
| **Portfolio & Process Documentation** | Incomplete Coursework write-up; missing personal contribution details or walkthrough adjustment | Complete Coursework post detailing assigned section and one specific geometric change made after personal playtesting | Professional portfolio entry featuring high-resolution annotated captures, insightful before-and-after spatial analysis, and producer playthrough documentation |

---

## Notes

- **Everything here is temporary geometry**: Nothing you build in this assignment is meant to survive into the final slice as-is. That's the point: the blockout exists so the team can test the actual experience before investing finished art time into a layout that might not work.
- **Only one person saves the shared level at a time**: Without a locking system in place, two people saving the same level file close together can silently overwrite each other's work. Coordinate verbally, and don't save over someone else's unsaved session.
- **If a space doesn't work, say so now**: Finding out a combat arena is too small while it's still grey boxes costs almost nothing. Finding out after it's been fully art-passed costs real time the team doesn't have.
