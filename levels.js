const LEVELS = [
  {
    name: "Level 1 - Warm-Up",
    hint: "Just a few moves \u2013 get a feel for the mirror mechanic.",
    start: [1, 2, 6, 3, 4, 5, 0, 7, 8, 0, 10, 11, 12, 9, 13, 14],
    optimal: 3,
    solution: [[2, "down"], [1, "right"], [0, "right"]]
  },
  {
    name: "Level 2 - Gentle Push",
    hint: "Every tile you move flips its partner. Plan two steps ahead.",
    start: [1, 2, 3, 7, 0, 5, 6, 11, 4, 9, 10, 0, 8, 12, 13, 14],
    optimal: 5,
    solution: [[7, "down"], [3, "down"], [2, "right"], [1, "right"], [0, "right"]]
  },
  {
    name: "Level 3 - Finding Rhythm",
    hint: "Watch how the mirrored tile can block or help you.",
    start: [5, 4, 2, 3, 1, 9, 0, 7, 8, 0, 6, 14, 12, 13, 11, 10],
    optimal: 7,
    solution: [[5, "down"], [1, "down"], [0, "right"], [4, "up"], [5, "left"], [1, "down"], [0, "right"]]
  },
  {
    name: "Level 4 - Mid Challenge",
    hint: "Try to free both blanks before committing to a sequence.",
    start: [2, 0, 6, 3, 4, 1, 7, 10, 5, 8, 14, 11, 12, 9, 0, 13],
    optimal: 9,
    solution: [[0, "right"], [4, "up"], [7, "down"], [6, "right"], [2, "down"], [1, "right"], [5, "up"], [4, "right"], [0, "down"]]
  },
  {
    name: "Level 5 - Getting Tricky",
    hint: "Think in pairs: each slide affects two tiles at once.",
    start: [4, 6, 7, 1, 5, 13, 0, 3, 12, 0, 2, 10, 14, 8, 9, 11],
    optimal: 11,
    solution: [[2, "down"], [3, "left"], [7, "up"], [6, "right"], [5, "down"], [1, "down"], [2, "left"], [6, "up"], [5, "right"], [4, "right"], [0, "down"]]
  },
  {
    name: "Level 6 - Brain Stretch",
    hint: "Long chains pay off \u2013 look for moves that set up the next one.",
    start: [9, 5, 0, 3, 1, 2, 7, 11, 4, 8, 13, 14, 12, 0, 10, 6],
    optimal: 12,
    solution: [[1, "right"], [0, "right"], [4, "up"], [7, "down"], [6, "right"], [5, "right"], [1, "down"], [2, "left"], [6, "up"], [5, "down"], [1, "down"], [0, "right"]]
  },
  {
    name: "Level 7 - Expert Territory",
    hint: "Near the end, every move matters. Work backwards from the goal.",
    start: [2, 5, 7, 0, 1, 6, 3, 11, 4, 12, 9, 14, 0, 8, 10, 13],
    optimal: 11,
    solution: [[2, "right"], [6, "up"], [5, "right"], [1, "down"], [0, "right"], [4, "up"], [7, "down"], [3, "down"], [2, "right"], [1, "right"], [0, "right"]]
  },
  {
    name: "Level 8 - Grand Finale",
    hint: "The hardest shuffle of all. Only the best paths succeed here.",
    start: [12, 8, 1, 2, 4, 0, 5, 6, 9, 10, 0, 11, 13, 14, 7, 3],
    optimal: 14,
    solution: [[4, "right"], [0, "down"], [1, "left"], [5, "up"], [6, "left"], [7, "left"], [4, "down"], [0, "down"], [1, "left"], [2, "left"], [3, "left"], [7, "up"], [4, "down"], [0, "down"]]
  }
];

if (typeof window !== 'undefined') {
  window.LEVELS = LEVELS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LEVELS };
}
