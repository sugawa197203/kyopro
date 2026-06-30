X, Y = map(int, input().split())

_a = (2 * Y - X) % 3
_b = (2 * X - Y) % 3

if _a != 0 or _b != 0:
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

if a < 0 or b < 0:
    print(0)
    exit()

MOD = 10**9 + 7

table = [1] * (10**7)

for i in range(1, 10**7):
    table[i] = (table[i - 1] * i) % MOD

ans = (table[a + b] * pow(table[a], -1, MOD)) % MOD
ans = (ans * pow(table[b], -1, MOD)) % MOD
print(ans)
