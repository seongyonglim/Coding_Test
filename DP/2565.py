N = int(input())
w = sorted([list(map(int, input().split()))for i in range(N)])
dp = [1 for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if w[i][1] > w[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))
