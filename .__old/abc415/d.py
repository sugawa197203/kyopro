from collections import deque

N, M = map(int, input().split())
A, B = [0] * M, [0] * M
kouritsu = deque([])

for i in range(M):
	A[i], B[i] = map(int, input().split())
	if A[i] > N:
		continue
	kouritsu.append((A[i] - B[i], A[i]))

if len(kouritsu) == 0:
	print(0)
	exit()

kouritsu = deque(sorted(kouritsu, key=lambda x: x[0]))
ans = 0
_ans = 0
# print("kouritsu:", kouritsu)
while True:
	saikouritu = kouritsu[0]
	if len(kouritsu) == 1:
		ans += N // saikouritu[1]
		break
	
	count = (N - saikouritu[1]) // saikouritu[0] + 1
	_ans += saikouritu[0] * count
	ans += count
	print("Current saikouritu:", saikouritu, "Count:", count, "N:", N, "ans:", ans)
	N -= count * saikouritu[0]
	while len(kouritsu) > 0 and kouritsu[0][1] > N:
		kouritsu.popleft()
	
	if len(kouritsu) == 0 or kouritsu[0][0] > N:
		break


	if N <= 0:
		break
_ans += N
print(ans)