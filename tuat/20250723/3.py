from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

ac = sorted(dict(Counter(A)).items(), key=lambda x: x[1])

count = len(ac) - K
if count < 0:
    print(0)
    exit()

ans = 0
for i in range(count):
    ans += ac[i][1]
print(ans)
