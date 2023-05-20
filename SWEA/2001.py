T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))

    mx = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += a[i+k][j+l]
            if mx < tmp:
                mx = tmp

    print('#{} {}'.format(t, mx))
