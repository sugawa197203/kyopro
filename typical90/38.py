from math import lcm

v = lcm(*map(int, input().split()))
print(v if v <= 10**18 else "Large")

