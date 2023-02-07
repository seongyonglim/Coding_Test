import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

inc = [1]*N
for i in range(1, N):
    tmp = inc.copy()
    for j in range(i, N):
        if (a[i-1] < a[j]):
            tmp[j] = max(tmp[i-1]+1, tmp[j])
    inc = tmp.copy()

dec = [1]*N
for i in range(N-2, -1, -1):
    tmp = dec.copy()
    for j in range(i, -1, -1):
        if (a[i+1] < a[j]):
            tmp[j] = max(tmp[i+1]+1, tmp[j])
    dec = tmp.copy()

res = [0]*N
for i in range(N):
    res[i] = inc[i]+dec[i]-1

print(max(res))
