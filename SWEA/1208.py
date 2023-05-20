for T in range(1, 11):
    cnt = int(input())
    a = list(map(int, input().split()))

    for i in range(cnt):
        a.sort()
        a[0] += 1
        a[-1] -= 1
    a.sort()
    print('#{} {}'.format(T, a[-1]-a[0]))
