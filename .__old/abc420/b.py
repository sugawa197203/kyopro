N, M = map(int, input().split())

S = [input().strip() for _ in range(N)]

ans = [0] * N

for i in range(M):
    tohyo = [S[j][i] for j in range(N)]
    zero, one = tohyo.count("0"), tohyo.count("1")
    if zero < one:
        for j in range(N):
            if S[j][i] == "0":
                ans[j] += 1
    elif one < zero:
        for j in range(N):
            if S[j][i] == "1":
                ans[j] += 1

max_score = max(ans)

_asn = [i + 1 for i in range(N) if ans[i] == max_score]

print(*_asn)
