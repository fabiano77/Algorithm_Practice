import sys

in_string = input()
in_string += '\0'

operator = ['+', '-', '\0']

last_op = -1
ops = []
nums = []
for i in range(len(in_string)):
    if in_string[i] in operator:
        ops.append(in_string[i])
        nums.append(str(int(in_string[last_op+1:i])))
        last_op = i

string = ''
for i in range(len(nums)):
    string += nums[i] + ops[i]

last_minus = -1
new_string = ''
for i in range(len(string)):
    if string[i] == '-':
        new_string += str(eval(string[last_minus+1:i]))+'-'
        last_minus = i
    elif string[i] == '\0':
        new_string += str(eval(string[last_minus+1:i]))

new_string = str(eval(new_string))

print(new_string)