from collections import deque

SIZE = 2000
N = int(input())
cloud = [tuple(map(int, input().split())) for _ in range(N)]

imos = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]
idimos = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]
counts = [0] * N
sum_cloud = 0

for i in range(N):
    c, d, a, b = cloud[i]
    a -= 1
    c -= 1
    imos[c][a] += 1
    imos[c][b] -= 1
    imos[d][a] -= 1
    imos[d][b] += 1
    idimos[c][a] += i
    idimos[c][b] -= i
    idimos[d][a] -= i
    idimos[d][b] += i
    
for y in range(SIZE):
    for x in range(1, SIZE):
        imos[y][x] += imos[y][x - 1]
        idimos[y][x] += idimos[y][x - 1]
        
for y in range(1, SIZE):
    for x in range(SIZE):
        imos[y][x] += imos[y - 1][x]
        idimos[y][x] += idimos[y - 1][x]
        
for y in range(SIZE):
    for x in range(SIZE):
        if imos[y][x] == 1:
            counts[idimos[y][x]] += 1
        if imos[y][x] >= 1:
            sum_cloud += 1

total = SIZE * SIZE
for i in range(N):
    print(total - (sum_cloud - counts[i]))
