N, K = map(int, input().split())

item = [[0, 0]]
dp = [[0]*(K+1)for i in range(N+1)]

for i in range(N):
    item.append(list(map(int, input().split())))

for i in range(1, N+1):
    W, V = item[i]
    for j in range(1, K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)

print(dp[N][K])
