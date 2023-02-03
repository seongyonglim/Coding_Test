import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1]*(N)

for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))
