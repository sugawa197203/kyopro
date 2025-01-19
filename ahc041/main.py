N, M, H = map(int, input().split())
A = list(map(int, input().split()))
# A = [(node, a) for node, a in enumerate(A)]
# A.sort(key=lambda x: x[1])
UV = [tuple(map(int, input().split())) for _ in range(M)]
POS = [tuple(map(int, input().split())) for _ in range(N)]

from collections import defaultdict
G = defaultdict(list)
for u, v in UV:
	G[u].append(v)
	G[v].append(u)


GlobalIgnoreTrees = set()
GlobalNodoes = []

class Node:
	def __init__(self, id:int, tree:'Tree'):
		self.id = id
		self.tree = tree
		self.globalNextids = G[id]
		self.globalNextNodes = []
		self.nextNode = []
		self.lengthByroot = 1
		self.parent:Node = None
	
	def addNextNode(self, nextNode:'Node'):
		if nextNode == self:
			raise Exception("addNextNode self")
		self.nextNode.append(nextNode)
		nextNode.parent = self

	def isGlobalNextNode(self, targetNode:'Node'):
		return targetNode.id in self.globalNextids

	def setGlobalNextNodes(self, globalNextNodes:list['Node']):
		self.globalNextNodes = globalNextNodes

class Tree:
	def __init__(self, root:'Node', rootScore:int):
		self.root = root
		self.score = rootScore
		self.length = 1
		self.nodeCount = 1
		self.treeId = root.id
		self.nextTrees:set[Tree] = set()
		root.tree = self
	
	def addNextTree(self, nextTree:'Tree'):
		self.nextTrees.add(nextTree)

	def hasNode(self, targetNode:'Node'):
		queue = [self.root]
		while queue:
			node = queue.pop()
			if node.id == targetNode.id:
				return True
			queue.extend(node.nextNode)
		return False
	
	def GetNodes(self) -> list['Node']:
		retval = []
		queue = [self.root]
		while queue:
			node = queue.pop()
			retval.append(node)
			queue.extend(node.nextNode)
		return retval

	def mergeTree(self, child:'Tree', targetNode:'Node'):
		if targetNode == None:
			raise Exception("mergeTree targetNode is None")

		if not self.hasNode(targetNode):
			raise Exception("mergeTree targetNode not found")

		if child in GlobalIgnoreTrees:
			raise Exception("mergeTree child is ignored")

		if not targetNode.isGlobalNextNode(child.root):
			raise Exception("mergeTree targetNode is not nextNode")
		
		# merge tree

		targetNode.addNextNode(child.root)
		self.nodeCount += child.nodeCount
		queue = [(child.root, targetNode.lengthByroot+1)]
		while queue:
			node, length = queue.pop(0)
			node.tree = self
			node.lengthByroot = length
			queue.extend([(nextNode, length+1) for nextNode in node.nextNode])

		# update score

		score = 0
		queue = [(self.root, 1)]
		while queue:
			node, length = queue.pop(0)
			self.length = length
			score += A[node.id] * length
			queue.extend([(nextNode, length+1) for nextNode in node.nextNode])
		self.score = score
		
	
	def getHightestScoreNodeInFillter(self, fillter:list['Node']) -> 'Node':
		queue = [(self.root, 1)]
		maxScore, maxNode = 0, None
		while queue:
			node, length = queue.pop(0)
			if node in fillter and A[node.id] * length > maxScore:
				maxScore = A[node.id] * length
				maxNode = node
			queue.extend([(nextNode, length+1) for nextNode in node.nextNode])
		return maxNode


GlobalNodoes = [Node(i, None) for i in range(N)]
GlobalTrees = { i: Tree(GlobalNodoes[i], A[i]) for i in range(N) }

for node in GlobalNodoes:
	node.setGlobalNextNodes([GlobalNodoes[nextId] for nextId in node.globalNextids])



# add next tree
for tree in GlobalTrees.values():
	for nextId in G[tree.treeId]:
		tree.addNextTree(GlobalTrees[nextId])

def CalcMinimumNextTreeScoreAbs(tree:Tree):
	if tree.treeId in GlobalIgnoreTrees:
		raise Exception("CalcMinimumNextTreeScoreAbs Ignore")
	
	minimumAbsScore, minimumAbsScoreId = 10**9, -1
	for nextTree in tree.nextTrees:
		if nextTree.treeId in GlobalIgnoreTrees:
			# print("CalcMinimumNextTreeScoreAbs Ignore", nextTree.treeId)
			continue
		if abs(tree.score - nextTree.score) < minimumAbsScore and tree.length + nextTree.length <= H:
			minimumAbsScore = abs(tree.score - nextTree.score)
			minimumAbsScoreId = nextTree.treeId
	return minimumAbsScore, minimumAbsScoreId

for _ in range(H):
	try:
		for i, tree in enumerate(GlobalTrees.values()):
				if tree.treeId in GlobalIgnoreTrees:
					continue
				minimumNextTreeScoreAbs, minimumNextTreeScoreAbsId = CalcMinimumNextTreeScoreAbs(tree)
				if minimumNextTreeScoreAbsId == -1:
					continue
				
				targetTree = GlobalTrees[minimumNextTreeScoreAbsId]
				if tree.score > targetTree.score:
					targetTree.mergeTree(tree, targetTree.getHightestScoreNodeInFillter(tree.root.globalNextNodes))
					GlobalIgnoreTrees.add(tree.treeId)
				else:
					tree.mergeTree(targetTree, tree.getHightestScoreNodeInFillter(targetTree.root.globalNextNodes))
					GlobalIgnoreTrees.add(targetTree.treeId)
	except Exception as e:
		ans = [-1]*N
		print(*ans)
		exit()


ans = [node.parent.id if node.parent != None else -1 for node in GlobalNodoes]

print(*ans)

