n, k = map(int, input().split())
if n < sum(range(1, k+1)):
    print(-1)
elif (n-sum(range(1, k+1)))%k:
    print(k)
else:
    print(k-1)

    '''
    1 2 3 4 -> 10
    3 4 5 6 -> 18
    4 5 6 7 -> 22
    5 6 7 8 -> 26
    '''