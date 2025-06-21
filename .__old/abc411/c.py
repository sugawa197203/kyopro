N, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
x = [False] * N

for a in A:
	a -= 1
	x[a] = not x[a]
	if N == 1:
		if x[0]:
			ans += 1
		else:
			ans -= 1
	elif a == 0:
		if x[a]:
			if x[a+1]:
				pass
			else:
				ans += 1
		else:
			if x[a+1]:
				pass
			else:
				ans -= 1
	elif a == N-1:
		if x[a]:
			if x[a-1]:
				pass
			else:
				ans += 1
		else:
			if x[a-1]:
				pass
			else:
				ans -= 1
	elif x[a]:
		if x[a-1] and x[a+1]:
			ans -= 1
		elif x[a-1] or x[a+1]:
			pass
		else:
			ans += 1
	else:
		if x[a-1] and x[a+1]:
			ans += 1
		elif x[a-1] or x[a+1]:
			pass
		else:
			ans -= 1
	print(ans)
				
	
