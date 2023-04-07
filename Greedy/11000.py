import sys
import heapq

N = int(sys.stdin.readline())
a = []
for i in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort()

cls = []
heapq.heappush(cls, a[0][1])
for s, e in a[1:]:
    if s < cls[0]:
        heapq.heappush(cls, e)
    else:
        heapq.heappop(cls)
        heapq.heappush(cls, e)

print(len(cls))
