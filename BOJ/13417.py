for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    ans = []
    for c in s:
        if not ans:
            ans.append(c)
        elif ans[0] < c:
            ans.append(c)
        else:
            ans.insert(0, c)
    print(''.join(ans))


    