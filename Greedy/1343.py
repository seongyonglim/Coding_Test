import sys

s = sys.stdin.readline().rstrip()

cnt = 0
ans = ''
flag = 0
for k in s:
    if k == 'X':
        cnt += 1
    else:
        if cnt % 4 == 0:
            ans += 'A'*cnt
        elif cnt % 4 == 2:
            ans += 'A'*(cnt-2)+'B'*2
        else:
            flag = 1
            break
        cnt = 0
        ans += '.'

if cnt % 4 == 0:
    ans += 'A'*cnt
elif cnt % 4 == 2:
    ans += 'A'*(cnt-2)+'B'*2
else:
    flag = 1

if flag:
    print(-1)
else:
    print(ans)
