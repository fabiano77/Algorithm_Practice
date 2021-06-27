n, m = map(int, input().split())
li = list(map(int, input().split()))

def bin_search():
    first, last = 0, sum(li)
    sol = 0
    while first <= last:
        promising = True
        mid = (first + last) // 2
        i = 0
        for _ in range(m):
            my_sum = 0
            while i < len(li):
                if my_sum + li[i] > mid:
                    break
                else:
                    my_sum += li[i]
                    i += 1
        if i < len(li):
            # promising = False
            first = mid + 1
        else:
            sol = mid
            last = mid - 1
    return sol
print(bin_search())