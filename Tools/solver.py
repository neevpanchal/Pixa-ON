"""tools/solver.py  –  Mirror Slide puzzle solver and level generator.

Game rules
----------
* 4×4 board stored as a tuple of 16 ints  (0 = blank, cells indexed 0..15
  in reading order).
* Two blanks, always point-symmetric:  cell i  ↔  cell 15-i.
* A move is (cell, direction):  the tile at *cell* slides into the adjacent
  blank in that direction; simultaneously the tile at cell (15-cell) slides
  in the OPPOSITE direction into the other blank.
* Solved state: (0, 1, 2, …, 14, 0)  –  blanks at 0 & 15, tiles 1-14 at 1-14.

Public API
----------
  neighbors(state)            – all legal moves and resulting states
  solve(state, node_cap)      – bidirectional BFS to SOLVED
  scramble(depth, seed)       – random walk from SOLVED
  generate_levels()           – build 8 levels and return level dicts
  write_levels_js(levels, path) – emit levels.js
"""

import json
import os
import random
from collections import deque

SOLVED = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0)

_DIRS = {
    'up': -4,
    'down': 4,
    'left': -1,
    'right': 1
}

_OPPOSITE = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left'
}

_LEVEL_META = [
    ('Warm-Up', 'Just a few moves \u2013 get a feel for the mirror mechanic.', 3),
    ('Gentle Push', 'Every tile you move flips its partner. Plan two steps ahead.', 5),
    ('Finding Rhythm', 'Watch how the mirrored tile can block or help you.', 7),
    ('Mid Challenge', 'Try to free both blanks before committing to a sequence.', 9),
    ('Getting Tricky', 'Think in pairs: each slide affects two tiles at once.', 11),
    ('Brain Stretch', 'Long chains pay off \u2013 look for moves that set up the next one.', 12),
    ('Expert Territory', 'Near the end, every move matters. Work backwards from the goal.', 13),
    ('Grand Finale', 'The hardest shuffle of all. Only the best paths succeed here.', 14)
]


def _row(i: int) -> int:
    return i >> 2


def _col(i: int) -> int:
    return i & 3


def neighbors(state: tuple[int, ...]) -> list[tuple[tuple[int, str], tuple[int, ...]]]:
    """Return all legal ((cell, direction), new_state) pairs for *state*.

    A move (cell, direction) is valid when:
      • state[cell] is not blank
      • the adjacent cell in that direction is blank
      • boundary rules are respected (no row-wrap for horizontal moves)

    The mirror action (tile at 15-cell slides oppositely) is always valid
    whenever the primary action is valid, by point-symmetry of the grid.

    Only *canonical* moves are generated (source cell in 0..7) because every
    resulting state is otherwise produced twice – once by (cell, dir) and once
    by its mirror (15-cell, opposite-dir).
    """
    result = []
    for cell in range(8):
        if state[cell] == 0:
            continue
        r = _row(cell)
        c = _col(cell)
        for dname, delta in _DIRS.items():
            if dname == 'up' and r == 0:
                continue
            if dname == 'down' and r == 3:
                continue
            if dname == 'left' and c == 0:
                continue
            if dname == 'right' and c == 3:
                continue
            target = cell + delta
            if state[target] != 0:
                continue
            mc = 15 - cell
            mt = 15 - target
            lst = list(state)
            lst[target] = lst[cell]
            lst[cell] = 0
            lst[mt] = lst[mc]
            lst[mc] = 0
            result.append(((cell, dname), tuple(lst)))
    return result


def _reverse_move(move: tuple[int, str]) -> tuple[int, str]:
    """Return the canonical reverse of a canonical move (cell, dname).

    Applying (cell, dname) moves a tile from *cell* to *target = cell+delta*.
    The reverse takes that tile from *target* back to *cell* (direction
    opposite).  We canonicalise so the source is always in 0..7:

      • target ≤ 7  →  (target, opposite(dname))          [already canonical]
      • target > 7  →  (15-target, dname)                  [mirror canonical]

    The second case is equivalent because moving the tile at (15-target) in
    direction *dname* (with its mirror at target moving opposite) has the same
    effect as moving the tile at *target* in direction opposite(dname).
    """
    cell, dname = move
    target = cell + _DIRS[dname]
    if target <= 7:
        return (target, _OPPOSITE[dname])
    return (15 - target, dname)


def _reconstruct(
    meeting: tuple[int, ...],
    fwd: dict[tuple[int, ...], tuple],
    bwd: dict[tuple[int, ...], tuple]
) -> tuple[list[list[int, str]], int]:
    """Build (move_list, length) for the full path  start → meeting → SOLVED.

    fwd[s] = (parent, move, depth) — forward BFS from start.
    bwd[s] = (parent, move, depth) — backward BFS from SOLVED; applying
      *move* to *parent* yields *s* (i.e. entries record forward-game moves
      that happen to move toward SOLVED).
    """
    fwd_moves = []
    s = meeting
    while fwd[s][0] is not None:
        parent, move, _ = fwd[s]
        fwd_moves.append(move)
        s = parent
    fwd_moves.reverse()

    bwd_moves = []
    s = meeting
    while bwd[s][0] is not None:
        parent, move, _ = bwd[s]
        bwd_moves.append(_reverse_move(move))
        s = parent

    all_moves = fwd_moves + bwd_moves
    return (all_moves, len(all_moves))


def solve(state: tuple[int, ...], node_cap: int = 400000) -> tuple[list, int] | None:
    """Find an optimal solution using bidirectional BFS.

    Expands layers alternately from *state* (forward) and from SOLVED
    (backward).  Each layer's size is bounded; we stop once we can prove no
    shorter path exists.

    Returns (move_list, optimal_move_count) on success.
    Returns None if the total node count exceeds *node_cap*.
    """
    if state == SOLVED:
        return ([], 0)

    fwd = {state: (None, None, 0)}
    bwd = {SOLVED: (None, None, 0)}
    fwd_q = deque([state])
    bwd_q = deque([SOLVED])

    nodes = 2
    best_cost = float('inf')
    best_meeting = None
    fwd_depth = 0
    bwd_depth = 0

    def _expand_layer(q, visited, other, next_depth) -> bool:
        nonlocal nodes, best_cost, best_meeting
        for _ in range(len(q)):
            if not q:
                return True
            s = q.popleft()
            for move, ns in neighbors(s):
                if ns not in visited:
                    visited[ns] = (s, move, next_depth)
                    q.append(ns)
                    nodes += 1
                    if nodes > node_cap:
                        return False
                if ns in other:
                    cost = next_depth + other[ns][2]
                    if cost < best_cost:
                        best_cost = cost
                        best_meeting = ns
        return True

    while fwd_q or bwd_q:
        if min(fwd_depth, bwd_depth) + 1 >= best_cost:
            break
        if fwd_q:
            fwd_depth += 1
            if not _expand_layer(fwd_q, fwd, bwd, fwd_depth):
                break
        if min(fwd_depth, bwd_depth) + 1 >= best_cost:
            break
        if bwd_q:
            bwd_depth += 1
            if not _expand_layer(bwd_q, bwd, fwd, bwd_depth):
                break

    if best_meeting is None:
        return None

    return _reconstruct(best_meeting, fwd, bwd)


def scramble(depth: int, seed: int) -> tuple[int, ...]:
    """Start from SOLVED and apply *depth* random legal moves.

    Never immediately undoes the previous move (avoids trivial back-and-forth).
    Returns the resulting board state (tuple of 16 ints).
    """
    rng = random.Random(seed)
    state = SOLVED
    prev = None
    for _ in range(depth):
        cands = [pair for pair in neighbors(state) if pair[1] != prev]
        if not cands:
            cands = list(neighbors(state))
        _, ns = rng.choice(cands)
        prev = state
        state = ns
    return state


def generate_levels(node_cap: int = 400000) -> list[dict]:
    """Build 8 levels with increasing difficulty (scramble depths 3-14)."""
    levels = []
    for idx, (name_sfx, hint, depth) in enumerate(_LEVEL_META):
        base_seed = 42 + idx * 997
        found = False
        for attempt in range(500):
            seed = base_seed + attempt * 13
            candidate = scramble(depth, seed)
            result = solve(candidate, node_cap=node_cap)
            if result is not None:
                moves, opt = result
                levels.append({
                    'idx': idx + 1,
                    'name': f"Level {idx + 1} - {name_sfx}",
                    'hint': hint,
                    'start': list(candidate),
                    'optimal': opt,
                    'solution': [[cell, dname] for cell, dname in moves],
                    'flag_easy': opt < 3
                })
                found = True
                break
        if not found:
            print(f"[WARNING] No solvable state found for level {idx + 1} (depth={depth}) after 500 attempts.")
    return levels


def write_levels_js(levels: list[dict], path: str) -> None:
    """Write the LEVELS constant to a JavaScript file."""
    lines = ['const LEVELS = [']
    last = len(levels) - 1
    for i, lv in enumerate(levels):
        comma = '' if i == last else ','
        start_s = json.dumps(lv['start'])
        sol_s = json.dumps(lv['solution'])
        lines += [
            '  {',
            f'    name: {json.dumps(lv["name"])},',
            f'    hint: {json.dumps(lv["hint"])},',
            f'    start: {start_s},',
            f'    optimal: {lv["optimal"]},',
            f'    solution: {sol_s}',
            f'  }{comma}'
        ]
    lines += ['];', '']
    text = '\n'.join(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Written {repr(path)}  ({len(levels)} levels, {len(text)} bytes)")


def print_summary(levels: list[dict]) -> None:
    """Print a formatted summary table to stdout."""
    depths = [d for _, _, d in _LEVEL_META]
    col_w = [4, 32, 9, 8, 0]
    sep = '  '
    print(f"{'#':<{col_w[0]}}{sep}{'Name':<{col_w[1]}}{sep}{'Scramble':>{col_w[2]}}{sep}{'Optimal':>{col_w[3]}}")
    print(f"{'-'*col_w[0]}{sep}{'-'*col_w[1]}{sep}{'-'*col_w[2]}{sep}{'-'*col_w[3]}")
    for lv, d in zip(levels, depths):
        print(f"{lv['idx']:<{col_w[0]}}{sep}{lv['name']:<{col_w[1]}}{sep}{d:>{col_w[2]}}{sep}{lv['optimal']:>{col_w[3]}}")


if __name__ == '__main__':
    levels = generate_levels()
    print_summary(levels)
    write_levels_js(levels, 'levels.js')
