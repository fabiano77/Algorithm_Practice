import sys
import math

M, N = map(int, input().split())

is_prime_list = [True for _ in range(N+1)]

for i in range(2,N+1,1):
    if is_prime_list[i] == False:
        pass
    else:
        isPrime = True
        for j in range(2,int(math.sqrt(i))):
            if is_prime_list[i] == False and i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            for j in range(i*2, N+1, i):
                is_prime_list[j] = False

for i in range(max(2,M), N+1):
    if i == 1:
        pass
    if is_prime_list[i] == True:
        print(i)