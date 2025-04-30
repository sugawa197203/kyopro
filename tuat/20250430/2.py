H, W, N = map(int, input().split())
T = list(input())
Grid = [list(input().strip()) for _ in range(H)]
ans = 0

direct = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

for startX in range(H):
    sx = startX
    for startY in range(W):
        startX = sx
        if Grid[startX][startY] == '#':
              continue
        for t in T:
            dx, dy = direct[t]
            nextpos = (startX + dx, startY + dy)
            if nextpos[0] < 0 or nextpos[0] >= H or nextpos[1] < 0 or nextpos[1] >= W or Grid[nextpos[0]][nextpos[1]] == '#':
                break
            startX, startY = nextpos
        else:
            ans += 1

print(ans)
