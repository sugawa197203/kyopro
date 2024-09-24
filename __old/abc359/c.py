Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())
Sx, Sy, Tx, Ty = Sx+2*10**16, Sy+2*10**16, Tx+2*10**16, Ty+2*10**16
yoko, tate = abs(Tx-Sx), abs(Ty-Sy)

if Sy % 2 == Ty % 2:
	print(tate + max(0, yoko//2 - tate//2))
else:
	if Ty % 2 == 0:
		Sx, Sy, Tx, Ty = Tx, Ty, Sx, Sy
	
	if Sx % 2 == 0:
		if Tx <= Sx:
			print(tate + max(0, yoko//2 - tate//2))
		else:
			print(tate + max(0, yoko//2 - tate))
	else:
		if Tx >= Sx:
			print(tate + max(0, yoko//2 - tate//2))
		else:
			print(tate + max(0, yoko//2 - tate))

print(tate, yoko)
			
