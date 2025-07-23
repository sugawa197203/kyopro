N, K, A = map(int, input().split())

A -= 1
for i in range(K):
    A += 1
    if A > N:
        A = 1

print(A)
