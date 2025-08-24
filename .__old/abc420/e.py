N, Q = map(int, input().split())

group = [{n} for n in range(N)]
brackcount = {id(g): 0 for g in group}
color = [0] * N

for _ in range(Q):
    q, *uv = input().split()
    # print("-" * 20)
    # print(q, uv)
    # print(group)
    # print([id(g) for g in group])
    # print(brackcount)
    # print(color)
    if q == "1":
        u, v = map(int, uv)
        u -= 1
        v -= 1
        ug = group[u]
        vg = group[v]
        if len(ug) < len(vg):
            ug, vg = vg, ug
        
        for x in vg:
            group[x] = ug
        brackcount[id(ug)] += brackcount[id(vg)]
        ug.update(vg)
        group[v] = ug
        # print(group)
        # print([id(g) for g in group])
    elif q == "2":
        v = int(uv[0])
        v -= 1
        vg = group[v]
        if color[v] == 0:
            color[v] = 1
            brackcount[id(vg)] += 1
        else:
            color[v] = 0
            brackcount[id(vg)] -= 1
        # print(color)
        # print(brackcount)
    elif q == "3":
        v = int(uv[0])
        v -= 1
        vg = group[v]
        if brackcount[id(vg)] > 0:
            print("Yes")
        else:
            print("No")
