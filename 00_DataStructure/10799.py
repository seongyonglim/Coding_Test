import sys
from collections import deque

a = input()
dq = deque()

cnt = 0
for i in range(len(a)):
    if a[i] == '(':
        dq.append(a[i])
    else:
        if a[i-1] == ')':
            cnt += 1
            dq.pop()
        else:
            cnt += len(dq)-1
            dq.pop()
print(cnt)
