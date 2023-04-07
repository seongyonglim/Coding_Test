import sys

A, B = map(int, sys.stdin.readline().split())
cnt = 1

while B > A:
    if B % 2:
        B = (B-1)/10
    else:
        B //= 2
    cnt += 1


if A != B:
    print(-1)
else:
    print(cnt)
