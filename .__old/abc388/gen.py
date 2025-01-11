N = 5*10**5
# 2 step
A = list(range(1, 2*N+1, 2))
filename = "ein"
with open(filename, "w") as f:
	f.write(f"{N}\n")
	f.write(" ".join(map(str, A)))