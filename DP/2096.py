import sys

N = int(sys.stdin.readline())

min_dp, max_dp = [0]*3, [0]*3

for i in range(1, N+1):
    a = list(map(int, sys.stdin.readline().split()))

    tmp = max_dp.copy()
    tmp[0] = a[0] + max(max_dp[0], max_dp[1])
    tmp[1] = a[1] + \
        max(max_dp[0], max_dp[1], max_dp[2])
    tmp[2] = a[2] + max(max_dp[1], max_dp[2])
    max_dp = tmp.copy()

    tmp = min_dp.copy()
    tmp[0] = a[0] + min(min_dp[0], min_dp[1])
    tmp[1] = a[1] + \
        min(min_dp[0], min_dp[1], min_dp[2])
    tmp[2] = a[2] + min(min_dp[1], min_dp[2])
    min_dp = tmp.copy()

print(max(max_dp[0], max_dp[1], max_dp[2]),
      min(min_dp[0], min_dp[1], min_dp[2]))
