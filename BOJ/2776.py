from bisect import bisect_left
for _ in range(int(input())):
    n = int(input())
    arr_1 = list(map(int, input().split()))
    arr_1.sort()
    m = int(input())
    arr_2 = list(map(int, input().split()))

    for item in arr_2:
        index = bisect_left(arr_1, item)
        if index < n and arr_1[index] == item:
            print(1)
        else:
            print(0)