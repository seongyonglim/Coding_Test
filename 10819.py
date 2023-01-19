from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

per = permutations(a)
res = 0

for p in per:
    tmp = 0
    for i in range(n-1):
        tmp += abs(p[i+1]-p[i])
    if res < tmp:
        res = tmp
print(res)
