N = int(input())
X = list(map(int, input().split()))
Q = int(input())
total = 0
import bisect
for q in range(Q):
    t, g = map(int, input().split())