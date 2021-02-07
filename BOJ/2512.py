n = int(input())
lst = list(map(int, input().split()))
m = int(input())

first = 0
last = max(lst)
sol = 0
while first <= last:
    mysum = 0
    middle = (first + last)//2
    for item in lst:
        if item > middle:
            mysum += middle
        else:
            mysum += item
    if mysum > m:
        last = middle-1
    else:
        sol = middle
        first = middle+1
print(sol)