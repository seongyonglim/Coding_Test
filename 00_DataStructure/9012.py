N = int(input())

for i in range(N):
    s = input()

    r = True
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                r = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        r = False

    if r:
        print("YES")
    else:
        print("NO")
