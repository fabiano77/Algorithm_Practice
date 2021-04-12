import sys
input = lambda: sys.stdin.readline().rstrip()

def date_to_365(month, day):
    ret_days = 0
    for m in range(1, month):
        if m == 2:
            ret_days += 28
        elif m in (4, 6, 9, 11):
            ret_days += 30
        else:
            ret_days += 31
    return ret_days + day

n = int(input())
data = []
for _ in range(n):
    ms, ds, me, de = map(int, input().split())
    data.append([date_to_365(ms, ds), date_to_365(me, de)])
data.sort()
last = date_to_365(3, 1)
end = date_to_365(11,30)
longest = data[0][0]
ans = 0
idx = 0

if data[0][0] > 60:
    print(0)
else:
    while last <= end and idx < len(data):
        while idx < len(data) and data[idx][0] <= last:
            longest = max(longest, data[idx][1])
            idx += 1
        
        last = longest
        ans += 1

    if last <= end:
        print(0)
    else:
        print(ans)