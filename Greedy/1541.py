import sys

a = sys.stdin.readline().rstrip()

ans = 0
nums = a.split('-')

for i in range(len(nums)):
    if i != 0:
        ans -= sum(map(int, nums[i].split('+')))
    else:
        ans += sum(map(int, nums[i].split('+')))

print(ans)
