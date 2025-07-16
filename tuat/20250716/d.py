from math import gcd
N = int(input())
AB = set()

XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        dx = x2 - x1
        dy = y2 - y1
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        AB.add((dx, dy))

ans = set()

for x, y in AB:
    ans.add((x, y))
    ans.add((-x, -y))

print(len(ans))

