import sys
input = sys.stdin.readline

N = int(input())

a = []
a = input().split()   # N개

operators = ['+', '-', '*', '//']
op = []
op = list(map(int, input().split()))  # N-1개


def solve(index, op_list, value, N):
    global a
    global max
    global min
    if index == 0:
        value = a[index]
        solve(index+1, op_list, value, N)
    elif index == N:
        int_val = int(value)
        if int_val > max:
            max = int_val
        if int_val < min:
            min = int_val
    else:
        for i in range(4):
            new_op_list = op_list.copy()
            if new_op_list[i] != 0:
                new_op_list[i] -= 1
                if i == 3 and eval(value) < 0:
                    new_value = str(-eval(''.join([value[1:] + operators[i] + a[index]])))
                else:
                    new_value = str(eval(''.join([value + operators[i] + a[index]])))
                solve(index+1, new_op_list, new_value, N)


max = -sys.maxsize
min = sys.maxsize

solve(0, op, '', N)

print(max)
print(min)
