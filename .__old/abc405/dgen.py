H, W = 1000, 1000
Grid = ['.' * W for _ in range(H-1)]
Grid.append('E' + '.' * (W - 1))

with open('d.txt', 'w') as f:
	f.write(f"{H} {W}\n")
	for row in Grid:
		f.write(row + '\n')


