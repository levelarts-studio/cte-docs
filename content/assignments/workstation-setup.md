---
id: workstation-setup
title: "Workstation Setup & Ergonomics"
entity: assignment
tier: 100
status: complete
requires: ["COMP-110", "COMP-101"]
standards: ["4.3", "4.4", "6.1", "6.3"]
evidence_for: "4.3"
portfolio: true
portfolio_section: "Digital Foundations"
est_time: 90
setting: lab
aliases: ["/a/workstation-setup"]
---

## The task

Two parts. First, take an honest look at your current workstation setup and hardware access. Second, design a custom creative PC on PCPartPicker that will actually do the job you want it to do on a realistic budget, justify every major component choice, and plan an ergonomic workstation environment around it.

You are not buying anything. You are learning to read hardware specifications, connect them to real creative workloads, and design a sustainable workstation that protects your body during long studio sessions. This skill will save you thousands of dollars—and protect your health—for the rest of your creative life.

## Before you start

- [Ergonomics and the Workstation](/learn/computing/ergonomics-and-the-workstation/) (`COMP-110`) — neutral posture, viewing distance, and healthy habits
- [What a Computer Is Doing](/learn/computing/what-a-computer-is-doing/) (`COMP-101`) — CPU, RAM, GPU/VRAM, storage pipeline, and hardware bottlenecks

## Steps

{{% steps %}}

### Step 1 — Audit what you actually have

In a few honest sentences (no judgment attached):

1. **Hardware access**: Do you have a computer at home? Desktop, laptop, shared family computer, tablet, or school Chromebook only?
2. **Current specs**: If you know any specs (processor, RAM, storage, graphics card), list them. If you don't know, that is fine—say so.
3. **Current use**: What do you currently use it for? (Schoolwork, gaming, video editing, web browsing?)
4. **Current ergonomic setup**: Where do you actually sit and work? (A desk, kitchen table, bed, couch?) How is your posture, screen height, and viewing distance?

> *If you have nothing at home, write that. It matters for the next part, not as a problem to solve here, but because it changes what "worth building" means for you.*

### Step 2 — Pick your job

Choose the creative industry focus driving this workstation build. It must be something covered in this pathway, or an adjacent creative field you are genuinely curious about:

- **3D Art & Game Development** (Blender, Unreal Engine 5)
- **Video Editing & Post-Production** (Premiere, DaVinci Resolve, After Effects)
- **Graphic Design & Digital Illustration** (Photoshop, Illustrator, Krita)
- **Music & Audio Production** (DAWs, recording, virtual instruments)
- **General Creative Multitasking** (Undecided / hybrid creative production)

Your whole build gets justified against this focus. A video editing rig and a Blender/Unreal rig require very different hardware priorities.

### Step 3 — Set a real budget

Pick a budget between **$800 and $2,000**. State your target number and explain why in a sentence.

> *"This is roughly what a family might actually spend on a first serious workstation"* or *"This represents saving money from a summer job"* are both great justifications.

### Step 4 — Build it on PCPartPicker

Go to [pcpartpicker.com](https://pcpartpicker.com) → **System Builder**. Build your system in this order to minimize compatibility headaches:

1. **CPU**: Pick this first, since socket type determines compatible motherboards.
2. **Motherboard**: The tool will filter to CPU-compatible options.
3. **RAM (Memory)**: Must match what the motherboard and CPU support (e.g., DDR4 vs DDR5).
4. **GPU (Video Card)**: Sized for your creative workload.
5. **Storage**: High-speed NVMe SSD for OS/apps, optional bulk drive.
6. **Case**: Ensure it fits your motherboard form factor and GPU length.
7. **Power Supply (PSU)**: Sufficient wattage with 20–30% overhead.
8. **Operating System**: Windows or Linux.

As you add parts, PCPartPicker automatically checks physical and electrical compatibility. **Pay attention to every warning.** A red warning means parts will physically or electrically fail together, not a mild suggestion.

> *You don't need an account to build a list, but creating a free account lets you save your list link for easy portfolio posting.*

### Step 5 — Hit your numbers

Cross-reference your build against your chosen job from Step 2:

| If your job is... | Prioritize | Guidelines |
| :--- | :--- | :--- |
| **Blender / Unreal (3D & Game Art)** | GPU & VRAM, then RAM | Blender is usable on 8GB RAM and 2GB VRAM but gets limiting fast; 16GB RAM is a realistic floor. Unreal Engine 5 wants more: Epic recommends 32GB RAM and 8GB+ VRAM for development. |
| **Video Editing** | Fast Storage & RAM | High-speed NVMe SSD and 32GB+ RAM for scrubbed timelines; strong GPU for effects and accelerated render exports. |
| **Graphic Design / Illustration** | CPU & RAM | Single-core CPU speed and 16–32GB RAM matter far more than high-end GPU; a mid-range GPU is plenty. |
| **Music & Audio Production** | CPU Cores & RAM | Multi-core CPU for processing audio tracks and plugins; 32GB RAM and fast NVMe storage for large sample libraries. |
| **Undecided / Creative Hybrid** | Balanced RAM & GPU | 16–32GB RAM and a solid mid-tier GPU (6–8GB VRAM); avoid extremes in either direction. |

If your total is over budget, cut something and explain the trade-off. If you are well under budget, decide whether to upgrade a bottleneck component or reserve budget for ergonomic workstation peripherals.

### Step 6 — Write your component justification

For each of the four core components (**CPU, GPU, RAM, Storage**), write 1 to 3 sentences covering:

- What it does in the machine
- Why you picked this specific model for your job and budget
- What you would upgrade first if you were given an additional $200

> *This is the core of the assignment. The parts list proves you can use the tool; the written justification proves you understand what you built.*

### Step 7 — Plan your ergonomic workstation setup

A powerful PC tower sitting on the floor does you no good if you are hunched over a coffee table with wrist pain. Connect your hardware build to an ergonomic workstation plan:

1. **Monitor & viewing setup**: What monitor size, stand, or arm will you use to maintain a 20-to-40 inch viewing distance with the top of the screen at or slightly below eye level?
2. **Keyboard & mouse placement**: How will you position your keyboard and mouse so wrists stay straight and elbows remain bent between 90 and 120 degrees?
3. **Seating & posture**: What chair or support (including improvised lumbar cushions or footrests) will you use to support neutral posture with feet flat and thighs parallel to the floor?
4. **Break routine**: What is your specific plan for the **20-20-20 rule** (eyes) and taking micro-breaks to stand and stretch every 20 to 30 minutes?

### Step 8 — Reality check

Write one honest paragraph:

Is this build realistic for you or your family right now? Would you actually buy or build it? Is there a smarter or cheaper alternative that gets you 80% of the performance—such as buying a refurbished workstation, shopping the used GPU market, or upgrading a single part (like adding RAM or an SSD) in a computer you already own?

> *There is no wrong answer here. A $2,000 dream build you never purchase still teaches critical systems thinking. Acknowledging realistic alternatives proves mature engineering judgment.*

### Step 9 — Post to your portfolio

On your portfolio's **Coursework** page, publish a new post using the standard format:

```text
Workstation Setup & Dream PC Build — Intro to Media Careers · Unit 1 · [Date]

What this is: An audit of my current digital setup, a custom PC build designed for [creative focus] on PCPartPicker, and an ergonomic workstation plan.
Tools used: PCPartPicker, Google Sites.
What I'd do differently: [One honest sentence about a hardware trade-off or budget choice].
```

Include all of the following in your post:
- **Current setup audit** (Step 1)
- **Career focus, budget, and rationale** (Steps 2–3)
- **PCPartPicker link** (or screenshot of the complete parts list with prices)
- **Component justification breakdown** (Step 6)
- **Ergonomic workstation plan** (Step 7)
- **Reality check paragraph** (Step 8)

{{% /steps %}}

## Submit

{{< callout type="info" >}}
**Google Classroom Submission**: Post the link to your published Google Sites portfolio Coursework page in Google Classroom.
{{< /callout >}}

## Rubric

| Criteria | Approaching | Proficient | Advanced |
| :--- | :--- | :--- | :--- |
| **Current Setup Audit** | Minimal or vague description of current hardware and setup | Clear, honest summary of current machine access, specs (or lack thereof), usage, and physical setup | Detailed reflection on how current access shapes creative goals and hardware needs |
| **PCPartPicker Build & Compatibility** | Parts list incomplete, over budget without explanation, or has compatibility errors | Fully compatible build within stated $800–$2,000 budget; zero red compatibility errors; saved list link or clean screenshot provided | Highly optimized parts list with excellent price-to-performance choices tailored to chosen field |
| **Component Justification** | Explanations missing for core parts, or copied specs without explanation | Thoughtful 1–3 sentence rationale for CPU, GPU, RAM, and Storage explaining choices relative to creative job and budget | Insightful technical justifications demonstrating clear understanding of bottlenecks, pipelines, and upgrade paths |
| **Ergonomic Workstation Plan** | Ergonomics omitted or limited to generic advice | Concrete plan addressing monitor viewing distance (20–40"), screen height, wrist/elbow alignment, neutral seating, and 20-20-20 breaks | Comprehensive workstation design integrating physical environment, posture adjustments, and proactive health habits |
| **Reality Check & Presentation** | Missing reality check; unformatted post or broken links | Honest, grounded reality check paragraph evaluating refurbished/upgrade alternatives; standard coursework write-up followed cleanly | Deep, mature analysis of cost vs performance; impeccably formatted portfolio post |

## Notes

- **This is not a gaming PC assignment**: A build optimized for playing games and a build optimized for creating 3D assets or editing video are not the same thing. Gaming prioritizes GPU frame rates at 1080p/1440p; creative production prioritizes VRAM capacity, system RAM, multi-core processing, and sustained NVMe read/write speeds.
- **PCPartPicker's compatibility checker does real work**: If it flags that a case won't fit a triple-fan GPU or a power supply lacks sufficient wattage, that is not a nitpick—it is the physical reality of the build.
- **Used and refurbished are legitimate answers**: If your reality check lands on *"I would buy an off-lease refurbished workstation and add a used GPU,"* that is a more sophisticated and practical answer than maxing out an unrealistic wishlist.
- **A fast PC at a bad desk still hurts**: A $2,000 tower on the floor connected to a screen 8 inches from your face on a kitchen chair will still cause repetitive strain and back injuries. A professional workstation accounts for the human being using it.
