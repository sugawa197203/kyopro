from itertools import permutations

N = int(input())
SS = [input() for _ in range(N)]
ans = set()
for S in permutations(SS, 2):
	s = "".join(S)
	ans.add(s)

print(len(ans))
