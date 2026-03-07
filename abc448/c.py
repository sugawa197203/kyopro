N, Q = map(int, input().split())
A = list(map(int, input().split()))

Aindex = sorted([(a, i) for i, a in enumerate(A)], key=lambda x: x[0])

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))

    B = {b - 1 for b in B}

    for a, i in Aindex:
        if i not in B:
            print(a)
            break
