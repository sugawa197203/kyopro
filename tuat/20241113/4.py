N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

ans = 0
maximum = 0
count = 0

for t in T:
    if count == 0:
        ans += 1
        maximum = t + K
        count += 1
    elif count < C and t <= maximum:
        count += 1
    else:
        ans += 1
        maximum = t + K
        count = 1

print(ans)