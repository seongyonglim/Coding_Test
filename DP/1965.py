from bisect import bisect_left
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [a[0]]

for i in range(1, n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    elif a[i] < dp[-1]:
        idx = bisect_left(dp, a[i])
        dp[idx] = a[i]
print(len(dp))
