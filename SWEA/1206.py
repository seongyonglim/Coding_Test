for i in range(10):
    N = int(input())
    ans = 0
    a = list(map(int, input().split()))

    for j in range(2, N-2):
        flag = 1
        tmp = [a[j]-a[j-2], a[j]-a[j-1], a[j]-a[j+1], a[j]-a[j+2]]
        if min(tmp) >= 1:
            ans += min(tmp)
    print('#%d %d' % (i, ans))
