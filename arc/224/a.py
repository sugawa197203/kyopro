def solve(K) -> int:

    k = int(K)
    _k = k
    while "00" not in K:
        k += _k
        K = str(k)

    return k


T = int(input())
for _ in range(T):
    K = input()
    print(solve(K))
