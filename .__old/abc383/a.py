N = int(input())

tank = 0
time = 0

for _ in range(N):
	t, water = map(int, input().split())
	tank = max(0, tank - (t - time))
	tank += water
	time = t

print(tank)
