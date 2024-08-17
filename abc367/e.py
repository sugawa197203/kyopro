N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

visited = {}
history = []

for i in range(K):
    if visited.get(tuple(A)) is not None:
        loop_start = visited[tuple(A)]
        loop_length = i - loop_start
        remaining = (K - loop_start) % loop_length
        A = history[loop_start + remaining]
        print(" ".join(map(str, A)))
        exit()
    visited[tuple(A)] = i
    history.append(A.copy())
    
    B = [0] * N
    for j in range(N):
        B[j] = A[X[j] - 1]
    A = B

print(" ".join(map(str, A)))