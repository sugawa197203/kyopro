N = int(input())
B = [1]
for _ in range(N - 1):
    B.append(int(input()))

A = [1] * N

maxid = 22
watched = set()

while maxid > 0:
    if maxid not in B:
        maxid -= 1
        continue

    
    
    max_kyuryo = 0
    min_kyuryo = 10 ** 9
    for i, (a, b) in enumerate(zip(A, B)):
        if i == 0:
            continue
        if b == maxid:
            max_kyuryo = max(max_kyuryo, a)
            min_kyuryo = min(min_kyuryo, a)

    A[maxid - 1] = max_kyuryo + min_kyuryo + 1
    maxid -= 1

print(A[0])
