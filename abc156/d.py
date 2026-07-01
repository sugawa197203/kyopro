N, A, B = map(int, input().split())

MOD = 10 ** 9 + 7
ans = pow(2, N, MOD) - 1
nCm = [N] * 10**6
for i in range(1, 10**6):
    nCm[i] = nCm[i - 1] * (N - i) * pow(i + 1, -1, MOD) % MOD

ans -= nCm[A - 1]
ans -= nCm[B - 1]
ans %= MOD

print(ans)
