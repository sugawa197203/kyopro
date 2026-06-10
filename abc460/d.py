from collections import deque

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def sim(h, w, s, count=10):
    while count > 0:
        count -= 1
        print_grid(s)
        next_s = [list(row) for row in s]
        for i in range(h):
            for j in range(w):
                if s[i][j] == ".":
                    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == "#":
                            next_s[i][j] = "#"
                else:
                    next_s[i][j] = "."
        s = ["".join(row) for row in next_s]
    exit()

H, W = map(int, input().split())
S = [input() for _ in range(H)]

sim(H, W, S)

blacksim = deque()
blackdist = [[float('inf')] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            flag = False
            for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == ".":
                    flag = True
                    break
            if flag:
                blacksim.append((i, j, 0))
                blackdist[i][j] = 0
            continue


if not blacksim or len(blacksim) == H * W:
    for i in range(H):
        print("." * W)
    exit()

while blacksim:
    i, j, dist = blacksim.popleft()

    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if blackdist[ni][nj] > dist + 1:
                blacksim.append((ni, nj, dist + 1))
                blackdist[ni][nj] = dist + 1

for i in range(H):
    for j in range(W):
        print("#" if blackdist[i][j] % 2 == 0 else ".", end="")
        # print(blackdist[i][j], end="")

    print()
