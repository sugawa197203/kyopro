from collections import deque
H, W = map(int, input().split())
S = [input() for _ in range(H)]

direct = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

start = ()
goal = ()

def is_inside(x, y):
    return 0 <= x < H and 0 <= y < W

def is_valid(x, y):
    return is_inside(x, y) and S[x][y] != '#'

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            start = (i, j)
        elif S[i][j] == 'G':
            goal = (i, j)

visited = {} # key (x, y, 出てく方向) value (来た方向) start は None

q = deque() # (x, y, 来た方向, 距離)

for from_d, (dx, dy) in direct.items():
    _next = (start[0] + dx, start[1] + dy)
    visited[(*start, from_d)] = None
    if is_valid(*_next):
        q.append((*_next, from_d, 1))
        before = (start[0] - dx, start[1] - dy)
        visited[(*before, from_d)] = None

print(visited)
# print(q)

while q:
    print(visited)
    print(q)
    input()
    x, y, from_d, dist = q.popleft()
    if S[x][y] == "G":
        print("Yes")
        route = []
        # print(visited)
        # print((x, y, from_d))
        _dx, _dy = direct[from_d]
        x, y = (x - _dx, y - _dy)
        while (x, y, from_d) in visited:
            route.append(from_d)
            from_d = visited[(x, y, from_d)]
            if from_d is None:
                break
            dx, dy = direct[from_d]
            x -= dx
            y -= dy
        route.reverse()
        # print(dist)
        print(*route, sep="")
        exit()
    
    if S[x][y] == "#":
        continue
    elif S[x][y] == ".":
        for to_d, (dx, dy) in direct.items():
            _next = (x + dx, y + dy)
            if is_valid(*_next) and (x, y, to_d) not in visited:
                if dist + 1 > 5000000:
                    continue
                if (*_next, to_d) in visited:
                    continue
                q.append((*_next, to_d, dist + 1))
                visited[(x, y, to_d)] = from_d
    elif S[x][y] == "o":
        dx, dy = direct[from_d]
        to_d = from_d
        _next = (x + dx, y + dy)
        if is_valid(*_next) and (x, y, to_d) not in visited:
            if dist + 1 > 5000000:
                continue
            if (*_next, to_d) in visited:
                continue
            q.append((*_next, to_d, dist + 1))
            visited[(x, y, to_d)] = from_d
    elif S[x][y] == "x":
        for to_d, (dx, dy) in direct.items():
            if to_d == from_d:
                continue
            _next = (x + dx, y + dy)
            if is_valid(*_next) and (x, y, to_d) not in visited:
                if dist + 1 > 5000000:
                    continue
                if (*_next, to_d) in visited:
                    continue
                q.append((*_next, to_d, dist + 1))
                visited[(x, y, to_d)] = from_d

print("No")
