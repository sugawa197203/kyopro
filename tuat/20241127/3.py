Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

pos = [
    (Ax, Ay),
    (Bx, By),
    (Cx, Cy),
    (Dx, Dy)
]

# Graham scan

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def graham_scan(points):
    points.sort()
    upper = []
    lower = []
    for p in points:
        while len(upper) >= 2 and cross(sub(upper[-1], upper[-2]), sub(p, upper[-1])) > 0:
            upper.pop()
        upper.append(p)
    for p in reversed(points):
        while len(lower) >= 2 and cross(sub(lower[-1], lower[-2]), sub(p, lower[-1])) > 0:
            lower.pop()
        lower.append(p)
    return upper[:-1] + lower[:-1]

convex_hull = graham_scan(pos)

print("Yes" if len(convex_hull) == 4 else "No")
