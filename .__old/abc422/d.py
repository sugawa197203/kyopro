from fractions import Fraction

N, K = map(int, input().split())
_N = 2**N
k, _k = divmod(K, _N)

if _k == 0:
    print("0")
    print(*([k] * _N))
    exit()

if _k == 1:
    print("1")
    print(k + 1, end=" ")
    print(*([k] * (_N - 1)))
    exit()

d = Fraction(_N, _k)
ans = [k] * _N
i = Fraction(0, 1)
for _ in range(_k):
    ans[int(i)] += 1
    i += d

X = 0
ANS = ans
for i in range(N):
    _ans = [0] * (len(ans) // 2)
    X = max(X, max(ans) - min(ans))
    for j in range(0, len(ans), 2):
        _ans[j // 2] = ans[j] + ans[j + 1]
    ans = _ans

print(X)
print(*ANS)