import sys

mk = sys.stdin.readline().rstrip()

min_ans = 0
max_ans = 0
min_count = 0
max_count = 0

for k in mk:
    if k == 'K':
        if min_count:
            min_ans = min_ans*(10**(min_count)) + 1*10**(min_count-1)
            min_count = 0
        min_ans = min_ans*10+5

        max_ans = max_ans*(10**(max_count+1))+5*10**(max_count)
        max_count = 0

    elif k == 'M':
        min_count += 1
        max_count += 1
if min_count:
    min_ans = min_ans*(10**(min_count)) + 1*10**(min_count-1)
for i in range(max_count):
    max_ans *= 10
    max_ans += 1

print(max_ans)
print(min_ans)
