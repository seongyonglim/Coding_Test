import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    count = 0
    error = False
    P = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        arr = deque()
    for p in P:
        if p == 'R':
            count += 1
        elif p == 'D':
            if arr and count % 2 == 0:
                arr.popleft()
            elif arr and count % 2 == 1:
                arr.pop()
            else:
                error = True
                print('error')
                break
    if count % 2 == 1:
        arr.reverse()
    if not error:
        print('['+','.join(arr)+']')
