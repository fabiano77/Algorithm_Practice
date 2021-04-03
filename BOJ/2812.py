n, k = map(int, input().split())
data = list(map(int, input()))

stack = []
for num in data:
    # 큰 숫자가 stack에 먼저 쌓이도록(높은 자릿수)
    while stack and stack[-1] < num and k > 0:
        # 큰 숫자를 발견하면, pop
        stack.pop()
        k -= 1
    stack.append(num)
    # print(stack)
    
while k:
    stack.pop()
    k -= 1

ans = ''
for item in stack:
    ans += str(item)
print(ans)