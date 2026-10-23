# Mirror Slide (Pixa-ON)

> *"Classic sliding tiles, but every move you make is mirrored on the opposite side of the board."*

**Mirror Slide** is a retro-styled browser sliding-tile puzzle game featuring a unique point-reflection mechanic: whenever you slide a tile into an adjacent blank cell, the tile in the point-symmetric cell simultaneously slides into the mirrored blank.

Built with vanilla HTML5, CSS3, and JavaScript — no frameworks, no external libraries, and no build steps. Double-click `index.html` to play!

---

## 🎮 How to Play

1. **Board Layout**:
   - 4×4 grid with tiles numbered 1 to 14, plus **two blank slots** (0).
   - Solved state: Tiles 1–14 arranged in reading order with blank slots at cell 0 (top-left) and cell 15 (bottom-right).
2. **Point Symmetry**:
   - The two blanks are always point-symmetric: any cell $(r, c)$ reflects to $(3-r, 3-c)$ (index $15 - i$).
3. **Mirrored Moves**:
   - Sliding a tile into an adjacent blank simultaneously slides its mirrored partner in the mirrored direction into the opposite blank.
   - Hovering over any movable tile highlights both the tile and its mirror partner in gold.
4. **Dual-Blank Crossroads**:
   - When a tile is adjacent to both blanks at once, two directional arrow buttons (`▲`, `▼`, `◀`, `▶`) appear on the tile so you can choose which path to slide.
5. **Controls**:
   - **Click**: Slide a tile into an adjacent blank (or click an arrow if touching both blanks).
   - **Z**: Undo previous move.
   - **R**: Restart current level.
   - **Audio**: Toggle retro 8-bit sound effects (on/off).

---

## 🎨 Design & Aesthetic

- **Cream Graph-Paper Background**: Styled via crisp SVG strokes (strictly 0% CSS gradients).
- **Chunky Navy Pixel Typography**: `#0D1F3C` with Google Font `'Press Start 2P'` and retro monospace fallback.
- **Gold Accent**: Warm arcade gold (`#F59E0B`) highlighting interactive cues, solved corner indicators, and level badges.
- **Hard Offset Shadows**: Sharp pixel offset drop-shadows with zero blur radius.

---

## 📁 Project Structure

```
├── index.html       # Single-file entry point (UI, styling, Web Audio engine, event handlers)
├── levels.js        # Global LEVELS array containing hand-crafted solvable levels & hints
├── AI_LOG.md        # AI collaboration log & development notes
├── README.md        # Project documentation
└── .gitignore       # Git ignore rules
```

---

## 🚀 Getting Started

Simply clone or download this repository, then open `index.html` directly in any modern browser:

```bash
git clone https://github.com/neevpanchal/Pixa-ON.git
cd Pixa-ON
# Open index.html in your browser
```
