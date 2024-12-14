with open("input4.txt", "w") as f:
	f.write("1000 1000 1000\n")
	f.write("H" * 1000 + "\n")
	for i in range(999):
		f.write("." * 1000 + "\n")
