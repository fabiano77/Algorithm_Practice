n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 마지막 도시의 가격 제거

total = 0

pos = 0
while pos < len(price):
    print('pos =', pos)
    # cnt = 0
    next_pos = pos + 1
    for ne in range(pos + 1, len(price)):
        next_pos = ne
        print('if price[pos]>price[ne] : ', price[pos], price[ne])
        if price[pos] > price[ne]:
            print('break')
            break
        # cnt += 1
                

    total += sum(distance[pos:next_pos]) * price[pos]
    print('total =', total)
    print('next_pos =', next_pos)
    pos = next_pos

print(total)