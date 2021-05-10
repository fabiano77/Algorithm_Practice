'''
(a d a a b c)   (1~6)
(a a b a b b) c (1~6)
=> 3

  (a d a a b c) (1~6)
a (a b a b b c) (2~7)

-> 2
'''

a, b = input().split()

d = len(b) - len(a)

ans = len(b)

for i in range(d+1):
    # range(5) -> [0, 1, 2, 3, 4]
    # 0, 1
    count = 0
    for x in range(len(a)):
        # x : [0, 1, 2, 3, 4, 5]
        if a[x] != b[x+i]:
            # x == 0: a[0] != b[1]
            #          a != a
            count = count + 1
    #print(f'i = {i} -> cnt = {count}')
    if count < ans:
        ans = count

print(ans)