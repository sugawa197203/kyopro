from sortedcontainers import SortedList

def get_near(A:SortedList[int], x:int) -> int:
	idx = A.bisect_left(x)
	if idx == len(A) or idx == 0:
		return A[0]
	else:
		return min(A[idx], A[idx-1], key=lambda y: abs(y - x))

def main(A:list[int], B:list[int], M:int):
    A = SortedList(A)
    total = 0
    for b in B:
        target = M - b
        idx = A.bisect_left(target)
        if idx == len(A):
            a = A[0]
        else:
            a = A[idx]
        total += (a + b) % M
        A.discard(a)
    print(total)

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	main(A, B, M)
