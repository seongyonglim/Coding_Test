import sys
from collections import deque

a = list(sys.stdin.readline().rstrip())
dq = deque()
res = 0
tmp2 = []
tmp = 1
cnt = 0

mark = False

for x in a:
    if x == '(' or x == '[':
        cnt += 1
        if mark:
            tmp2.append(tmp)
            tmp = 1
            mark = False
        dq.append(x)
    elif x == ')':
        tmp *= 2
        if len(tmp2) != 0 and cnt == 1:
            tmp += tmp2.pop()
        dq.pop()
        mark = True
    elif x == ']':
        tmp *= 3
        if len(tmp2) != 0 and cnt == 1:
            tmp += tmp2.pop()
        cnt -= 1
        dq.pop()
        mark = True
    if len(dq) == 0:
        res += tmp
        tmp = 1
    print(len(dq), x, tmp, tmp2, cnt)
    print(res)
