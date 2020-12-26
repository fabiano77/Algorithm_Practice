import sys

input = sys.stdin.readline

N = int(input())

words = []
numeric = [str(i) for i in range(9, -1, -1)]
alpha_numeric = dict()
alpha = dict()
result = 0

for _ in range(N):
    words.append(input().rstrip())
words.sort(key = len, reverse = True)
maxlen = len(words[0])

for i in range(len(words)):
    words[i] = words[i].rjust(maxlen)

for word in words:
    for i in range(maxlen):
        if word[i].isalpha():
            if word[i] not in alpha_numeric.keys():
                alpha_numeric[word[i]] = 10**(maxlen-i)
            else:
                alpha_numeric[word[i]]+= 10**(maxlen-i)

for value in sorted(alpha_numeric.values(), reverse = True):
    for key in alpha_numeric.keys():
        if key not in alpha.keys() and alpha_numeric[key] == value:
            alpha[key] = numeric[len(alpha)]
            break

for word in words:
    temp = ''
    for char in word:
        if char.isalpha():
            temp += alpha[char]
    result += int(temp)

print(result)