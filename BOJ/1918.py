expression = input()

# A + B -> AB+
def to_postfix(a):
    result = ''
    stack = []
    for char in a:
        if char.isalpha():
            result += char
        else:
            if char == '(':
                stack.append(char)

            elif char == '*' or char == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(char)

            elif char == '+' or char == '-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)

            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()

    return result

print(to_postfix(expression))