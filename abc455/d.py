N, Q = map(int, input().split())

class Tower:
    def __init__(self, n: int, init_link: int):
        self.n: int = n
        self.next: Link | None = Link(init_link)
        self.next.prev = self
    
    def __len__(self):
        l = self.next
        retval = 0
        while l is not None:
            retval += 1
            l = l.next
        return retval
    
    def __str__(self):
        l = self.next
        retval = []
        while l is not None:
            retval.append(str(l.n))
            l = l.next
        return f"[{' '.join(retval)}]"

class Link:
    def __init__(self, n: int):
        self.n: int = n
        self.prev: Link | Tower | None = None
        self.next: Link | None = None

towers = [Tower(i, i) for i in range(N)]
linkByCard = [t.next for t in towers]

for _ in range(Q):
    c, p = map(int, input().split())
    c -= 1
    p -= 1

    C_link = linkByCard[c]
    P_link = linkByCard[p]
    if C_link.prev is not None:
        C_link.prev.next = None
    C_link.prev = P_link
    P_link.next = C_link

for t in towers:
    print(len(t), end=" ")
