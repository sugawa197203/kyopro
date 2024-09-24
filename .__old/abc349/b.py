S = input()
d = dict()

t = [0] * 101

for c in S:
	if c not in d:
		d[c] = 1
	else:
		d[c] += 1

for k, v in d.items():
	t[v] += 1

for _t in t:
	if _t == 0 or _t == 2:
		continue
	print("No")
	exit()

print("Yes")