n = int(input())
k = int(input())
t = 0
first = 1
last = n*n
ans = 0
while first <= last:
    t = 0
    middle = (first + last) // 2
    for i in range(1, n+1):
        if middle > n*i:
            t += n
        else:
            num = ((middle - 1) // i)
            if num < 0: num = 0
            t += num
    # print(f'first:{first}, middle:{middle}, last:{last}, t:{t}')
    if t <= (k-1):
        ans = middle
        first = middle + 1
    elif t > (k-1):
        last = middle - 1

print(ans)
# print(f'output : {ans}')
# B = [i*j for i in range(1, n+1) for j in range(1, n+1)]
# B.sort()
# print(f'answer : {B[k-1]}')
