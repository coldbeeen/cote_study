# 치킨 배달
# 1945

"""

거리를 계산하는 공식이 l1 거리라고 하는데, 오히려 신경쓸 필요가 없는게 원래 그래프 문제를 풀 때 그런 식으로 거리를 계산해왔음
=> 인접노드 한칸당 1로 생각하라는 뜻 ㅇㅇ

치킨거리는 집을 기준으로 정해진다. 그러나 a와 b사이의 거리==b와 a사이의 거리이므로, 
치킨집을 폐업시킨다는 입장에서 봤을때 치킨 거리들의 총합을 기준으로 정렬시켜야 문제를 풀 수 있을 것

이후 <구글링>
라고 생각했는데,,, 그게 아니라 오히려 조합으로 치킨거리들을 다 구하면 되는 문제였음

"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []  # 집의 좌표
chick = []  # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0  # 도시의 치킨 거리
    for h in house:
        chi_len = 999  # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)
print(result)