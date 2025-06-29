N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = sum([abs(a - b) for a, b in zip(A, B)])

print("Yes" if K >= diff and (K - diff) % 2 == 0 else "No")

