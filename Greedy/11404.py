import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[100001]*(n+1)for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b],c)

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1, n+1):
            if j==k:
                graph[j][k] = 0
            else:
                graph[j][k] = min(graph[j][k] , graph[j][i]+graph[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1000001:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()