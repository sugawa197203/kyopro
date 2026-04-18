
T = int(input())

direct = {
    (0, 1): 'R',
    (0, -1): 'L',
    (1, 0): 'U',
    (-1, 0): 'D'
}

def neighbor(n:int, pos: tuple[int, int], watched: set[tuple[int, int]]) -> dict[str, tuple[int, int]]:
    neighbors = {}
    for (dx, dy), direction in direct.items():
        new_pos = (pos[0] + dx, pos[1] + dy)
        if (new_pos not in watched) and (0 <= new_pos[0] < n and 0 <= new_pos[1] < n):
            neighbors[direction] = new_pos
    return neighbors


def solve(N:int, A:int, B:int) -> tuple[bool, str]:
    if N % 2 == 1:
        return (False, "")
    if A == 1 and B == N - 1:
        return (False, "")
    if A == 2 and B == N:
        return (False, "")
    if A == N - 1 and B == 1:
        return (False, "")
    if A == N and B == 1:
        return (False, "")

    watched = set()
    now = (0, 0)
    watched.add((A - 1, B - 1))
    result = ""

    neighbors = neighbor(N, now, watched)
    if 'R' in neighbors:
        result += 'R'
        now = neighbors['R']
    elif 'D' in neighbors:
        result += 'D'
        now = neighbors['D']
    else:
        assert(-1)
    
    neighbors = neighbor(N, now, watched)
    if 'R' in neighbors:
        result += 'R'
        now = neighbors['R']
    elif 'D' in neighbors:
        result += 'D'
        now = neighbors['D']
    else:
        assert(-1)

    for i in range(N**2 - 4):
        neighbors = neighbor(N, now, watched)
        if result[-1] in "RL":
            if result[-1] in neighbors:
                result += result[-1]
                now = neighbors[result[-1]]
            elif 'U' in neighbors:
                result += 'U'
                now = neighbors['U']
            elif 'D' in neighbors:
                result += 'D'
                now = neighbors['D']
            else:
                assert(-1)
        elif result[-1] == 'U':
            if result[-2] == 'D':
                assert(-1)
            if result[-2] in neighbors:
                result += result[-2]
                now = neighbors[result[-2]]
            elif 'R' if result[-2] == 'L' else 'L' in neighbors:
                result += 'R' if result[-2] == 'L' else 'L'
                now = neighbors['R' if result[-2] == 'L' else 'L']
            else:
                assert(-1)





for _ in range(T):
    N, A, B = map(int, input().split())
    possible, result = solve(N, A, B)
    if possible:
        print("Yes")
        print(result)
    else:
        print("No")
