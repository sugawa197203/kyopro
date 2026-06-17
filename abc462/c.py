from bisect import bisect_left, bisect_right

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
XY.sort()

minY = N + 1
ans = 0
nowX = 0

for x, y in XY:
    if x != nowX:
        nowX = x
        if y < minY:
            minY = y
            ans += 1

print(ans)

