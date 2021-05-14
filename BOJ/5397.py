for _ in range(int(input())):
    front_stack = []
    end_stack = []
    data = input()
    for char in data:
        if char == '<':
            if front_stack:
                end_stack.append(front_stack.pop())
        elif char == '>':
            if end_stack:
                front_stack.append(end_stack.pop())
        elif char == '-':
            if front_stack:
                front_stack.pop()
        else:
            front_stack.append(char)
    print(''.join(front_stack)+''.join(reversed(end_stack)))
