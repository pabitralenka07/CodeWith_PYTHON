"""
8-Puzzle Solver — A* (Manhattan Distance) vs BFS comparison
State: tuple of 9 ints, 0 = blank
Goal:  (1,2,3,4,5,6,7,8,0)
"""

import heapq
import random
import time
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL_POS = {val: (i // 3, i % 3) for i, val in enumerate(GOAL)}


def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = sum(
        1
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
        if tiles[i] > tiles[j]
    )
    return inversions % 2 == 0


def manhattan_distance(state):
    dist = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        goal_r, goal_c = GOAL_POS[val]
        cur_r, cur_c = i // 3, i % 3
        dist += abs(goal_r - cur_r) + abs(goal_c - cur_c)
    return dist


def neighbors(state):
    idx = state.index(0)
    r, c = idx // 3, idx % 3
    moves = []
    if r > 0:
        moves.append((-3, "Up"))
    if r < 2:
        moves.append((3, "Down"))
    if c > 0:
        moves.append((-1, "Left"))
    if c < 2:
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


def solve_astar(start):
    if start == GOAL:
        return [], 0

    open_heap = []
    counter = 0
    g_score = {start: 0}
    came_from = {}
    heapq.heappush(open_heap, (manhattan_distance(start), counter, start))
    closed = set()
    explored = 0

    while open_heap:
        f, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)
        explored += 1

        if current == GOAL:
            return reconstruct_path(came_from, current), explored

        for nbr, move in neighbors(current):
            tentative_g = g_score[current] + 1
            if nbr in closed:
                continue
            if tentative_g < g_score.get(nbr, float("inf")):
                g_score[nbr] = tentative_g
                came_from[nbr] = (current, move)
                counter += 1
                f_score = tentative_g + manhattan_distance(nbr)
                heapq.heappush(open_heap, (f_score, counter, nbr))

    return None, explored


def solve_bfs(start):
    if start == GOAL:
        return [], 0

    visited = {start}
    queue = deque([(start, [])])
    explored = 0

    while queue:
        current, path = queue.popleft()
        explored += 1

        if current == GOAL:
            return path, explored

        for nbr, move in neighbors(current):
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, path + [move]))

    return None, explored


def print_grid(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()


def random_solvable_state(shuffle_moves=25):
    state = GOAL
    prev = None
    for _ in range(shuffle_moves):
        opts = [ (n, m) for n, m in neighbors(state) if n != prev ]
        prev = state
        state = random.choice(opts)[0]
    return state


def read_state_from_input():
    print("Enter the 8-puzzle start state.")
    print("Use 0 for the blank tile. You can enter all 9 numbers at once")
    print("(space or comma separated), e.g.:  7 2 6 8 3 0 5 1 4")
    print("Or press Enter to type it row by row (3 numbers per row).\n")

    raw = input("All 9 values (or blank to enter row by row): ").strip()

    values = []
    if raw:
        values = [int(x) for x in raw.replace(",", " ").split()]
    else:
        for r in range(3):
            while True:
                row_raw = input(f"Row {r+1} (3 numbers, space separated): ").strip()
                row_vals = [int(x) for x in row_raw.replace(",", " ").split()]
                if len(row_vals) == 3:
                    values.extend(row_vals)
                    break
                print("  Need exactly 3 numbers, try again.")

    if len(values) != 9 or sorted(values) != list(range(9)):
        raise ValueError(f"Invalid state: must contain each of 0-8 exactly once. Got: {values}")

    return tuple(values)


if __name__ == "__main__":
    import sys

    if "--random" in sys.argv:
        random.seed(42)
        start = random_solvable_state(shuffle_moves=25)
    else:
        start = read_state_from_input()

    print("\nSTART STATE:")
    print_grid(start)
    solvable = is_solvable(start)
    print(f"Solvable: {solvable}\n")

    if not solvable:
        print("This state is UNSOLVABLE (odd inversion count). No solution exists.")
        print("Swap any two non-blank tiles to make it solvable, then try again.")
        sys.exit(0)

    t0 = time.perf_counter()
    path_astar, explored_astar = solve_astar(start)
    t_astar = time.perf_counter() - t0

    print("=== A* (Manhattan Distance) ===")
    print(f"Total steps to solve: {len(path_astar)}")
    print(f"States explored: {explored_astar}")
    print(f"Time: {t_astar*1000:.2f} ms")
    print(f"Move sequence: {path_astar}\n")

    print("--- Step-by-step ---")
    state = start
    print_grid(state)
    for i, move in enumerate(path_astar, 1):
        for nbr, m in neighbors(state):
            if m == move:
                state = nbr
                break
        print(f"Step {i}: move blank {move}")
        print_grid(state)

    t0 = time.perf_counter()
    path_bfs, explored_bfs = solve_bfs(start)
    t_bfs = time.perf_counter() - t0

    print("=== BFS (uninformed) ===")
    print(f"Total steps to solve: {len(path_bfs)}")
    print(f"States explored: {explored_bfs}")
    print(f"Time: {t_bfs*1000:.2f} ms\n")

    print("=== Comparison ===")
    print(f"Both find optimal path length: {len(path_astar)} == {len(path_bfs)} -> {len(path_astar) == len(path_bfs)}")
    print(f"A* explored {explored_astar} states vs BFS {explored_bfs} states "f"({explored_bfs / max(explored_astar,1):.1f}x more)")
    
    