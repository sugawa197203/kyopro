N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

_A = [0] * 46
_B = [0] * 46
_C = [0] * 46

for a in A:
    _A[a % 46] += 1

for b in B:
    _B[b % 46] += 1

for c in C:
    _C[c % 46] += 1

ans = 0

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += _A[i] * _B[j] * _C[k]

print(ans)

