def reverse(string):
    return string[::-1]

a, b = input().split()
c = str(int(reverse(a)))+'+'+str(int(reverse(b)))
print(int(reverse(str(eval(c)))))