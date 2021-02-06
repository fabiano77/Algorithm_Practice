p = [0] * 101
init_lst = [0, 1, 1, 1, 2, 2]

for i in range(len(init_lst)):
    p[i] = init_lst[i]

for _ in range(int(input())):
    n = int(input())
    if n >= 6:
        for i in range(6, n+1):
            p[i] = p[i-1] + p[i-5]
    print(p[n])