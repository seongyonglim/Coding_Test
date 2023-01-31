import sys

N = int(sys.stdin.readline())

a = []
dp = [[0]*N for _ in range(N)]
for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    if len(a[i]) == 2:
        dp[0][i] = a[i][0]

l = 3
for i in range(1, N):
    for j in range(N):
        le = len(a[j])
        if le <= l:
            m = 0
            for k in range(1, le-1):
                m = max(m, dp[i-1][a[j][k]-1])
            if m == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = a[j][0]+m
        else:
            dp[i][j] = dp[i-1][j]
    l += 1

for i in range(N):
    print(dp[N-1][i])
