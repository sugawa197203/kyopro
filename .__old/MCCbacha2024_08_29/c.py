N, D = map(int, input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

enables = [False] * N

D2 = D * D

distances = [[0] * N for _ in range(N)]

for i, (xi, yi) in enumerate(zip(X, Y)):
    for j, (xj, yj) in enumerate(zip(X, Y)):
        distances[i][j] = (xi - xj) ** 2 + (yi - yj) ** 2

stack = [0]

while stack:
    i = stack.pop()
    if enables[i]:
        continue
    enables[i] = True
    for j in range(N):
        if distances[i][j] <= D2:
            stack.append(j)

print(*["Yes" if enable else "No" for enable in enables], sep="\n")