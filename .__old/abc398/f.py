S = input()

if len(S) == 1:
	print(S)
	exit()

rS = S[::-1]

t = "#" + "#".join(rS) + "#"
n = len(t)
p = [0] * n
c = 0
r = 0
maxlen = 0
retval = []
for i in range(n):
	if i < r:
		p[i] = min(p[2 * c - i], r - i)
	else:
		p[i] = 1
	while i - p[i] >= 0 and i + p[i] < n and t[i - p[i]] == t[i + p[i]]:
		p[i] += 1
	if i + p[i] > r:
		r = i + p[i]
		c = i

	if maxlen <= p[i] - 1:
		maxlen = p[i] - 1
		if t[i] != "#":
			retval.append(t[i])
	else:
		break

if maxlen == 1:
	print(S + rS[1:])
	exit()

retval.append(t[i])

lenret = len(retval)
print(S[:lenret] + "".join(retval) + rS[len(S) - lenret:])
	
