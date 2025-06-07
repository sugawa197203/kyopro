N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(101):
	count = 0
	for a in A:
		if a >= i:
			count += 1
	if count >= i:
		ans = i

print(ans)