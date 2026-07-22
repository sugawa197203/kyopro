N = int(input())
S = list(input())
Q = int(input())

swap = False

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if swap:
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
        else:
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
    else:
        swap = not swap

if swap:
    S = S[N:] + S[:N]
print(''.join(S))
    
