from collections import deque
N = int(input())
s = input()
d = {}
a = deque([])

for i in range(N):
    d[chr(ord('A')+i)] = int(input())

for i in s:
    if i.isalpha():
        a.append(d[i])
    else:
        n1 = a.pop()
        n2 = a.pop()
        if i == '+':
            a.append(n2+n1)
        elif i == '-':
            a.append(n2-n1)
        elif i == '*':
            a.append(n2*n1)
        elif i == '/':
            a.append(n2/n1)
print('%.2f' % (a[0]))
