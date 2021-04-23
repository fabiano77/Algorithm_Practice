import sys
input = lambda: sys.stdin.readline().rstrip()
g = int(input()) # 게이트, 1에서 g까지의 번호
p = int(input()) # 비행기의 개수, i번째 비행기를 1번부터 gi번째 게이트중 하나에 영구적 도킹

gate = [0] * (g+1)

# gi 의 입력
gi = [int(input()) for _ in range(p)]

ans = 0

for i in range(p):
    dock_idx = gi[i]
    while gate[dock_idx] != 0:
        dock_idx
    if dock_idx == 0:
        break
    gate[dock_idx] = True
    ans += 1

print(ans)






'''