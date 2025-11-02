from collections import defaultdict
N, M = map(int, input().split())
Grid = [input() for _ in range(N)]

count = defaultdict(int)

for i in range(N - M + 1):
    for j in range(N - M + 1):
        subgrid = [g[j:j+M] for g in Grid[i:i+M]]
        count[tuple(subgrid)] += 1

print(len(count))
