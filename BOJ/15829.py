def hash(data):
    r = 31
    m = 1234567891
    h_val = 0
    for order, askii in enumerate(data):
        char = ord(askii)
        num = char - (ord('a') - 1)
        h_val = ( h_val + (num * (r ** order))) % m
    return h_val

l = int(input())
string = input()
print(hash(string))
