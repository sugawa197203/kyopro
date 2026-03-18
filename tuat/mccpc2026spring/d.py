N = int(input())
A = list(map(int, input().split()))

flags = [False] * (N + 1)

ans = 0

for a in A:
    if a != 0 and not flags[a]:
        flags[a] = True
        ans += 1

print(ans)
