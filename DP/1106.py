import sys

C, N = map(int, sys.stdin.readline().split())
INF = 100*1000
dp = [0] + [INF] * (C+100)
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(b, C+b):
        dp[j] = min(dp[j], dp[j-b]+a)
print(min(dp[C:]))
