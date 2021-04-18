T = int(input())
button = [300, 60, 10]
ans = [0, 0, 0]

if T == 0:
    print(-1)
else:
    while T > 0:
        for i in range(3):
            if T >= button[i] or i == 2:
                T -= button[i]
                ans[i] += 1
                break

    if T == 0:
        for a in ans:
            print(a, end=' ')
    else:
        print(-1)