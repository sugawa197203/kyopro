from collections import Counter

S = input()
ignore = set()

c = dict(Counter(S)).items()
c = sorted(c, key=lambda x: x[1], reverse=True)
count = c[0][1]
for k, v in c:
    if v == count:
        ignore.add(k)
    else:
        break

ans = ""

for s in S:
    if s not in ignore:
        ans += s

print(ans)
