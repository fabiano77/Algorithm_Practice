# def solve(target, index, value):
#     global weight
#     global N
#     for i in range(index-1, -1, -1):
#         if value + weight[i] == target:
#             return True
#         elif value + weight[i] > target:
#             pass
#         else:
#             value += weight[i]
#             solve(target, i, value)
#     return False

# N = int(input())

# weight = list(map(int, input().split()))

# weight.sort()

# for i in range(1, 10000000):
#     if solve(i, N, 0) == False:
#         print(i)
#         break

# 위 코드는 시간초과

N = int(input())

weight = list(map(int, input().split()))

weight.sort()

last_sum = 1
for i in range(N):
    if last_sum < weight[i]:
        break    
    last_sum += weight[i]
print(last_sum)