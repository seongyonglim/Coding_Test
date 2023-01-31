import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    que = [(i, a[i]) for i in range(N)]
    a.sort(reverse=True)
    cnt = 0
    for x in a:
        while que[0][1] != x:
            que.append(que.pop(0))
        cnt += 1

        if que.pop(0)[0] == M:
            break

    print(cnt)
