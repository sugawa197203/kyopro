N, M = map(int, input().split())
S = input()
T = input()

ans = 10**9

for i in range(N - M + 1):
    cnt = 0
    
    for j, t in enumerate(T):
        diff = ord(S[i + j]) - ord(t)
        if diff < 0:
            diff += 10
        cnt += diff
    ans = min(ans, cnt)
print(ans)