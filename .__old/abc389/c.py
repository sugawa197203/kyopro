import queue

_queue = queue.Queue()
t = []
Q = int(input())-1
_, l = input().split()
_queue.put((int(l), 0))
t.append(int(l))

front = 0
for i in range(Q):
	inp = input().split()
	if inp[0] == "1":
		l = int(inp[1])
		_queue.put((l, len(t)))
		t.append(t[len(t)-1] + l)
	elif inp[0] == "2":
		l, idx = _queue.get()
		front += l
	else:
		l, idx = _queue.queue[int(inp[1])-1]
		print(t[idx] - l - front)
	
