N, K = map(int, input().split())
R = list(map(int, input().split()))

import sys
sys.setrecursionlimit(10**6)

def f(ans):
    sm = sum(ans)
    if sm == N:
        return
    
    if sm % K == 0:
        print(" ".join(map(str, ans)))
    for i in range(N-1, -1, -1):
        ans[i] += 1
        if ans[i] <= R[i]:
            break
        ans[i] = 1
    f(ans)

ans = [1] * N

f(ans)

