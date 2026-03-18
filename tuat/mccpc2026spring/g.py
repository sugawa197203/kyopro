N, K = map(int, input().split())

if N <= 3:
    print(0)
    exit()

S = input()

from collections import Counter

counter = Counter(S)

yogan = 0
maxyogan = 0
if S[1] == '.':
    yogan += 1

for i, s in enumerate(S[2:], start=2):
    if K <= i:
        if S[i - K] == '.':
            yogan -= 1
    if s == '.':
        yogan += 1
    maxyogan = max(maxyogan, yogan)

print(counter['.'] - maxyogan)
