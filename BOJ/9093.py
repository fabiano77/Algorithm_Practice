for _ in range(int(input())):
    li = input().split()
    for i in range(len(li)):
        li[i] = li[i][::-1]
    print(' '.join(li))