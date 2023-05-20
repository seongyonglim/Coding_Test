T = int(input())

for C in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    now = set([num])
    nxt = set()
    for _ in range(cnt):
        while now:
            n = list(now.pop())
            l = len(n)
            for i in range(l):
                for j in range(i+1, l):
                    n[i], n[j] = n[j], n[i]
                    nxt.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        nxt, now = now, nxt
    print('#{} {}'.format(C, max(now)))
