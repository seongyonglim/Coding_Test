import sys
import heapq

N = int(sys.stdin.readline())

se = []

for i in range(N):
    se.append(list(map(int, sys.stdin.readline().split())))

se.sort()

cls = []

heapq.heappush(cls, se[0][1])

for s, e in se[1:]:
    if s < cls[0]:
        heapq.heappush(cls, e)
    else:
        heapq.heappop(cls)
        heapq.heappush(cls, e)

print(len(cls))
