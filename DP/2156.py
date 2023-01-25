n = int(input())

a = [0]
for i in range(n):
    a.append(int(input()))
dp = [0]
dp.append(a[1])

if (n > 1):
    dp.append(a[1]+a[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3] + a[i-1] + a[i], dp[i-2] + a[i]))
print(dp[n])
