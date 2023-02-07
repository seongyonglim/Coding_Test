import sys
N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+1)
mx = 0
for i in range(0, N):
    mx = max(mx, dp[i])
    if i+a[i][0] <= N:
        dp[i+a[i][0]] = max(mx+a[i][1], dp[i+a[i][0]])

print(max(dp))
