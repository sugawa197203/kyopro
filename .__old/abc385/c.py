N = int(input())
H = list(map(int, input().split()))
import collections

ans = 1

for length in range(1, N+1):
	table = [1] * N
	for left in range(N-length):
		#print(left, length)
		if H[left] == H[left+length]:
			#print(f"{left} {left+length} same")
			table[left+length] = 1 + table[left]
	
	ans = max(ans, max(table))

print(ans)