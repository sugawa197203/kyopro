N, A = map(int, input().split())
T = list(map(int, input().split()))
endtime = T[0] + A
print(endtime)
for i in range(1, N):
	if T[i] < endtime:
		endtime += A
	else:
		endtime = T[i] + A
	print(endtime)