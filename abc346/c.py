N, K = map(int, input().split())
A = list(map(int, input().split()))

import bisect
s = (K * (K + 1)) // 2
A = list(set(A))
A.sort()
i = bisect.bisect_right(A, K)
print(s - sum(A[:i]))
