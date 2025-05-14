N, M, K = map(int, input().split())
A = []
R = []
for i in range(M):
    c, *ar = input().split()
    A.append(list(map(int, ar[:-1])))
    R.append(ar[-1])

flag = [0] * ((1 << N) + 1)
print(flag)
for a, r in zip(A, R):
    if r == "x":
        f = 0
        for _a in a:
            f |= 1 << _a
        print(f"{f=:b}")
        flag[f] = 1

print(flag.count(0))
