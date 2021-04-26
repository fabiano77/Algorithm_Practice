n = int(input())
fact = 1
for i in range(2, n+1):
    fact *= i
str_fact = str(fact)
for i in range(1, len(str_fact)+1):
    if str_fact[-i] != '0':
        print(i-1)
        break