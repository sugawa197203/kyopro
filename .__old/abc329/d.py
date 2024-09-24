import numpy as np
import math
import sys
import collections
import bisect
import copy
import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))

N = 200000
M = 200000
A = [i+1 for i in range(200000)]

class hyo:
	def __init__(self, id):
		self.v = 0
		self.id = id
	
	def add(self):
		self.v += 1
	
	def get(self):
		return self.v

	def g(self):
		return self.v * 2000000 + (200000 - self.id)
	
	def getId(self):
		return self.id

tohyo = []
sorter = []
for i in range(N):
	h = hyo(i+1)
	tohyo.append(h)
	sorter.append(h)

ans = []
for a in A:
	tohyo[a-1].add()
	#sorter.sort(key=lambda x: x.getId())
	#sorter.sort(key=lambda x: x.get(), reverse=True)
	
	sorter.sort(key=lambda x: x.g(), reverse=True)
	
	ans.append(sorter[0].getId())

print(*ans, sep='\n')
	

