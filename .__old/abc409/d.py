T = int(input())

for _ in range(T):
	N = int(input())
	S = list(input())
	oriS = "".join(S)

	if N == 1:
		print(*S)
		continue

	if N == 2:
		S.sort()
		print("".join(S))
		continue


	# _ans = []
	# l, r = 0, 1
	# while l < N:
	# 	f = S[:l] if l != 0 else []
	# 	p = S[l]
	# 	c = S[l + 1:r]
	# 	b = S[r:]
	# 	# print(f"{f=} {p=} {c=} {b=} {l=} {r=}")
	# 	ans = "".join(f) + "".join(c) + p + "".join(b)
	# 	_ans.append("".join(ans))
	# 	if r != N:
	# 		r += 1
	# 		continue
	# 	l += 1
	# 	r = l+1

	# _ans = sorted(_ans)[0]
	# print(">>>", _ans)

	l, r = 0, 0

	for i in range(N - 1):
		if S[i] > S[i + 1]:
			l = i
			break
	else:
		print("".join(S))
		continue

	ls = S[l]

	for i in range(l + 1, N - 1):
		if ls < S[i + 1]:
			r = i + 1
			break
	else:
		r = N
	
	front = "".join(S[:l])
	pop = S[l]
	center = "".join(S[l+1:r])
	back = "".join(S[r:])
	ans = front + center + pop + back
	print(ans)
	# if ans != _ans:
	# 	print("WRONG ANSWER")
	# 	print("Expected:", _ans)
	# 	print("Got:", ans)
	# 	print("Input:", oriS)
	# 	exit(1)

