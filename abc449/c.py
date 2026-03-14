from collections import defaultdict

N, L, R = map(int, input().split())
S = input()
ans = 0

faralphabet = defaultdict(int)
nearalphabet = defaultdict(int)
for i, s in enumerate(S):
    nearalphabet[s] += 1
    if i >= L:
        faralphabet[S[i - L]] += 1
        nearalphabet[S[i - L]] -= 1

    if i >= R + 1:
        faralphabet[S[i - R - 1]] -= 1
    
    ans += faralphabet[s]

print(ans)
