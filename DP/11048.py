import sys

N, M = map(int, sys.stdin.readline().split())

a = [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N)]

dp[0][1] = a[0][1]

for i in range(1, M+1):
    dp[0][i] = dp[0][i-1] + a[0][i]

for i in range(1, N):
    dp[i] = dp[i-1].copy()
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + a[i][j]

print(dp[-1][-1])

'''

1   2   3   4
0   0   0   5
9   8   7   6

1   3   6   10
1   3   6   15
10  18  25  31


1   0   0
0   1   0
0   0   1


1   1   1
1   2   2
1   2   3
'''
