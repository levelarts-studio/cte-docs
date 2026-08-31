---
id: lab-setup-and-conventions
title: "Lab Setup and Conventions"
entity: assignment
tier: 200
status: draft
requires: ["BLND-101", "COMP-113"]
standards: ["4.3", "4.5", "6.1", "6.2", "6.8", "16.1"]
evidence_for: "4.5"
portfolio: true
portfolio_section: "Coursework"
est_time: 150
setting: lab
aliases: ["/a/lab-setup-and-conventions"]
---

## The task

Set up your workstation, your folder structure, and your copy of Blender so that everything you make this year has a place to live and a name that makes sense. Then learn how this lab runs.

This is the least exciting lab of the year and the one that saves you the most pain. Students who skip it lose files in March.

## Before you start

- [Interface and Navigation](/m/BLND-101/) — you'll configure preferences here
- [Lab Safety, Equipment, and File Conventions](/m/COMP-113/) — the rules and why they exist

## Steps

{{% steps %}}

### Step 1 — Build your folder structure

In your drive, make this. Exactly this:

```text
GAD1/
  01_Projects/
  02_Reference/
  03_Textures/
  04_Exports/
  05_Renders/
```

The numbers force the order so the folders don't shuffle alphabetically. Every project you start this year goes in `01_Projects` in its own subfolder.

### Step 2 — Learn the naming convention

Every file you save uses this pattern:

`LASTNAME_ProjectName_v01.blend`

- **No spaces**: Use underscores. Spaces break things in ways you won't see until export.
- **Two-digit version numbers**: `v01`, not `v1`, so `v10` doesn't sort before `v2`.
- **Never overwrite a working file**: When you make a real change, save a new version. Disk space is free. Your Tuesday afternoon is not.

### Step 3 — Configure Blender

Open **Edit → Preferences**:

1. **Input**: If you're on a laptop or a mouse without a middle button, turn on **Emulate 3 Button Mouse** and **Emulate Numpad**.
2. **Save & Load**: Confirm **Auto Save Temporary Files** is on and note the timer.
3. **Save Preferences** at the bottom left, or none of this survives a restart.

Then save a first file into `01_Projects` using the naming convention. It can be the default cube. The point is the path and the name.

### Step 4 — Walk the lab

With your teacher, locate and note:

- The nearest exit and the evacuation route from this room
- The fire extinguisher
- Where peripherals and cables are stored, and how they get returned
- How to report broken or missing equipment
- The rule on food and drink at the stations, and why it exists

### Step 5 — Write it up

Post to your portfolio's **Coursework** page using the standard write-up format, plus:

- A screenshot of your folder structure
- A screenshot of your Blender window with your first saved file open, filename visible
- In your own words, the lab's file naming convention and why version numbers matter
- In your own words, three lab rules and the reason behind each

> *Copying the rules off this page word for word does not count. Explaining why "no spaces in filenames" exists shows you understood it.*

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the link to your portfolio in Google Classroom.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Folder structure** | Missing or renamed folders | Structure built exactly as specified | Project subfolder already started and organized |
| **Naming convention** | File saved with spaces, no version, or wrong pattern | File named `LASTNAME_Project_v01.blend` and saved in the right folder | Explains why the convention prevents specific problems |
| **Blender configured** | Preferences not saved, or not set for the hardware | Input and autosave set correctly, preferences saved | Notes an additional setting changed and why |
| **Lab knowledge** | Rules copied from the page | Three rules in own words with reasons | Connects a rule to a real consequence in a production environment |
| **Write-up** | Screenshots missing or unreadable | Both screenshots present, write-up format followed | Screenshots cropped and legible, presented cleanly |

## Notes

- **Every project this year assumes this structure**: Later assignments will say *"save to 04_Exports"* without explaining it again.
- **The naming convention is not busywork**: It's **4.5 Document & Asset Management**, and it is the first thing a studio checks when they look at a junior artist's files. In GAD2 your whole team will be sharing assets, and a file called `final_final_2.blend` will cost somebody an afternoon.
