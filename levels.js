// levels.js - Mirror Slide Puzzle Game Levels
// Solved state: blanks (0) at cells 0 and 15, tiles 1-14 in cells 1-14.
// Point symmetry: cell (r, c) mirrors to (3-r, 3-c), i.e., index (15 - i).

const LEVELS = [
  {
    name: "Level 1: First Reflection",
    hint: "Slide tile 1 to the right — watch how tile 14 copies the motion!",
    start: [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14]
  },
  {
    name: "Level 2: The Crossroads",
    hint: "Tiles 6 and 9 touch both blanks! Click either directional arrow to choose your path.",
    start: [1, 5, 2, 3, 4, 0, 6, 7, 8, 9, 0, 11, 12, 13, 10, 14]
  },
  {
    name: "Level 3: Twin Dance",
    hint: "The blanks travel down the outer columns. Bring tile 7 and tile 8 into place first.",
    start: [1, 2, 3, 7, 4, 5, 6, 0, 0, 9, 10, 11, 8, 12, 13, 14]
  }
];

if (typeof window !== 'undefined') {
  window.LEVELS = LEVELS;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LEVELS };
}
