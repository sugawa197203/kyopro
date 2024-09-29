import numpy as np; import sortedcontainers as sc; import math; import bisect; import itertools; import sys; debug = lambda *arg : print(*arg, file=sys.stderr);

a,b = map(int, input().split())

print("Even" if a*b%2 == 0 else "Odd")

