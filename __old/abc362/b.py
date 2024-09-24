xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

vecAB = [xb - xa, yb - ya]
vecAC = [xc - xa, yc - ya]

naisekiBAC = vecAB[0] * vecAC[0] + vecAB[1] * vecAC[1]
if naisekiBAC == 0:
	print("Yes")
	exit()

vecBA = [xa - xb, ya - yb]
vecBC = [xc - xb, yc - yb]
naisekiABC = vecBA[0] * vecBC[0] + vecBA[1] * vecBC[1]
if naisekiABC == 0:
	print("Yes")
	exit()

vecCA = [xa - xc, ya - yc]
vecCB = [xb - xc, yb - yc]
naisekiCAB = vecCA[0] * vecCB[0] + vecCA[1] * vecCB[1]
if naisekiCAB == 0:
	print("Yes")
	exit()

print("No")