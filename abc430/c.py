N, A, B = [int(x) for x in input().split()]
S = list(input())

ain = []
Bin = []
ans = 0

for r in range(1, N + 1):
    if S[r - 1] == 'a':
        ain.append(r)
    else:
        Bin.append(r)
    if len(ain) >= A:
        leftA = ain[-A]
    else:
        continue
    if len(Bin) >= B:
        leftB = Bin[-B]
    else:
        leftB = 0
    if leftA > leftB:
        ans += (leftA - leftB)

print(ans)