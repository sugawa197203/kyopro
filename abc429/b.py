N, M = map(int, input().split())

A = list(map(int, input().split()))

sA = sum(A)

for i in range(N):
    if sA - A[i] == M:
        print("Yes")
        exit()

print("No")