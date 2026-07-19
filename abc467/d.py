from fractions import Fraction


def solve(Px, Py, Qx, Qy, Rx, Ry, Sx, Sy):
    katamukiPQ = (Qy - Py) / (Qx - Px) if Qx != Px else float("inf")
    katamukiRS = (Sy - Ry) / (Sx - Rx) if Sx != Rx else float("inf")
    if katamukiPQ != katamukiRS:
        return True

    midPQx = Fraction(Px + Qx, 2)
    midPQy = Fraction(Py + Qy, 2)
    midRSx = Fraction(Rx + Sx, 2)
    midRSy = Fraction(Ry + Sy, 2)

    katamukiMid = (
        (midRSy - midPQy) / (midRSx - midPQx) if midRSx != midPQx else float("inf")
    )
    if katamukiMid != -1 / katamukiPQ:
        return False
    return True


T = int(input())
for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = map(int, input().split())
    if solve(Px, Py, Qx, Qy, Rx, Ry, Sx, Sy):
        print("Yes")
    else:
        print("No")
