N, Q = map(int, input().split())
S = input()

Sacc = [0] * (N + 1)
for i in range(N):
    Sacc[i + 1] = Sacc[i] + (1 if S[i:i + 2] == 'AC' else 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(Sacc[r - 1] - Sacc[l - 1])
