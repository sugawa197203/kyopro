import sys
debug = lambda *x: print(*x, file=sys.stderr)

N = int(input())
A = list(map(int, input().split()))

maxlength = 0

d = dict()

pos = 1

while True:
	if pos >= N:
		maxlength = max(maxlength, len(d)*2)
		break
	
	if A[pos] == A[pos-1]:
		if not A[pos] in d:
			d[A[pos]] = pos
			pos += 2
			continue
		
		maxlength = max(maxlength, len(d)*2)
		kv = list(d.items())
		_p = d[A[pos]]
		for k, v in kv:
			if d[k] <= _p:
				del d[k]
		d[A[pos]] = pos
		pos += 2
	else:
		maxlength = max(maxlength, len(d)*2)
		d = dict()
		if 3 <= pos and A[pos - 3] == A[pos - 2] == A[pos - 1]:
			d[A[pos-1]] = pos
			pos += 1
			continue

		pos += 1
		
print(maxlength)