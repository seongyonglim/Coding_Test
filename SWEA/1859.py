T = int(input())

for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0

    sellPrice = 0
    for val in a[::-1]:
        if val > sellPrice:
            sellPrice = val
        else:
            ans += sellPrice - val
    print("#%d %d" % (i+1, ans))
