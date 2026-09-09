---
id: COMP-101
title: "What a Computer Is Doing"
weight: 10
entity: module
subject: computing
tier: 100
status: complete
tools: []
prereqs: []
standards: ["4.4"]
keywords: ["hardware", "cpu", "core", "ram", "volatile memory", "gpu", "vram", "storage", "ssd", "nvme", "pipeline", "bottleneck"]
duration: 10
video: ""
aliases: ["/m/COMP-101"]
---

## What you'll be able to do

- Explain what the CPU, RAM, GPU, and storage each do
- Trace how a file gets from a drive to your screen
- Say why 3D work is harder on a computer than most tasks
- Read a spec and know which number matters for what

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Four parts, four jobs

Almost everything a computer does comes down to four components passing work between them:

- **CPU (processor)**. The general-purpose worker. It executes instructions very fast, one sequence at a time per core, and a modern CPU has several cores so it can run several sequences at once. Good at complicated logic where each step depends on the last.
- **RAM (memory)**. The desk you work on. Anything open right now lives here because it is enormously faster than a drive. It is also volatile: cut the power and it is gone, which is why unsaved work disappears in a crash.
- **GPU (graphics card)**. Thousands of much simpler cores working at the same time. Terrible at complicated logic, extraordinary at doing the same small calculation to millions of things at once, which is exactly what rendering pixels and transforming vertices is. It has its own separate memory called **VRAM**.
- **Storage (SSD or hard drive)**. The filing cabinet. Slower than RAM, but it keeps its contents with the power off. An SSD has no moving parts and is many times faster than a spinning hard drive; NVMe drives are faster again.

### The pipeline

Open a file and this happens:

1. Storage hands the file to RAM
2. The CPU reads it and works out what needs to happen
3. Anything visual gets handed to the GPU, along with textures and models loaded into VRAM
4. The GPU draws the frame and sends it to your display
5. Repeat, ideally 60 times a second

Every stage can be the bottleneck, and the slowest one decides your experience. A powerful GPU with too little RAM still stutters, because the pipeline stalls before the GPU is ever asked to do anything.

### What happens when something runs out

- **RAM full.** The system starts using storage as overflow, which is thousands of times slower. Everything crawls. This is the most common cause of "my computer got really slow."
- **VRAM full.** The GPU starts pulling data across from system RAM mid-frame. Load a scene needing more VRAM than the card has and you get heavy stuttering, and in Unreal it can crash the editor outright and lose unsaved work.
- **Storage slow.** Loading takes forever. Unreal is unusually sensitive here because it streams textures and assets constantly rather than loading everything once, which is why an SSD is treated as a requirement rather than an upgrade.

### What this means for your work

The software you are about to use sits at the demanding end.

Blender is remarkably light to start: it will run on a 4-core CPU, 8GB of RAM, and a GPU with 2GB of VRAM. But 2GB becomes limiting quickly once models get dense, and 16GB of RAM is a more realistic starting point.

Unreal Engine 5 is a different story. Epic recommends 32GB of RAM and a GPU with 8GB or more of VRAM for development. Eight gigs of system RAM will technically open the editor and then force it to swap to disk constantly.

That gap is why Blender goes home with you and Unreal stays in the lab.

### Reading a spec sheet

Match the number to the job:

| If you are... | The number that matters |
| :--- | :--- |
| **Opening big scenes** | System RAM |
| **Rendering, real-time viewport** | GPU and VRAM |
| **Simulations, some rendering** | CPU cores |
| **Loading levels, streaming assets** | SSD, ideally NVMe |

Spec for your heaviest task, not your average one.

## Quick Check

{{< quickcheck question="A classmate's machine has a strong GPU with 12GB VRAM but only 8GB of system RAM. They open a large Unreal project and everything crawls. Why?" >}}

- **A.** The GPU is not powerful enough for Unreal
- **B.** System RAM filled up and the machine started using storage as overflow
- **C.** VRAM and system RAM are the same thing, so both are full
- **D.** The CPU is doing the rendering instead of the GPU

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> The pipeline stalls before the GPU is involved. When RAM runs out, the system falls back to storage, which is thousands of times slower. <em>C</em> is wrong because VRAM and system RAM are separate.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **CPU**
- **Core**
- **RAM**
- **Volatile memory**
- **GPU**
- **VRAM**
- **SSD / NVMe**
- **Pipeline**
- **Bottleneck**

## Next

- [Workstation Setup & Ergonomics](/assignments/workstation-setup/) — complete the ergonomic lab and hardware verification
- [Files, Folders, and Paths](/learn/computing/files-folders-and-paths/) (`COMP-103`) — learn directory trees, absolute paths, and extensions
