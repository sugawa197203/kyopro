N = int(input())
slimes = dict()

for i in range(N):
	size, count = map(int, input().split())
	while count != 0:
		count, a = divmod(count, 2)
		slimes[size] = slimes.get(size, 0) + a
		size *= 2

for size, count in slimes.items():
	if count >= 2:
		while count != 0:
			count, a = divmod(count, 2)
			slimes[size] = slimes.get(size, 0) + a
			size *= 2

print(sum(slimes.values()))