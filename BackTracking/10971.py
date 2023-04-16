import sys

N = int(sys.stdin.readline())

W = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

visited = [0]*N
res = 10000001


def dfs(start, idx, val):
    global res
    if sum(visited) == N and W[idx][start]:
        val += W[idx][start]
        if val < res:
            res = val
            return
    if val > res:
        return
    for i in range(N):
        if not visited[i] and W[idx][i]:
            visited[i] = 1
            dfs(start, i, val+W[idx][i])
            visited[i] = 0


for i in range(N):
    visited[i] = 1
    dfs(i, i, 0)
    visited[i] = 0
print(res)
