N = int(input())
S = {}
for i in range(N):
    s, t = input().split()
    S[s] = int(t)

X = input()

total = 0
for s, t in S.items():
    if s == X:
        break
    total += t

print(sum(S.values()) - total - S[X])

