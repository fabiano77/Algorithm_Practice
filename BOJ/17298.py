n = int(input())
data = list(map(int, input().split()))
stack = []
sol = [-1] * n

stack.append(data.pop())

while data:
    item = data.pop()

    while stack:
        if item < stack[-1]:
            sol[len(data)] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(item)

for a in sol:
    print(a, end = ' ')