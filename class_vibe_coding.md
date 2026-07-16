# Vibe Coding: Build a Chess Game

## Goal

Use an AI coding assistant in VS Code to build a small chess game. Practice giving one clear prompt at a time, testing each change, and making small edits yourself.

The game uses simplified rules:

- Capture the enemy king to win.
- Ignore check and checkmate. A player may leave the king in danger.
- No castling, en passant, or pawn promotion.
- Pawns may move one square forward and capture one square diagonally.

## In-class activity

Work in pairs if possible. One person prompts and the other tests; switch roles halfway through. Do **not** give the AI every prompt at once. For many commercial AIs, they are actually capable of this now. But do not do it. Complete and test one step before continuing.

### Step 1: Introduce the activity

- Vibe coding means describing a small goal, letting AI write code, and checking the result.
- AI output can be wrong. Read the changed files and test after every prompt.
- Today, a working simple game is better than a complicated unfinished game.

### Step 2: Create the project

1. In VS Code, create and open a folder named `vibe-chess`.
2. Open your AI coding assistant and enter:

> Create `index.html`, `style.css`, and `script.js` for a browser-based chess game. In this step, only make a page with the heading "Capture the King" and an empty area for the board. Connect the CSS and JavaScript files. Keep the code simple and do not use libraries.

Open `index.html` in a browser. Confirm that the heading appears.

### Step 3: Display the board

Prompt:

> Add an 8-by-8 chessboard with alternating light and dark squares. Use CSS variables named `--light-square` and `--dark-square` for the colors. Use JavaScript to place all chess pieces in their normal starting positions. Unicode chess symbols are fine. Do not add movement yet.

Test: Count eight rows and eight columns. Check that both armies appear.

### Step 4: Select and move pieces

Prompt:

> Let a player click one piece to select it, then click any square to move it there. Show the selected square with a visible outline. For now, allow any piece to move anywhere. Change only what is needed for this step.

Test: Move one white piece and one black piece.

### Step 5: Add sliding-piece movement

Prompt:

> Add basic movement rules for rooks, bishops, and queens. They cannot jump over another piece. If a move is not allowed, leave the board unchanged and show a short message. Do not add check or checkmate rules.

Test one legal and one illegal move for each piece type.

### Step 6: Add the other movement rules

Prompt:

> Add basic movement rules for kings, knights, and pawns. Kings move one square, knights move in an L shape and may jump, and pawns move one square forward or capture one square diagonally. Do not add castling, en passant, promotion, check, or checkmate.

Test a knight jump, a king move, a pawn move, and a pawn capture.

### Step 7: Add turns and captures

Prompt:

> Add alternating white and black turns. A player may select only their own piece. Allow a piece to capture an opponent's piece by moving onto its square, but never allow it to capture a piece of the same color. Display whose turn it is.

Test: Try moving twice with the same color and capturing your own piece. Both should be rejected.

### Step 8: Win by capturing the king

Prompt:

> When a king is captured, stop the game and display which color won. Add a "New Game" button that restores the starting position. Winning is only by capturing the king; do not add check or checkmate.

For a quick test, ask the AI to temporarily start the black king beside a white piece. Capture it, confirm the win message, and then undo that temporary code change.

### Step 9: Make two tiny changes yourself

Without asking AI:

1. Change the heading to a name you choose.
2. Change `--light-square` and `--dark-square` in `style.css` to your own board colors.

Refresh the browser and confirm both changes.

### Step 10: Test and fix one bug

Trade computers with another pair. Test:

- selecting and moving a piece;
- one illegal move;
- alternating turns;
- capturing a piece; and
- starting a new game.

If something fails, describe only that problem to the AI:

> Bug: [describe what you did, what you expected, and what happened]. Find the smallest fix. Do not add new features. Explain the change in two sentences or fewer.

### Step 11: Wrap up

Be ready to answer:

- Which prompt produced the best result, and why?
- What mistake did testing catch?
- Which part of the code can you now recognize or change yourself?

## Finished when

Your browser shows a playable two-person chessboard with turns, captures, a capture-the-king win, and a new-game button. Visual polish and full tournament chess rules are not required.
