# Vibe Coding: Build a Chess Game

## Goal

Use an AI coding assistant in VS Code to build a small chess game. Practice giving one clear prompt at a time, testing each change, and making small edits yourself.

The game uses simplified rules:

- Capture the enemy king to win.
- Ignore check and checkmate. A player may leave the king in danger.
- No castling, en passant, or pawn promotion.
- Pawns may move one square forward and capture one square diagonally.

## In-class activity

Work in pairs if possible. One person prompts and the other tests; switch roles halfway through. Do **not** give the AI every prompt at once. For many commercial AIs, they are actually capable of this now. But do not do it. Let's talk about why at the end.

Complete and test one step before continuing.

### Step 1: Introduce the activity

- Vibe coding means describing a small goal, letting AI write code, and checking the result.
- AI output can be wrong. Read the changed files and test after every prompt. Currently, this is probably beyond you, but you can ask AI to write comments or walk you through a section of code.
- For today, a working simple game is better than a complicated unfinished game.

### Step 2: Create the project

1. In VS Code, create and open a folder named `vibe-chess`.
2. Open your AI coding assistant and enter:

> Create `index.html`, `style.css`, and `script.js` for a browser-based chess game. In this step, only make a page with the heading "Capture the King" and an empty area for the board. Connect the CSS and JavaScript files. Keep the code simple and do not use libraries.

Open `index.html` in a browser. Confirm that the heading appears.

### Step 3: Display the board

Prompt:

> Add an 8-by-8 chessboard with alternating light and dark squares. Use CSS variables named `--light-square` and `--dark-square` for the colors. Use JavaScript to place all chess pieces in their normal starting positions. Unicode chess symbols are fine. Do not add movement yet.

Test: Count eight rows and eight columns. Check that both armies appear.

Task: Locate where the code for placing the chess pieces are. Ask AI if you are unfamiliar with coding. 

### Step 4: Select and move pieces

Starting with this step, the sample prompts are omitted. Write your own prompt for each step and keep a record of the exact words you use. If a prompt does not work, revise it and record the new version too. Test that each step works as intended before moving on.

Your AI assistant should already have context from the work you completed in the previous steps, so your prompts can be brief and conversational. They do not need to sound formal, but they should clearly describe the change you want.

For this step, make it possible to select a piece by clicking it and then move it by clicking another square. The selected square should have a visible outline. For now, any piece may move to any square.

Record your prompt and any revisions.

Test: Move one white piece and one black piece.

### Step 5: Add sliding-piece movement

Add the basic movement rules for rooks, bishops, and queens. These pieces cannot jump over another piece. An illegal move should leave the board unchanged and display a short message. Do not add check or checkmate.

Record your prompt and any revisions.

Test one legal and one illegal move for each piece type. What does your program do when an illegal move is attempted? Do you want to improve that?

### Step 6: Add the other movement rules

Add the basic movement rules for kings, knights, and pawns. Kings move one square. Knights move in an L shape and may jump over pieces. Pawns move one square forward and capture one square diagonally. Do not add castling, en passant, promotion, check, or checkmate.

Record your prompt and any revisions.

Test a knight jump, a king move, a pawn move, and a pawn capture.

### Step 7: Add turns and captures

Add alternating white and black turns, and display whose turn it is. A player may select only a piece of their own color. A piece may capture an opponent's piece by moving onto its square, but it may not capture a piece of the same color.

Record your prompt and any revisions.

Test: Try moving twice with the same color and capturing your own piece. Both should be rejected.

### Step 8: Win by capturing the king

Make the game stop when a king is captured and display which color won. Add a "New Game" button that restores the starting position. A player wins only by capturing the king; do not add check or checkmate.

Record your prompt and any revisions.

For a quick test, ask the AI to temporarily start the black king beside a white piece. Capture it, confirm the win message, and then undo that temporary code change.

### Step 9: Make two tiny changes yourself

Without asking AI to do it for you:

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

Write your own bug-fixing prompt. Include what you did, what you expected to happen, and what actually happened. Ask for a small fix without new features and a brief explanation of the change. Record the prompt and any revisions.

### Step 11: Wrap up

Be ready to answer:

- Which prompt produced the best result, and why?
- What mistake did testing catch?
- Which part of the code can you now recognize or change yourself?

## Finished when

Your browser shows a playable two-person chessboard with turns, captures, a capture-the-king win, and a new-game button. Visual polish and full tournament chess rules are not required.


## So, why not just let AI do it in one go?

The main lesson here is that AI is best used as a tool in your workflow, not as a replacement for your own thinking. It can be great for repetitive tasks, brainstorming ideas, drafting text, organizing information, and helping you move faster. That is where it is strongest.

But the important part is that the judgment still belongs to you. You are the one who decides what matters, what is worth doing, and whether the result is actually good. AI can help generate options, but it cannot replace your experience, your values, or your responsibility.

A good way to think about it is this: AI is more like a very capable assistant than a decision-maker. You would not let a tool make a medical decision, a scientific claim, or a financial plan for you without questioning it, just because it sounds confident. The same standard should apply here.

You can also think of it like hiring a team member. If you are starting a business, AI can help you do work faster, but your success still depends on your leadership. You still need to plan expenses, allocate resource, set goals, assign tasks, check the results, and think ahead about what could go wrong. If you do not know where you are going, even the smartest assistant will not save you. For example, imagine yourself the sole inheritor of Jeff Bezos, and Jeff pass you his business, you are left with the most amount of resource, best talented people, best logistics in the world, can you confidently say that you will not squander that in one year? Do you have a basic plan of what to do?

This is why we don't let AI to do everything in one go. Among many other reasons, it takes away your autonomy. When your magic pill stopped working, can you know what went wrong? When you business go underwater, do you know where is the boat leaking? In terms of coding, do you know what went wrong and can you fix it?

So the goal is not to let AI do everything for you. The goal is to use it well: to support your work, speed up your process, and help you think more clearly while still keeping your own judgment at the center. 
