N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

import bisect

A.sort(reverse=True)
B.sort(reverse=True)

Aruisekiwa = [0] * (N)
Bruisekiwa = [0] * (N)

Aruisekiwa[0] = A[0]
Bruisekiwa[0] = B[0]

for i in range(1, N):
	Aruisekiwa[i] = Aruisekiwa[i-1] + A[i]
	Bruisekiwa[i] = Bruisekiwa[i-1] + B[i]


Xind = bisect.bisect_right(Aruisekiwa, X)
Yind = bisect.bisect_right(Bruisekiwa, Y)

if Xind == N:
	None
else:
	Xind += 1
if Yind == N:
	None
else:
	Yind += 1


print(min(Xind, Yind))