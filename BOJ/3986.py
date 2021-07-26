ans = 0
for _ in range(int(input())):
    s = input()
    stack = []
    for c in s:
        stack.append(c)
        while len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                break
    if not stack: ans += 1
print(ans)
