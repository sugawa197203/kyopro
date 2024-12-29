import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())

if N == 5:
	a, b = ["A", "B"] if input("? A B\n") == "<" else ["B", "A"]
	c, d = ["C", "D"] if input("? C D\n") == "<" else ["D", "C"]
	
	if input(f"? {a} {c}\n") == "<":
		a, b, c, e = a, c, d, b
	else:
		a, b, c, e = c, a, b, d
	
	if input(f"? {b} E\n") == "<":
		if input(f"? {c} E\n") == "<":
			c, d = c, "E"
		else:
			c, d = "E", c
	else:
		if input(f"? {a} E\n") == "<":
			b, c, d = "E", b, c
		else:
			a, b, c, d = "E", a, b, c
	
	if input(f"? {c} {e}\n") == "<":
		if input(f"? {d} {e}\n") == "<":
			pass
		else:
			d, e = e, d
	else:
		if input(f"? {b} {e}\n") == "<":
			c, d, e = e, c, d
		else:
			b, c, d, e = e, b, c, d


	print(f"! {a}{b}{c}{d}{e}")
	exit()


alphabet = [chr(i) for i in range(65, 65+N)]

def cmp(a, b):
	print(f'? {a} {b}')
	return input() == '<'

def mergeSort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left = mergeSort(arr[:mid])
	right = mergeSort(arr[mid:])

	merged = []
	i = j = 0
	while i < len(left) and j < len(right):
		if cmp(left[i], right[j]):
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1

	merged += left[i:]
	merged += right[j:]

	return merged

print('! ' + ''.join(mergeSort(alphabet)))
