import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0]*N
for i in range(N):
    dp[i] = a[i]
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+a[i])

print(max(dp))

'''
1 100 2 50 60 3 5 6 7 8

1   100 2   50  60  3   5   6   7   8
1   
1   101
1   101 3
1   101 3   53
1   101 3   53  113
1   101 3   53  113 6
1   101 3   53  113 6   11
1   101 3   53  113 6   11  17
1   101 3   53  113 6   11  17  24
1   101 3   53  113 6   11  17  24  32

2   1   5   6   7
2
2   1
2   1   7
2   1   7   13
2   1   7   13  20

'''
