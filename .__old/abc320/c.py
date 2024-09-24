import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

M = int(input())
S1 = input()
S2 = input()
S3 = input()

ERROR = True

for s1 in S1:
	if s1 in S2 and s1 in S3:
		ERROR = False
		break

if ERROR:
	print(-1)
	sys.exit()

result = 100000000000

for i, s1 in enumerate(S1):
	if not s1 in S2:
		continue
	if not s1 in S3:
		continue

	l = []
	l.append(i)

	f1 = False
	f2 = False
	k = 0
	for j, s2 in enumerate(S2):
		if s2 == s1:
			k = j
			if f1 and i == j:
				print("1", j)
				l.append(j)
				f2 = True
			f1 = True
	if not f2:
		print("2", k + M)
		l.append(k + M)

	f1 = False
	f2 = False
	k = 0
	for j, s3 in enumerate(S3):
		if s3 == s1:
			k = j
			if f1 and i == j:
				print("3", j)
				l.append(j)
				f2 = True
			f1 = True
	if not f2:
		print("4", k + M)
		l.append(k + M)
	
	print(l, s1)
	l.sort()
	if l[1] == l[2]:
		l[2] += M
	
	
	result = min(result, max(l))

print(result)

