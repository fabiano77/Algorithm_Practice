x, y = map(int, input().split())
z = (y*100)//x
new_z = z

sol = 0
if z >= 99:
    print(-1)
else:
    first = 1
    last = x
    while first <= last:
        mid = (first + last) // 2

        new_z = ((y+mid)*100)//(x+mid)
        if new_z == z:
            first = mid+1
        else:
            sol = mid
            last = mid-1
    print(sol)

