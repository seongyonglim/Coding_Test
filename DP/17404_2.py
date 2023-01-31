N = int(input())
rgb = []
MAX = 1000*1000+1
res = MAX

dp = [[MAX, MAX, MAX]for _ in range(N)]

for _ in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp[0] = [MAX, MAX, MAX]
    dp[0][i] = rgb[0][i]

    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if j != i:
            res = min(res, dp[N-1][j])

print(res)
