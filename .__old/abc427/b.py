N = int(input())

ans = 0

def f(n):
    retval = 0
    while n != 0:
        retval += n % 10
        n //= 10
    return retval

A = [1] * (N + 1)

for i in range(2, N + 1):
    A[i] = f(A[i - 1]) + A[i - 1]
    # print(i, A)

print(A[N])