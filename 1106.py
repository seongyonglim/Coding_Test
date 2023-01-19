C, N = map(int, input().split())

dp = [100001] * (C+100)

dp[0] = 0

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, C+100):
    for a in arr:
        if a[1] <= i:
            for j in range(i-a[1], i+1):
                dp[i] = min(dp[i], dp[j]+a[0])

print(min(dp[C:]))
