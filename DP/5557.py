import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(N-1)]

dp[0][a[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if j-a[i] >= 0:
            dp[i][j] += dp[i-1][j-a[i]]
        if j+a[i] <= 20:
            dp[i][j] += dp[i-1][j+a[i]]

print(dp[-1][a[-1]])

'''

8 3 2 4 8 7 2 4 0 8 8

0   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
8   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0
3   0   0   0   0   0   1   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0
2   0   0   0   1   0   0   0   1   0   1   0   0   0   1   0   0   0   0   0   0   0
4   0   0   0   1   0   1   0   1   0   1   0   1   0   1   0   0   0   1   0   0   0
8   0   1   0   1   0   1   0   0   0   1   0   1   0   1   0   1   0   1   0   1   0
7   0   0   1   0   1   0   1   0   2   0   2   0   2   0   0   0   1   0   1   0   1
2   1   0   1   0   2   0   3   0   3   0   4   0   2   0   3   0   1   0   2   0   1
4   2   0   3   0   4   0   5   0   4   0   6   0   4   0   6   0   3   0   3   0   1
0   4   0   6   0   8   0   10  0   8   0   12  0   8   0   12  0   6   0   6   0   2
8   8   0   12  0   8   0   12  0   10  0   12  0   10  0   15  0   4   0   6   0   4

'''