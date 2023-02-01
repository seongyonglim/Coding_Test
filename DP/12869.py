import sys
from itertools import permutations

N = int(sys.stdin.readline())

scv = list(map(int, sys.stdin.readline().split()))

while len(scv) != 3:
    scv.append(0)

dp = [[[0]*61 for _ in range(61)]for _ in range(61)]


def dfs(s1, s2, s3):
    if s1 == 0 and s2 == 0 and s3 == 0:
        return 0
    if dp[s1][s2][s3]:
        return dp[s1][s2][s3]

    dp[s1][s2][s3] = 1 + min(dfs(max(s1-1, 0), max(s2-3, 0), max(s3-9, 0)), dfs(max(
        s1-1, 0), max(s2-9, 0), max(s3-3, 0)), dfs(max(s1-3, 0), max(s2-1, 0), max(s3-9, 0)), dfs(max(s1-3, 0), max(s2-9, 0), max(s3-1, 0)), dfs(max(s1-9, 0), max(s2-1, 0), max(s3-3, 0)), dfs(max(s1-9, 0), max(s2-3, 0), max(s3-1, 0)))

    return dp[s1][s2][s3]


print(dfs(scv[0], scv[1], scv[2]))
