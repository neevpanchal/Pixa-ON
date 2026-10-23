# AI_LOG.md

## Tools & Environment
- **Antigravity Coding Assistant (Gemini 3.8 Flash)**: Full-stack code generation, architectural design, state-machine modeling, and documentation.
- **Stitch (Google)**: Generative UI design and prototyping tool used to generate the high-fidelity retro-futuristic "Optical Core" sci-fi frontend aesthetic (Title Screen, Reflector Core In-Game HUD, Chamber Select, and Technical Manual).
- **Node.js (v24.19.0)**: Algorithmic test harness, headless browser automation over Chrome DevTools Protocol (CDP), and build-less script execution.
- **Python (v3.12)**: Bidirectional breadth-first search (BFS) puzzle solver and level generator (`tools/solver.py`).
- **Google Chrome & Chrome DevTools Protocol (CDP)**: Automated headless browser testing, layout regression capture, and interactive screenshot verification.
- **Web Audio API**: Procedural, real-time synthesized 8-bit and sci-fi audio effects (zero external sound files).
- **Git & GitHub CLI (`gh`)**: Source code management, repository creation, and GitHub Pages automated deployment.

---

## Key Prompts & Engineering Milestones

### Prompt 1: Initial Game Construction
> *"Build a browser puzzle game as a single index.html (HTML, CSS and JavaScript, no frameworks, no build step, opens by double-clicking the file). Game: 'Mirror Slide'..."*

- **Architecture**: Separated pure algorithmic game logic (`applyMove`, `isSolved`, `getLegalDirections`) from DOM rendering.
- **Point Symmetry Mechanics**: Implemented mathematical inversion $(r, c) \leftrightarrow (3-r, 3-c)$ ($i \leftrightarrow 15 - i$). Moving a tile simultaneously moves its mirrored counterpart in the inverted direction.
- **Dual-Blank Crossroads**: Handled the ambiguous case where a tile touches both blanks by rendering dual directional arrow buttons (`▲`, `▼`, `◀`, `▶`).
- **Initial Aesthetics**: Vintage cream graph paper (pure SVG strokes, zero CSS gradients), chunky navy pixel typography (`Press Start 2P`), and gold accents.

---

### Prompt 2: GitHub Repository Setup
> *"Push this on my GitHub, pixa on"*

- Initialized local git repository, added `.gitignore` (ignoring Python cache, system files, artifacts) and initial `README.md`.
- Authenticated via GitHub CLI (`gh`) and pushed the repository to [`https://github.com/neevpanchal/Pixa-ON`](https://github.com/neevpanchal/Pixa-ON).

---

### Prompt 3: Solver Verification & Self-Test Suite
> *"I added tools/solver.py and a new levels.js, which replaces the placeholder one. Each level has a stored solution (list of [cell, direction] moves).
> 1. Add a self-test in the JS (a function runSelfTest() I can call from the browser console) that replays every level's stored solution using the game's own applyMove function and checks that the final state is solved. Log PASS/FAIL per level.
> 2. If any level fails, tell me whether the bug is in the JS rules or the Python rules by comparing both implementations for the first move that differs.
> 3. Make the level select show all levels with the number of moves of the best solution as a 'par'."*

- **`runSelfTest()` Implementation**: Built a console-callable test suite verifying that every stored solution solves the puzzle using the pure `applyMove` engine.
- **Algorithmic Parity**: Compared JavaScript and Python state transitions step-by-step; achieved 100% agreement with 8/8 levels passing.
- **Optimal Par Display**: Surfaced optimal move counts as target "par" scores across level cards and in-game HUD.
- **Solver Reconstruction**: Committed and tested `tools/solver.py` for bidirectional BFS shortest-path solvability.

---

### Prompt 4: Comprehensive QA & Playtesting Audit
> *"Open index.html in the browser. Play every level yourself. Report any bug, unclear UI or confusing moment, with a screenshot. Check: undo, restart without reload, win screen, the two-arrow choice case, keyboard and mouse. Fix the bugs you find and tell me what you changed."*

- **Automated Chrome CDP Test Suite**: Spawned headless Google Chrome via CDP in Node.js to programmatically play through levels and capture screenshots.
- **Dual-Arrow Body Clicking**: Fixed an issue where clicking the body of a dual-blank tile did not register an intuitive direction; added coordinate vector dot-product calculation to pick the closest direction.
- **Full Keyboard Navigation**: Added Arrow keys and WASD controls alongside existing mouse and touch inputs.
- **State Integrity**: Confirmed that `Z` (Undo) and `R` (Restart without page reload) properly reset state and move counters.

---

### Prompt 5: Game-Feel Polish
> *"Polish the game for feel:
> - Smooth tile slide animation (about 120 ms), a subtle 'ghost' highlight on the mirrored tile so the player sees the twist.
> - Sound effects with the Web Audio API (no downloaded files needed): a tile click, a mirror 'ping', a win jingle, a bump for illegal moves. Add a mute button.
> - A 'How to play' overlay with a tiny animated example, shown on the first level.
> - Level complete screen showing moves versus par and a one-line message.
> - Mobile-friendly layout.
> Do not break any existing behavior. Keep the single-file structure."*

- **120 ms Slide Animations & Mirror Ghosting**: Added cubic-bezier CSS transform slides for both tiles and `.partner-ghost` glowing highlights on hover and during transit.
- **Synthesized Web Audio API**: Generated real-time procedural sound effects (quartz click, resonant mirror ping, 5-note victory fanfare, and bump thud) with persistent mute toggle.
- **Animated Tutorial Overlay**: Built an animated CSS board showing tiles sliding in mirror symmetry, auto-triggered on Level 1.
- **Level Complete Screen**: Displayed move count vs par comparison with contextual performance messages.
- **Mobile Responsive Design**: Added `touch-action: manipulation`, clamp scaling, and mobile-friendly tap targets.

---

### Prompt 6: Frontend Redesign via Stitch Mockups
> *"I want to change the current frontend to this I created using stitch change the frontend design and edit it like the photos I have added in this prompt, and edit the website."*

- **Stitch "Optical Core" Sci-Fi Theme**: Transformed the visual identity into an amber & cobalt dark carbon terminal (`#0D0C0A`, `#F59E0B`, `#3B82F6`).
- **Title Screen (`// PARALLEL REFLECTION ENGINE`)**: Implemented reflected `ƧΓIDE` logo, cyan laser beam divider, light sensor & emitter dock widgets (matching Image 3).
- **In-Game Reflector Core Matrix**: Added 45° diagonal mirror axis line (`--- MIRROR AXIS 45° ---`), Sector Alpha / Beta pair highlights, zero-padded numbers (`01`-`14`), and left-side telemetry widgets (Symmetry Protocol, Target Schematic, Linked Pair Target) (matching Image 1).
- **Chamber Select Screen**: Sector clearance progress meter, 8 chamber cards with mini-schematics, active chamber briefing panel, and sector controller map (matching Image 4).
- **Technical Manual Modal**: 3-step technical diagram (`[INPUT]`, `[REFLECT]`, `[TARGET]`) and commencement button (matching Image 2).

---

### Prompt 7: Documentation & GitHub Pages Deployment
> *"Create a README for this project and commit all the changes that happened on GitHub, and also upload the index.html file on GitHub. In the readme also attach the live URL of the website."*

- Enabled GitHub Pages deployment via GitHub CLI (`gh api --method POST repos/neevpanchal/Pixa-ON/pages`).
- Verified live deployment status: `https://neevpanchal.github.io/Pixa-ON/` (HTTP 200 OK).
- Authored comprehensive `README.md` featuring live demo links, gameplay mechanics, controls table, architecture, and verification instructions.

---

### Prompt 8: Comprehensive AI_LOG Expansion
> *"And also add all the prompts in AI_log. And also all the changes where the AI got wrong, and also add stitch in the tools."*

- Updated `AI_LOG.md` with all historical prompts, complete engineering decisions, tool attribution (including Stitch), and detailed failure/recovery post-mortems.

---

### Prompt 9: Mirror Axis Overlay Removal
> *"Remove this mirror axis because the user is not able to see the numbers on tiles"*

- Removed the overlapping diagonal axis SVG line and `--- MIRROR AXIS 45° ---` badge from the 4×4 board frame.
- Guaranteed all 14 numbers (`01` through `14`) and empty sockets are completely clear and legible on all viewports without visual obstructions.
- Verified and deployed update to GitHub repository and live GitHub Pages site.

---

## When AI Got It Wrong & How It Was Resolved

### 1. Browser Subagent Sandbox Dependency & Network Block
- **Issue**: An attempt to run visual automated browser tests using the built-in browser subagent failed because Playwright could not download its browser binaries inside the sandbox container (blocked with HTTP 404 from azureedge).
- **Correction**: Abandoned the external driver download. Instead, directly spawned the local Google Chrome binary (`C:\Program Files\Google\Chrome\Application\chrome.exe`) with `--remote-debugging-port=9224 --headless=new` and controlled it natively using Node.js v24 `WebSocket` communicating over Chrome DevTools Protocol (CDP).

### 2. SVG Background Stroke Hex Format
- **Issue**: The graph-paper SVG background data URI initially contained an invalid 5-digit hex stroke `%23DECFA` instead of a 6-digit hex code, causing rendering inconsistencies in certain browser engines.
- **Correction**: Audited the SVG stroke attribute and normalized it to `%23DCD3C0` (and later `%23211C14` for the dark theme), ensuring 100% consistent cross-browser rendering without CSS gradients.

### 3. Dual-Arrow Tile Body Click Conflict
- **Issue**: When a tile was adjacent to both empty sockets, small directional arrow buttons appeared on the edges. If a player clicked the center of the tile body rather than the tiny arrow buttons, the move did not execute, leading to perceived click unresponsiveness.
- **Correction**: Added a vector resolution handler to the tile body click event: calculated the click offset $(X - \text{center}_X, Y - \text{center}_Y)$, computed the dot product with valid movement vectors, and automatically executed the move in the direction closest to where the player tapped.

### 4. Input Race Condition During 120 ms Slide Animation
- **Issue**: Introducing a 120 ms CSS slide animation created a race condition where rapid keypresses or clicks during transit could alter the internal 16-element array while DOM elements were still animating, desynchronizing the visual board from the state machine.
- **Correction**: Implemented an explicit state lock `Game.isAnimating = true` during the 120 ms window. Any input attempts during animation are dropped or played as subtle feedback bumps, and the state lock only releases after `boardState` is cleanly committed and re-rendered.

### 5. Test Harness Move Sequence Mismatch
- **Issue**: During headless testing of the win modal flow in `scratch/test_polish.js`, the test script hardcoded an obsolete move sequence from early placeholder levels. When executed on the new `levels.js` layout, the move failed as illegal, leaving the win modal unopened.
- **Correction**: Updated test scripts to pull ground-truth move sequences dynamically from `window.LEVELS[currentLevelIndex].solution`, ensuring headless test runs accurately match the solver's shortest path with proper animation pauses.

### 6. Shell `curl` Hang During HTTP Status Verification
- **Issue**: Testing the newly activated GitHub Pages endpoint using PowerShell's `curl` alias caused the process to hang without terminating due to shell-specific proxy/DNS handling.
- **Correction**: Replaced shell `curl` with Node's native `fetch()` API (`node -e "fetch('...').then(r => console.log(r.status))"`), which cleanly completed and confirmed `HTTP Status: 200` in under 2 seconds.

### 7. Diagonal Mirror Axis Overlay Obscuring Grid Numbers
- **Issue**: Faithfully transcribing the Stitch design mockup included a literal diagonal dashed axis line and a rotated badge (`--- MIRROR AXIS 45° ---`) across the center of the 4x4 matrix. In active gameplay, this badge physically covered tiles `06`, `07`, `09`, and `10`, making their numbers difficult to read.
- **Correction**: Removed the overlapping diagonal axis SVG and badge from the playable puzzle matrix so all 14 tile numbers are 100% visible and unobstructed, while preserving the concept cleanly in the left telemetry schematic panel and the technical manual.