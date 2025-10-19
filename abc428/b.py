N, K = map(int, input().split())
S = input()

from collections import defaultdict

ans = defaultdict(int)

for i in range(N - K + 1):
    ans[S[i : i + K]] += 1

ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
size = ans[0][1]
print(size)

_ans = []
for k, v in ans:
    if v == size:
        _ans.append(k)

_ans.sort()

print(*_ans)

