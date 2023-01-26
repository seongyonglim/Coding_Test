S = input()
T = input()

res = 0

while len(T) != len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
    if S == T:
        res = 1

print(res)
