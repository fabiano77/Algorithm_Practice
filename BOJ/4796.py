import sys

input = sys.stdin.readline

T = 0
while True:
    T += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    result = (V//P)*L
    V = V%P
    if V > L:
        result += L
    else:
        result += V
    print("Case {}: {}".format(T, result))