N, M = map(int, input().split())
notingR, notingC = set(), set()
RC = [tuple(map(int, input().split())) for _ in range(M)]
RC.reverse()

ans = 0
for r, c in RC:
    if r not in notingR and c not in notingC:
        ans += 1
    notingR.add(r)
    notingC.add(c)

print(ans)
