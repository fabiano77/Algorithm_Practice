n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
i = 0
ans = ''

for num in arr:
    while not stack or (stack[-1] != num and i <= n):
        i += 1
        stack.append(i)
        ans += '+'
    if stack[-1] == num:
        stack.pop()
        ans += '-'
    else:
        break


if i > n:
    print('NO')
else:
    for s in ans:
        print(s)