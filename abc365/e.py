N = int(input())
A = list(map(int, input().split()))
ans = 0

h = set()

for i in range(N - 1):
    for j in range(i + 1, N):
        a = 0
        h.add((i, j + 1))
        for k in range(i, j + 1):
            a ^= A[k]
        ans += a

print(ans)


b = []
ans = 0
print(h)

for i in range(2, N+1):
    for j in range(N-i+1):
        b.append([0] * (N-i+1))
        a = 0
        h.remove((j, j+i))
        for k in range(j, j+i):
            a ^= A[k]
        ans += a

print(ans)
print(h)

