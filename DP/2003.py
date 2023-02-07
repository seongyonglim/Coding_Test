import sys
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

l, r = 0, 1
cnt = 0
s = a[l]
while 1:
    if s < M:
        if r < N:
            s += a[r]
            r += 1
        else:
            break
    else:
        if s == M:
            cnt += 1
        s -= a[l]
        l += 1
print(cnt)
