from math import isqrt


def A123663(n):
    return (m := n << 1) - 1 - isqrt((m << 1) - 1)


solve = A123663

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
