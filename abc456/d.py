MOD = 998244353

S = input()

dpa = dpb = dpc = 0

for ch in S:
    if ch == 'a':
        dpa = (dpa + dpb + dpc + 1) % MOD
    elif ch == 'b':
        dpb = (dpa + dpb + dpc + 1) % MOD
    elif ch == 'c':
        dpc = (dpa + dpb + dpc + 1) % MOD

ans = (dpa + dpb + dpc) % MOD
print(ans)
