import sys

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())

a = []

dp = [0]*(T+1)
dp[0] = 1

for _ in range(1, k+1):
    p, n = map(int, sys.stdin.readline().split())
    dp2 = dp.copy()
    for i in range(T+1):
        for j in range(1, n+1):
            if i-p*j >= 0:
                dp2[i] += dp[i-p*j]
            else:
                break
    dp = dp2.copy()

print(dp[-1])

'''
0   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  
0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0    
1   1   1   1   1   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
5   1   1   1   1   1   2   1   1   1   1   2   1   1   1   1   2   1   1   1   1   1
10  1   1   1   1   1   2   1   1   1   1   3   2   2   2   2   4   2   2   2   2   4

'''
