# https://www.acmicpc.net/problem/9019
from collections import deque

def D(item):
    item *= 2
    if item >= 10000:
        return item % 10000
    return item

def S(item):
    item -= 1
    if item < 0:
        return 9999
    return item

def L(item):
    item *= 10
    item += item // 10000
    return item % 10000

def R(item):
    item += (item % 10) * 10000
    return item // 10

funcs = [D, S, L, R]

def solve(num, target):
    arr = [-1] * 10000
    arr[num] = ''
    q = deque()
    q.append(num)
    while q:
        n = q.popleft()
        for i in range(4):
            new_n = funcs[i](n)
            if arr[new_n] == -1:
                arr[new_n] = arr[n] + funcs[i].__name__
                q.append(new_n)
        if arr[target] != -1:
            print(arr[target])
            return
        

for _ in range(int(input())):
    a, b = map(int, input().split())
    solve(a, b)