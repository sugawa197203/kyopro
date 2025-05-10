def acc(__A) -> list[int]:
    res = [0]
    for x in __A:
        res.append(res[-1]+x)
    return res


n = int(input())
a = list(map(int,input().split()))
ac = acc(a)    
ans = 0
a = [0]+a
for i in range(1,n):
	ans += a[i]*(ac[n]-ac[i])
print(ans)