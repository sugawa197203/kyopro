R = int(input())
ans = 0
b = R
RR = R ** 2
for t in range(R-1):
	print(RR, t, b)
	while 4 * RR < (2 + 4*t) ** 2 + (4*b) ** 2:
		b -= 1
	ans += b
print(ans * 4 + 1)
