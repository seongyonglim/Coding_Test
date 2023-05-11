import sys

N = int(sys.stdin.readline())

s = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

visited = [False]*N

min_diff = int(1e9)


def dfs(cnt, idx):
    global min_diff
    if cnt == N//2:
        p1, p2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    p1 += s[i][j]
                elif not visited[i] and not visited[j]:
                    p2 += s[i][j]

        min_diff = min(min_diff, abs(p1-p2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, idx+1)
            visited[i] = False


dfs(0, 0)
print(min_diff)
