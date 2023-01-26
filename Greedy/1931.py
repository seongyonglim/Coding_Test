N = int(input())

a = []
for i in range(N):
    a.append(list(map(int, input().split())))

a.sort()
a.sort(key=lambda x: x[1])

cnt = 0
e = 0
for i in a:
    if i[0] >= e:
        e = i[1]
        cnt += 1
print(cnt)
