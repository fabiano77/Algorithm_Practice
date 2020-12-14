import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
a_list = []
for _ in range(N):
    a_list.append(list(map(int, input().split())))

min = sys.maxsize

combi_list = list(combinations(range(N), N//2))
for team_list in combi_list[:len(combi_list)//2]:
    combi_team = list(combinations(team_list,2))
    rest_team = list(set(list(range(N))) - set(team_list))
    rest_combi = list(combinations(rest_team,2))
    score_a = 0
    score_b = 0
    for i, j in combi_team:
        score_a += a_list[i][j] + a_list[j][i]
    for i, j in rest_combi:
        score_b += a_list[i][j] + a_list[j][i]
    if abs(score_a - score_b) < min:
        min = abs(score_a - score_b)

print(min)
