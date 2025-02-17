S1, S2 = input().split()

s1 = S1 == "sick"
s2 = S2 == "sick"

if s1 and s2:
	print("1")
elif s1:
	print("2")
elif s2:
	print("3")
else:
	print("4")