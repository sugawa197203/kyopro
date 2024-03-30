S = input()

ls = list(S)

s = set()

for l in ls:
	s.add(l)

for _s in s:
	if ls.count(_s) == 1:
		index = ls.index(_s)
		print(index + 1)
		exit()
