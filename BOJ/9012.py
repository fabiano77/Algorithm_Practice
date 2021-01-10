n = int(input())

for _ in range(n):
    ans = True
    in_data = input()
    stack = []
    for ch in in_data:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0 or stack.pop() != '(':
                ans = False
                break
    if len(stack) > 0:
        ans = False

    if ans:
        print('YES')
    else:
        print('NO')