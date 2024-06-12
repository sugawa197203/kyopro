with open("in.txt", "w") as f:
	f.write(f"{3*10**5}\n")
	for i in range(3*10**5):
		f.write(f"{10**8} ")