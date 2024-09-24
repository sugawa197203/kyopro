N = int(input())
A = list(map(int, input().split(" ")))

Af = [False] * N

resutl = []

for i in range(N):
	if Af[i]:
		continue

	Af[i] = True
	next = A[i]

	while True:
		next = A[next - 1]
		
		if Af[next - 1]:
			start = next
			resutl.append(start)
			while True:
				next = A[next - 1]
				if next == start:
					print(len(resutl))
					print(" ".join(map(str, resutl)))
					exit()
				resutl.append(next)
		
		Af[next - 1] = True


