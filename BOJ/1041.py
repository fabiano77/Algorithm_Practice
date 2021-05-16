#    +---+        
#    | D |        
#+---+---+---+---+
#| E | A | B | F |
#+---+---+---+---+
#    | C |        
#    +---+   
# 1면: 5*(n-2)**2 + 4*(n-2) 개
# 2면: 8*(n-2) + 4 개 
# 3면: 4개

two = [(0, 1), (0, 2), (0, 4), (0, 3), (1, 5), (2, 5), (4, 5), (3, 5), (1, 2), (1, 3), (4, 2), (4, 3)]
three = [(0, 1, 2), (0, 1, 3), (0, 4, 2), (0, 4, 3), (5, 1, 2), (5, 1, 3), (5, 4, 2), (5, 4, 3)]

n = int(input())
numbers = list(map(int, input().split()))

max_3 = 200
for i, j, k in three:
    max_3 = min(max_3, numbers[i]+numbers[j]+numbers[k])
max_2 = 200
for i, j in two:
    max_2 = min(max_2, numbers[i]+numbers[j])
max_1 = min(numbers)

if n == 1:
    pass
    print(sum(numbers)-max(numbers))
else:
    ans = max_3 * 4 + max_2 * (8*(n-2) + 4) + max_1 * (5*((n-2)**2) + 4*(n-2))
    print(ans)