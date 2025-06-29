N, M = map(int, input().split())
V = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    V[b-1] += 1

print(V.count(1))

