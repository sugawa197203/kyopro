def cross(x1,y1,x2,y2):
    return x1*y2 - x2*y1

def is_convex(n, vertexes):
    flg = True
    for i in range(n):
        a = vertexes[i%n]
        b = vertexes[(i+1)%n]
        c = vertexes[(i+2)%n]

        vec_ab = [b[0]-a[0], b[1]-a[1]]
        vec_bc = [c[0]-b[0], c[1]-b[1]]

        if cross(*vec_ab, *vec_bc)<0:
            flg = False
            break
    return flg

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

n = 4
vertexes = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]

if is_convex(n, vertexes):
    print("Yes")
else:
    print("No")