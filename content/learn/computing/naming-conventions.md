---
id: COMP-105
title: "Naming Conventions"
weight: 50
entity: module
subject: computing
tier: 100
status: complete
tools: []
prereqs: []
standards: ["4.5"]
keywords: ["naming conventions", "versioning", "file naming", "underscores", "overwriting", "file hygiene"]
duration: 10
video: ""
aliases: ["/m/COMP-105"]
---

## What you'll be able to do

- Write a filename that stays sortable and clear as a project grows
- Use version numbers correctly
- Avoid the characters and habits that cause files to break or misbehave
- Apply one consistent naming pattern across a whole project

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Why this is worth ten minutes

"Untitled document (3).docx" tells you nothing. Six months from now, in a folder with forty other files, it will tell you even less. A naming convention is a small, boring habit that pays for itself the first time you need to find something fast, or the first time you're handing files to someone else.

### The pattern

A dependable filename has three parts, in order:

```text
NAME_ProjectDescription_v01.ext
```

- **Name or initials** identify who made it, useful the moment more than one person touches a shared folder.
- **Project description** is short and specific. `poster` tells you less than `poster_recycling-campaign`.
- **Version number**, always two digits: `v01`, `v02`, not `v1`, `v2`. Two digits keep files sorted correctly once you pass nine versions, since `v10` sorts before `v2` in plain alphabetical order but after `v09` in a two-digit system.

### Spaces are the enemy

Never use spaces in a filename you plan to share, upload, or use in any software.

Spaces get silently converted to `%20` the moment a file's name becomes part of a web address, which is exactly what happens when Drive generates a shareable link. That can break the link entirely, or make it work sometimes and fail other times depending on what's reading it. Use an **underscore** (`_`) or a **hyphen** (`-`) instead. Both work everywhere spaces don't.

### Versioning, not overwriting

The temptation is to keep one file and just keep saving over it. Don't. **Save a new version every time you make a real change**, not every keystroke, but every meaningful step: after a first draft, after a big revision, before you try something risky.

This costs almost nothing. Storage is cheap. What it buys you: if version 4 turns out worse than version 3, you can go back. If a file gets corrupted, you have a backup two steps behind it. Overwriting a working file is the single most common way students lose their own work.

### Characters to avoid

Some characters cause real problems depending on the system a file ends up in:

`/ \ : * ? " < > |`

Several of those are illegal in Windows filenames outright and will be blocked automatically. Others work fine locally but break the moment a file crosses into a URL, a command line, or a different operating system. Sticking to letters, numbers, underscores, and hyphens means never having to think about it.

### One convention, used everywhere

The actual value isn't in any single filename. It's in **applying the same pattern across an entire project**, so that a folder full of files sorts logically without you doing anything extra, and so that anyone who understands the convention can find the newest version of anything at a glance.

## Quick Check

{{< quickcheck question="Two students are collaborating and one shares a file called Final Poster Design copy (2).png. What is the biggest problem with this filename?" >}}

- **A.** It's too long
- **B.** Spaces and vague versioning make it unclear which file is current and it may break when shared as a link
- **C.** PNG is the wrong file format for a poster
- **D.** Nothing, this is a normal filename

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> Spaces risk breaking as a shared link, and &ldquo;Final... copy (2)&rdquo; gives no real indication of what changed or whether a newer version exists. A clear version number would fix both problems at once.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Naming convention**
- **Version number**
- **Underscore**
- **Overwriting**

## Next

- [File System & Naming Conventions Drill](/assignments/file-system-drill/) — organize your Drive workspace and practice professional naming standards
- [Reading a Spec Sheet](/learn/computing/reading-a-spec-sheet/) (`COMP-108`) — identify CPU, GPU, VRAM, and RAM specs
