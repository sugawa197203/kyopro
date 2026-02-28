S = input()
T = input()

si = 0
ti = 0

ans = 0

while si < len(S) and ti < len(T):
    if S[si] == T[ti]:
        si += 1
        ti += 1
        continue

    ans += 1
    if T[ti] == 'A':
        ti += 1
        continue

    if S[si] == 'A':
        si += 1
        continue

    ans = -1
    break

if ans != -1:
    if si < len(S):
        for i in range(si, len(S)):
            if S[i] != 'A':
                ans = -1
                break
        else:
            ans += len(S) - si
    if ti < len(T):
        for i in range(ti, len(T)):
            if T[i] != 'A':
                ans = -1
                break
        else:
            ans += len(T) - ti

print(ans)
