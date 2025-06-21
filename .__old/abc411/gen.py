N, Q = 5000, 5000*3
from random import randint
with open("./input.txt", "w") as f:
	f.write(f"{N} {Q}\n")
	for i in range(N):
		f.write(f"2 {i+1} a\n")
	for i in range(2*N):
		if i % 2 == 0:
			f.write(f"1 {randint(1, N)}\n")
		else:
			f.write(f"3 {randint(1, N)}\n")


