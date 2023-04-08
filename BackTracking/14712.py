import sys

N, M = map(int, sys.stdin.readline().split())

board = [[0]*(M+1) for _ in range(N+1)]

ans = 0


def dfs(i, j):
    global ans

    if i > N:
        i, j = 1, j+1
    if j > M:
        ans += 1
        return

    dfs(i+1, j)

    if board[i-1][j] == 0 or board[i][j-1] == 0 or board[i-1][j-1] == 0:
        board[i][j] = 1
        dfs(i+1, j)
        board[i][j] = 0


dfs(1, 1)
print(ans)
