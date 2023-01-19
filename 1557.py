def is_square(n):
    return int(n ** 0.5) ** 2 == n


K = int(input())
cnt = 0
for i in range(1000000001):
    if is_square(i):
        cnt += 1
        if cnt == K:
            print(i)
