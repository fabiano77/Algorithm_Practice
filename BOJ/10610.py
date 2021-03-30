def reverse(string):
    new = ''
    for s in string[::-1]:
        new += s
    return new

a, b = input().split()
c = reverse(str(int(a)))+'+'+reverse(str(int(b)))

print(reverse(str(eval(c))))