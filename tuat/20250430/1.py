N = int(input())
A = list(map(int, input().split()))

called = set()

for i in range(1, N+1):
    if not i in called:
        called.add(A[i-1])
ans = set(range(1, N+1)) - called
print(len(ans))
print(*sorted(ans))

