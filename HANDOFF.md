# CSC 101 Fall 2026 Handoff

Status date: 2026-08-09

## Current State

- Repo is on `main` and was clean when this handoff was created.
- Course repo has moved from numbered class files to topic-named class files, such as `class_welcome_setup.md`, `class_vibe_coding.md`, and `class_agentic_ai_danger.md`.
- README schedule is present and mostly populated for the Fall 2026 Wednesday course arc.
- Strongest current materials: `class_vibe_coding.md`, `class_agentic_ai_danger.md`, and `challenge_ai_trading.md`.
- Stubbier materials that need another pass: `class_linux_jeopardy.md`, `class_graph_algorithms.md`, and the late-semester Impostor/AI reflection items in `readme.md`.

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
- [ ] Reorder README schedule rows around late October and early November.
  - Current order has Class 11 / Nov 4 before Class 9 / Oct 21 and Class 10 / Oct 28.
- [ ] Replace placeholder `<>` in the Class 1 challenge column or intentionally remove it.
- [ ] Replace placeholder `[Link](#)` in `class_linux_jeopardy.md`.
- [x] Remove Advent of Cyber and Pixel Art Competition from scheduled/assigned work.
  - Advent of Cyber remains only under `## Additional Learning` in `readme.md`.
  - Former Advent and Pixel Art syllabus point buckets are now TBA.
- [ ] Assign replacement tasks for the TBA syllabus point buckets.
- [ ] Decide whether `class_graph_algorithms.md` is a reserve topic or should appear in the README schedule.

## Content Development Tasks

- [ ] Expand `class_linux_jeopardy.md` into a student-facing activity page.
- [ ] Flesh out Impostor Hunt and Impostor Hunt Reflection rows in `readme.md`.
- [ ] Clarify the late-semester AI sequence:
  - Agentic AI lesson
  - AI Trading challenge
  - Trading reflection
  - Impostor Hunt
  - Impostor Hunt reflection
- [ ] Review assignment/challenge labels for consistency: `[GHP]`, `[AIT]`, `[SAT]`, `[LSH]`, `[WTQ]`, `[XGB]`, `[EXT]`, `[QDT]`, `[LSY]`.
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
