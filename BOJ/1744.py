import sys

input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

result = 0
previous = -11111
length = len(nums)
zero_index = length
for i in range(length):
    if nums[i] <= 0:
        zero_index = i
        break
neg_len = length - zero_index

for i in range(0, zero_index-1, 2):
    if nums[i] > 1 and nums[i+1] > 1:
        result += nums[i] * nums[i+1]
    else:
        result += nums[i] + nums[i+1]

if (length-neg_len) % 2 == 1:
    result += nums[zero_index-1]

for i in range(length-1, zero_index, -2):
    result += nums[i] * nums[i-1]
if (neg_len) % 2 == 1:
    result += nums[zero_index]

print(result)