T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T+1):
    n = int(input())
    a = [[0]*n for _ in range(n)]
    a[0][0] = 1

    x, y = 0, 0
    cur = 1
    i = 0

    while cur != n*n:
        cur += 1
        if x+dx[i] < 0 or x+dx[i] >= n or y+dy[i] < 0 or y+dy[i] >= n or a[x+dx[i]][y+dy[i]] != 0:
            i = (i+1) % 4
        x += dx[i]
        y += dy[i]
        a[x][y] = cur

    print('#{}'.format(t))
    for line in a:
        for element in line:
            print(element, end=' ')
        print()
