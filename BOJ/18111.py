n, m, b = map(int, input().split())
flatten = n * m
my_map = []
for _ in range(n):
    my_map += list(map(int, input().split()))

hieght = 0
min_time = -1

first = min(my_map)
last = max(my_map)

for middle in range(first, last+1):
    temp_b = b
    time = 0
    for block in my_map:
        dif = block - middle
        temp_b += dif
        if dif < 0:
            # 블록 쌓기
            time -= dif
        else:
            # 블록 깎기
            time += dif * 2
    #print(f'middle {middle}, temp_b = {temp_b}, time = {time}')
    if temp_b >= 0:
        if min_time == -1 or time < min_time or (time == min_time and middle > hieght) :
            min_time = time
            hieght = middle
    else:
        break


print(min_time, hieght)