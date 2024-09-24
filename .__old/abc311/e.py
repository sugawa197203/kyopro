import bisect

H, W, N = map(int, input().split(" "))

A, B = [], []
ana = dict()

for i in range(N):
	a, b = map(int, input().split(" "))
	A.append(a)
	B.append(b)
	ana[(a, b)] = True

A.sort()
B.sort()

count = 0

if H * W == N:
	print(0)
	exit()

maxsize = max(H, W)
minsize = min(H, W)

for size in range(1, maxsize):
	print(size)
	for h in range(1, H + 1):
		for w in range(1, W + 1):

			hidariueX = bisect.bisect_left(A, w)
			hidariueY = bisect.bisect_left(B, h)
			migishitaX = bisect.bisect_right(A, w + size - 1)
			migishitaY = bisect.bisect_right(B, h + size - 1)

			if hidariueX < migishitaX and hidariueY < migishitaY:
				if (hidariueX, hidariueY) in ana:
					continue
				if (migishitaX, migishitaY) in ana:
					continue
			
			count += 1

print(count)
		