N = int(input())
S = [input() for _ in range(N)]
maxlen = max(map(len, S))
ans = []

for i in range(maxlen):
    ans.append([])

for i in range(N):
    for j in range(maxlen):
        if j < len(S[i]):
            ans[j].append(S[i][j])
        else:
            ans[j].append("*")

for _ans in ans:
    absstr = ""
    f = True
    for a in _ans:
        if f and a == "*":
            continue
        f = False
        absstr += a
    print(absstr[::-1])


