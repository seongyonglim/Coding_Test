import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [[0]*2 for _ in range(n+1)]
    a = [[0]+list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][1] + a[0][i], dp[i-1][0])
        dp[i][1] = max(dp[i-1][0] + a[1][i], dp[i-1][1])
    print(max(dp[n]))
