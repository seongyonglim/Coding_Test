N, K = map(int, input().split())

cur = 0
a = [i for i in range(1, N+1)]
r = []

for _ in range(N):
    cur += K-1
    if N >= len(a):
        cur %= len(a)
    r.append(a.pop(cur))

print(r)
