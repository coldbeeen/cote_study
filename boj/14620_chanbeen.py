import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

g = [list(map(int, input().split())) for _ in range(N)]

price = []

for i in range(1, N-1):
    for j in range(1, N-1):
        price.append(g[i][j] + g[i-1][j] + g[i+1][j] + g[i][j-1] + g[i][j+1]) #가격 저장 배열

visited = [[0] * N for _ in range(N)] #방문 여부를 관리하는 배열

comb_list = list(combinations(range(0, (N-2)*(N-2)), 3)) #price index로 가능한 조합의 수

result = []

for comb in comb_list:
    sum = 0
    flag = 0
    for i in range(len(comb)):
        row, char = comb[i] // (N - 2) + 1, comb[i] % (N - 2) + 1 #price가 1차원 배열이므로, 화단의 행/열 인덱스로 복구
        
        if visited[row][char] != 1 and visited[row-1][char] != 1 and visited[row+1][char] != 1 and visited[row][char-1] != 1 and visited[row][char+1] != 1:
            sum += price[comb[i]]
            visited[row][char] = visited[row-1][char] = visited[row+1][char] = visited[row][char-1] = visited[row][char+1] = 1 #방문 처리
        else:
            flag = 1 #겹치는 꽃잎이 존재함
            break
    
    visited = [[0] * N for _ in range(N)] #다음 경우의 수를 위해, 방문 관리 배열 초기화
    
    if flag == 1: #겹치는 꽃잎이 존재하면 패스
        continue
    
    result.append(sum)

print(min(result)) #가능한 경우의 수 중 최소 비용 출력

#처음 푼 방법은 24퍼에서 틀림, 왜?
#제일 작은 값만 따라가면 모든 경우를 돌지 못 하기 때문..
#제일 작은 것만 골라나가는 것이 답이 아닐 때가 있음
#Ex : 1 10 11 vs 3 5 7
#따라서 모든 경우의 수를 탐색할 필요가 있음