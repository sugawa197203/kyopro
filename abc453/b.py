T, X = map(int, input().split())
A = list(map(int, input().split()))

ans = [(0, A[0])]
val = A[0]

for i in range(1, T+1):
    if abs(val - A[i]) >= X:
        ans.append((i, A[i]))
        val = A[i]

for _ans in ans:
    print(*_ans)
