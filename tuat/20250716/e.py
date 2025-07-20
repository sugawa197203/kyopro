from sortedcontainers import SortedList
N, K = map(int, input().split())


ans = SortedList(key=lambda x: x[0])

for i in range(N):
    a, b = map(int, input().split())
    ans.add((a, b))

k = 0
for i in range(N):
    a, b = ans[i]
    k += b
    if k >= K:
        print(ans[i][0])
        break
