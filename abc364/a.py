N = int(input())
before = ""
for i in range(N-1):
	S = input()
	if S == before and S == "sweet":
		print("No")

		exit()

	before = S

print("Yes")

