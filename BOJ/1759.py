from itertools import combinations

l, c = map(int, input().split())
li = sorted(list(input().split()))
group = ['a', 'e', 'i', 'o', 'u']

for a in combinations(li,l):
    if len(list(filter(lambda x: x in group, a))) >= 1 and len(list(filter(lambda x: x not in group, a))) >= 2:
        print(''.join(a))
