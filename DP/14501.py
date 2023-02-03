import sys
N = int(input())

a = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N):
    for j in range(i+a[i][0], N+1):
        dp[j] = max(dp[j], dp[i]+a[i][1])

print(max(dp))
