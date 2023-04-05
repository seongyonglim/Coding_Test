import sys


def posi(n):
    if n <= 0:
        return 0
    else:
        return n


N = int(sys.stdin.readline())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = (dp[posi(i-1)]+dp[posi(i-2)]+dp[posi(i-3)] +
             dp[posi(i-4)]+dp[posi(i-5)]+dp[posi(i-6)])/6+1

print(dp[N])
