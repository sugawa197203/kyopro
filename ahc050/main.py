from fractions import Fraction

class IntVec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f"{self.x} {self.y}"


class Filed:
	def __init__(self, n, line):
		self.Size = IntVec2(n, n)
		self.Possibility = [[Fraction("1/1") for _ in range(n)] for _ in range(n)]
		self.FreeSpaceCount = 0
		self.__field = [[False for _ in range(n)] for _ in range(n)]

		for i in range(n):
			for j in range(n):
				self.__field[i][j] = line[i][j] == '#'
				if not self.__field[i][j]:
					self.FreeSpaceCount += 1
	
	def IsStone(self, x, y):
		if x < 0 or x >= self.Size.x or y < 0 or y >= self.Size.y:
			return True
		return self.__field[x][y]

	def SlipPossibility(self):
		newPossibility = [[Fraction("0.0") for _ in range(self.Size.x)] for _ in range(self.Size.y)]
		for i in range(self.Size.x):
			for j in range(self.Size.y):
				if self.IsStone(i, j):
					newPossibility[i][j] = Fraction("0.0")
				else:
					for direct in [IntVec2(0, 1), IntVec2(1, 0), IntVec2(0, -1), IntVec2(-1, 0)]:
						pos = IntVec2(i, j)
						while not self.IsStone(pos.x + direct.x, pos.y + direct.y):
							pos.x += direct.x
							pos.y += direct.y
						newPossibility[pos.x][pos.y] += self.Possibility[i][j] * Fraction("1/4")
						
		self.Possibility = newPossibility
	
	def GetMinPossibilityPos(self):
		minimum = Fraction("99999999999")
		minPos = IntVec2(-1, -1)
		for i in range(self.Size.x):
			# print(f"{self.Possibility[i]}")
			for j in range(self.Size.y):
				if self.IsStone(i, j):
					continue
				if self.Possibility[i][j] < minimum:
					minimum = self.Possibility[i][j]
					minPos = IntVec2(i, j)
		# input(f"Minimum: {minimum} at {minPos}")
		return minPos
	
	def PlaceStone(self, x, y):
		if not self.IsStone(x, y):
			self.__field[x][y] = True
			self.FreeSpaceCount -= 1

def ReadField(n):
	line = []
	for i in range(n):
		line.append(input().strip())
	return Filed(n, line)

if __name__ == "__main__":
	n, m = map(int, input().split())
	field = ReadField(n)
	freeCount = n * n - m
	for i in range(freeCount):
		field.SlipPossibility()
		minPos = field.GetMinPossibilityPos()
		field.PlaceStone(minPos.x, minPos.y)
		print(f"{minPos.x} {minPos.y}")
		
