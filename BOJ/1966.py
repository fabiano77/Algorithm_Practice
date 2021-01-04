T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0
    while len(queue):
        if max(queue) > queue[0]:
            queue.append(queue.pop(0))
            if m == 0: 
                m = len(queue)
            m -= 1
        else:
            queue.pop(0)
            cnt += 1
            if m == 0: 
                print(cnt)
                break        
            m -= 1