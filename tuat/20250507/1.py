from itertools import permutations
N = int(input())
pos = []
for i in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

ans = 0
cnt = 0
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for route in permutations(range(N)):
    d = 0
    for i in range(N - 1):
        d += distance(pos[route[i]][0], pos[route[i]][1], pos[route[i + 1]][0], pos[route[i + 1]][1])
    ans += d
    cnt += 1

print(ans / cnt)
