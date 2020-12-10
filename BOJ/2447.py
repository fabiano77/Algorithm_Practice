import sys
input = sys.stdin.readline

def print_star(num, queue_list, queue_start, blank):
    if num == 1:
        if blank: queue_list[queue_start] = queue_list[queue_start]+' '
        else: queue_list[queue_start] = queue_list[queue_start]+'*'
    else:
        stage = num//3
        for i in range(0, 3*stage, stage):
            for j in range(0, 3*stage, stage):
                if blank or (i == stage and i == j):
                    print_star(stage, queue_list, i+queue_start, True)
                else:
                    print_star(stage, queue_list, i+queue_start, False)

N = int(input())
str_list = [str('') for _ in range(N)]

print_star(N, str_list, 0, False)

for item in str_list:
    print(item)
