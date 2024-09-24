SA = list(input())
SB = list(input())
SC = list(input())

d = {'a': SA, 'b': SB, 'c': SC}

turn = 'a'

while True:
	if not d[turn]:
		print(turn.upper())
		break
	_turn = d[turn].pop(0)
	turn = _turn
