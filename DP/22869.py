import sys

N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] + [0]*(N-1)

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if dp[j] == 1 and (i-j)*(abs(a[i]-a[j])+1) <= K:
            dp[i] = 1
            break

if dp[-1] == 1:
    print('YES')
else:
    print('NO')
