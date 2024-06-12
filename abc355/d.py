import bisect

N = int(input())
L, R = [], []
for i in range(N):
	l, r = map(int, input().split())
	L.append(l)
	R.append(r)
keyL, KeyR = list(range(N)), list(range(N))

keyL.sort(key=lambda x: L[x])
KeyR.sort(key=lambda x: R[x])

ans = 0

for l, r in zip(L, R):
	idxLR = bisect.bisect_right(keyL, r, key=lambda x: L[x])
	idxRL = bisect.bisect_left(KeyR, l, key=lambda x: R[x])
	ans += N - (N - idxLR) - idxRL - 1

print(ans // 2)
