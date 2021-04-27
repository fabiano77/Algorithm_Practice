import sys
input = lambda: sys.stdin.readline().rstrip()

stack_f = list(map(str, input()))
stack_b = []
m = int(input())
# print(list_string)
for _ in range(m):
    command = input()
    if command[0] == 'L':
        if stack_f:
            stack_b.append(stack_f.pop())
    elif command[0] == 'D':
        if stack_b:
            stack_f.append(stack_b.pop())
    elif command[0] == 'B':
        if stack_f:
            stack_f.pop()
    elif command[0] == 'P':
        stack_f.append(command[2])

print(''.join(stack_f)+''.join(reversed(stack_b)))