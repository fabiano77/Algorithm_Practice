tc = int(input())
for _ in range(tc):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(len(li)-2):
        ans = max(ans, li[i+2]-li[i])
    print(ans)
    