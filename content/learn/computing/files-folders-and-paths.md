---
id: COMP-103
title: "Files, Folders, and Paths"
weight: 30
entity: module
subject: computing
tier: 100
status: complete
tools: []
prereqs: []
standards: ["4.5"]
keywords: ["filepath", "directory", "folder structure", "nesting", "extension", "google drive"]
duration: 10
video: ""
aliases: ["/m/COMP-103"]
---

## What you'll be able to do

- Explain what a file actually is and how a folder differs from one
- Read a file path and know what it's telling you
- Explain what a file extension does and why it matters
- Navigate Google Drive the way you'd navigate a folder tree anywhere else

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### A file is not a document

A **file** is any single item stored on a computer: a document, an image, a video, a saved project. A **folder** (sometimes called a directory) doesn't hold data itself. It holds other files and other folders, and it exists purely to organize things.

That distinction matters more than it sounds like it should. A folder named "Final" with nothing in it is meaningless. A file inside the wrong folder is genuinely lost, even though it still technically exists somewhere.

### Nesting

Folders can go inside folders, as deep as you want. That's called **nesting**, and it's how every real project gets organized: a top-level folder for the class, a folder inside it for each project, maybe a folder inside that for reference images.

Nesting too shallow means one folder holding two hundred loose files with no structure. Nesting too deep means six clicks to reach anything. Somewhere in between is where real projects live, usually two to four levels.

### Paths

A **path** is the full address of a file: every folder you'd click through to reach it, in order, written out as text.

```text
GAD1/01_Projects/Lantern/lantern_v03.blend
```

Read left to right, each slash is one level deeper: the `GAD1` folder contains `01_Projects`, which contains `Lantern`, which contains the actual file. Software shows you a path constantly, in title bars, in save dialogs, in error messages, so being able to read one at a glance saves real time.

### Extensions

The letters after the final dot in a filename are the **extension**, and they tell the computer, and you, what kind of file it is: `.docx` is a Word document, `.png` is an image, `.mp4` is a video, `.blend` is a Blender project.

The extension is not decoration. It's how your computer decides which program should open a file, and changing it does not change what's actually inside the file. Renaming `photo.png` to `photo.docx` does not turn an image into a document; it just makes the computer try to open an image with Word and fail.

Windows hides extensions by default. Turning that display on (**View → File name extensions** in File Explorer) is worth doing, because it's much easier to spot a naming mistake when you can actually see what you typed.

### Google Drive works the same way, underneath

Drive looks different from a traditional file browser, but the same ideas apply. What Drive calls a folder is a folder. What looks like a flat list of files inside it is still a directory, with a path, even if Drive doesn't always show you that path directly.

One real difference: a Google Doc, Sheet, or Slide deck doesn't have a traditional extension the way a downloaded file does, because it lives natively in Google's system rather than as a file with a `.docx` or `.pptx` ending. Export one of those as a Word or PowerPoint file, though, and it immediately gets a real extension, because now it's a standalone file again.

### Why this matters for a shared class folder

Once you're sharing folders with a teacher, a team, or a client, structure stops being a personal preference and becomes something other people depend on. A well-organized project folder means anyone can find what they need without asking. A messy one means everyone, including you in three weeks, wastes time hunting.

## Quick Check

{{< quickcheck question="A student renames poster_design.png to poster_design.docx, hoping it will open in Google Docs as an editable document. What actually happens?" >}}

- **A.** The image converts into an editable Word document automatically
- **B.** The file is still an image; only its name changed, and Docs won't be able to open it as intended
- **C.** The file becomes corrupted and unusable
- **D.** Nothing happens until the file is re-uploaded

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> An extension is a label, not a converter. The actual image data inside the file never changes, so the file is still a <code>.png</code> wearing the wrong name.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **File**
- **Folder**
- **Nesting**
- **Path**
- **Extension**
- **Directory**

## Next

- [Naming Conventions](/learn/computing/naming-conventions/) (`COMP-105`) — version numbers, underscores, and avoiding special characters
- [File System & Naming Conventions Drill](/assignments/file-system-drill/) — organize your Drive workspace and practice professional naming standards
