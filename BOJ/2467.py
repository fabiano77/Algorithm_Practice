n = int(input())
li = list(map(int, input().split()))

first, last = 0, n-1
val = int(1e11)
sol = (first, last)
while first < last:
    temp = li[first] + li[last]
    if abs(temp) <= val:
        val = abs(temp)
        sol = (first, last)
    if abs(li[first+1]+li[last]) <= abs(li[first]+li[last-1]) :
        first += 1
    else:
        last -= 1
for i in list(map(lambda x: li[x], sol)):
    print(i, end=' ')