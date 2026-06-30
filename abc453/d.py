from collections import deque
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dtype = [UP, DOWN, LEFT, RIGHT]

outputWatched = [[[False] * 4 for _ in range(W)] for _ in range(H)]

q = deque()
start = None

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            start = (i, j)
            break
    if start is not None:
        break

class Memo:
    def __init__(self, dist:str, parent=None):
        self.parent = parent
        self.dist = dist

start_memo = Memo(dist="")

def dist_str(d):
    if d == UP:
        return 'U'
    elif d == DOWN:
        return 'D'
    elif d == LEFT:
        return 'L'
    elif d == RIGHT:
        return 'R'

for d in dtype:
    outputWatched[start[0]][start[1]][d] = True
    next_pos = (start[0] + directions[d][0], start[1] + directions[d][1])
    if 0 <= next_pos[0] < H and 0 <= next_pos[1] < W and S[next_pos[0]][next_pos[1]] != '#':
        m = Memo(dist=dist_str(d), parent=start_memo)
        q.append((next_pos[0], next_pos[1], d, m))

while q:
    x, y, d, memo = q.popleft()

    tile = S[x][y]
    if tile == '#':
        continue
    elif tile == '.':
        for nd in dtype:
            if not outputWatched[x][y][nd]:
                outputWatched[x][y][nd] = True
                next_pos = (x + directions[nd][0], y + directions[nd][1])
                if next_pos != (x, y) and 0 <= next_pos[0] < H and 0 <= next_pos[1] < W and S[next_pos[0]][next_pos[1]] != '#':
                    m = Memo(dist=dist_str(nd), parent=memo)
                    q.append((next_pos[0], next_pos[1], nd, m))
    elif tile == 'o':
        if not outputWatched[x][y][d]:
            outputWatched[x][y][d] = True
            next_pos = (x + directions[d][0], y + directions[d][1])
            if 0 <= next_pos[0] < H and 0 <= next_pos[1] < W and S[next_pos[0]][next_pos[1]] != '#':
                m = Memo(dist=dist_str(d), parent=memo)
                q.append((next_pos[0], next_pos[1], d, m))
    elif tile == 'x':
        for nd in dtype:
            if d != nd and not outputWatched[x][y][nd]:
                outputWatched[x][y][nd] = True
                next_pos = (x + directions[nd][0], y + directions[nd][1])
                if next_pos != (x, y) and 0 <= next_pos[0] < H and 0 <= next_pos[1] < W and S[next_pos[0]][next_pos[1]] != '#':
                    m = Memo(dist=dist_str(nd), parent=memo)
                    q.append((next_pos[0], next_pos[1], nd, m))
    elif tile == 'G':
        print("Yes")
        route = []
        while memo.parent is not None:
            route.append(memo.dist)
            memo = memo.parent
        print("".join(reversed(route)))
        exit()

print("No")
