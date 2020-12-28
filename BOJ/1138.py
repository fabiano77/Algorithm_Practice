N = int(input())

left_high = list(map(int, input().split()))

sol = [N+1 for _ in range(N)]

for i in range(N):
    #print(sol)
    position = 0
    cnt = 0
    #print('cnt =', cnt, ', left_higt[',i,'] =',left_high[i])
    while cnt != left_high[i]:
        if sol[position] > i+1: 
            cnt += 1
        position += 1
    while sol[position] < i+1:
        position += 1
    sol[position] = i+1

for i in range(len(sol)):
    if i != 0: print(end=' ')
    print(sol[i], end='')