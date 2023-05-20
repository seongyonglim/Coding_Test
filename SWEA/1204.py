T = int(input())

for _ in range(T):
    t = int(input())
    a = [0]*101

    scores = list(map(int, input().split()))
    for score in scores:
        a[100-score] += 1
    print('#%d %d' % (t, 100-a.index(max(a))))
