n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
sol = int(1e9)
def bin_search():
    global sol
    start = max(li)
    end = sum(li)
    while start <= end:
        mid = (start+end) // 2
        count = 0
        wallet = 0
        for pay in li:
            if wallet - pay < 0:
                wallet = mid
                count += 1
            wallet -= pay
        
        if count > m :
            start = mid+1
        else:
            end = mid-1
            if mid < sol:
                sol = mid

bin_search()
print(sol)
