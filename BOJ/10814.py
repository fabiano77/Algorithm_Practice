n = int(input())

people = []
for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])

people.sort(key = lambda x: x[0])

for item in people:
    print(item[0], item[1])