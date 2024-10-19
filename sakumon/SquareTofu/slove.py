a, b = map(int, input().split())
ans = 0

while b:
	q, r = divmod(a, b)
	ans += q
	a, b = b, r

print(ans)
