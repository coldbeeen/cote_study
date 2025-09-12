#약 30분 소요

from itertools import combinations

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9

home = []
chick = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1: #집
            home.append((i, j))
        elif city[i][j] == 2: #치킨집
            chick.append((i, j))
            
for case in combinations(chick, M): #M개의 치킨집을 선택하는 각 케이스
    total_dist = 0
    
    for h in home: #각 집마다
        chick_dist = 1e9
        
        for i in range(M): #M개의 치킨집 중 최소 치킨 거리 계산
            chick_dist = min(chick_dist, abs(h[1] - case[i][1]) + abs(h[0] - case[i][0]))
        
        total_dist += chick_dist #모든 집에 대해 최소 치킨 거리 합산
        
    answer = min(answer, total_dist) #total_dist에 따라 answer 갱신
    
print(answer)

#r과 c는 1부터 시작, 인덱스 접근 시 유의
#거리 측정 방식은 맨해튼 거리 측정법, x좌표 y좌표 각각 절댓값 뺄셈 후 더하기
#0 : 빈 집, 1 : 집, 2 : 치킨집
#M개만 남기고 치킨집을 폐업시킬 때, 치킨 거리 최소화시키게 치킨집 남기는 방법?
#현재 있는 치킨집들 중 M개를 남기는 combinations 적용
#각 case내, 각 집마다 치킨 거리 합 계산 (3중 반복)
#치킨 거리 최소값 답으로 도출