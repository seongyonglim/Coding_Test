import sys

n = int(sys.stdin.readline())
cnt = 0

if n < 5:
    if n % 2:
        print(-1)
    else:
        print(n//2)

else:
    cnt = n//5
    n %= 5

    if n % 2:
        cnt += (n+5)//2-1
    else:
        cnt += n//2
    print(cnt)
