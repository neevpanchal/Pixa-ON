# 🪞 MIRROR SLIDE // OPTICAL_CORE

> *"Classic sliding tiles, but every deliberate move you make is mirrored on the opposite side of the board."*

🔗 **Live Playable Game**: [https://neevpanchal.github.io/Pixa-ON/](https://neevpanchal.github.io/Pixa-ON/)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Pure Vanilla](https://img.shields.io/badge/tech-HTML5%20%7C%20CSS3%20%7C%20JS-F59E0B.svg)](#technology-stack)
[![Zero Assets](https://img.shields.io/badge/audio-Web%20Audio%20API-3B82F6.svg)](#synthesized-audio)
[![Self-Test](https://img.shields.io/badge/self--test-8%2F8%20PASS-10B981.svg)](#algorithmic-verification--self-test)

---

## 🛰️ Overview

**Mirror Slide (Optical Core)** is a retro-futuristic sci-fi sliding-tile puzzle game powered by a point-reflection mechanic. When you slide a tile into an empty socket in **Sector Alpha**, its symmetrical counterpart in **Sector Beta** simultaneously executes an inverted slide along the 45° diagonal axis.

Built entirely in vanilla **HTML5, CSS3, and JavaScript** with **zero external assets, zero frameworks, and zero build tools**. Double-click `index.html` to run locally or play directly on GitHub Pages!

---

## 🎮 How to Play

1. **The Objective**:
   - Calibrate the optical core by arranging tiles **`01` to `14`** in sequential reading order.
   - Leave the top-left corner (`SOCKET 0 ALPHA`) and bottom-right corner (`SOCKET 0 BETA`) empty.
2. **Point Symmetry**:
   - The board operates on point reflection: every cell coordinate $(r, c)$ maps directly to $(3-r, 3-c)$ ($i \leftrightarrow 15 - i$).
3. **Mirrored Moves**:
   - Sliding any tile into an adjacent empty socket simultaneously causes its mirrored partner on the opposite side of the board to slide into its empty socket in reverse.
   - **Hover Ghosting**: Hovering over any movable tile highlights Sector Alpha in **amber** (`#F59E0B`) and its mirrored counterpart in **cobalt blue** (`#3B82F6`).
4. **Dual-Blank Crossroads**:
   - When a tile is adjacent to both empty sockets, dual directional arrow buttons (`▲`, `▼`, `◀`, `▶`) illuminate on the tile, allowing you to choose your desired path.
5. **Telemetric HUD**:
   - Watch the live **Linked Pair Target** indicator (`TILE [XX] ⇄ TILE [YY]`) and the **Optical Target Schematic** as you maneuver the quartz tiles.

---

## ⌨️ Controls & Keybindings

| Input | Action |
|---|---|
| **Click / Tap** | Slide tile into adjacent blank (or choose arrow on crossroads) |
| **Arrow Keys / WASD** | Slide tiles in the specified direction |
| **Z** | Undo previous move |
| **R** | Restart current chamber |
| **H** | Hint (illuminates next optimal move pair) |
| **M** | Toggle audio mute (`🔊 STEREO` / `🔇 MUTED`) |
| **ESC** | Open Chamber Select / Return to Title / Close Modal |
| **Enter / Space** | Confirm / Deploy laser / Dismiss manual |

---

## 🌟 Key Features

- **Sci-Fi Optical Terminal Aesthetic**:
  - Dark carbon console background with crisp SVG grid lines (strictly 0% CSS gradients).
  - Amber (`#F59E0B`) and cobalt blue (`#3B82F6`) HUD telemetry panels with technical reticle corner brackets (`⌜ ⌝ ⌞ ⌟`).
  - Diagonal 45° laser axis beam spanning the reflector matrix (`--- MIRROR AXIS 45° ---`).
- **Parallel Reflection Engine Title Screen**:
  - Features the reflected `ƧΓIDE` logo, glowing cyan laser divider, light sensor and emitter dock telemetry cards.
- **Chamber Select Screen**:
  - Visual sector clearance progress meter.
  - 8 hand-crafted chambers with optimal par targets, star ratings, and chamber preview schematics.
  - Active chamber briefing panel with tactical descriptions and controller hotkey maps.
- **Smooth 120 ms Slide Animations**:
  - Fluid cubic-bezier transitions for both the player tile and its mirrored twin, preventing input race conditions while keeping the action tactile and responsive.
- **Zero-Download Synthesized Audio (Web Audio API)**:
  - Mechanical quartz relay clicks for tile movement.
  - Resonant harmonic optical mirror pings ($1520\text{ Hz} \to 1200\text{ Hz}$) on reflection.
  - 5-note celebratory arpeggios ($\text{C}_5 - \text{E}_5 - \text{G}_5 - \text{B}_5 - \text{C}_6$) on chamber clearance.
  - Low warning thuds ($110\text{ Hz} \to 45\text{ Hz}$) with visual shake on illegal moves.
  - Persistent audio mute toggle with `localStorage` memory.
- **Mobile-Friendly Layout**:
  - `touch-action: manipulation` across all buttons and tiles eliminates 300ms mobile tap delays.
  - Responsive layout adapts from desktop dual-column telemetry to vertical smartphone viewports down to 360 px width.

---

## 🧪 Algorithmic Verification & Self-Test

Every chamber in the game has been verified for mathematical solvability and shortest-path optimality using a bidirectional breadth-first search (BFS) solver.

### Run Browser Console Self-Test
Open the game in any browser, open Developer Tools Console (`F12`), and run:

```javascript
runSelfTest()
```

Output:
```
=== RUNNING OPTICAL CORE SELF-TEST (8 CHAMBERS) ===
[PASS] Chamber 1: Level 1 - Warm-Up (3 moves, Par: 3) -> Solved!
[PASS] Chamber 2: Level 2 - Gentle Push (5 moves, Par: 5) -> Solved!
[PASS] Chamber 3: Level 3 - Finding Rhythm (7 moves, Par: 7) -> Solved!
[PASS] Chamber 4: Level 4 - Mid Challenge (9 moves, Par: 9) -> Solved!
[PASS] Chamber 5: Level 5 - Getting Tricky (11 moves, Par: 11) -> Solved!
[PASS] Chamber 6: Level 6 - Brain Stretch (12 moves, Par: 12) -> Solved!
[PASS] Chamber 7: Level 7 - Expert Territory (11 moves, Par: 11) -> Solved!
[PASS] Chamber 8: Level 8 - Grand Finale (14 moves, Par: 14) -> Solved!
✓ ALL 8/8 CHAMBERS PASSED!
```

### Run Python BFS Solver
```bash
python tools/solver.py
```

---

## 📁 Repository Structure

```
├── index.html       # Single-file self-contained frontend (UI, styling, Web Audio engine, event handlers)
├── levels.js        # Global LEVELS array containing 8 solvable chambers, hints, pars & solutions
├── AI_LOG.md        # AI collaboration log & development notes
├── README.md        # Comprehensive project documentation
├── .gitignore       # Git ignore rules
└── tools/
    └── solver.py    # Bidirectional BFS shortest-path puzzle solver & level generator
```

---

## 🚀 Local Setup & Installation

No npm, package managers, or build steps required.

```bash
# 1. Clone repository
git clone https://github.com/neevpanchal/Pixa-ON.git

# 2. Navigate to directory
cd Pixa-ON

# 3. Open in browser (Windows PowerShell)
Start-Process index.html
```

Or visit the live build instantly at: **[https://neevpanchal.github.io/Pixa-ON/](https://neevpanchal.github.io/Pixa-ON/)**

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
