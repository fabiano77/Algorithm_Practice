a = input()
if not '0' in a or sum(map(int, a)) % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(a, reverse=True)))