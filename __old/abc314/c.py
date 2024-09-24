import numpy as np
import math
import sys
import collections
import bisect
import copy

N, M = map(int, input().split(" "))
S = input()
C = list(map(int, input().split(" ")))

SBUF = [0] * M
RESULT = []
ISINCFLAG = [False] * M
STARTINDEX = [0] * M

for i, s in enumerate(S):
	if ISINCFLAG[C[i] - 1] == False:
		ISINCFLAG[C[i] - 1] = True
		RESULT.append(" ")
		STARTINDEX[C[i] - 1] = i
		SBUF[C[i] - 1] = s
		continue

	RESULT.append(SBUF[C[i] - 1])
	SBUF[C[i] - 1] = s

for i in range(M):
	RESULT[STARTINDEX[i]] = SBUF[i]

print("".join(RESULT))
