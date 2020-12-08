import sys
import itertools
import copy
input = sys.stdin.readline


def calcul_op(list_, operator_idx):
    # print("calcul_op : list_=",list_, "operator_idx =", operator_idx)
    # while len(op_idx_list):
    #     op_idx = op_idx_list.pop(0)
    new_num = int
    if list_[operator_idx] == '*':
        new_num = list_[operator_idx-1] * list_[operator_idx+1]
    elif list_[operator_idx] == '+':
        new_num = list_[operator_idx-1] + list_[operator_idx+1]
    elif list_[operator_idx] == '-':
        new_num = list_[operator_idx-1] - list_[operator_idx+1]

    new_list = []

    if operator_idx - 2 > 0:
        new_list.extend(list_[:operator_idx-1])

    new_list.append(new_num)

    if operator_idx + 2 < len(list_):
        new_list.extend(list_[operator_idx+2:])

    return new_list


N = int(input().rstrip())
ex = input().rstrip()

ex_list = []
idx = 0
op_idx_list = []
for char in ex:
    if char.isnumeric():
        ex_list.append(int(char))
    else:
        ex_list.append(str(char))

order = [i+1 for i in range(N//2)]
order_list = []
for par_cnt in range(1, (len(order)+1)//2+1):
    order_list.extend(list(map(list, itertools.combinations(order, par_cnt))))

new_order_list = copy.copy(order_list)
for item in order_list:
    # print("\nitem =",item, end='')
    del_item = False
    for idx in range(len(item)):
        if idx == 0:
            pass
        elif item[idx] - item[idx-1] == 1:
            # print("del ",item, end = '')
            del_item = True
    if del_item:
        new_order_list.remove(item)

for order_item in new_order_list:
    for item in order:
        if item not in order_item:
            order_item.append(item)

# print(new_order_list)

#exit(1)
max = -sys.maxsize -1
if len(ex_list) == 1:
    max = ex_list[0]
for order_item in new_order_list:
    ex_list_copy = copy.copy(ex_list)
    # print('\torder_item :', order_item)
    while len(order_item):
        op_idx = order_item.pop(0)
        # print("op_idx :",op_idx)
        ex_list_copy = calcul_op(ex_list_copy, (op_idx*2)-1)
        for i in range(len(order_item)):
            if op_idx < order_item[i]:
                order_item[i] -= 1
        # print(ex_list_copy)
    # print('ex_list[0] :',ex_list_copy[0])
    if ex_list_copy[0] > max:
        max = ex_list_copy[0]
            
print(max)
