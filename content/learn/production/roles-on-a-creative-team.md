---
id: PROD-102
title: "Roles on a Creative Team"
weight: 20
entity: module
subject: production
tier: 100
status: draft
tools: []
prereqs: []
standards: ["16.2"]
keywords: ["roles", "team", "discipline", "producer", "art director", "lead", "technical artist", "QA", "pipeline", "handoff", "who decides", "job titles"]
duration: 10
video: ""
aliases: ["/m/PROD-102"]
---

## What you'll be able to do

- Name the main disciplines on a creative production team and what each one owns
- Explain how one person's output becomes another person's starting material
- Describe how team size changes what the roles look like
- Identify who makes the call when a team disagrees

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### The disciplines

Most game and media teams are built from the same handful of disciplines: **design**, **art**, **programming**, **audio**, **production**, and **quality assurance**, with business and marketing alongside them.

What each one owns:

- **Design** decides the rules. Systems, mechanics, progression, level layouts, and what the player experience is supposed to feel like. Designers produce documents and then change them based on what playtesting reveals.
- **Art** decides how it looks. Concept art, characters, environments, texturing, animation, effects, and UI.
- **Programming** makes it run. Gameplay systems, tools for everyone else, and fixing what breaks.
- **Audio** covers music, sound effects, and mixing.
- **Production** keeps it moving. Schedules, dependencies, budgets, and unblocking people.
- **QA** finds what's broken before players do.

### Roles are links in a chain

This is the part people miss. A role is not just a job description. Each discipline's output is the next discipline's raw material.

Designers write a spec. Programmers build to that spec. Artists make assets. Programmers integrate those assets into levels the designers laid out. When one link stalls, everything downstream stalls with it, and the delay compounds rather than staying contained.

That's why "I'll finish my part eventually" is a bigger deal on a team than it is on solo work. Somebody is waiting on you, whether they've said so or not.

Teams that skip QA until late in a project reliably produce the same set of problems: piled-up bugs, pieces that don't fit together, and a schedule that slips. Predictable, because the feedback that would have caught it early never happened.

### Team size changes everything

The same job has a different shape depending on how many people are in the room.

- **Small teams** consolidate. A programmer might also design. An artist might handle sound. Nobody specializes because there aren't enough people to.
- **Mid-sized studios** grow leads. Once a team is a few dozen people, each discipline gets a **lead** (Lead Artist, Design Lead, Lead Programmer) and a producer layer appears to manage the dependencies between them.
- **Large studios** subdivide. A single "animator" at a small studio can become a team of twelve at a big one, split into character animators, technical animators, and riggers.

None of these is more correct. The structure follows the size.

### Two roles worth knowing about

**The lead** sits between the director's vision and the people doing the work. Leads assign the day-to-day tasks, review work in progress, catch technical problems before they reach the director, and mentor the newer people. It's the least glamorous position on most teams and one of the most structurally important.

**The technical artist** sits between art and programming. They're not mainly making content and they're not mainly writing systems. They understand both sides well enough to build the pipelines and handoff processes that let everyone else work. Their absence usually isn't noticed directly; it shows up as everything taking longer than it should.

### Who decides

Every team eventually disagrees about something. Teams that work have already answered the question of who has the final say, before the argument happens.

Sometimes it's a director. Sometimes it's whoever owns that discipline. Sometimes the team votes. What matters is that it was decided in advance, not in the middle of the fight.

## Quick Check

{{< quickcheck question="An environment artist finishes a set of props two days late. The level designer says it's fine because they had other work. The producer disagrees. Who is right?" >}}

- **A.** The level designer, since nobody was actually blocked
- **B.** The producer, because a late handoff pushes everything downstream
- **C.** Neither, deadlines on creative work are always flexible
- **D.** The artist, since quality matters more than speed

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> The level designer only sees their own next two days. The producer sees the chain: props go into levels, levels go to playtest, playtest feedback drives the next round of design. A two-day slip early doesn't stay two days. That's why production exists as its own discipline.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Discipline**
- **Lead**
- **Producer**
- **Technical artist**
- **QA**
- **Handoff**
- **Dependency**
