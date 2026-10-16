from collections import deque

TOTAL_M = 3
TOTAL_C = 3


def is_valid(m_left, c_left):
    m_right = TOTAL_M - m_left
    c_right = TOTAL_C - c_left

    if not (0 <= m_left <= TOTAL_M and 0 <= c_left <= TOTAL_C):
        return False

    if not (0 <= m_right <= TOTAL_M and 0 <= c_right <= TOTAL_C):
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True


def get_next_states(state):
    m_left, c_left, boat = state

    moves = [
        (1, 0),  # 1 Missionary
        (2, 0),  # 2 Missionaries
        (0, 1),  # 1 Cannibal
        (0, 2),  # 2 Cannibals
        (1, 1)   # 1 Missionary + 1 Cannibal
    ]

    next_states = []

    for m, c in moves:

        if boat == 0:   # Boat on Left
            new_m = m_left - m
            new_c = c_left - c
            new_boat = 1

        else:           # Boat on Right
            new_m = m_left + m
            new_c = c_left + c
            new_boat = 0

        if is_valid(new_m, new_c):
            next_states.append(
                ((new_m, new_c, new_boat), (m, c))
            )

    return next_states


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, []))

    visited = {start}

    while queue:

        state, path = queue.popleft()

        if state == goal:
            print_solution(path + [state])
            return

        for next_state, move in get_next_states(state):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [state])
                )

    print("No solution found.")


def print_solution(path):
    print("\n--- Solution ---")

    for i, state in enumerate(path):
        m_left, c_left, boat = state

        m_right = TOTAL_M - m_left
        c_right = TOTAL_C - c_left

        side = "Left" if boat == 0 else "Right"

        print(
            f"Step {i}: "
            f"Left(M={m_left}, C={c_left}) | "
            f"Right(M={m_right}, C={c_right}) | "
            f"Boat: {side}"
        )

solve()

