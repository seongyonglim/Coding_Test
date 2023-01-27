# 6588 - 골드바흐의 추측 (수학) (에라토스테네스의 체)

arr = [0 for _ in range(1000001)]

for i in range(2, 1000001):
    if (arr[i] == 0):
        for j in range(i+i, 1000001, i):
            arr[j] = 1

while 1:
    n = int(input())
    if (n == 0):
        break

    for i in range(3, int(n//2)+1, 2):
        if arr[i] == 0:
            if arr[n-i] == 0:
                print(n, '=', i, '+', n-i)
                break
