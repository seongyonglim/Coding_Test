import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N+1)]

for i in range(6, N+1):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

print(dp[N])


# 0   1   2   3   4   5   6   7   8 * 9 * 10  11  12  13 * 14 * 15  16
# 0   1   2   3   3   3   6   9   9   9   18  27  36  36  36  72  72
# 0   1   2   3   4   5   6   9   12  15  18  27  36  45  54  63  72
