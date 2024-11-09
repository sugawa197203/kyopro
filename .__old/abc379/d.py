import bisect
Q = int(input())
table = [float('inf')] * Q

for i in range(Q):
	query = list(map(int, input().split()))
