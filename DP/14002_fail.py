from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
dp = []
res = []

for i in A:
    tmp = bisect_left(dp, i)
    if len(dp) <= tmp:
        dp.append(i)
        res.append(i)
        if res != sorted(res):
            res = dp.copy()
    else:
        dp[tmp] = i

print(len(dp))
print(*res)
