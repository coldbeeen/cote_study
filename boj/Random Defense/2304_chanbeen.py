#구글링
import sys

input = sys.stdin.readline

N = int(input())

pillar = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: x[0])

max_height = 0
max_height_idx = 0

for p in pillar:
    if max_height < p[1]:
        max_height = p[1] #최댓값 찾기
        max_height_idx = pillar.index(p) #반복문 범위 설정을 위한 인덱스

result = max_height #최댓값 기둥 높이 미리 더해놓기

#맨 왼쪽에서 최댓값으로
height = pillar[0][1]

for i in range(max_height_idx):
    result += (pillar[i + 1][0] - pillar[i][0]) * height
    
    if height < pillar[i + 1][1]: #다음 기둥의 높이가 더 크면 값 갱신
        height = pillar[i + 1][1]

#맨 오른쪽에서 최댓값으로
height = pillar[-1][1]

for i in range(N - 1, max_height_idx, -1):
    result += (pillar[i][0] - pillar[i - 1][0]) * height
    
    if height < pillar[i - 1][1]: #다음 기둥의 높이가 더 크면 값 갱신
        height = pillar[i - 1][1]

print(result)