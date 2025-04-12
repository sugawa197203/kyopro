N, K = map(int, input().split())
S = list(input())
if N == 1:
	print("".join(S))
	exit()

if K == 0:
	print("." * N)
	exit()

ocount = 0
for i in range(N):
	if S[i] == "o":
		ocount += 1

if ocount >= K:
	for i in range(N):
		if S[i] == "?":
			S[i] = "."
	
	print("".join(S))
	exit()

if S[0] == "o":
	S[1] = "."

if S[N - 1] == "o":
	S[N - 2] = "."

for i in range(1, N - 2):
	if S[i] == "o":
		S[i - 1] = "."
		S[i + 1] = "."

_S = S.copy()

left, right = 0, 0
f = True
while f:
	while S[left] != "?":
		left += 1
		if left == N:
			f = False
			break
	if not f:
		break

	right = left
	while S[right] == "?":
		right += 1
		if right == N:
			f = False
			break

	if (right - left) % 2 == 1:
		if left == 0:
			l = "?"
		else:
			l = S[left - 1]
		if right == N:
			r = "?"
		else:
			r = S[right]
		
		if (l in "o" and r in "o"):
			S[left] = "."
			for i in range(left, right):
				S[i] = "o" if S[i - 1] == "." else "."
		elif (l in "." and r in "."):
			S[left] = "o"
			for i in range(left, right):
				S[i] = "." if S[i - 1] == "o" else "o"
	elif (right - left) % 2 == 0:
		if left == 0:
			l = "?"
		else:
			l = S[left - 1]
		if right == N:
			r = "?"
		else:
			r = S[right]
		
		if (l in "o" and r in "."):
			S[left] = "."
			for i in range(left, right):
				S[i] = "o" if S[i - 1] == "." else "."
		elif (l in "." and r in "o"):
			S[left] = "o"
			for i in range(left, right):
				S[i] = "." if S[i - 1] == "o" else "o"

# print("".join(S))
# print("".join(_S))

for i in range(1, N):
	# print("".join(S))
	if S[i - 1] == ".":
		if S[i] == "o":
			pass
		elif S[i] == "?":
			if i < N - 1 and S[i + 1] == ".":
				S[i] = "o"
			elif i < N - 2 and S[i + 1] == "?" and S[i + 2] == "o":
				S[i] = "o"
				S[i + 1] = "."
		elif S[i] == ".":
			pass
	elif S[i - 1] == "o":
		if S[i] == "o":
			raise ValueError("???????")
		elif S[i] == "?":
			S[i] = "."
		elif S[i] == ".":
			pass
	elif S[i - 1] == "?":
		if S[i] == "o":
			S[i - 1] = "."
			if i < N - 1 and S[i + 1] == "o":
				raise ValueError("???????")
			elif i < N - 1 and S[i + 1] == "?":
				S[i + 1] = "."
			elif S[i] == ".":
				pass
		elif S[i] == "?":
			pass
		elif S[i] == ".":
			pass

if S[N - 1] == "?":
	if S[N - 2] == ".":
		S[N - 1] = "o"
	elif S[N - 2] == "o":
		S[N - 1] = "."
	elif S[N - 2] == "?":
		if N > 2 and S[N - 3] == "o":
			S[N - 1] = "o"
			S[N - 2] = "."
ocount = 0
for i in range(N):
	if S[i] == "o":
		ocount += 1

if ocount > K:
	print("".join(_S))
else:
	print("".join(S))