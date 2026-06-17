from collections import defaultdict
N = int(input())
A = []
for i in range(N):
    K, *a = map(int, input().split())
    A.append(a)

ans = defaultdict(list)

for i in range(N):
    for a in A[i]:
        ans[a].append(i + 1)

for i in range(1, N + 1):
    ans[i].sort()
    print(len(ans[i]), *ans[i])
