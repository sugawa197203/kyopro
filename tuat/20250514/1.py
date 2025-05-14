ax1, ay1, az1, ax2, ay2, az2 = map(int, input().split())
bx1, by1, bz1, bx2, by2, bz2 = map(int, input().split())


def box_collision(box1, box2):
    return (
        box1[0] < box2[3]
        and box1[3] > box2[0]
        and box1[1] < box2[4]
        and box1[4] > box2[1]
        and box1[2] < box2[5]
        and box1[5] > box2[2]
    )


box1 = (ax1, ay1, az1, ax2, ay2, az2)
box2 = (bx1, by1, bz1, bx2, by2, bz2)

if box_collision(box1, box2):
    print("Yes")
else:
    print("No")
