N = int(input())
D = list(map(int, input().split()))

for i in range(N-1):
	ans = [D[i]]
	for j in range(i+1, N-1):
		ans.append(D[j] + ans[-1])
	
	print(*ans)
