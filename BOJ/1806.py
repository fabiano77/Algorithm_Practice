n, s = map(int, input().split())

li = list(map(int, input().split()))

head, tail = 0, 0
ans = len(li) + 1
t_sum = li[0]

while True:
    if t_sum >= s:
        ans = min(ans, head - tail + 1)
        if tail == head:
            head += 1
            if head >= n:
                break
            t_sum += li[head]
        else:
            t_sum -= li[tail]
            tail += 1
    else:
        head += 1
        if head >= n:
            break
        t_sum += li[head]

if ans > n:
    print(0)
else:
    print(ans)