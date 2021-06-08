li = [int(input()) for _ in range(9)]
li.sort()

for i in range(0, 8):
    for j in range(i+1, 9):
        if sum(li) - (li[i] + li[j]) == 100:
            li.pop(j)
            li.pop(i)
            for item in li:
                print(item)
            exit()