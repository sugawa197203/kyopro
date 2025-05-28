N, M, H, K = map(int, input().split())
S = input()
xy = {}
for i in range(M):
    x, y = map(int, input().split())
    xy[(x, y)] = True

pos = (0, 0)


def direct(c: str):
    return {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}[c]


for s in S:
    d = direct(s)
    H -= 1
    if H < 0:
        print("No")
        exit()
    pos = (pos[0] + d[0], pos[1] + d[1])
    if pos in xy:
        H = max(H, K)

print("Yes")
