N = int(input())
SA = []

for i in range(N):
	s, a = input().split(" ")
	a = int(a)
	
	SA.append((s, a))


ind = SA.index(min(SA, key=lambda x: x[1]))
for i in range(N): 
	print(SA[(i + ind) % N][0])
