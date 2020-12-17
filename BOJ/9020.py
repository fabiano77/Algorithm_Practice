import sys
import math
input = sys.stdin.readline

T = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    min = n
    for i in range(2, n//2+1):
        if isPrime(i) and isPrime(n-i):
            if abs(n-2*i) < min:
                sol = i, n-i
    print(sol[0], sol[1])


