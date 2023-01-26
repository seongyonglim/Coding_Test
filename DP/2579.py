N = int(input())

a = [int(input()) for _ in range(N)]

a.insert(0, 0)

dp = [0 for _ in range(N+1)]
dp[1] = a[1]

if N > 1:
    dp[2] = a[1]+a[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+a[i], dp[i-3]+a[i-1]+a[i])

print(dp[N])
