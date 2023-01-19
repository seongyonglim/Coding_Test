n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:  # 가장 왼쪽 원소끼리 합침
            dp[i][0] += dp[i-1][0]
        elif j == i:  # 가장 오른쪽 원소끼리 합침
            dp[i][j] += dp[i-1][j-1]
        else:  # j-1와 j번째 둘중에 큰 값을 합침
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))  # 마지막층 최대값 출력
