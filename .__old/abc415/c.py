def solve(N, S):
	badlist = set()
	# print("N:", N, "S:", S)
	for i in range(2**N):
		if S & (1 << i):
			badlist.add(i + 1)
	
	# print("Bad list:", badlist)
	l = [0]
	# print(l)
	watched = {0}
	for i in range(N):
		nextl = []
		for j in range(N):
			for k in range(len(l)):
				if l[k] & (1 << j):
					continue
				yakuhin = l[k] | (1 << j)
				# print("Checking:", yakuhin)
				if yakuhin not in badlist and yakuhin not in watched:
					nextl.append(yakuhin)
					watched.add(yakuhin)
		l = nextl
		# print(l)
	
	if len(l) == 0:
		print("No")
	else:
		print("Yes")
		


T = int(input())
for _ in range(T):
	N = int(input())
	S = input()
	S = ''.join(list(reversed(S)))
	S = int(S, base=2)
	solve(N, S)
