import sys
import bisect
import itertools

#####segfunc#####
def segfunc(x, y):
    max(x, y)
    return
#################

#####ide_ele#####
ide_ele = 0
#################

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


debug = lambda *a: print(*a, file=sys.stderr)

N, Q = map(int, input().split())
S = input()

_S = S.split("/")
onetwo = []

slashind = []
_sl = 0
for _s in _S[:-1]:
	_sl += len(_s)
	slashind.append(_sl)
	_sl += 1

for i in range(len(_S)-1):
	one, two = 0, 0
	# count 1
	for s in _S[i][::-1]:
		if s == "1":
			one += 1
		else:
			break
	
	# count 2
	for s in _S[i+1]:
		if s == "2":
			two += 1
		else:
			break
	
	onetwo.append((one, two))

debug(onetwo)
debug(slashind)

for q in range(Q):
	l, r = map(int, input().split())
	l -= 1
	r -= 1


