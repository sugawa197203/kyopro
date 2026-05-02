from collections import defaultdict

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

pattern = defaultdict(int)

for i in A:
    for j in B:
        for k in C:
            men = sorted([i, j, k])
            pattern[tuple(men)] += 1

print(pattern[(4, 5, 6)] / (6.0 * 6.0 *6.0))

