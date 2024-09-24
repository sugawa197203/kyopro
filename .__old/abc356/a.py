N, L, R = map(int, input().split())

l = list(range(1, N+1))
m = l[L-1:R]
m.reverse()
l = l[:L-1] + m + l[R:]
print(*l)