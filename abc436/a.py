N = int(input())
S = input()

N = N - len(S)

if N <= 0:
	print(S)
else:
	print("o" * N + S)