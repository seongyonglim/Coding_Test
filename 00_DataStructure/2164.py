from collections import deque

N = int(input())

a = deque([i for i in range(1, N+1)])

for i in range(N-1):
    a.popleft()
    a.append(a.popleft())

print(a[0])
