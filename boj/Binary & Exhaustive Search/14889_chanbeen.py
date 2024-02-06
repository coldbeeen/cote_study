import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

team = [list(map(int, input().split())) for _ in range(N)]

comb_list = list(combinations(range(1, N+1), N//2)) #팀 가를 수 있는 경우의 수

num_list = list(range(1, N+1)) #팀 가르기를 위해 참가한 멤버 수만큼 인덱스 생성

result = []

for i in range(len(comb_list)//2): #다 돌 필요 없고, 절반까지만 돌면 됨
    start_team = []
    link_team = []
    start_power = 0
    link_power = 0
    
    for num in num_list: #팀 가르기
        if num in comb_list[i]:
            start_team.append(num)
        else:
            link_team.append(num)
    
    start_comb = list(combinations(start_team, 2))
    link_comb = list(combinations(link_team, 2)) #팀별 power 계산을 위해 (N/2)C2로 분리
    
    for comb in start_comb:
        start_power += team[comb[0]-1][comb[1]-1]
        start_power += team[comb[1]-1][comb[0]-1]
    
    for comb in link_comb:
        link_power += team[comb[0]-1][comb[1]-1]
        link_power += team[comb[1]-1][comb[0]-1] #팀별 멤버 간의 power 연산
        
    result.append(abs(start_power - link_power)) #절댓값 처리 후 리스트에 추가

print(min(result)) #힘의 최소 차이 출력