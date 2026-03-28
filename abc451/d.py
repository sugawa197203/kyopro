vv = []
mx = 10**9+100

def explore(v):
    if v != 0:
        vv.append(v)
    
    e = 0
    while True:
        w = int(f"{v if v != 0 else ''}{2**e}")
        
        if w <= mx:
            explore(w)
        else:
            break
        e += 1

explore(0)
vv_set = sorted(set(vv))
N = int(input())
print(vv_set[N-1])