N = int(input())
K = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += min(a, K - a)

print(ans * 2) 
