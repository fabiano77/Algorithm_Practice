import sys

input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    command = input().rstrip()
    if len(command) > 4 and command[0:4] == 'push':
        stack.append(command[5:])
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)