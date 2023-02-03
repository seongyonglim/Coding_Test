import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

for i in range(N-1):
    mx, idx = a[i], i
    for j in range(i+1, min(N, S+i+1)):
        if mx < a[j]:
            mx = a[j]
            idx = j
    S -= idx-i
    for j in range(idx, i, -1):
        a[j] = a[j-1]
    a[i] = mx
print(*a)
