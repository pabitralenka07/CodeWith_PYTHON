"""
Generic N x N Sliding Puzzle Solver
State: tuple of N*N ints, 0 = blank
Goal:  (1, 2, ..., N*N-1, 0)

Algorithm: A* with Manhattan Distance + Linear Conflict heuristic (admissible, optimal).
BFS is included for N=3 only (comparison) — auto-skipped for N>=4 because the
state space explodes (4x4 alone has ~10 trillion states; BFS would never finish).
"""

import heapq
import random
import sys
import time
from collections import deque


def make_goal(n):
    return tuple(list(range(1, n * n)) + [0])


def goal_positions(n):
    goal = make_goal(n)
    return {val: (i // n, i % n) for i, val in enumerate(goal)}


def is_solvable(state, n):
    """
    Generalized solvability check.
    - Odd width (n odd): solvable iff inversion count is EVEN.
    - Even width (n even): solvable iff
        (inversions + row_of_blank_counted_from_bottom) is ODD.
    """
    tiles = [t for t in state if t != 0]
    inversions = sum(
        1
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
        if tiles[i] > tiles[j]
    )

    if n % 2 == 1:
        return inversions % 2 == 0

    blank_idx = state.index(0)
    blank_row_from_top = blank_idx // n
    blank_row_from_bottom = n - blank_row_from_top  # 1-indexed from bottom
    return (inversions + blank_row_from_bottom) % 2 == 1


def manhattan_distance(state, n, goal_pos):
    dist = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        gr, gc = goal_pos[val]
        cr, cc = i // n, i % n
        dist += abs(gr - cr) + abs(gc - cc)
    return dist


def linear_conflict(state, n, goal_pos):
    """
    Linear conflict adds 2 moves for every pair of tiles that are in their
    goal row (or column) but reversed relative to each other -- they must
    step out of the line to let each other pass, costing 2 extra moves
    beyond what Manhattan distance alone predicts.
    This stays admissible and tightens the heuristic considerably, which
    matters a lot once N >= 4.
    """
    conflict = 0
    grid = [state[i * n:(i + 1) * n] for i in range(n)]

    # row conflicts
    for r in range(n):
        row_tiles = []
        for c in range(n):
            val = grid[r][c]
            if val != 0 and goal_pos[val][0] == r:
                row_tiles.append((c, goal_pos[val][1]))
        for i in range(len(row_tiles)):
            for j in range(i + 1, len(row_tiles)):
                c1, g1 = row_tiles[i]
                c2, g2 = row_tiles[j]
                if g1 > g2:
                    conflict += 1

    # column conflicts
    for c in range(n):
        col_tiles = []
        for r in range(n):
            val = grid[r][c]
            if val != 0 and goal_pos[val][1] == c:
                col_tiles.append((r, goal_pos[val][0]))
        for i in range(len(col_tiles)):
            for j in range(i + 1, len(col_tiles)):
                r1, g1 = col_tiles[i]
                r2, g2 = col_tiles[j]
                if g1 > g2:
                    conflict += 1

    return conflict * 2


def heuristic(state, n, goal_pos):
    return manhattan_distance(state, n, goal_pos) + linear_conflict(state, n, goal_pos)


def neighbors(state, n):
    idx = state.index(0)
    r, c = idx // n, idx % n
    moves = []
    if r > 0:
        moves.append((-n, "Up"))
    if r < n - 1:
        moves.append((n, "Down"))
    if c > 0:
        moves.append((-1, "Left"))
    if c < n - 1:
        moves.append((1, "Right"))

    for delta, label in moves:
        new_idx = idx + delta
        new_state = list(state)
        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
        yield tuple(new_state), label


def reconstruct_path(came_from, state):
    path = []
    while state in came_from:
        state, move = came_from[state]
        path.append(move)
    path.reverse()
    return path


def solve_astar(start, n, goal, goal_pos, node_limit=8_000_000):
    """A* with Manhattan + Linear Conflict. node_limit guards against runaway
    memory/time on large N — returns (None, explored) if exceeded."""
    if start == goal:
        return [], 0

    open_heap = []
    counter = 0
    g_score = {start: 0}
    came_from = {}
    heapq.heappush(open_heap, (heuristic(start, n, goal_pos), counter, start))
    closed = set()
    explored = 0

    while open_heap:
        if explored > node_limit:
            return None, explored  # bailed out — too large for this approach

        f, _, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        closed.add(current)
        explored += 1

        if current == goal:
            return reconstruct_path(came_from, current), explored

        for nbr, move in neighbors(current, n):
            if nbr in closed:
                continue
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(nbr, float("inf")):
                g_score[nbr] = tentative_g
                came_from[nbr] = (current, move)
                counter += 1
                fs = tentative_g + heuristic(nbr, n, goal_pos)
                heapq.heappush(open_heap, (fs, counter, nbr))

    return None, explored


def solve_bfs(start, n, goal, node_limit=500_000):
    """Uninformed BFS -- only practical for n == 3. Guarded with a node_limit
    so it can't hang indefinitely on larger boards."""
    if start == goal:
        return [], 0

    visited = {start}
    queue = deque([(start, [])])
    explored = 0

    while queue:
        if explored > node_limit:
            return None, explored
        current, path = queue.popleft()
        explored += 1

        if current == goal:
            return path, explored

        for nbr, move in neighbors(current, n):
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path + [move]))

    return None, explored


def print_grid(state, n):
    width = len(str(n * n - 1))
    for r in range(n):
        row = state[r * n:(r + 1) * n]
        print(" ".join(str(x).rjust(width) if x != 0 else "_".rjust(width) for x in row))
    print()


def random_solvable_state(n, shuffle_moves=None):
    goal = make_goal(n)
    if shuffle_moves is None:
        shuffle_moves = n * n * 8  # scale shuffle depth with board size
    state = goal
    prev = None
    for _ in range(shuffle_moves):
        opts = [(s, m) for s, m in neighbors(state, n) if s != prev]
        prev = state
        state = random.choice(opts)[0]
    return state


def read_state_from_input(n):
    total = n * n
    print(f"Enter the {n}x{n} puzzle start state ({total} numbers, 0 = blank).")
    print(f"Enter all {total} values at once (space/comma separated),")
    print(f"or press Enter to type it row by row ({n} numbers per row).\n")

    raw = input(f"All {total} values (or blank for row by row): ").strip()

    values = []
    if raw:
        values = [int(x) for x in raw.replace(",", " ").split()]
    else:
        for r in range(n):
            while True:
                row_raw = input(f"Row {r+1} ({n} numbers, space separated): ").strip()
                row_vals = [int(x) for x in row_raw.replace(",", " ").split()]
                if len(row_vals) == n:
                    values.extend(row_vals)
                    break
                print(f"  Need exactly {n} numbers, try again.")

    if len(values) != total or sorted(values) != list(range(total)):
        raise ValueError(f"Invalid state for {n}x{n}: must contain each of 0-{total-1} exactly once. Got: {values}")

    return tuple(values)


def read_size():
    raw = input("Board size N (e.g. 3 for 8-puzzle, 4 for 15-puzzle): ").strip()
    n = int(raw)
    if n < 2:
        raise ValueError("N must be >= 2")
    return n


if __name__ == "__main__":
    if "--random" in sys.argv:
        random.seed(42)
        n = int(sys.argv[sys.argv.index("--random") + 1]) if len(sys.argv) > sys.argv.index("--random") + 1 and sys.argv[sys.argv.index("--random") + 1].isdigit() else 3
        start = random_solvable_state(n)
    else:
        n = read_size()
        start = read_state_from_input(n)

    goal = make_goal(n)
    goal_pos = goal_positions(n)

    print(f"\n{n}x{n} — START STATE:")
    print_grid(start, n)
    solvable = is_solvable(start, n)
    print(f"Solvable: {solvable}\n")

    if not solvable:
        print("This state is UNSOLVABLE. Swap any two non-blank tiles to fix parity, then retry.")
        sys.exit(0)

    if n >= 5:
        print(f"NOTE: n={n} has an astronomically large state space. Plain A* with")
        print("Manhattan + Linear Conflict may take a long time or fail to finish on")
        print("hard instances — this is genuinely research territory (needs pattern")
        print("database heuristics / IDA*). Proceeding anyway with a node cap...\n")

    # --- A* ---
    t0 = time.perf_counter()
    path_astar, explored_astar = solve_astar(start, n, goal, goal_pos)
    t_astar = time.perf_counter() - t0

    print(f"=== A* (Manhattan + Linear Conflict), N={n} ===")
    if path_astar is None:
        print(f"Did not finish within node limit ({explored_astar} states explored).")
        print("Try a smaller shuffle depth, or n<=4 for reliable results.")
        sys.exit(0)

    print(f"Total steps to solve: {len(path_astar)}")
    print(f"States explored: {explored_astar}")
    print(f"Time: {t_astar*1000:.2f} ms")
    print(f"Move sequence: {path_astar}\n")

    print("--- Step-by-step ---")
    state = start
    print_grid(state, n)
    for i, move in enumerate(path_astar, 1):
        for nbr, m in neighbors(state, n):
            if m == move:
                state = nbr
                break
        print(f"Step {i}: move blank {move}")
        print_grid(state, n)

    # --- BFS comparison: only meaningful/feasible for n == 3 ---
    if n == 3:
        t0 = time.perf_counter()
        path_bfs, explored_bfs = solve_bfs(start, n, goal)
        t_bfs = time.perf_counter() - t0

        print("=== BFS (uninformed), N=3 ===")
        if path_bfs is None:
            print(f"BFS exceeded node limit ({explored_bfs} states).")
        else:
            print(f"Total steps to solve: {len(path_bfs)}")
            print(f"States explored: {explored_bfs}")
            print(f"Time: {t_bfs*1000:.2f} ms\n")
            print("=== Comparison ===")
            print(f"Optimal path length matches: {len(path_astar) == len(path_bfs)}")
            print(f"A* explored {explored_astar} states vs BFS {explored_bfs} "
                  f"({explored_bfs / max(explored_astar,1):.1f}x more)")
    else:
        print(f"(BFS skipped for N={n} — state space too large to be feasible;")
        print(f" A* with Manhattan+Linear Conflict is the practical approach.)")
        