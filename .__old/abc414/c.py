A = int(input())
N = int(input())

def base_n(num_10:int,n:int):
	str_n = ''
	while num_10:
		if num_10%n>=10:
			return -1
		str_n += str(num_10%n)
		num_10 //= n
	return int(str_n[::-1])

ans:int = 0

def Akaibun(num:int, a:int):
	if num != int(str(num)[::-1]):
		return False
	_num = base_n(num, a)
	return _num == int(str(_num)[::-1])

for i in range(1, 10):
	if i > N:
		print(ans)
		exit()
	
	if Akaibun(i, A):
		ans += i

for i in range(1, 10):
	i = i * 10 + i
	if i > N:

		print(ans)
		exit()
	
	if Akaibun(i, A):

		ans += i


for i in range(10, 10**7):
	sti = str(i)
	back = sti[:-1][::-1]
	numi = int(sti + back)
	if numi > N:

		print(ans)
		exit()
	if Akaibun(numi, A):

		ans += numi
	
	back = sti[::-1]
	numi = int(sti + back)
	if numi <= N:
		if Akaibun(numi, A):
			ans += numi
