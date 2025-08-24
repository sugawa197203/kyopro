from math import ceil

N = int(input())
RC = [list(map(int, input().split())) for _ in range(N)]

minR = min(R for R, C in RC)
minC = min(C for R, C in RC)
maxR = max(R for R, C in RC)
maxC = max(C for R, C in RC)

r = ceil((maxR - minR) / 2)
c = ceil((maxC - minC) / 2)

print(min(r, c) + abs(r - c))
