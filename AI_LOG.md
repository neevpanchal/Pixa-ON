# AI_LOG.md

## Tools
- **Antigravity Coding Assistant (Gemini 3.8 Flash)**: Code generation, architectural design, state-machine modeling, and documentation.
- **Node.js (v24.19.0)**: Algorithmic validation, BFS shortest-path solver to guarantee level solvability, and headless logic testing.
- **Web Audio API**: Real-time synthesized 8-bit sound effects (procedural audio without external audio assets).
- **Git & GitHub CLI (`gh`)**: Version control and GitHub repository management.

## Key Prompts
1. *"Build a browser puzzle game as a single index.html (HTML, CSS and JavaScript, no frameworks, no build step, opens by double-clicking the file). Game: 'Mirror Slide'..."*
   - Designed pure logic function `applyMove(state, tileCell, direction)` decoupled from the DOM.
   - Enforced strict point-reflection symmetry: $(r, c) \leftrightarrow (3-r, 3-c)$ ($i \leftrightarrow 15 - i$).
   - Implemented dual-blank arrow selection buttons on tiles adjacent to both blanks.
   - Crafted cream graph-paper aesthetic with chunky navy pixel typography, gold accents, hard offset shadows, and zero CSS gradients.
   - Designed hand-crafted levels in `levels.js` verified with a BFS search script to ensure solvability.

2. *"Push this on my GitHub, pixa on"*
   - Initialized git repository, added `.gitignore` and `README.md`.
   - Documented hackathon AI workflow in `AI_LOG.md`.
   - Created and published repository to GitHub via GitHub CLI (`gh`).

## When AI Got It Wrong
1. **Browser Subagent Sandbox Dependency Issue**:
   - *Issue*: An attempt to run headless visual browser testing failed because Playwright could not download its browser driver inside the restricted sandbox environment (HTTP 404 from azureedge).
   - *Fix*: Instead of relying on external browser drivers, built a standalone Node.js test harness (`scratch/verify_levels.js` & `scratch/thorough_check.js`) that simulated state transitions, validated pure function invariants, tested point symmetry, and verified BFS shortest solution paths for all levels.
2. **SVG Background Stroke Format**:
   - *Issue*: The initial SVG background string had a 5-digit hex value (`%23DECFA`) instead of a valid 6-digit hex code, which could cause inconsistent rendering on some browser engines.
   - *Fix*: Audited and updated the stroke attribute to a standard 6-digit hex color (`%23DCD3C0`) to ensure 100% reliable graph-paper grid rendering across all browsers without using CSS gradients.