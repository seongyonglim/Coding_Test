import sys

N = int(sys.stdin.readline())

p = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0]*(N+1)

for i in range(1, N+1):
    for j in range(1, N+1):
        if j <= i:
            dp[i] = max(dp[i], dp[i-j]+p[j])

print(dp[N])
