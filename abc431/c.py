from sortedcontainers import SortedList

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

B = SortedList(B)
count = 0
for h in H:
    idx = B.bisect_left(h)
    if idx == len(B):
        continue

    count += 1
    B.pop(idx)

    if count == K:
        print("Yes")
        exit()

print("No")
