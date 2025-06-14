N, H, M = 3000, 3000, 3000
AB = [(1, 1)] * N
with open('input.txt', 'w') as f:
	f.write(f"{N} {H} {M}\n")
	for a, b in AB:
		f.write(f"{a} {b}\n")