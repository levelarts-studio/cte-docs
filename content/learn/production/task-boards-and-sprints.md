---
id: PROD-203
title: "Task Boards and Sprints"
weight: 60
entity: module
subject: production
tier: 200
status: complete
tools: ["google-sheets"]
prereqs: ["PROD-204"]
standards: ["16.7", "2.8"]
keywords: ["task", "sprint", "estimate", "status", "google sheets", "task list", "kanban"]
duration: 10
video: ""
aliases: ["/m/PROD-203"]
---

## What you'll be able to do

- Write a task so someone else could pick it up without asking questions
- Estimate how long a task will actually take
- Understand what a sprint is and why work gets organized into them
- Read a task list as a temperature check on how a project is actually going

<div class="hx:p-4 hx:my-4 hx:rounded-lg hx:bg-slate-900 hx:border hx:border-slate-800 hx:text-slate-400 hx:text-sm">
  🎥 <em>Video lesson embedding point (captions & transcript available).</em>
</div>

## Read

### Why write tasks down at all

If it's not written down, it isn't happening, as far as anyone else on the team can tell. Work you're quietly doing in your head doesn't help your teammates plan, and it doesn't help you either, three weeks from now, when you're trying to remember what you'd already figured out.

A task list's whole value is that anyone, including you, can look at it and know the true state of things without having to ask.

### Writing a useful task

A task like "fix the level" tells nobody anything. A useful task has:

- **A specific, actionable description.** Not "fix the level," but "fix collision on the north bridge so the player doesn't fall through."
- **Who it's assigned to.**
- **What "done" looks like.** One line describing the finished state, so there's no ambiguity about whether it's actually complete.
- **Status.** Not started, in progress, or done.

The test: could someone who wasn't there when it was written pick it up and know exactly what to do?

### Estimating

Nobody estimates perfectly, and that's fine. What matters is estimating consistently enough to plan around. A useful habit: if a task feels bigger than something you could finish in one sitting, break it into smaller pieces. "Build the level" isn't an estimate. "Greybox the first room" is something you can actually put a number on.

When something takes longer than you thought, that's information for next time, not a failure this time.

### Sprints

A sprint is a fixed block of time, commonly one to two weeks, where you commit to a specific, limited set of tasks and focus on finishing those before adding anything new. At the end, you check what actually got done against what you planned.

The discipline isn't really the time limit. It's naming a small, specific set of work and protecting it from new additions mid-sprint. New ideas don't disappear, they go on the list for later instead of derailing what you already committed to.

### Reading your own list as a signal

A list where almost everything sits at "not started" and nothing moves to "done" is telling you something real: you're planning faster than you're finishing. That's worth noticing on your own list before it becomes a surprise at a review.

## Quick Check

{{< quickcheck question="A task reads: \"Make the level better.\" What's the main problem, and how would you fix it?" >}}

- **A.** It's not assigned to anyone, that's the only issue
- **B.** It isn't specific enough to know what "done" looks like or for someone else to pick it up
- **C.** Nothing is wrong, general tasks give room for creativity
- **D.** It should already be marked done since level work is ongoing

<details style="margin-top: 1rem; padding: 0.75rem 1rem; border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 0.375rem; background: rgba(0, 0, 0, 0.2);">
  <summary style="cursor: pointer; font-weight: 600; color: #818cf8;">Show answer</summary>
  <div style="margin-top: 0.6rem; opacity: 0.95;">
    <strong>B.</strong> A vague task can't be estimated and can't be confirmed finished. The fix is a specific description and a one-line definition of what "done" means.
  </div>
</details>

{{< /quickcheck >}}

## Terms

- **Task**
- **Sprint**
- **Estimate**
- **Status**

## Next

- [Production Schedule & Task List](/assignments/schedule-and-taskboard/) — build your personal production task list and workload reflection
- [Version Control for Teams](/m/PROD-202/) — configure Git LFS and multi-developer branching
