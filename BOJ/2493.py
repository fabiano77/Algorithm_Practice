n = int(input())
li = list(map(int, input().split()))
stack = []
index = 0
for i, item in enumerate(li):
    index = i+1
    while stack:
        if stack[-1][0] >= item:
            print(stack[-1][1], end=' ')
            break
        else:
            stack.pop()
    if not stack:
        print(0, end=' ')
    stack.append((item, index))