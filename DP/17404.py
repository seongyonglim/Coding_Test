N = int(input())
rgb = []
MAX = 1000*1000+1

dp = [[MAX, MAX, MAX]for _ in range(N)]

for _ in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp[0] = [rgb[0][0], rgb[0][1], rgb[0][2]]
    dp[0][i] = MAX

    for j in range(1, N-1):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    dp[N-1][i] = rgb[N-1][i] + min(dp[N-2][(3+i+1) % 3], dp[N-2][(3+i+2) % 3])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
