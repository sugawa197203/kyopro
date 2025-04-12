islogin = False

N = int(input())
ans = 0
for i in range(N):
	S = input()
	if S == "login":
		islogin = True
	elif S == "logout":
		islogin = False
	elif S == "public":
		pass
	elif S == "private":
		if not islogin:
			ans += 1

print(ans)