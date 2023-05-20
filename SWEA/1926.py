N = int(input())

for i in range(1, N+1):
    tmp = i
    res = ''
    while tmp:
        if tmp % 10 in [3, 6, 9]:
            res += '-'
        tmp //= 10
    if len(res):
        print(res, end=' ')
    else:
        print(i, end=' ')
