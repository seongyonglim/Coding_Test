import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

s = []
visited = [False] * (N+1)


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(len(a)):
        if visited[i]:
            continue
        visited[i] = True
        s.append(a[i])
        dfs()
        s.pop()
        visited[i] = False


dfs()
