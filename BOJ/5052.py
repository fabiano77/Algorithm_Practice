import sys
# import time
# start_time = time.time()
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    flag = 'YES'
    number_list = []
    for _ in range(n):
        number_list.append(input().rstrip())
    # number_list.sort(key = len)
    number_list.sort()
    print(number_list, number_list[1:])    
    print(list(zip(number_list, number_list[1:])))

    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if len(number_list[i]) == len(number_list[j]):
                continue
            if number_list[i] == number_list[j][0:len(number_list[i])]:
                flag = 'NO'
                break
        if flag == 'NO':
            break
            
    print(flag)