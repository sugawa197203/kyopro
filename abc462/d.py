N, D = map(int, input().split())
S = []
for i in range(N):
    s, t = map(int, input().split())
    if s <= t - D + 1:
        S.append((s, True))
        S.append((t - D + 1, False))

S.sort(key=lambda x: x[0])

ablecount = 0

def nC2(n):
    return n * (n - 1) // 2

ans = 0
last = 0
for s, addorremove in S:
    
    if ablecount >= 2:
        # print(f"{s=}, {ablecount=}, {last=}")
        ans += nC2(ablecount) * (s - last)
    if addorremove:
        ablecount += 1
    else:
        ablecount -= 1
    last = s

print(ans)
