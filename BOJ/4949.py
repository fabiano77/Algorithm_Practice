
while True:
    ans = True
    stack = []
    s = input()
    if s == '.':
        break

    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == ']':
            if stack:
                prev = stack.pop()
            else:
                prev = '.'

            if prev == '(' and ch == ')':
                pass
            elif prev == '[' and ch == ']':
                pass
            else:
                ans = False
                

    if ans == False or stack:
        print('no')
    else:
        print('yes')