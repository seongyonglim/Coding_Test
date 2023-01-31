import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque(enumerate(map(int, sys.stdin.readline().split())))

ans = []
while dq:
    idx, paper = dq.popleft()
    ans.append(idx + 1)

    if paper > 0:
        dq.rotate(-(paper - 1))
    elif paper < 0:
        dq.rotate(-paper)

print(*ans)
