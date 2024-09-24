import bisect

simentai = []
kisusimentai = []

simentainum = 185

for i in range(1, simentainum):
	n = int(i * (i + 1) * (i + 2) / 6)
	simentai.append(n)
	if n % 2 == 1:
		kisusimentai.append(n)
	
while True:
	simentaicount = 0
	kisusimentaicount = 0
	N = int(input())
	if N == 0:
		break
	_N = N
	n = _N

	while True:
		index = bisect.bisect_right(simentai, _N) - 1
		print("DEBUG", index, _N, simentai[index])
		n = simentai[index]
		simentaicount += 1
		if n == _N:
			break
		_N -= n

	_N = N
	while True:
		index = bisect.bisect_right(kisusimentai, _N) - 1
		n = kisusimentai[index]
		kisusimentaicount += 1
		if n == _N:
			break
		_N -= n

	
	print(simentaicount, kisusimentaicount)
