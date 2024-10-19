import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

N = int(input())
A = list(map(int, input().split()))

print(min([len(bin(a)) - bin(a).rfind("1") - 1 for a in A]))

