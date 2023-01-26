N, K = map(int, input().split())

a = list(map(int, input().split()))

diff = []

for i in range(N-1):
    diff.append(a[i+1]-a[i])

diff.sort(reverse=True)

diff = diff[K-1:]

print(sum(diff))
