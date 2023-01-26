n = int(input())
a = list(map(int, input().split()))

s = sorted(a, reverse=True)
total = 0

for i in s:
    if len(a) == 1:
        break
    idx = a.index(i)
    if idx == 0:
        total += a[idx] - a[idx+1]
    elif idx == len(a)-1:
        total += a[idx] - a[idx-1]
    else:
        total += min(a[idx] - a[idx+1], a[idx] - a[idx-1])
    del a[idx]
print(total)
