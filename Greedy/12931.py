N = int(input())
B = list(map(int, input().split()))

cnt = 0
while (sum(B) != 0):
    cnt2 = 0
    for i in range(N):
        if B[i] % 2:
            B[i] -= 1
            cnt += 1
        else:
            cnt2 += 1
    if cnt2 == N:
        B = [i//2 for i in B]
        cnt += 1

print(cnt)
