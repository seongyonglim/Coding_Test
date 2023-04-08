import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

min = 1000000001
max = -1000000001


def dfs(idx, tmp):
    global min
    global max
    if idx == N:
        if min > tmp:
            min = tmp
        if max < tmp:
            max = tmp

    for i in range(len(op)):
        if op[i]:
            op[i] -= 1
            if i == 0:
                dfs(idx+1, tmp + a[idx])
            elif i == 1:
                dfs(idx+1, tmp - a[idx])
            elif i == 2:
                dfs(idx+1, tmp * a[idx])
            elif i == 3:
                if tmp > 0:
                    dfs(idx+1, tmp // a[idx])
                else:
                    dfs(idx+1, -(abs(tmp)//a[idx]))
            op[i] += 1


dfs(1, a[0])
print(max)
print(min)
