import sys
N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
K = int(sys.stdin.readline())

if N == 1:
    print(0)
elif N == 3:
    print(min(a[0][0]+a[1][0], a[0][1]))

else:
    dp = [0]*(N)
    dp[0] = 0
    dp[1] = a[0][0]

    for i in range(1, N-2):
        dp[i+1] = min(dp[i]+a[i][0], dp[i-1]+a[i-1][1])
        dp[i+2] = min(dp[i+1]+a[i+1][0], dp[i]+a[i][1])

    res = [dp[-1]]
    for i in range(0, N-3):
        dp2 = dp.copy()
        dp2[i+3] = dp[i]+K
        for j in range(i+3, N-2):
            dp2[j+1] = min(dp2[j]+a[j][0], dp2[j-1]+a[j-1][1])
            dp2[j+2] = min(dp2[j+1]+a[j+1][0], dp2[j]+a[j][1])
        res.append(dp2[-1])

    print(min(res))
