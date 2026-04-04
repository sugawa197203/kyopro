S = input()
T = input()
N = len(S)
M = len(T)
ans = int((N * (N + 1)) // 2)
left, right = 0, 0
lastleft = -1
r = 0
print(f"{ans=}, {N=}")
for left in range(N - M):
    if right - left < M:
        r = 0
        for _right in range(right, N):
            if S[_right] == T[r]:
                r += 1
            if r == M:
                right = _right
                break
    ans -= (N - right)
    print(f"{left=}, {r=}, {right=}")

print(ans)
