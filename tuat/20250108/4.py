N, M, Q = map(int, input().split())
WV = []
for i in range(N):
    w, v = map(int, input().split())
    WV.append((w, v))

WV.sort(key=lambda x: x[1], reverse=True)

X = list(map(int, input().split()))
import bisect
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    ans = 0
    box = X[:L] + X[R+1:]
    box.sort()
    for w, v in WV:
        idx = bisect.bisect_left(box, w)
        if idx < len(box):
            ans += v
            box.pop(idx)
    print(ans)
