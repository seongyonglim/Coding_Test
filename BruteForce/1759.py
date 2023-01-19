import itertools

L, C = map(int, input().split())

arr = input().split()
arr.sort()

nCr = itertools.combinations(arr, L)
s = []

for i in nCr:
    s.append(''.join(i))

for i in s:
    mo = 0
    ja = 0
    for j in i:
        if j in 'aeiou':
            mo += 1
        else:
            ja += 1
        if mo >= 1 and ja >= 2:
            print(i)
            break
