N, R = map(int, input().split())
L = list(map(int, input().split()))

ans = 0

left = 0

for i in range(N + 1):
    if i == R:
        left = i
        break
    if L[i] == 0:
        left = i
        break

right = N

for i in range(N):
    if N - i == R:
        right = i
        break
    if L[N - i - 1] == 0:
        right = i
        break

onecount = L[left:(N - right)].count(1)
# print(onecount, left, right)
ans = onecount + N - (right + left)

print(ans)