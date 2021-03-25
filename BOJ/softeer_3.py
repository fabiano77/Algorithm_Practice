import sys

input = lambda: sys.stdin.readline().rstrip()
k, n = map(int, input().split())
# 조립라인, 작업장

# 작업시간, 작업시간, 이동시간, 이동시간

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(len(data)-1):
    for j in range(k):
        min_time = -1

        for other in range(0, k-1):
            bias = k + other * (k-1)
            # print(f'bias = {bias}')
            # print(f'other {other}')
            
            time = int()
            if other < j: 
                time = data[i][bias + other] + data[i][other]
            else: 
                time = data[i][bias + other] + data[i][other + 1]

            # print(f'min_time = {min_time}, time={time}')
            if min_time == -1:
                min_time = time
            else:
                min_time = min(min_time, time)

        # print(f'min_time2 = {min_time}')
        data[i+1][j] = data[i+1][j] + min(data[i][j], min_time)

print(min(data[-1]))




'''

4, 2
a, b, c, d, a->b, a->c, a->d, b->a, b->c, b->d, c->a, c->b, c->d, d->a, d->b, d->c  (4+4*3)

3, 4
a, b, c, a->b, a->c, b->a, b->c, b->a, b->c   (3+3*2)

1, 1, 2, 1,   2,       4,   2,    5,   1
3, 2, 2, 3,   2,       5,   3,    2,   3
2, 3, 3, 2,   1,       3,   4,    2,   5
4, 5, 6



작업시간, 작업시간, 


'''