N = int(input())
S = input()
M = 1

import math

sqrtN = math.ceil(math.sqrt(N))

if N == 2:
    print(1)
    exit(0)

for i in range(3, sqrtN, 2):
    if N % i == 0:
        M = i
        break
    



