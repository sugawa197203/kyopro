N, A, B = map(int, input().split())
while True:
	if N <= A:
		print("Ant")
		break
	N -= A
	if N <= B:
		print("Bug")
		break
	N -= B