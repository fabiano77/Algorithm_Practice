s = input()
for ord_alphabet in range(ord('a'), ord('z')+1):
    print(s.count(chr(ord_alphabet)), end=' ')
print()