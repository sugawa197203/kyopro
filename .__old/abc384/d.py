import sys

# debug = lambda *args: print(*args, file=sys.stderr)
# debug = lambda *args: None

N, S = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
# debug(sumA)
if sumA == S:
	print("Yes")
	sys.exit()

if sumA < S:
	S = S % sumA

if S == 0:
	print("Yes")
	sys.exit()

AA = A + A

length = AA[0]
# debug(AA, S, length)
if length == S:
	print("Yes")
	sys.exit()

lefti = 0
for righti in range(1, 2*N):
	length += AA[righti]
	# debug(f"1 righti: {righti}, lefti: {lefti}, length: {length}, S: {S}")
	if length == S:
		print("Yes")
		sys.exit()
	if length < S:
		continue
	while True:
		length -= AA[lefti]
		lefti += 1
		# debug(f"2 righti: {righti}, lefti: {lefti}, length: {length}, S: {S}")
		if length == S:
			print("Yes")
			sys.exit()
		if lefti < righti and length < S or lefti >= N:
			break

# debug(f"length: {length}, S: {S}")
if length == S:
	print("Yes")
else:
	print("No")
