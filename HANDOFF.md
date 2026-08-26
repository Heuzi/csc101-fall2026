# CSC 101 Fall 2026 Handoff

Status date: 2026-08-25

## Current State

- Repo is on `main` and was clean when this handoff was created.
- Course repo has moved from numbered class files to topic-named class files, such as `class_welcome_setup.md`, `class_vibe_coding.md`, and `class_agentic_ai_danger.md`.
- README schedule is present and mostly populated for the Fall 2026 Wednesday course arc.
- Strongest current materials: `class_vibe_coding.md`, `class_agentic_ai_danger.md`, and `challenge_ai_trading.md`.
- Stubbier materials that need another pass: `class_graph_algorithms.md` and the late-semester Impostor/AI reflection items in `readme.md`.

## Completed Before

- [x] Updated the Typing.com classroom join link/code in the welcome/setup material.
- [x] Added `Class #` to the README schedule table.
- [x] Moved the main Advent of Cyber link into `## Additional Learning` in `readme.md`.
- [x] Replaced the old Fall 2025 portfolio repo link with `https://github.com/Heuzi/csc101-portfolio-fall2026`.
- [x] Renamed class files away from `class01.md` style names into topic-based names.
- [x] Built out the Vibe Coding chess activity.
- [x] Built out the Agentic AI danger lesson.
- [x] Built out the AI Trading Agent Simulation challenge.

## Immediate Cleanup Tasks

- [ ] Keep syllabus updates synchronized with course-content and README schedule updates.
  - Edit `syllabus/csc101A_syllabus_fall2026.tex` when `readme.md` schedule/content changes.
  - Regenerate `syllabus/csc101-syllabus.pdf` after syllabus edits.
- [x] Fix broken syllabus link in `readme.md`.
  - `syllabus/csc101-syllabus.pdf` is generated from `syllabus/csc101A_syllabus_fall2026.tex`.
  - `syllabus/csc101-syllabus-old.pdf` remains as the old syllabus copy.
- [ ] Fix stale numbered class link in `challenge_sat.md`.
  - Current file points to `./class03.md`.
  - Likely target is `./class_boolean_logic.md`.
- [x] Reorder README schedule rows around late October and early November.
  - Current order is Class 9 / Oct 21, Class 10 / Oct 28, and Class 11 / Nov 4.
- [ ] Replace placeholder `<>` in the Class 1 challenge column or intentionally remove it.
- [x] Replace the scheduled 4-point Linux Jeopardy component with the 4-point Vibe Coding Project Share.
- [x] Remove Advent of Cyber and Pixel Art Competition from scheduled/assigned work.
  - Advent of Cyber remains only under `## Additional Learning` in `readme.md`.
  - Former Advent and Pixel Art syllabus point buckets are now TBA.
- [x] Assign replacement tasks for the former TBA syllabus point buckets.
  - Activity 1 is the 10-point AI Trading Agent Simulation: trading log (5) and reflection (5).
  - Activity 2 is the 5-point AI Cheating and Impostor Hunt activity.
- [x] Set revised letter-grade thresholds for the 61-point course total: A = 50, B = 46, C = 42, D = 36, and F below 36.
- [x] Clarify the A-grade LinkedIn Learning minimum: complete at least six of the seven LinkedIn Learning activities.
- [ ] Decide whether `class_graph_algorithms.md` is a reserve topic or should appear in the README schedule.

## Content Development Tasks

- [x] Add the Vibe Coding Project Share to the October 14 README and syllabus schedule.
- [ ] Flesh out Impostor Hunt and Impostor Hunt Reflection rows in `readme.md`.
- [x] Clarify the late-semester AI sequence:
  - Agentic AI lesson
  - Activity 1: AI Trading log and reflection
  - Activity 2: AI Cheating/Impostor Hunt and reflection
- [ ] Review assignment/challenge labels for consistency: `[GHP]`, `[SAT]`, `[LSH]`, `[WTQ]`, `[XGB]`, `[EXT]`, `[QDT]`, and `[LSY]`; `[AIT]` is now Activity 1 rather than a Weekly Challenge.
- [ ] Check whether every README challenge has a corresponding complete challenge file.
- [ ] Decide whether `class_graph_algorithms.md` should be updated, archived, or linked from the schedule.

## Verification Commands

Run these after edits:

```powershell
git status --short --branch
git diff --check
rg -n "class03|class01|class02|class04|class05|class06|class07|class08|class09|class10|class11|csc101-syllabus\.pdf|Advent of Cyber" -g "*.md"
```

Optional local-link check:

```powershell
$files = Get-ChildItem -Recurse -File -Filter *.md
foreach ($file in $files) {
  $lines = Get-Content -LiteralPath $file.FullName
  for ($i = 0; $i -lt $lines.Count; $i++) {
    $matches = [regex]::Matches($lines[$i], '!??\[[^\]]*\]\(([^)]+)\)')
    foreach ($m in $matches) {
      $target = $m.Groups[1].Value.Trim()
      if ($target -match '^(https?:|mailto:|#|app:)' -or $target -eq '') { continue }
      $pathPart = ($target -split '#')[0] -replace '^<|>$',''
      if ($pathPart -eq '') { continue }
      $resolved = Join-Path $file.DirectoryName $pathPart
      if (-not (Test-Path -LiteralPath $resolved)) {
        '{0}:{1}: missing {2}' -f (Resolve-Path -LiteralPath $file.FullName -Relative), ($i + 1), $target
      }
    }
  }
}
```
