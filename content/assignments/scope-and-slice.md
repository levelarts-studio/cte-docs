---
id: scope-and-slice
title: "Scope & Vertical Slice Definition"
entity: assignment
tier: 200
status: complete
requires: ["PROD-204"]
standards: ["16.9", "GD.18.3", "5.8"]
evidence_for: "16.9"
portfolio: true
portfolio_section: "GAD2 U1"
est_time: 90
setting: studio
aliases: ["/a/scope-and-slice"]
---

## The task

As a studio, lock the scope of the slice you're building this year. Sort every feature from your greenlit pitch and your early GDD draft into **Must**, **Should**, **Could**, or **Won't**, and produce one scope contract document the whole team signs and holds itself to.

This is the document you will point back to in March when someone wants to add one more mechanic.

**Deliverable**: Team-signed Vertical Slice Scope Contract (shared doc) + individual portfolio reflection entry.

## Before you start

Read [Scope and the Vertical Slice](/learn/production/scope-and-the-vertical-slice/) (`PROD-204`).

---

## Steps

{{% steps %}}

### Step 1 — List every feature anyone has proposed

Pull every mechanic, asset, system, and level requirement from your greenlit pitch, your GDD draft, and any group brainstorming sessions. Get them all written into a single shared raw list before sorting anything.

> [!NOTE]
> **Do not pre-filter at this stage.** Even unrealistic or ambitious ideas belong on the initial raw list so they can be formally evaluated and officially classified into the contract.

### Step 2 — Sort into MoSCoW, as a group

As a team, review every item and assign it to one of the four MoSCoW buckets:

- **Must have:** If even one of these features is missing, the vertical slice fails to demonstrate the core game loop.
- **Should have:** Genuinely valuable and planned for inclusion, but the core slice remains playable without it.
- **Could have:** Low-cost polish items and stretch goals. The first items cut when deadlines tighten.
- **Won't have:** Explicitly cut or deferred for this vertical slice.

If team members disagree on whether an item is a *Must* or a *Should*, talk it out. That debate is valuable: it exposes differing assumptions about the core loop before production begins.

### Step 3 — Stress-test the Must-have list

Once sorted, read your **Must-have** list out loud as a single continuous sentence describing what a player experiences in the slice:

> *"The player controls [Character] in [Location], uses [Core Mechanic] to solve/defeat [Primary Challenge], and completes the slice at [End Trigger]."*

Ask honestly: **Is this genuinely buildable by this team in our available lab hours before deadline?** If you are unsure, move the least critical item from *Must* down to *Should*. A lean Must-have list now is what makes spring milestones achievable.

### Step 4 — Write the Won't-have list clearly

The **Won't-have** section is the most important part of your contract. Do not treat it as a graveyard of discarded bullet points. Write each cut feature as a clear sentence explaining *why* it is omitted:

- *Example:* `"Multiplayer / Co-op — Out of scope for a 5-minute single-player vertical slice; revisit only in post-slice full production."`
- *Example:* `"Branching Narrative Dialogue Trees — Requires custom UI and narrative scripting beyond current timeline; slice will feature direct environmental objectives instead."`

### Step 5 — Define the slice boundary

Write a single, tightly scoped paragraph defining the start, middle, and end conditions of the slice:
- **Where does the player start?** (e.g., waking up in the broken maintenance bay).
- **What is the central objective?** (e.g., restore power to the primary airlock).
- **Where does the slice end?** (e.g., stepping through the airlock as the station alarms trigger).

This boundary paragraph is the studio's concrete definition of "Done" for the year.

### Step 6 — Build the scope contract document

Format your studio's scope contract into a clean document (Google Doc or Notion page) containing:
1. **Title & Game Hook:** Game title, logline, and studio team name.
2. **Slice Boundary Paragraph:** The narrative and gameplay start/end conditions.
3. **MoSCoW Feature Tables:**
   - Must-have features
   - Should-have features
   - Could-have features
   - Won't-have features (with rationale for each)
4. **Team Signatures:** Date and typed/signed names of every studio member committing to this scope.

### Step 7 — Post it where the team works

Link the signed scope contract at the top of your team's GDD and pin it to your Kanban task board (Trello/GitHub Projects). Whenever a new idea or mechanic is proposed during sprints, check the contract first.

{{% /steps %}}

---

## Submit

{{< callout type="info" >}}
**Google Classroom & Portfolio Submission**:
1. **Team Link**: One team member posts the direct link to the published **Scope Contract** document in Google Classroom.
2. **Individual Reflection**: Each student posts a short reflection entry to their Google Sites portfolio **Coursework** page under the `GAD2 U1` section:
   - **One feature you argued to keep in Must-have**, and your reasoning.
   - **One feature you agreed to move to Won't-have**, and how cutting it protects the team's schedule.
{{< /callout >}}

---

## Rubric

### Assessment Rubric

| Criteria | Proficient (4-5 pts) | Developing (2-3 pts) | Beginning (0-1 pt) |
|---|---|---|---|
| **MoSCoW Prioritization Rigor** | Clean, realistic separation of Must, Should, Could, and Won't; Must-have list is tightly scoped to a 5–10 minute playable core loop achievable within lab constraints. | Must-have list is slightly bloated or contains features that should be classified as Should/Could. | Features are arbitrarily listed without clear criteria; unrealistic scope for available time. |
| **Won't-Have Rationale** | All deferred/cut features are explicitly documented with professional rationale explaining why they are out of scope for this slice. | Won't-have section is present but lacks clear justification or consists of one-word bullet points. | Missing Won't-have section or features quietly discarded without team consensus. |
| **Slice Boundary Definition** | Slice start, middle gameplay loop, and end trigger are unambiguously defined in a clear narrative/gameplay boundary paragraph. | Slice boundary is somewhat vague (e.g., clear start but ambiguous victory/completion state). | Missing boundary paragraph; no clear definition of what "done" means for the slice. |
| **Contract Alignment & Sign-off** | Document is fully signed by all studio members, dated, linked from the team task board/GDD, and formatted cleanly. | Document is missing 1 or 2 signatures or is not linked in team workspace. | Incomplete document or unshared draft. |
| **Individual Reflection** | Portfolio entry demonstrates critical thinking, clearly explaining one defended Must-have and one embraced Won't-have trade-off. | Reflection is brief or only discusses one feature without clear rationale. | Missing portfolio reflection entry. |

---

## Notes

- **This document is a contract with your future selves, not with me.** Its entire value is in what it stops the team from doing in February: relitigating a decision that was already made in September.
- **Revisit it, don't rewrite it.** At each milestone review, check whether the build still matches the scope contract. If something has genuinely changed, update it deliberately as a group, the same way you did here. Don't let it drift quietly.
- **Won't have is not permanent for the studio, only for this slice.** An idea in Won't have this year might be exactly the right pitch for someone's next project. Cutting it now doesn't waste it; it ensures the project ships.
