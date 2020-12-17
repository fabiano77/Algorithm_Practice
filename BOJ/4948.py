import sys
import math

input = sys.stdin.readline

while True:
    i = int(input().rstrip())
    if i == 0:
        break
    cnt_prime = 0
    for j in range(i+1, 2*i+1):
        is_prime = True
        for k in range(2, int(math.sqrt(j))+1):
            if j % k == 0:
                is_prime = False
                break
        if is_prime:
            cnt_prime += 1
    print(cnt_prime)