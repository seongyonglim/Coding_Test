import sys

N = int(sys.stdin.readline())
n = int(sys.stdin.readline())

dist = [[-1]*N for _ in range(N)]
a = []

for i in range(n):
    a.append(list(map(int, sys.stdin.readline())))

for s, e in a:
    dist[s][e] = 1
    dist[e][s] = 1
