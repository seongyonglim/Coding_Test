n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [10001]*(k+1)
dp[0] = 0

for i in range(1, k+1):
    for c in coins:
        if i >= c and dp[i-c] != -1:
            dp[i] = min(dp[i], dp[i-c]+1)
    if dp[i] == 10001:
        dp[i] = -1

print(dp[k])


s = 'hi my name is seongyonglim'

s.split(' ')
