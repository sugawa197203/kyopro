N = 3000

with open('in', 'w') as f:
	f.write(f'{N}\n')
	for i in range(N):
		f.write("#" * N + '\n')
