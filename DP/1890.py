N = int(input())

game = []
dp = [[0]*N for i in range(N)]

for _ in range(N):
    game.append(list(map(int, input().split())))

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] >= 1 and game[i][j] != 0:
            if i+game[i][j] < N:
                dp[i+game[i][j]][j] += dp[i][j]
            if j+game[i][j] < N:
                dp[i][j+game[i][j]] += dp[i][j]
print(dp[-1][-1])
