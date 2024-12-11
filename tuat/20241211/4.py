N = int(input())

from sympy import divisor_count

ans = [0] * (N)

for i in range(N):
    ans[i] = divisor_count(i+1)

for i in range(N):
    ans[i] = ans[i] * (i+1)

print(sum(ans))
