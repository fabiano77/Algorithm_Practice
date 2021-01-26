import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    flag = 'YES'
    number_list = []
    for _ in range(n):
        number_list.append(input().rstrip())
    number_list.sort(key = len)

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