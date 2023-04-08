import sys

N, S = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

cnt = 0


def dfs(idx, sum):
    global cnt
    if idx >= N:
        return
    sum += a[idx]
    if sum == S:
        cnt += 1

    dfs(idx+1, sum)
    dfs(idx+1, sum-a[idx])


dfs(0, 0)
print(cnt)
