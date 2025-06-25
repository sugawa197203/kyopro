from itertools import accumulate

N = int(input())
C1, C2 = [0] * N, [0] * N
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        C1[i] = p
    else:
        C2[i] = p

C1 = [0] + list(accumulate(C1))
C2 = [0] + list(accumulate(C2))

Q = int(input())
for q in range(Q):
    l, r = map(int, input().split())
    a = C1[r] - C1[l-1]
    b = C2[r] - C2[l-1]
    print(a, b)


