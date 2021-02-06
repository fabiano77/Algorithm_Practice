lst = []
for _ in range(int(input())):
    lst.append(input())
lst.sort()
lst.sort(key = lambda x : sum(map(int, filter(lambda n : n.isnumeric() , x))))
lst.sort(key = len)
for s in lst:
    print(s)