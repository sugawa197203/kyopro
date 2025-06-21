N, Q = map(int, input().split())
class Node:
	def __init__(self, value):
		self.value = value
		self.patent = None
	
	def setparent(self, node):
		self.patent = node

PC = [Node("") for i in range(N)]
PCcount = [0] * N
PCLast = [PC[i] for i in range(N)]
Server = Node("")
ServerCount = 0
ServerLast = Server

for _ in range(Q):
	q, *ps = input().split()
	q = int(q)
	if q == 1:
		p = int(ps[0]) - 1
		PC[p] = Server
		PCLast[p] = ServerLast
		PCcount[p] = ServerCount
	elif q == 2:
		p, s = int(ps[0]) - 1, ps[1]
		n = Node(s)
		n.setparent(PCLast[p])
		PCLast[p] = n
		PCcount[p] += 1
	elif q == 3:
		p = int(ps[0]) - 1
		Server = PC[p]
		ServerCount = PCcount[p]
		ServerLast = PCLast[p]
ans = []
while ServerLast is not None:
	ans.append(ServerLast.value)
	ServerLast = ServerLast.patent

for a in ans[::-1]:
	print(a, end="")